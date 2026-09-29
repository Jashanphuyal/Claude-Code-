"""Filter test_final.csv to rows whose domain appears in the verified prospects CSV.

Usage:
    python match_domains.py [UNVERIFIED_CSV] [VERIFIED_CSV] [OUTPUT_CSV]
"""
import re
import sys

import pandas as pd

UNVERIFIED_CSV = "test_final.csv"
VERIFIED_CSV = "September_2026_Spam_Promo_ENRICHED.xlsx - Spam - Coaches & Consultants (1).csv"
OUTPUT_CSV = "final_matched.csv"

BUSINESS_EMAIL_COL = "Email 1 (Business)"


def normalize_domain(value):
    """Lowercase, strip scheme / leading www. / path. Returns None if unparseable."""
    if not isinstance(value, str):
        return None
    d = value.strip().lower()
    if not d:
        return None
    if "@" in d and "/" not in d:  # an email address slipped in
        d = d.rsplit("@", 1)[1]
    d = re.sub(r"^https?://", "", d)
    d = re.sub(r"^www\.", "", d)
    d = re.split(r"[/?#]", d, maxsplit=1)[0]
    d = d.split(":", 1)[0].strip().strip(".")
    if not d or "." not in d or " " in d:
        return None
    return d


def domain_from_email(value):
    if not isinstance(value, str) or "@" not in value:
        return None
    return normalize_domain(value.strip().rsplit("@", 1)[1])


FREE_EMAIL_DOMAINS = {
    "gmail.com", "googlemail.com", "yahoo.com", "hotmail.com", "outlook.com",
    "live.com", "icloud.com", "me.com", "aol.com", "protonmail.com", "proton.me",
}


def any_business_email_domain(row):
    """Last resort for column-shifted rows: first non-free-mail email domain in the
    row, ignoring the sender (From Email) column."""
    for col, value in row.items():
        if col == "From Email" or not isinstance(value, str):
            continue
        v = value.strip()
        if "@" in v and " " not in v:
            d = domain_from_email(v)
            if d and d not in FREE_EMAIL_DOMAINS:
                return d
    return None


def row_domains(df):
    """Per-row domain: Domain column, else Website, else business email,
    else any business email found in the row."""
    domains = pd.Series([None] * len(df), index=df.index, dtype=object)
    if "Domain" in df.columns:
        domains = df["Domain"].map(normalize_domain)
    if "Website" in df.columns:
        domains = domains.fillna(df["Website"].map(normalize_domain))
    if BUSINESS_EMAIL_COL in df.columns:
        domains = domains.fillna(df[BUSINESS_EMAIL_COL].map(domain_from_email))
    missing = domains.isna()
    if missing.any():
        domains[missing] = df[missing].apply(any_business_email_domain, axis=1)
    return domains


def read_csv(path):
    # keep_default_na=False so values like "NA" / "" are kept verbatim.
    return pd.read_csv(path, encoding="utf-8", dtype=str, keep_default_na=False)


def main(argv):
    unverified_path = argv[1] if len(argv) > 1 else UNVERIFIED_CSV
    verified_path = argv[2] if len(argv) > 2 else VERIFIED_CSV
    output_path = argv[3] if len(argv) > 3 else OUTPUT_CSV

    unverified = read_csv(unverified_path)
    verified = read_csv(verified_path)

    if "Domain" in verified.columns:
        verified_domains = verified["Domain"].map(normalize_domain)
        if BUSINESS_EMAIL_COL in verified.columns:
            verified_domains = verified_domains.fillna(
                verified[BUSINESS_EMAIL_COL].map(domain_from_email)
            )
    elif BUSINESS_EMAIL_COL in verified.columns:
        verified_domains = verified[BUSINESS_EMAIL_COL].map(domain_from_email)
    else:
        sys.exit(f"Verified CSV has neither 'Domain' nor '{BUSINESS_EMAIL_COL}' column")
    verified_set = set(verified_domains.dropna())

    unverified_domains = row_domains(unverified)
    mask = unverified_domains.isin(verified_set)
    matched = unverified[mask]  # original row order and column order preserved
    matched.to_csv(output_path, encoding="utf-8", index=False)

    skipped = int(unverified_domains.isna().sum())
    unmatched_verified = sorted(verified_set - set(unverified_domains[mask]))

    print(f"Total rows in {unverified_path}: {len(unverified)}")
    print(f"  rows with missing/unparseable domain (skipped): {skipped}")
    print(f"Total unique verified domains: {len(verified_set)}")
    print(f"Total matched rows: {len(matched)}")
    print(f"  unique domains among matched rows: {unverified_domains[mask].nunique()}")
    print(f"Wrote {output_path}")
    print(f"Verified domains with no matching row ({len(unmatched_verified)}):")
    for d in unmatched_verified:
        print(f"  - {d}")


if __name__ == "__main__":
    main(sys.argv)
