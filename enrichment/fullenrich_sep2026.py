#!/usr/bin/env python3
"""FullEnrich run for the September 2026 Spam/Promo campaign file (master prompt V2).

Env:
  FULLENRICH_API_KEY   required
  FE_CREDIT_CAP        hard cap on credits spent this run (required, integer)
  FE_ROUNDS            comma list of rounds to run, default "validate,1,2,3,4"
  FE_HUNT_FILE         optional JSON from the surname hunt (key, first, last, linkedin, domain, confidence)

Usage:
  python3 fullenrich_sep2026.py <input.xlsx> <output.xlsx>

Every email FullEnrich returns is written back (any status, including ones equal
to the From email) EXCEPT role accounts. Business = person@own-domain,
Personal = person@free-provider.
"""
import json, os, re, sys, time, urllib.request, urllib.error
import openpyxl

API = "https://app.fullenrich.com/api/v1"
KEY = os.environ.get("FULLENRICH_API_KEY")
CAP = int(os.environ.get("FE_CREDIT_CAP", "0"))
ROUNDS = os.environ.get("FE_ROUNDS", "validate,1,2,3,4").split(",")
STATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fe_state.json")

FREE = {
    "gmail.com", "googlemail.com", "yahoo.com", "yahoo.co.uk", "yahoo.fr", "yahoo.de", "yahoo.com.au",
    "ymail.com", "hotmail.com", "hotmail.co.uk", "hotmail.fr", "hotmail.de", "outlook.com", "outlook.fr",
    "live.com", "live.co.uk", "msn.com", "aol.com", "icloud.com", "me.com", "mac.com", "protonmail.com",
    "proton.me", "pm.me", "gmx.com", "gmx.de", "gmx.net", "web.de", "mail.com", "zoho.com", "yandex.com",
    "yandex.ru", "qq.com", "163.com", "126.com", "comcast.net", "att.net", "verizon.net", "sbcglobal.net",
    "bigpond.com", "optusnet.com.au", "btinternet.com", "orange.fr", "free.fr", "libero.it", "t-online.de",
    "hey.com", "fastmail.com", "tutanota.com", "rocketmail.com", "rediffmail.com", "naver.com",
}
ROLE = {
    "role", "sales", "admin", "hello", "hi", "hey", "info", "contact", "contactus", "support", "help",
    "team", "office", "billing", "accounts", "accounting", "bookings", "booking", "noreply", "no-reply",
    "donotreply", "do-not-reply", "reply", "mail", "email", "enquiries", "enquiry", "inquiries", "inquiry",
    "marketing", "news", "newsletter", "press", "media", "pr", "hr", "jobs", "careers", "legal", "privacy",
    "orders", "order", "shop", "store", "service", "customerservice", "customercare", "care", "feedback",
    "partners", "partnerships", "affiliates", "affiliate", "webmaster", "postmaster", "abuse", "security",
    "general", "hola", "ciao", "bonjour", "welcome", "community", "members", "studio", "concierge",
    "wholesale", "returns", "shipping", "finance", "invoices", "payments", "ops", "operations", "events",
    "social", "collabs", "collab", "business", "corp", "offers", "leadership", "ceo", "founder", "founders",
    "owner", "management", "clients", "client", "customers", "questions", "ask", "start", "yes",
}


def is_role(local):
    base = re.sub(r"[\d._+-]+$", "", local.lower())
    return local.lower() in ROLE or base in ROLE


def classify(email, lead_domain):
    local, _, dom = email.lower().partition("@")
    if is_role(local):
        return "ROLE"
    if dom in FREE:
        return "PERSONAL"
    return "BUSINESS"


def req(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(API + path, data=data, method=method,
                               headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    with urllib.request.urlopen(r, timeout=60) as resp:
        return json.loads(resp.read())


def balance():
    return req("GET", "/account/credits").get("balance")


def load_leads(wb):
    leads = {}
    for ws in wb:
        if ws["A1"].value != "SN":
            continue
        hdr = [c.value for c in ws[1]]
        col = {h: i for i, h in enumerate(hdr)}
        for row in ws.iter_rows(min_row=2):
            v = [c.value for c in row]
            if v[0] is None:
                continue
            key = f"{ws.title}|{v[0]}"
            li = (v[col["LinkedIn"]] or "").strip()
            leads[key] = dict(key=key, sheet=ws.title, row=row[0].row, first=v[1], last=v[2],
                              company=v[3], linkedin=li if "/in/" in li else None,
                              domain=v[col["Domain"]], from_email=(v[col["From Email"]] or "").lower())
    return leads


def payload(lead, fields):
    d = {"enrich_fields": fields, "custom": {"key": lead["key"]}}
    if lead["linkedin"]:
        d["linkedin_url"] = lead["linkedin"]
    if lead["first"]:
        d["firstname"] = lead["first"]
    if lead["last"]:
        d["lastname"] = lead["last"]
    if lead["domain"]:
        d["domain"] = lead["domain"]
    if lead["company"]:
        d["company_name"] = lead["company"]
    return d


def eligible(lead):
    return bool(lead["linkedin"] or (lead["first"] and lead["last"] and lead["domain"]))


def extract_emails(obj, out):
    """Walk any FullEnrich result shape, collecting (email, status)."""
    if isinstance(obj, dict):
        e = obj.get("email")
        if isinstance(e, str) and "@" in e:
            out.append((e.strip().lower(), obj.get("status") or obj.get("email_status") or ""))
        for k, val in obj.items():
            if k in ("most_probable_email", "most_probable_personal_email") and isinstance(val, str) and "@" in val:
                out.append((val.strip().lower(), obj.get(k + "_status") or ""))
            else:
                extract_emails(val, out)
    elif isinstance(obj, list):
        for x in obj:
            extract_emails(x, out)
    return out


def run_batch(name, items, state):
    spent = state["spent"]
    if not items:
        return {}
    for i in range(0, len(items), 100):
        chunk = items[i:i + 100]
        worst = sum(3 if "contact.personal_emails" in d["enrich_fields"] else 0 for d in chunk) + \
                sum(1 if "contact.emails" in d["enrich_fields"] else 0 for d in chunk)
        if spent + worst > CAP:
            print(f"[{name}] stopping: worst case {worst} would exceed cap ({spent}/{CAP})")
            break
        eid = req("POST", "/contact/enrich/bulk", {"name": f"GM_Sep2026_{name}_{i // 100}", "datas": chunk})["enrichment_id"]
        print(f"[{name}] submitted {len(chunk)} -> {eid}")
        while True:
            time.sleep(15)
            res = req("GET", f"/contact/enrich/bulk/{eid}")
            if res.get("status") not in ("IN_PROGRESS", "CREATED", "QUEUED"):
                break
        cr = (res.get("cost") or {}).get("credits", 0)
        spent += cr
        state["spent"] = spent
        for d in res.get("datas", []):
            k = (d.get("custom") or {}).get("key")
            if not k:
                continue
            found = extract_emails(d.get("contact", d), [])
            state["results"].setdefault(k, [])
            for e, s in found:
                if e not in [x[0] for x in state["results"][k]]:
                    state["results"][k].append([e, s, name])
        json.dump(state, open(STATE, "w"), indent=1)
        print(f"[{name}] credits this batch {cr}, total {spent}, balance {balance()}")
    return state


def main(src, dst):
    if not KEY or not CAP:
        sys.exit("Set FULLENRICH_API_KEY and FE_CREDIT_CAP")
    wb = openpyxl.load_workbook(src)
    leads = load_leads(wb)
    state = json.load(open(STATE)) if os.path.exists(STATE) else {"spent": 0, "results": {}, "done": []}
    print("balance", balance(), "cap", CAP)
    elig = [l for l in leads.values() if eligible(l)]
    hunted = apply_hunt(leads, {l["key"] for l in elig})
    print(f"{len(elig)} eligible of {len(leads)}")

    def hits():
        return {k for k, v in state["results"].items() if v}

    for rnd in ROUNDS:
        if rnd in state["done"]:
            continue
        if rnd == "validate":
            run_batch("VALIDATE", [payload(elig[0], ["contact.emails"])], state)
        elif rnd == "1":
            run_batch("R1", [payload(l, ["contact.emails"]) for l in elig[1:]], state)
        elif rnd == "2":
            run_batch("R2", [payload(l, ["contact.personal_emails"]) for l in elig if l["key"] not in hits()], state)
        elif rnd == "3":
            h = hits()
            run_batch("R3", [payload(l, ["contact.personal_emails"]) for l in elig if l["key"] in h], state)
        elif rnd == "4":
            run_batch("R4", [payload(l, ["contact.emails", "contact.personal_emails"]) for l in hunted], state)
        state["done"].append(rnd)
        json.dump(state, open(STATE, "w"), indent=1)

    write_back(wb, leads, state)
    wb.save(dst)
    print("saved", dst, "credits spent", state["spent"])


def apply_hunt(leads, already):
    """Fill names/LinkedIn/domain found by the surname hunt; return leads that became eligible."""
    path = os.environ.get("FE_HUNT_FILE")
    if not path or not os.path.exists(path):
        return []
    newly = []
    for h in json.load(open(path)):
        lead = leads.get(h.get("key"))
        if not lead or lead["key"] in already or h.get("confidence") not in ("HIGH", "MEDIUM"):
            continue
        li = h.get("linkedin") or ""
        lead["linkedin"] = lead["linkedin"] or (li if "/in/" in li else None)
        lead["first"] = lead["first"] or h.get("first")
        lead["last"] = lead["last"] or h.get("last")
        lead["domain"] = lead["domain"] or h.get("domain")
        if eligible(lead):
            newly.append(lead)
    print(f"surname hunt made {len(newly)} more leads eligible")
    return newly


def write_back(wb, leads, state):
    all_from = {l["from_email"] for l in leads.values() if l["from_email"]}
    for k, emails in state["results"].items():
        lead = leads.get(k)
        if not lead:
            continue
        ws = wb[lead["sheet"]]
        r = lead["row"]
        existing = {str(ws.cell(r, c).value or "").lower() for c in (5, 7, 9, 11, 13)}
        extra = []
        for e, status, rnd in emails:
            kind = classify(e, lead["domain"])
            if kind == "ROLE" or e in existing:
                continue
            note = f"{status or 'UNKNOWN'} (FullEnrich {rnd})"
            if e == lead["from_email"]:
                note += " - SAME AS FROM EMAIL"
            elif e in all_from:
                note += " - is another lead's From email"
            slot = None
            pref = 5 if kind == "BUSINESS" else 7
            for c in [pref, 9, 11, 13]:
                if not ws.cell(r, c).value:
                    slot = c
                    break
            if slot:
                ws.cell(r, slot).value = e
                ws.cell(r, slot + 1).value = f"{kind} | {note}"
                existing.add(e)
            else:
                extra.append(f"{e} [{kind} | {note}]")
        if extra:
            ws.cell(r, 31).value = "; ".join(extra)
    for ws in wb:
        if ws["A1"].value == "SN":
            ws.cell(1, 31).value = "FullEnrich Extra Emails"


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
