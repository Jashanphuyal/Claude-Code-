"""Run FullEnrich on every lead in the September 2026 campaign workbook.

Usage:
    FULLENRICH_API_KEY=... python3 run_fullenrich.py <input.xlsx> <output.xlsx>

- Sends every lead that has (first + last name + domain/company) or a LinkedIn /in/ URL.
- Asks for both work emails and personal emails.
- Keeps EVERY email FullEnrich returns (any status: valid, catch-all, invalid, ...)
  EXCEPT role accounts (info@, hello@, contact@, sales@, support@ ...).
- Raw API responses are checkpointed to fe_raw.json, so a re-run resumes
  instead of re-spending credits.
"""
import json, os, re, sys, time
import urllib.request, urllib.error
import openpyxl
from openpyxl.styles import Font, PatternFill

API = "https://app.fullenrich.com/api/v2"  # v1 is deprecated
KEY = os.environ["FULLENRICH_API_KEY"]
LEAD_TABS = ["Spam - Coaches & Consultants", "Spam - Ecom",
             "Promotions - Coaches & Consulta", "Promotions - Ecom"]
BATCH = 100
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "fe_raw.json")

ROLE_LOCALS = {
    "info", "hello", "hi", "hey", "contact", "contactus", "contact-us", "sales", "support",
    "help", "helpdesk", "team", "admin", "administrator", "office", "enquiries", "enquiry",
    "inquiries", "inquiry", "marketing", "media", "press", "pr", "news", "newsletter",
    "noreply", "no-reply", "donotreply", "do-not-reply", "billing", "accounts", "accounting",
    "finance", "invoices", "orders", "order", "shop", "store", "customerservice",
    "customer-service", "customercare", "care", "service", "services", "feedback", "jobs",
    "careers", "hr", "recruiting", "webmaster", "postmaster", "hostmaster", "abuse",
    "mailer", "mail", "bounce", "notifications", "alerts", "partners", "partnerships",
    "affiliates", "legal", "privacy", "security", "it", "tech", "operations", "ops",
    "booking", "bookings", "reservations", "events", "general", "welcome", "community",
    "members", "membership", "concierge", "wholesale", "returns", "studio", "academy",
    "podcast", "collab", "collabs", "hola", "bonjour", "ciao", "hallo", "love", "reception",
}


def is_role(email):
    local = email.split("@", 1)[0].lower()
    base = re.split(r"[+]", local)[0]
    return base in ROLE_LOCALS or base.rstrip("0123456789") in ROLE_LOCALS


def call(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(API + path, data=data, method=method, headers={
        "Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="replace")
            if e.code in (429, 500, 502, 503, 504) and attempt < 4:
                time.sleep(2 ** (attempt + 1)); continue
            raise SystemExit(f"FullEnrich {method} {path} -> HTTP {e.code}: {msg}")
        except urllib.error.URLError:
            if attempt < 4:
                time.sleep(2 ** (attempt + 1)); continue
            raise


def domain_of(row):
    d = row[20] or row[16] or ""
    d = re.sub(r"^https?://", "", str(d)).split("/")[0].lower()
    return d[4:] if d.startswith("www.") else d


def load_leads(wb):
    leads = []
    for tab in LEAD_TABS:
        for r in wb[tab].iter_rows(min_row=2, values_only=True):
            if r[0] is None:
                continue
            first, last = (r[1] or "").strip(), (r[2] or "").strip()
            li = str(r[14] or "").strip()
            li = li if "/in/" in li else ""
            dom, company = domain_of(r), (r[3] or "").strip()
            if not ((first and last and (dom or company)) or li):
                continue
            c = {"first_name": first, "last_name": last,
                 "enrich_fields": ["contact.work_emails", "contact.personal_emails"],
                 "custom": {"key": f"{tab}|{r[0]}"}}
            if dom: c["domain"] = dom
            if company: c["company_name"] = company
            if li: c["linkedin_url"] = li
            leads.append(c)
    return leads


EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$", re.I)


def extract_emails(item):
    """Every email anywhere in a result item, with type (Personal/Business) and status.

    Walks the whole item so it works whatever the v2 response nesting is; an
    email counts as Personal when any enclosing key mentions 'personal'.
    """
    out = {}

    def walk(node, personal, status):
        if isinstance(node, dict):
            st = node.get("status") if isinstance(node.get("status"), str) else status
            for k, v in node.items():
                if k == "custom":
                    continue
                walk(v, personal or "personal" in k.lower(), st)
        elif isinstance(node, list):
            for v in node:
                walk(v, personal, status)
        elif isinstance(node, str) and EMAIL_RE.match(node.strip()):
            em = node.strip().lower()
            if em not in out or (not out[em][1] and status):
                out[em] = ("Personal" if personal else "Business", status or "")

    walk(item, False, "")
    return [(em, kind, st) for em, (kind, st) in out.items()]


def main(src, dst):
    wb = openpyxl.load_workbook(src)
    leads = load_leads(wb)
    raw = json.load(open(RAW)) if os.path.exists(RAW) else {}
    done = {k for res in raw.values() for k in res.get("keys", [])}
    todo = [c for c in leads if c["custom"]["key"] not in done]
    print(f"{len(leads)} enrichable leads, {len(todo)} still to send")
    print("credits before:", call("GET", "/account/credits"))

    for i in range(0, len(todo), BATCH):
        chunk = todo[i:i + BATCH]
        resp = call("POST", "/contact/enrich/bulk",
                    {"name": f"Sept 2026 spam-promo {i // BATCH + 1}", "data": chunk})
        eid = resp.get("enrichment_id") or resp.get("id")
        print(f"batch {i // BATCH + 1}: {len(chunk)} leads, id {eid}")
        while True:
            time.sleep(15)
            res = call("GET", f"/contact/enrich/bulk/{eid}")
            if str(res.get("status", "")).upper() in ("FINISHED", "COMPLETED", "DONE", "CANCELED", "CANCELLED", "FAILED", "CREDITS_INSUFFICIENT", "RATE_LIMIT", "UNKNOWN"):
                break
        print("  status:", res.get("status"))
        raw[eid] = {"keys": [c["custom"]["key"] for c in chunk], "result": res}
        json.dump(raw, open(RAW, "w"), indent=1)
        if res.get("status") == "CREDITS_INSUFFICIENT":
            print("Out of credits - stopping. Re-run after topping up to resume.")
            break
    print("credits after:", call("GET", "/account/credits"))

    # key -> list of (email, type, status), role accounts removed
    found, roles_dropped = {}, 0
    for res in raw.values():
        items = res["result"].get("data") or res["result"].get("datas") or []
        for item in items:
            key = (item.get("custom") or {}).get("key")
            for em, kind, status in extract_emails(item):
                if is_role(em):
                    roles_dropped += 1; continue
                lst = found.setdefault(key, [])
                if em not in [x[0] for x in lst]:
                    lst.append((em, kind, status))

    hdr_font, fill = Font(bold=True), PatternFill("solid", fgColor="FFF2CC")
    flat = wb.create_sheet("FullEnrich Results")
    flat.append(["Tab", "SN", "First Name", "Last Name", "Business Name", "Domain",
                 "From Email", "FE Email", "Type", "FE Status"])
    for tab in LEAD_TABS:
        ws = wb[tab]
        base = ws.max_column
        for j in range(5):
            for k, h in enumerate((f"FE Email {j + 1}", f"FE Type {j + 1}", f"FE Status {j + 1}")):
                c = ws.cell(1, base + 1 + j * 3 + k, h); c.font = hdr_font; c.fill = fill
        extra_col = base + 16
        ws.cell(1, extra_col, "FE Extra Emails").font = hdr_font
        for row in ws.iter_rows(min_row=2):
            sn = row[0].value
            if sn is None:
                continue
            ems = found.get(f"{tab}|{sn}", [])
            for j, (em, kind, status) in enumerate(ems[:5]):
                ws.cell(row[0].row, base + 1 + j * 3, em)
                ws.cell(row[0].row, base + 2 + j * 3, kind)
                ws.cell(row[0].row, base + 3 + j * 3, status)
            if len(ems) > 5:
                ws.cell(row[0].row, extra_col, "; ".join(f"{e} ({k}, {s})" for e, k, s in ems[5:]))
            for em, kind, status in ems:
                v = [c.value for c in row]
                flat.append([tab, sn, v[1], v[2], v[3], v[20], v[18], em, kind, status])
    for c in flat[1]:
        c.font = hdr_font
    wb.save(dst)
    n_leads = len(found)
    n_emails = sum(len(v) for v in found.values())
    print(f"Done: {n_emails} non-role emails across {n_leads} leads; "
          f"{roles_dropped} role emails dropped. Saved {dst}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
