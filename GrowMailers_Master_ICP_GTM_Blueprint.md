# GrowMailers Master Blueprint

## Ideal Customer Profile, Market Sizing, Deliverability Framework and Go-To-Market Plan for Shopify DTC Brands

**Prepared for:** Shardul Phuyal, GrowMailers

**Version:** 2.0. This replaces the *Ecommerce and DTC Brands Report* of 27 September 2026

**Date:** 28 September 2026

**Classification:** Internal strategy document

> **How to use this document.** Every section opens with a bottom line. Read those alone and you have the strategy in ten minutes. Underneath are the tables, diagrams and SOPs the team works from day to day. Figures come from named public sources current to September 2026, including the US Census Bureau, Store Leads, Klaviyo, Omnisend, Validity, Triple Whale, Google and company filings. Where a number is our own estimate or a planning assumption, we say so. The legal sections are research, not legal advice.

### Contents

1. Executive Summary & Strategic Intent
2. E-Commerce & DTC Taxonomies
3. Macro Industry Pressures & Customer Acquisition Economics
4. Tech Stack Ecosystem & Intelligence Signals
5. Target Audience Specification & Multi-Tier ICP Definitions
6. Addressable Market Sizing & Geolocation Deep-Dive
7. Organizational Structures & Decision-Maker Buying Profiles
8. Financial Dynamics, Margin Structures & Category Unit Economics
9. Operational Cycles & the Annual E-Commerce Cash Calendar
10. Email Performance Benchmarks & Measurement Systems
11. Automated Flow Architecture vs. Campaign Blasts
12. Subscriber Database Hygiene, List Management & ESP Cost Control
13. Technical Deliverability Engineering & Authentication Protocols
14. Inbox Placement Testing, Domain Reputation & Risk Management
15. Global Retail Holidays & Regional Peak Promotional Windows
16. Go-To-Market Execution Windows & Sales Timelines
17. International Marketing Compliance & Cold Outreach Law
18. GTM Audit SOP, Prospecting Scripts & Qualification Playbook

Appendices: A. Glossary. B. Sources and data notes.

---

# 1. Executive Summary & Strategic Intent

> **Bottom line:** A DTC brand now barely breaks even, or loses money, on the first order it buys with paid media. Its profit comes from the second, third and fourth orders, and email and SMS are the cheapest way to produce them. GrowMailers sells into that gap with two offers. **Ascent** is a USD 5,000 one-time project that fixes the plumbing: authentication, list hygiene and inbox repair. **Lhotse** is a USD 3,000 to 5,500 monthly retainer that runs the whole retention program. The ideal client runs Shopify or Shopify Plus with Klaviyo and sells a repeat-purchase product. Lhotse targets brands turning over USD 3M to 20M a year. Ascent targets USD 1M to 50M+.

## 1.1 The business thesis

Three pressures are hitting DTC brands at once. **Acquisition costs more every year.** Meta's average price per ad rose 12% year on year in Q2 2026, and it has risen by 6% to 14% every quarter since Q2 2024. **Each order costs more to fulfil.** Tariffs, the end of duty-free entry for low-value parcels into the US and higher freight all eat into margin. About four in five brands told ShipBob that the 2025 tariff changes raised their costs. **The inbox has become stricter.** Gmail, Yahoo and Microsoft now require authentication, one-click unsubscribe and low complaint rates from bulk senders, and they reject mail that fails. Every brand in our ICP sends enough volume to count as a bulk sender.

The result is that retention is where DTC profit comes from. A repeat order driven by email costs cents. A new customer bought through paid media costs 38% to 63% of the first order's value in ad spend, depending on category. Yet most USD 3M to 20M brands still run the email program they set up years ago. Their flows are thin, campaigns go to the whole list, and they pay Klaviyo every month to store dormant and bot profiles. Nobody has checked their authentication since it was first set up. GrowMailers exists to close that gap.

## 1.2 The two offers

| | **Ascent** | **Lhotse** |
|---|---|---|
| Format | One-time technical project | Monthly managed retainer |
| Price | USD 5,000 | USD 3,000 to 5,500 a month (USD 36,000 to 66,000 a year) |
| Scope | SPF, DKIM and DMARC; branded sending domain and alignment; list cleaning and suppression; bot defences; sunset policy; inbox repair; warm-up plan | Email and SMS strategy; flow architecture; campaign calendar and execution; segmentation; design and copy; CRO of forms and landing pages; reporting; ongoing hygiene |
| Delivery | 2 to 3 weeks of repair, plus up to 10 weeks of monitored warm-up if a new domain is needed | Ongoing, after 2 to 3 weeks of onboarding |
| Revenue target | USD 1M to 50M+ | USD 3M to 20M |
| Buying trigger | Bounces, spam placement, "via klaviyomail.com", a Black Friday scare, a rising Klaviyo bill | Flat email revenue, a lost email manager, a disappointing agency, new growth targets |
| Success measures | Aligned DMARC pass; Gmail spam rate below 0.1%; bounces below 1%; placement restored at weak providers; fewer billed profiles | Email share of website revenue; revenue per recipient; holdout-tested incremental revenue; margin protected through discount discipline |

Ascent is a repair project with a clear end, and it is the natural way into a new account. It suits brands that can see the symptoms but cannot diagnose them. It also suits enterprise brands whose CRM teams need a specialist to rebuild authentication or move sending domains without interrupting revenue, a zero-downtime repair (Section 13.8).

We recommend banding Lhotse's price by scope:

| Suggested band | Monthly fee | Typical brand | Scope |
|---|---|---|---|
| Lhotse Core | USD 3,000 to 3,500 | USD 3M to 6M, email-led | Full flow build and upkeep; 2 to 3 segmented campaigns a week; monthly reporting; hygiene |
| Lhotse Growth | USD 3,500 to 4,500 | USD 6M to 12M, email and SMS | Core, plus a managed SMS program, a structured test plan, replenishment and subscription flows, and quarterly holdout tests |
| Lhotse Scale | USD 4,500 to 5,500 | USD 12M to 20M, multi-market | Growth, plus CRO sprints, predictive segmentation, multi-country calendars and a weekly strategist call |

*A suggested structure for GrowMailers to confirm against its actual packaging.*

```
  EXTERNAL AUDIT ──► ASCENT PROJECT ──► 30-DAY RESULTS REVIEW ──► LHOTSE PROPOSAL
  (free, 15 min)     (USD 5,000)        (proof in their own data)  (USD 3,000–5,500/mo)
        └── Lhotse-first path when the brand is USD 3M–20M and its technical base is sound ──┘
```

Lead with Ascent when the audit finds technical debt, since nobody should scale campaigns on a broken sending setup. Lead with Lhotse when the technical base is sound and the gap is in strategy and execution. We also recommend crediting part of the Ascent fee against the first Lhotse month for brands that convert within 60 days. That turns Ascent into a paid trial.

## 1.3 Financial positioning

**Against an in-house hire.** Glassdoor puts a US Email Marketing Manager at USD 66,000 to 107,000 base pay. That is roughly USD 85,000 to 135,000 fully loaded (our estimate, assuming 25% to 30% on-costs), for one person with one skill set, a ramp-up period and a single point of failure. Lhotse costs USD 36,000 to 66,000 a year and brings a strategist, designer, copywriter and deliverability specialist from day one.

**Against email revenue.** Healthy brands earn 20% to 30% of website revenue from email and SMS:

| Brand revenue | Email revenue at 20% to 30% | Lhotse as share of email revenue | Verdict |
|---|---|---|---|
| USD 1.5M | USD 300k to 450k | 8% to 22% | Too heavy. Sell Ascent. |
| USD 3M | USD 600k to 900k | 4% to 11% | Works |
| USD 5M | USD 1.0M to 1.5M | 2.4% to 6.6% | Comfortable |
| USD 10M | USD 2.0M to 3.0M | 1.2% to 3.3% | Sweet spot |
| USD 20M | USD 4.0M to 6.0M | 0.6% to 1.7% | Easy to justify |

**Ascent against an incident.** A USD 5M brand earning USD 1M a year from email makes about USD 19,000 a week from the channel. If a reputation problem pushes a quarter of its mail into spam, it loses around USD 4,800 a week in an ordinary month (our estimate), and much more in Black Friday week. Ascent pays for itself in one to two weeks of restored placement.

## 1.4 The fundamental DTC margin gap

A median apparel order, using Triple Whale's category medians and FIGS' reported cost structure:

```
  FIRST ORDER (bought with paid media)            REPEAT ORDER (driven by email)
  Order value              USD 103.37             Order value              USD 103.37
  − Product cost (33.5%)  −USD  34.63             − Product cost (33.5%)  −USD  34.63
  − Selling costs (23.1%) −USD  23.88             − Selling costs (23.1%) −USD  23.88
  = Before acquisition     USD  44.86             = Before acquisition     USD  44.86
  − Ad cost per purchase  −USD  39.24             − Email/SMS cost        ≈−USD   0.10
  ═════════════════════════════════════           ═════════════════════════════════
  LEFT BEFORE OVERHEAD     ≈ USD   5.62           LEFT BEFORE OVERHEAD     ≈ USD  44.76
```

The first order buys the customer, and the second earns the profit. Here a repeat order is worth about eight times a first order, and the gap widens every year that ad costs rise. We are not selling "better emails". We are selling a bigger share of orders that come with no acquisition cost.

## 1.5 What this blueprint commits GrowMailers to

1. **Sell only to brands that own their list.** The minimum stack is Shopify or Shopify Plus with Klaviyo. The brand must own its products and sell mainly through its own site.
2. **Pick the lead offer from evidence.** Ascent when an outside audit finds technical debt. Lhotse when the brand is USD 3M to 20M and its program is underbuilt.
3. **Focus on four verticals.** Beauty and personal care, health and supplements, food and beverage, and pet supplies.
4. **Sell by the calendar.** Never pitch a new retainer into the pre-Black Friday freeze.
5. **Prove value with holdout tests,** not platform-attributed revenue alone.
6. **Keep GrowMailers' own sending clean.** A deliverability agency on a blocklist has no credibility.

---

# 2. E-Commerce & Direct-to-Consumer (DTC) Taxonomies

> **Bottom line:** Whether a brand owns its customer list decides fit, and revenue comes second. A USD 30M Amazon seller is a worse prospect than a USD 4M Shopify brand, because it cannot email most of its buyers. Dropshippers and print-on-demand stores are excluded as well. They technically hold a list, but they lack the margin, product control and staying power to benefit from retention work.

## 2.1 Business models and list ownership

| Model | Definition | Owns an emailable list? | Ascent fit | Lhotse fit |
|---|---|---|---|---|
| **DTC brand** | Makes or owns its products; sells mainly through its own site or app | Yes, fully | **Strong** | **Strong** |
| **DNVB** | A DTC brand born online that controls the product from design to sale | Yes | **Strong** | **Strong**, if cash is sound |
| **Subscription-first DTC** | Core revenue is recurring orders, often through ReCharge | Yes | **Strong** | **Strong** (churn and dunning flows) |
| **Omnichannel retailer** | Own stores, website, marketplaces and wholesale, with shared data | Web buyers yes; store buyers partly | **Strong** (enterprise repairs) | Conditional: size on web revenue |
| **Hybrid Amazon + DTC** | Material revenue on Amazon and on its own site | Only DTC buyers | Conditional | Conditional: the DTC site must clear the floor on its own |
| **Wholesale-led brand** | Retail partners bring most revenue | Small DTC list | Only if DTC ≥ USD 1M | Exclude |
| **Marketplace-only seller** | Sells through Amazon, Etsy or TikTok Shop | No. The marketplace masks buyer emails. | **Exclude** | **Exclude** |
| **Dropshipper** | Holds no stock; a supplier ships each order | Technically | **Exclude** | **Exclude** |
| **Print-on-demand / creator merch** | Printed to order (Printful, Printify, Fourthwall) | Rarely brand-owned | **Exclude** | **Exclude** |

"E-commerce" in the Census sense covers any retail sale ordered online, from Amazon to a two-person Shopify store. Only the rows marked Strong or Conditional are GrowMailers' market. ShipBob's 2026 survey found 65% of brands name their own website as their top channel, 20% name Amazon and 12% name retail or wholesale. Because 86% of brands sell on two or more channels, **always size a prospect on website revenue.** Amazon and wholesale revenue never passes through Klaviyo.

## 2.2 Why dropshippers and print-on-demand are excluded

Retention email works when customers run out of a product and trust the brand enough to reorder. Dropshipped generic goods have neither. Their thin margins cannot fund USD 36,000 a year of retention work, many of these stores close within months (Ascent's value depends on a domain the brand keeps for years), and cheap traffic brings low-quality subscribers who damage both results and case studies. They are easy to screen out. Printful and Printify are top-ten apps on US Shopify stores, and Fourthwall accounts for 7.0% of US stores running Klaviyo.

## 2.3 Qualification decision tree

```
START ─► Is the brand's own website its main sales channel?
          ├─ NO ──► Does the own site alone clear USD 1M (Ascent) / USD 3M (Lhotse)?
          │          ├─ NO ──► EXCLUDE (marketplace-led or wholesale-led)
          │          └─ YES ─► CONTINUE, sizing on website revenue only
          └─ YES ─► Does it make or own its products?
                     ├─ NO ──► EXCLUDE (dropship, print-on-demand, creator merch, reseller)
                     └─ YES ─► Shopify or Shopify Plus?
                                ├─ NO ──► PARK
                                └─ YES ─► Is Klaviyo the ESP?
                                           ├─ Omnisend ───────────────► PARK (never force a migration)
                                           ├─ Shopify Email / Mailchimp ─► NURTURE
                                           └─ YES ─► Target vertical?
                                                      ├─ YES ─► QUALIFIED. Score it (Section 4).
                                                      └─ NO ──► SECONDARY. Only with visible repeat purchase.
```

## 2.4 Edge cases

- **A USD 25M brand doing 60% on Amazon.** Its website makes USD 10M, which is a Lhotse-band site. Qualify it on that figure, and expect a low email share because Amazon buyers never joined the list.
- **A retailer with physical stores.** A strong Ascent candidate, because more sending tools mean more authentication gaps. For Lhotse, check whether store customers are captured into Klaviyo at checkout. Report email share against web revenue only.
- **A holding company with several brands.** Each brand has its own domain, list and reputation, so each is a separate Ascent project. Sell to the group once.
- **A subscription-heavy brand.** Renewals are not attributed to email, so email share looks low. Judge the program on churn prevention and cross-sell instead.
- **A headless Shopify Plus build.** Tech-detection tools miss its apps. Confirm the stack by subscribing and reading the email headers (Section 18).

---

# 3. Macro Industry Pressures & Customer Acquisition Economics

> **Bottom line:** Online retail keeps growing, but the cost of winning each customer is growing faster than the margin on their first order. At current ad inflation, a median apparel brand's first order slips into loss within two years. Retention is where DTC brands make their money, and that is the case GrowMailers sells.

## 3.1 Market scale

The US Census Bureau reports USD 340.2 billion of US e-commerce in Q2 2026, which is 17.1% of all retail and 12.2% more than a year earlier. Full-year 2025 came to about USD 1.23 trillion (up about 5.4%). eMarketer puts DTC at about 19% of US e-commerce, roughly USD 234 billion, and expects the share to stay flat to 2028. Growth sped up in 2026, but Census figures include price rises, so tariff pass-through explains part of it. Brands are selling more dollars' worth of goods, not necessarily more units, and not at better margins.

## 3.2 Paid media inflation

Meta's Q2 2026 results showed average price per ad up 12%, with impressions up 14%. At flat conversion rates, that means roughly 12% more ad spend per purchase. Google Shopping and Search are also auctions and move the same way, so for those channels use the prospect's own ad account as the benchmark. Here is what compounding does to the apparel economics in Section 1.4, where about USD 44.86 is available before acquisition:

| Year | Cost per purchase at +12% a year | Left from the first order |
|---|---|---|
| Today | USD 39.24 | USD 5.62 |
| +1 year | USD 43.95 | USD 0.91 |
| +2 years | USD 49.22 | −USD 4.36 |
| +3 years | USD 55.13 | −USD 10.27 |

*Our estimate, assuming flat conversion and flat order value.*

Nothing breaks visibly. The first order just earns a little less each month until it quietly starts losing money. Brands that already earn their profit from repeat orders can absorb this, and brands that don't will find their growth plan stops adding up.

## 3.3 Tariffs and landed cost

The trade rules changed several times in 2026. The US Supreme Court struck down one set of tariffs in February, and a temporary 10% surcharge followed. New tariffs of 10% to 12.5% on about 60 economies took effect on 24 July, with Canada and the UK at 10%. US Customs suspended duty-free entry for low-value parcels indefinitely, and the USD 800 exemption ends by law on 1 July 2027. Importing brands absorb a higher cost of goods, and Canadian, UK and Australian brands shipping to US customers now pay duties they did not pay before. Trade press put several 2025 DTC closures down to this mix of tariffs, inflation, scarcer capital and high acquisition costs.

## 3.4 CAC, CPA and payback

- **CPA** is ad spend divided by all purchases, new and returning. Triple Whale's medians use this definition.
- **CAC** is marketing spend divided by *new* customers only, so it is always higher than CPA.
- **Contribution per order** is revenue minus product, fulfilment and payment costs.

```
  Payback (orders) = New-customer CAC ÷ Contribution per order before acquisition

  Beauty example:  CAC ≈ USD 50 (1.5 × median CPA of USD 33.44)
                   Contribution ≈ USD 38.93 (Section 8)  →  payback ≈ 1.3 orders
```

Across the verticals in Section 8, beauty, supplements and apparel need about 1.3 to 1.6 orders to recover CAC. Food and pet need about 2.2 to 2.5. **In every target vertical, profit depends on repeat orders.**

## 3.5 The retention math

Retention work adds profit through three levers: **repeat rate** (the share of buyers who come back), **frequency** (how quickly they return) and **contribution per repeat order** (bundles, cross-sell and discount discipline). Take a USD 8M beauty brand that acquires 50,000 new customers a year. Lifting its 12-month repeat rate from 25% to 30% adds 2,500 repeat customers. At 1.4 repeat orders each and about USD 39 of contribution per order, that is roughly **USD 136,000 of extra contribution a year** (our illustration). That is two to four times Lhotse's annual fee, from one lever alone.

## 3.6 What this means for the pitch

- **Talk about contribution margin, not open rates.** "Orders you don't pay Meta for" lands with founders and CFOs.
- **Compare Lhotse with buying the same orders through ads.** At a USD 40 blended CPA, 150 extra repeat orders a month would cost USD 6,000 in ad spend, which is more than Lhotse.
- **Avoid claims without a source.** The popular line that "CAC rose 60% in five years" comes from a 2022 vendor press release with no stated method. Senior buyers have seen it before.

---

# 4. E-Commerce Tech Stack Ecosystem & Intelligence Signals

> **Bottom line:** A brand's installed apps show its size, budget and likely pain before anyone speaks to it. Shopify plus Klaviyo is the entry ticket. Klaviyo plus at least one paid growth tool marks a brand with a retention budget. Attentive, Northbeam and Shopify Plus are the strongest size signals. We turn these signals into two scores: a **Lhotse Fit Score** and an **Ascent Urgency Score**.

## 4.1 The DTC stack

```
 ┌──────────────────────────────────────────────────────────────────────────┐
 │ STOREFRONT          Shopify · Shopify Plus (USD 2,300–2,500/mo)           │
 │ OWNED CHANNELS      Klaviyo · Postscript · Attentive · Omnisend · others  │
 │ REVENUE MODEL       ReCharge (subscriptions) · loyalty and referral apps  │
 │ MEASUREMENT         Triple Whale · Northbeam                              │
 │ CUSTOMER EXPERIENCE Gorgias (support) · Okendo / Yotpo (reviews)          │
 │ OPERATIONS          3PL (84% of brands use one) · inventory · returns     │
 └──────────────────────────────────────────────────────────────────────────┘
   Every tool that emails as the brand (support, reviews, subscriptions) is
   another sender that must pass DMARC alignment, so each is an Ascent checkpoint.
```

## 4.2 What each tool signals

| Tool | Share of US Shopify stores | Signal | What it tells us | Offer angle |
|---|---|---|---|---|
| **Shopify Plus** | 2.5% | Strong (size) | USD 27,600 to 30,000 a year in fees, which is 2.8% of revenue at USD 1M, so almost always a USD 1M+ brand | Both |
| **Klaviyo** | 14.5% | Gate | Required. About 64% of US Shopify stores with a detectable ESP use it. | Both |
| **Attentive** | 0.58% | Strong (size) | Enterprise-leaning, high volume, big SMS budget | Ascent; Lhotse Scale |
| **Northbeam** | 0.11% | Strong (size) | Large ad budget and a measurement-literate team | Lead with incrementality |
| **Postscript** | 1.7% | Medium | Runs SMS; has a retention budget | Lhotse Growth |
| **ReCharge** | 2.1% | Medium | Repeat-purchase model already in place | Churn, dunning, cross-sell |
| **Triple Whale** | 1.3% | Medium | Watches blended efficiency closely | Frame results as MER impact |
| **Gorgias** | 1.0% | Medium | Has a CX team that sends from the brand domain | DMARC alignment check |
| **Mailchimp** | 5.8% | Weak | Rarely a scaled DTC program | Nurture |
| **Omnisend alone** | 2.2% | Neutral | Often a deliberate choice, especially in Australia | Park; never force a migration |
| **Printful / Printify / Fourthwall** | Top-10 apps | Exclusion | Print-on-demand model | Exclude |

*Our division of Store Leads counts by 1,179,951 live US Shopify stores (September 2026).*

Three platform facts shape the pitch. **Klaviyo is growing into the mid-market.** Its Q2 2026 revenue rose 26% to USD 370.6M, and customers paying it more than USD 50,000 a year grew 36% to 4,477. Bigger brands are putting more money into owned channels. **Shopify Email rewrites the sender** to shopifyemail.com when a domain is unauthenticated or has no DMARC record or two of them. The rewrite is visible from outside, which makes it a clean Ascent finding. **Owners value Klaviyo's power but resent its bills.** Complaints centre on cost and complexity, so GrowMailers sells the expertise that makes Klaviyo worth paying for, never a migration.

## 4.3 Intent-scoring formulas

### Lhotse Fit Score (LFS, 0 to 100)

```
  LFS = Platform (0–20) + Size (0–30) + Stack (0–20) + Vertical (0–15) + Program Gap (0–15) − Penalties
  GATE: no Klaviyo → LFS = 0 (park or nurture)
```

| Component | Criteria | Points |
|---|---|---|
| **Platform** | Shopify Plus / standard Shopify ≥ USD 250k a month / below that | 20 / 12 / 0 |
| **Size** (estimated monthly sales) | USD 420k to 1.0M (USD 5M to 12M a year) | 30 |
| | USD 1.0M to 1.67M (USD 12M to 20M) / USD 250k to 420k (USD 3M to 5M) | 25 / 20 |
| | Above USD 1.67M / below USD 250k | 10 / 5 |
| **Stack** (cap 20) | Postscript or Attentive +6; ReCharge +6; Triple Whale or Northbeam +5; Gorgias +3; reviews or loyalty app +3 | up to 20 |
| **Vertical** | Beauty, supplements, food and beverage, pet / apparel or home with replenishable lines / other | 15 / 8 / 3 |
| **Program gap** (cap 15, from the audit) | Welcome is one email or missing +5; full-list campaigns more than 4 a week +4; no browse abandonment +3; no post-purchase or replenishment +3 | up to 15 |
| **Penalties** | Unverified registered-agent address −20; hired an email agency in the last 6 months −10; marketplace-led, dropship or print-on-demand → exclude | |

### Ascent Urgency Score (AUS, 0 to 100)

| Component | Criteria | Points |
|---|---|---|
| **Authentication gaps** (cap 40) | No DMARC record 20; two or malformed DMARC records 20; shared Klaviyo domain ("via klaviyomail.com") with more than 5,000 profiles 20; Shopify sender rewrite 15; SPF over 10 lookups or duplicated 10 | up to 40 |
| **Exposure** (cap 30) | List above 50,000 10; Attentive or Postscript plus daily cadence 10; Microsoft-heavy market (UK, Canada, Australia) 5; Black Friday within 12 weeks 5 | up to 30 |
| **Visible symptoms** (cap 30) | Test emails in spam at 2+ providers 15; transactional mail in spam 10; no one-click unsubscribe header 10; welcome email more than 1 hour late 5 | up to 30 |

### Priority matrix

```
                        ASCENT URGENCY SCORE
                   Low (< 40)               High (≥ 40)
              ┌──────────────────────┬──────────────────────┐
  LHOTSE  High│ LHOTSE-FIRST          │ ASCENT NOW,          │
  FIT    (≥60)│ Lead with program     │ LHOTSE NEXT          │
  SCORE       │ gaps and upside       │ Fix base, then pitch │
              ├──────────────────────┼──────────────────────┤
          Low │ NURTURE / DISCARD     │ ASCENT ONLY          │
         (<60)│ Re-score quarterly    │ USD 1–3M or USD 20M+ │
              └──────────────────────┴──────────────────────┘
```

## 4.4 Verify before outreach

Tech databases lag and miss headless builds. Before outreach, confirm three things by hand: Klaviyo is live (its script is on the site, or its headers appear in a real email), mail actually arrives after sign-up, and the growth tools are visible on the site (a ReCharge portal, a Gorgias chat widget). A stale signal leads to a wrong pitch. Market context matters too. **Australia has the highest Klaviyo penetration of our markets, at 23.6% of Shopify stores against 14.5% in the US,** and Klaviyo's revenue outside the Americas grew 35% in Q2 2026. Australian and UK buyers are more experienced, so lead there with deliverability depth and measurement rather than flow basics.

---

# 5. Target Audience Specification & Multi-Tier ICP Definitions

> **Bottom line:** Our ICP is a Shopify or Shopify Plus brand on Klaviyo that owns its products and its list, sells mainly through its own site, and operates in beauty, supplements, food and beverage or pet. **Lhotse** targets USD 3M to 20M in annual revenue. That is the band where email earns USD 600k to 6M a year and a USD 36k to 66k retainer beats a USD 70k to 100k+ hire. **Ascent** targets USD 1M to 50M+, including enterprise brands with internal teams that need a specialist, zero-downtime repair.

## 5.1 Hard gates

| Gate | Requirement | How we verify it |
|---|---|---|
| Platform | Shopify or Shopify Plus | Store Leads; storefront source |
| ESP | Klaviyo installed and sending | Subscribe and read the headers |
| List ownership | Own website is the main channel | Site review; Amazon is not the main call to action |
| Product ownership | Makes or owns its products | No dropship or print-on-demand apps; branded product pages |
| Revenue floor | USD 1M+ (Ascent) or the vertical floor (Lhotse) in website revenue | Store Leads estimated monthly sales |
| Geography | US, UK, Canada, Australia, Ireland or NZ, confirmed as the real operating base | Address, phone, founder profile, shipping origin |
| Lawful contact | A compliant route to a decision maker (Section 17) | Contact source recorded |

## 5.2 Ascent tiers

| | **A1: Emerging** | **A2: Growth** | **A3: Enterprise Repair** |
|---|---|---|---|
| Annual revenue | USD 1M to 3M | USD 3M to 20M | USD 20M to 50M+ |
| Estimated monthly sales | USD 83k to 250k | USD 250k to 1.67M | USD 1.67M to 4.2M+ |
| Typical staff | 3 to 10 | 8 to 40 | 40 to 80+ |
| Working SKU range | 10 to 80 | 30 to 300 | 100 to 1,000+ |
| Active Klaviyo profiles | 10k to 40k | 40k to 250k | 250k to 1M+ |
| Monthly email sends | 50k to 250k | 250k to 1.5M | 1.5M to 8M+ |
| Who signs | Founder | Founder below USD 5M; VP Marketing above | CMO or VP; finance reviews |
| Typical trigger | Shopify rewrite, shared Klaviyo domain, bots, rising bill | Microsoft spam placement, bounce spikes, peak worry | Domain migration, DMARC enforcement, incident recovery |
| Ascent angle | "Fix the foundations once, for under 0.5% of revenue" | "Protect the channel that earns you USD 1M+ a year" | "A zero-downtime specialist repair your team can hand off" |

*Staff ranges draw on Eightx data for online-first brands. SKU, profile and send ranges are GrowMailers qualification ranges. No public source reports list size by revenue band.*

## 5.3 Lhotse tiers

| | **L1: Entry** | **L2: Core (sweet spot)** | **L3: Scale** |
|---|---|---|---|
| Annual revenue | USD 3M to 5M | USD 5M to 12M | USD 12M to 20M |
| Email revenue at 20% to 30% | USD 600k to 1.5M | USD 1.0M to 3.6M | USD 2.4M to 6.0M |
| Suggested band | Core (USD 3,000 to 3,500) | Growth (USD 3,500 to 4,500) | Scale (USD 4,500 to 5,500) |
| Retainer as share of email revenue | 2.4% to 7% | 1.2% to 5.4% | 0.9% to 2.8% |
| Decision maker | Founder | VP Marketing or Head of Growth | CMO or VP; retention lead influences |
| Competing alternative | Freelancer, or the founder doing it | The first in-house hire | In-house team plus agency |
| Core pitch | "A full retention team for less than one hire" | "Stop hiring for skills you need part-time" | "Strategy, deliverability and testing your team has no time for" |

**Below USD 3M,** Lhotse would take 12% to 22% of a USD 1.5M brand's email revenue. Sell Ascent and revisit later. **Above USD 20M,** brands usually have in-house retention teams, and Ascent is the right way in.

**Vertical-adjusted Lhotse floors** (from the unit economics in Section 8):

| Vertical | Lhotse floor | Reason |
|---|---|---|
| Beauty and personal care | USD 3M | About USD 39 contribution per repeat order |
| Health and supplements | USD 3M | High margin and a 30-day reorder cycle |
| Pet supplies | USD 4M | About USD 22 per repeat order |
| Food and beverage | USD 5M | About USD 17 per repeat order |

A food or pet brand with an average order value above about USD 90, or a strong subscription base, can qualify at USD 3M.

## 5.4 Why these four verticals

US Klaviyo users over-index in these categories compared with all Shopify stores: beauty and fitness at 12.8% against 10.9%, food and drink at 8.8% against 7.1%, and health at 7.3% against 4.4%. Their customers run out of the product and come back, so owned channels pay.

| Vertical | Planning reorder cycle | Flows that earn most | Watch-outs |
|---|---|---|---|
| **Beauty and personal care** | 30 to 75 days | Quiz-led welcome, replenishment, reviews, VIP | Shade returns; discount culture |
| **Health and supplements** | 30 days | Replenishment, subscription save and dunning, education | Health claims are regulated (FTC, ASA, TGA) |
| **Food and beverage** | 14 to 45 days | Back-in-stock, replenishment, seasonal | Low margin, perishability, shipping cost |
| **Pet supplies** | 30 to 45 days | Replenishment, pet birthday, win-back | Chewy and Amazon Subscribe & Save |

*Reorder cycles are planning assumptions. Replace them with each brand's median days between orders.* Apparel is the largest category (29.1% of US Shopify stores) and a secondary target. It fits when repeat purchase is visible, as with basics, uniforms or restockable essentials.

## 5.5 Exclusion rules

| Rule | How to detect it | Action |
|---|---|---|
| Marketplace-only or marketplace-led | No real own-site checkout; "Buy on Amazon" as the main call to action | Exclude |
| Dropshipper | DSers, Zendrop, AutoDS or CJdropshipping apps; 2 to 4 week shipping; generic products | Exclude |
| Print-on-demand or creator merch | Printful, Printify, Fourthwall or Spring | Exclude |
| Non-owner merchant models | Resellers, affiliates, or white-label stores where a distributor owns the customer | Exclude |
| No ESP, or Mailchimp with no automation | No welcome email after sign-up | Nurture |
| Registered-agent address | Address matches a known agent; founder based abroad | Verify, then re-tag or exclude |
| Below the floor | Estimated sales under USD 83k a month, or under the vertical floor | Nurture; re-score quarterly |
| USD 50M+ with an in-house team | CRM job posts; large team | Ascent repair projects only |
| Personal Gmail as the only contact (Canada, UK, Ireland) | Contact data | Do not cold email |
| Hired an email agency in the last 6 months | Agency credits, announcements | Nurture; revisit in 9 to 12 months |

## 5.6 Portrait of an ideal Lhotse client

*An illustrative composite.* A USD 7M supplements brand in Austin on Shopify Plus, with 85% of revenue from its own site. It has 18 staff and a three-person marketing team under a Head of Growth. Its stack is Klaviyo, Postscript, ReCharge, Triple Whale and Gorgias. The list holds 95,000 profiles, but only about 35,000 have clicked or bought in six months. The welcome series is two emails. There is no replenishment flow, even though 60% of revenue comes from 30-day products. Email is 14% of website revenue. **It scores about 85 on LFS and 35 on AUS, which makes it a Lhotse-first account.** The first quarter would build replenishment and post-purchase flows, move campaigns to engaged segments, suppress roughly 40,000 dormant profiles (cutting the Klaviyo bill), and set up a holdout test so the Head of Growth can show the founder real incremental revenue.

---

# 6. Addressable Market Sizing & Geolocation Deep-Dive

> **Bottom line:** The serviceable pool, anchored on Shopify Plus, is roughly **4,500 brands across six countries**, two-thirds of them in the US. At a mid-point Lhotse fee that is about USD 230M a year in retainer value, and GrowMailers needs well under 1% of it. The constraint is focus and timing, not market size. Registered-agent hubs such as Sheridan, Wyoming (20,043 Shopify stores) show why every list needs geographic cleaning.

## 6.1 The store base

| Country | Live Shopify stores | Shopify Plus stores | Stores with Klaviyo | Online share of retail |
|---|---|---|---|---|
| United States | 1,179,951 | 28,965 | 203,080 | About 16.4% (2025) |
| United Kingdom | 231,312 | 6,311 | 43,546 | 27.5% (2025) |
| Canada | 147,721 | 3,812 | 22,584 | 7.5% (Jul 2026) |
| Australia | 138,276 | 3,725 | 35,621 | 24% (2025) |
| New Zealand | 26,522 | 581 | 5,322 | n/a |
| Ireland | 12,873 | 502 | 2,786 | 5.7% (Jul 2026, Irish retailers) |
| **Total** | **1,736,655** | **43,896** | **312,939** | |

*Store Leads, 18 September 2026. Klaviyo counts cover all platforms. Each country measures online share differently, so treat that column as a rough guide.*

## 6.2 From stores to serviceable brands

```
  Shopify Plus stores (six countries)                  43,896
     │ ÷ 1.5 store domains per merchant
  Distinct Plus merchants                              ≈ 29,263
     │ × 60% on Klaviyo                  ← planning assumption
  Plus merchants on Klaviyo (TAM base)                 ≈ 17,558
     │ × 30% in our four verticals       ← Klaviyo category mix
  Target-vertical merchants                            ≈ 5,268
     │ × 85% after exclusions            ← marketplace-led, POD, registry shells
  SERVICEABLE POOL (SAM base)                          ≈ 4,478 brands
```

| Country | Plus merchants | On Klaviyo | Target verticals | **Serviceable pool** | Share |
|---|---|---|---|---|---|
| United States | 19,310 | 11,586 | 3,476 | **2,955** | 66% |
| United Kingdom | 4,207 | 2,524 | 757 | **643** | 14% |
| Canada | 2,541 | 1,525 | 458 | **389** | 9% |
| Australia | 2,483 | 1,490 | 447 | **380** | 8% |
| New Zealand | 387 | 232 | 70 | **60** | 1% |
| Ireland | 335 | 201 | 60 | **51** | 1% |
| **Total** | **29,263** | **17,558** | **5,268** | **4,478** | 100% |

*Our estimates. Australia's true Klaviyo rate is probably higher, and New Zealand's food-heavy mix (13.0% of stores) probably lifts its vertical share.* **This is a floor.** Many USD 1M to 5M brands avoid the Plus fee and are missing from the count. **Validation step:** use GrowMailers' paid Store Leads account to export stores by country, filtered to Klaviyo and our categories, in estimated-sales bands of USD 83k to 833k a month and USD 833k to 1.67M a month. Then replace these assumptions with real counts.

| Layer | Definition | Brands | Annual value |
|---|---|---|---|
| **TAM** | Plus merchants on Klaviyo, any vertical, at a USD 51k Lhotse mid-point | ≈ 17,558 | ≈ USD 895M |
| **SAM** | Serviceable pool in our verticals | ≈ 4,478 | ≈ USD 228M retainer value + ≈ USD 22M one-time Ascent value |
| **SOM** (12 to 24 months) | 12 to 20 Lhotse clients and 30 to 50 Ascent projects a year | 42 to 70 | ≈ USD 0.76M to 1.27M a year (0.3% to 0.5% of SAM) |

*Our planning scenario. SOM is limited by delivery capacity, not by demand.*

## 6.3 Country roles

| Country | GTM role | Key hubs | Mailbox risk | Playbook note |
|---|---|---|---|---|
| **United States** | Primary, year-round (≈ 2,955 brands) | California, New York, Florida, Texas, New Jersey, Utah | Gmail-heavy (54.4%) | Most permissive B2B email law |
| **United Kingdom** | Secondary; strongest in Q1 (≈ 643) | London (52,471 stores) | Microsoft holds 32.3% | Test Microsoft placement in every audit |
| **Australia** | Secondary; Jan to Mar and Jul to Aug (≈ 380) | New South Wales, Victoria | Microsoft holds 30.2% | Most mature Klaviyo market; lead with depth |
| **Canada** | Selective (≈ 389) | Ontario (44.7%), Quebec (19.5%) | Microsoft holds 27.9% | Strictest law (CASL); Quebec's 28,853 stores need French |
| **Ireland** | Add-on to UK (≈ 51) | Dublin | Microsoft-heavy (assumed) | Company addresses only |
| **New Zealand** | Add-on to Australia (≈ 60) | Auckland (11,232 stores) | No public data | Food brands are 13.0% of stores |

## 6.4 US state targeting

| State | Stores with 10 to 49 staff | Klaviyo rate | Note |
|---|---|---|---|
| California | 3,407 | 16.6% | Largest cluster; beauty and wellness |
| New York | 1,730 | not read | Fashion and beauty density |
| Florida | 1,134 | 14.8% | Many stores, few brand-sized. Filter tightly. |
| Texas | 983 | 13.6% | As Florida |
| New Jersey | 469 | not read | Consumer goods and beauty |
| Utah | 411 | 18.8% | Highest Klaviyo rate read; supplements cluster |
| Illinois | 398 | 13.5% | Food and consumer goods |
| Colorado | 380 | 15.3% | Outdoor, pet, natural products |

In Florida, Texas and Georgia, only 1.0% to 1.5% of stores have 10 or more staff, against 3.0% to 3.8% in California and New York. Use stricter revenue filters there.

## 6.5 Registry traps

**Sheridan, Wyoming, a town of under 20,000 people, hosts 20,043 Shopify stores, the third-highest count of any US city.** This is not a DTC boom. Founders outside the US form LLCs through registered agents, and the agent's address becomes the store's address. The same thing happens in Cheyenne, Wyoming, in Delaware (Wilmington, Lewes, Dover), in New Mexico, and at mass virtual-office addresses in London.

**Screening SOP:**

1. Flag any address that matches a known registered-agent or virtual-office location.
2. Check for a local phone number, a real returns address and the stated shipping origin.
3. Find where the founder and team actually work, using LinkedIn or the About page.
4. If the real base is outside our six countries, exclude the account. If it is inside, re-tag it to the real country and apply that country's law.
5. Log the check in the CRM.

## 6.6 Coverage from Nepal

For a team working in Nepal time (NPT, UTC+5:45):

| Market | Local 09:00 to 17:00 in Nepal time | Approach |
|---|---|---|
| UK and Ireland | 13:45 to 21:45 (BST) / 14:45 to 22:45 (GMT) | Best overlap. Live calls in the afternoon. |
| Australia (Sydney, Melbourne) | 04:45 to 12:45 (AEST) / 03:45 to 11:45 (AEDT) | Call Australian afternoons during the Nepal morning |
| New Zealand (Auckland) | 02:45 to 10:45 (NZST) / 01:45 to 09:45 (NZDT) | Nepal mornings; schedule emails |
| US and Canada Eastern | 18:45 to 02:45 (EDT) / 19:45 to 03:45 (EST) | Evening call shift; schedule emails |
| US and Canada Pacific | 21:45 to 05:45 (PDT) / 22:45 to 06:45 (PST) | Late calls; schedule emails |

Schedule every outreach email to arrive between 08:00 and 10:00 in the recipient's time zone.

---

# 7. Organizational Structures & Decision-Maker Buying Profiles

> **Bottom line:** Below USD 5M the founder signs. From USD 5M to 20M a marketing leader signs and a retention lead influences the decision. Above USD 20M finance reviews the contract. Founders need to hear about cash and margin, growth leaders about blended efficiency, and CRM leads about relief from workload and risk. Lhotse starts competing with a salary at the point where a brand would hire its first email manager, usually between USD 3M and 8M.

## 7.1 How teams change with scale

| Revenue | Marketing team | Budget share to agencies | Who runs email | Who signs |
|---|---|---|---|---|
| USD 1M to 3M | 2 to 3 people | about 5% | Founder or freelancer | Founder |
| USD 3M to 8M | 4 to 6, including an email manager | about 7% | First email hire | Founder |
| USD 8M to 20M | 7 to 12 | about 7% | Retention lead | VP Marketing, CMO or Head of Growth |
| USD 20M to 50M | 15 to 25, led by a VP or CMO | about 5% | Head of Retention and team | CMO or VP; finance reviews |

*Recruiter and agency guides (ATTN, eCommerce Placement). No independent survey exists.*

Between about USD 3M and 15M, brands move from needing a "Klaviyo specialist" to needing a "lifecycle strategist". Many have someone who can build a flow but nobody who can design a retention strategy, and Lhotse fills that gap. Marketing spend also shrinks as a share of revenue with scale. Brands under USD 5M are estimated to spend 30% to 45%, while ten public consumer brands spend a median of 13.3%. Smaller brands feel every dollar, so L1 has to be sold as a cost-saver.

```
  USD 3M BRAND                         USD 10M BRAND                        USD 30M BRAND
       Founder/CEO                          Founder/CEO                               CEO
   ┌──────┼─────────┐             ┌─────────┼──────────┬────────┐         ┌──────┬───┴───┬─────────┐
  Ops   Marketing   CX          COO   Head of Growth  Finance   CX        CFO    CMO     COO   Head of E-com
        generalist                 ┌──────┼────────┬───────┐                ┌────┴──────────────┐
          └─ Email: founder or     Paid   Email/   Creative Content   VP Growth     Head of Retention
             freelancer            media  retention                    (paid)       ├─ Email mgr
             ◄── LHOTSE L1               mgr ◄── LHOTSE L2                          ├─ SMS mgr
                                         competes with this hire                    └─ CRM analyst
                                                                                    ◄── ASCENT A3
```

## 7.2 Buyer profiles

| | **Founder / CEO** | **VP Marketing / Head of Growth** | **CMO** | **CRM / Retention Lead** |
|---|---|---|---|---|
| Owns | Cash, margin, strategy, exit | Growth against total marketing spend | Brand, growth, team, board story | Flows, campaigns, list health, deliverability |
| Top KPIs | Cash, contribution margin, MER | MER, new-customer revenue, CAC | Growth, LTV to CAC, team productivity | Flow revenue, email share, spam and bounce rates |
| Main fear | Paying an agency that over-promises | Missing target as ad costs rise | A public failure at peak | Being blamed for an incident; burnout |
| What they need to hear | "Here's the cost, the payback, and how you'll know." | "Owned revenue lowers blended CAC. Here's the MER impact." | "Specialist depth, measured by holdout, no risk to peak." | "We take the grunt work and fix what you haven't had time for." |
| Proof they trust | A model built with their own numbers | Holdout-tested lift | Case studies at their scale | Technical findings and a clear SOP |
| Best lead offer | Ascent A1 or Lhotse Core | Lhotse Growth | Ascent A3, then Lhotse Scale | Ascent, positioned as their ally |
| Deal-killers | Vague promises, long lock-ins | Vanity metrics | A junior team, no risk plan | Anything that threatens their role |

## 7.3 Objection-handling playbook

| Objection | Behind it | Response | Proof |
|---|---|---|---|
| "We already have an agency." | Inertia, sometimes quiet dissatisfaction | "No need to switch. Ascent is a one-time technical repair most agencies don't do. Here's what your headers show." | External audit |
| "We'll do it in-house." | Belief that a hire is cheaper | "A good hire costs USD 85k to 135k fully loaded and brings one skill set. Lhotse is USD 36k to 66k for a team." | Section 1.3 comparison |
| "Our open rates are fine." | Opens inflated by Apple MPP | "Apple auto-opens most mail. Let's look at clicks and placed orders." | Section 10 benchmarks |
| "Klaviyo says deliverability is fine." | Averages hide problem providers | "About a third of UK, Canadian and Australian inboxes are Microsoft. Let's check by provider." | Provider-level check |
| "Not now, it's Black Friday prep." | A genuine freeze | "Agreed, no retainer now. Here are two freeze-safe fixes, and let's book January." | Section 16 fix list |
| "Too expensive." | Unclear ROI or tight cash | "At your margins, Lhotse needs about 80 to 140 extra repeat orders a month. You do 6,000." | Section 8 breakeven |
| "An agency failed us before." | Past over-promising | "What did they measure? We report holdout-tested lift, not platform credit." | Sample holdout report |
| "Isn't DMARC at p=none a fail?" | Scare tactics from past vendors | "No, p=none meets every mailbox provider's rules. Enforcement is best practice, done carefully." | Section 13 |

---

# 8. Financial Dynamics, Margin Structures & Category Unit Economics

> **Bottom line:** In every target vertical, the first paid-media order barely breaks even or loses money, and profit begins with the second order. Beauty and supplements have the margins that let Lhotse pay for itself fastest: it needs incremental orders equal to only about 1% to 2.5% of a mid-size brand's monthly orders. Food and pet earn less per order, so their Lhotse floor is higher. Discounting in flows can wipe out a third of a repeat order's contribution, which makes managing discounts part of the Lhotse job.

## 8.1 What real DTC financials show

| Company (year) | Revenue | Gross margin | Marketing spend | Profit |
|---|---|---|---|---|
| FIGS, US apparel (FY2025) | USD 631.1M | 66.5% | 14.8% of revenue | Net 5.4% |
| Hims & Hers, US telehealth (FY2025) | USD 2,347.6M | 74% | 39% of revenue | Net 5.5% |
| Temple & Webster, AU home (FY26) | A$665M | 30.2% (delivered) | 15.2% of revenue | EBITDA 3.3% |

Even at scale and with strong gross margins, DTC net margins sit around 5%. The durable ones are built on repeat customers. At Temple & Webster, 62% of FY26 orders came from repeat customers. FIGS earns about USD 216 per active customer a year, and Hims & Hers about USD 81 per subscriber a month.

## 8.2 Unit economics by vertical

| Vertical | Median order value | Gross margin* | Fulfilment and payments* | Median ad cost per purchase | **First-order contribution** | **Repeat-order contribution** |
|---|---|---|---|---|---|---|
| Apparel | USD 103.37 | 60% | 15% | USD 39.24 | **USD 7.27** | **USD 46.51** |
| Beauty | USD 68.29 | 72% | 15% | USD 33.44 | **USD 5.49** | **USD 38.93** |
| Supplements | USD 71.26 | 72% | 14% | USD 44.81 | **−USD 3.48** | **USD 41.33** |
| Food and beverage | USD 69.87 | 45% | 20% | USD 28.96 | **−USD 11.49** | **USD 17.47** |
| Pet | USD 69.95 | 50% | 18% | USD 32.68 | **−USD 10.29** | **USD 22.39** |

*Order values and ad costs are Triple Whale medians for US DTC brands (90 days to 21 September 2026, its own customers). \*Gross margin and fulfilment rates are GrowMailers planning assumptions, more conservative than the FIGS example in Section 1.4. Replace them with the prospect's real numbers during discovery.* Triple Whale's ad cost figure includes returning buyers, so the true first-order contribution is *worse* than shown.

## 8.3 LTV curves

```
  CUMULATIVE CONTRIBUTION PER CUSTOMER (USD, one block ≈ USD 5; ▒ = loss)

                  After order 1        After order 3
  Apparel         █  7                 ████████████████████  100
  Beauty          █  5                 █████████████████  83
  Supplements     ▒  −3                ████████████████  79
  Pet             ▒▒ −10               ███████  34
  Food & bev      ▒▒ −11               █████  23
```

| Vertical | 12-month expected orders | 12-month contribution | 24-month expected orders | 24-month contribution |
|---|---|---|---|---|
| Apparel | 1.4 | USD 25.87 | 1.7 | USD 39.83 |
| Beauty | 1.6 | USD 28.85 | 2.1 | USD 48.31 |
| Supplements | 2.2 | USD 46.12 | 3.0 | USD 79.18 |
| Food and beverage | 2.0 | USD 5.98 | 2.8 | USD 19.96 |
| Pet | 2.3 | USD 18.82 | 3.3 | USD 41.21 |

*Expected order counts are planning assumptions. No method-backed public benchmark for repeat rate by category exists, and the widely quoted "25% to 30%" traces back to blog posts. Use each brand's own cohort data.*

Supplements has the strongest 12- and 24-month economics, because its 30-day reorder cycle quickly turns a slightly negative first order positive. Food is thin at every step and only scales through frequency and bigger baskets. That is why replenishment timing and bundles matter most in food and pet.

## 8.4 What Lhotse and Ascent must earn

| Vertical | Repeat contribution | Lhotse at USD 3,000/mo | Lhotse at USD 5,500/mo | Ascent (USD 5,000 once) |
|---|---|---|---|---|
| Apparel | USD 46.51 | 65 orders/mo | 119 orders/mo | 108 orders |
| Beauty | USD 38.93 | 78 | 142 | 129 |
| Supplements | USD 41.33 | 73 | 134 | 121 |
| Food and beverage | USD 17.47 | 172 | 315 | 287 |
| Pet | USD 22.39 | 134 | 246 | 224 |

**In context:** a USD 5M beauty brand does about 6,100 orders a month, so Lhotse needs 78 to 142 of them to be *incremental*, or 1.3% to 2.3%. A USD 5M food brand does about 5,960 orders and needs 172 to 315, or 2.9% to 5.3%. That is achievable but demanding, which is why the food floor is USD 5M and why holdout testing matters most in low-margin verticals.

## 8.5 Sensitivity: what moves the model

| Lever | Change | Effect (beauty) |
|---|---|---|
| Repeat rate | +5 points on a 25% base | About 20% more repeat orders |
| Repeat order value | +10% through bundles | Contribution per repeat order rises from USD 38.93 to about USD 43.85 |
| Frequency | Reminder moved from day 45 to day 38 for a 40-day product | Catches buyers before they switch brands |
| **Discount leakage** | **20% off every repeat order** | **Contribution falls from USD 38.93 to USD 25.27 (−35%)** |

Many brands put a 15% to 20% code in every flow email out of habit. On a USD 68 beauty order, 20% off removes USD 13.66 of revenue while product and shipping costs stay the same. Saving discounts for win-back, first-order conversion and peak, and using education and social proof elsewhere, can add more profit than any new flow. **In sales:** rebuild this model live on every discovery call using the prospect's own numbers. When their spreadsheet shows Lhotse needs only 1% to 3% of monthly orders, the price objection usually goes away.

---

# 9. Operational Cycles & the Annual E-Commerce Cash Calendar

> **Bottom line:** Brands pay for fourth-quarter stock in summer, so cash is tightest in August and September and most plentiful in January and February. That cycle, more than any marketing calendar, decides when a founder will sign a retainer. Sell Lhotse when budgets reset and cash returns. Sell Ascent's fast, low-risk fixes when pressure is high.

## 9.1 The inventory cash cycle

```
  MAY–JUN        JUN          LATE JUN        SEP              OCT–NOV        DEC           JAN
  Forecast Q4 ─► Purchase ──► 30% factory ──► 70% balance ───► Stock lands ─► Revenue ───► Returns,
  demand         orders       deposit         on arrival       at 3PL         peaks        cash dip
                                              ▲ PEAK CASH OUTFLOW              ▲ PEAK INFLOW
                                              worst time to ask for a retainer  email sells stock
                                                                                already paid for
```

That last point gives Ascent a cash argument in the fourth quarter: *every order lost to the spam folder is inventory you have already paid for.*

## 9.2 Month-by-month calendar

| Month | Cash and inventory | Brand focus | Pitch window | GrowMailers motion |
|---|---|---|---|---|
| **January** | Returns land (US online returns were 19.3% in 2025); new budgets | Post-peak review; resolutions (supplements) | ★★★★★ | **Best window.** Lhotse on post-peak data; Ascent for December bounce victims |
| **February** | Recovering | Valentine's Day; Mothering Sunday prep (UK and Ireland) | ★★★★★ | Lhotse starts |
| **March** | Stable | Mothering Sunday (7 Mar 2027); Easter | ★★★★ | Lhotse for US, Canada and non-gifting brands; Ascent everywhere |
| **April** | Stable; UK tax year starts | Mother's Day build | ★★★★ | Both; Australian brands plan EOFY |
| **May** | Q4 forecasting | Mother's Day (9 May 2027); Australian EOFY prep | ★★★ | Australian brands must be ready by early May |
| **June** | Q4 orders and deposits go out | Father's Day; Australian EOFY sales | ★★★★ | **Second window opens:** Black Friday readiness |
| **July** | Tightening; Australian budgets reset | Prime Day; US back-to-school | ★★★★ | Lhotse starts still have time for peak; Ascent domain projects |
| **August** | Tight; stock in transit | Black Friday planning and audits | ★★★ | Ascent first; last Lhotse starts that can be fully peak-ready |
| **September** | **Peak cash outflow** | Peak creative and segmentation | ★★ | Last call; new sending domains start warming by mid-September |
| **October** | Stock arrives; setup locks | Prime Big Deal Days; volume ramp | ★ | Freeze-safe Ascent fixes until about 16 October |
| **November** | **Change freeze** | Black Friday and Cyber Monday | ☆ | No pitching. Book January starts. |
| **December** | Peak revenue | Shipping cut-offs; Boxing Day | ☆ | Book January. December pain feeds January pitches. |

## 9.3 Fiscal-year differences and cash signals

The US and Canada mostly run calendar fiscal years, so January is their buying moment. Some UK and Irish brands reset budgets in April. **Australia runs July to June,** which gives two good windows, January to March and July to August after EOFY. New Zealand often runs April to March.

| Outside signal | What it suggests | Implication |
|---|---|---|
| Heavy discounting in August and September emails | Excess stock or a cash squeeze | Lead with Ascent or margin protection; delay the Lhotse pitch |
| Pre-orders or "ships in 6 weeks" notices | Cash tied up in inventory | Low-commitment, value-first approach |
| Product launches and hiring posts | Growth mode | Lhotse, framed as scaling what already works |
| Funding announcement | Budget and pressure to grow | Lhotse Scale with board-ready reporting |
| Founder posting about tariffs or ad costs | Margin pressure is front of mind | Lead with retention economics (Sections 3 and 8) |

---

# 10. Email Marketing Performance Benchmarks & Measurement Systems

> **Bottom line:** Open rates have stopped meaning much, because Apple's privacy feature auto-opens most mail. Judge a program on click rate, placed-order rate, revenue per recipient, share of website revenue and, above all, holdout-tested incremental lift. Healthy DTC brands earn 20% to 30% of website revenue from email and SMS. Below 8%, there is no real program.

## 10.1 How much revenue email should drive

| Email and SMS share of website revenue | Reading | GrowMailers action |
|---|---|---|
| Under 8% | No real program | Lhotse full build, flows first |
| 8% to 20% | Underbuilt | Lhotse: flow gaps and segmentation |
| 20% to 30% | Healthy | Lhotse: optimization and testing |
| 30% to 40% | Top quartile | Ascent to protect it; Lhotse Scale if the team is stretched |
| Above 40% | Check attribution | Often a generous attribution window, heavy discounting or low paid spend |

*Flypost (50+ DTC brands on Klaviyo); Level CFO puts the median at 18% to 22%.*

**Always record the attribution window.** Klaviyo credits any order within five days of an open or click to email. That overstates email's real effect, and machine opens make it worse. Merchants have publicly reported Klaviyo claiming several times more conversions than they could verify.

## 10.2 Platform benchmarks

| Measure | Klaviyo campaigns | Klaviyo flows | Omnisend campaigns | Omnisend flows |
|---|---|---|---|---|
| Click rate | 1.69% | 5.58% | 0.74% | 4.66% |
| Placed-order rate | 0.97% to 1.34% | 1.62% to 2.17% | 0.08% | 1.49% |
| Unsubscribe rate | not shown | not shown | 0.20% | 0.59% |

*Klaviyo 2026 benchmarks; Omnisend 2025 data. The platforms define clicks and orders differently, so compare a brand only with its own platform's figures.* **Rule of thumb:** on Klaviyo, a campaign placed-order rate well below 1% signals a program problem.

## 10.3 The Apple MPP distortion

Apple Mail Privacy Protection (MPP) pre-loads messages, which registers an "open" whether or not anyone reads the email. Litmus reported Apple at 62.26% of tracked opens in July 2026, with MPP affecting roughly 55% to 60% of all opens. Omnisend's average open rate rose from 26.6% to 30.7% between 2024 and 2025, driven by machines, not people. The distortion does three kinds of damage. **Engagement segments get polluted** ("opened in 90 days" includes people who never looked), **subject-line tests become unreliable**, and **sunset policies fail** because a machine-opened profile never looks inactive. The fix is to define engagement by clicks, site activity and orders, exclude Apple privacy opens wherever the platform allows it, and treat opens as a diagnostic only. A sudden drop in opens at a single provider still points to a placement problem.

```
            ▲ Most trustworthy
   INCREMENTAL REVENUE ........ holdout-tested lift (the CFO's number)
   REVENUE PER RECIPIENT ...... reach × relevance × conversion
   PLACED-ORDER RATE .......... did the email produce purchases?
   CLICK RATE ................. did a human engage?
   DELIVERABILITY HEALTH ...... bounces, complaints, provider placement
   OPEN RATE .................. diagnostic only (distorted by MPP)
            ▼ Least trustworthy
```

## 10.4 Operating targets for a Lhotse client

| Metric | Healthy | Act when |
|---|---|---|
| Campaign click rate (Klaviyo) | 1.5% to 2%+ | Below 1% for four weeks |
| Campaign placed-order rate (Klaviyo) | About 1% or better | Well below 1% |
| Spam complaint rate | Below 0.05% | Above 0.05% (Klaviyo flags it); above 0.1% (Gmail's line) means act now |
| Bounce rate | Below 1% | Above 2% (Klaviyo flags it) |
| Campaign frequency | 2 to 5 a week; up to daily at peak | Only with engagement-based targeting |

## 10.5 Incrementality testing

**Flow holdout SOP:**

1. Add a random split at flow entry: 90% get the flow, 10% get nothing (use 80/20 for smaller brands).
2. Measure orders from both groups over the same window, such as 14 days.
3. Run for at least four weeks, and until the holdout group has 100+ orders.
4. Incremental orders = (mailed conversion − holdout conversion) × mailed recipients.
5. Report platform-attributed and incremental revenue side by side.

| Illustration | Mailed (90%) | Holdout (10%) |
|---|---|---|
| Entrants per month | 18,000 | 2,000 |
| 14-day conversion | 4.0% (720 orders) | 2.8% (56 orders) |
| Incremental orders | 1.2 points × 18,000 = **216** | |
| At USD 68 order value | **USD 14,688 incremental a month**, against USD 48,960 platform-attributed | |

In this example, about 30% of attributed revenue is truly incremental, and that is still a strong result. A client who hears the honest number from GrowMailers first will trust every number after it. **Campaign holdouts** work the same way: leave a random 10% out of all campaigns for a month. **Ascent** is measured before and after: placement by provider, Gmail spam rate, bounces and revenue per recipient, compared with the same weeks a year earlier.

**Monthly client scorecard:** revenue share (with the attribution window stated), flow vs. campaign split, revenue per recipient, holdout results against fees, click and order rates by segment, Gmail spam rate, bounces, DMARC pass rate, net list growth, profiles suppressed and Klaviyo tier.

---

# 11. Automated Email Flow Architecture vs. Campaign Blasts

> **Bottom line:** Flows earn far more per email than campaigns. Klaviyo's 2026 data shows flows producing about 41% of email revenue from 5.3% of sends, at nearly 18 times the revenue per recipient. Campaigns still bring in most email revenue, though. A managed program needs both: a complete flow system as the foundation, and a segmented, disciplined campaign calendar on top.

## 11.1 Flows vs. campaigns

| | Flows (behaviour-triggered) | Campaigns (one-off sends) |
|---|---|---|
| Share of sends | About 2% to 5% | About 95% |
| Share of email revenue | About 30% to 41% | About 60% to 70% |
| Revenue per email (Omnisend) | USD 2.87 | USD 0.18 |
| Share of revenue from new buyers | About 48% | About 16% |
| Deliverability effect | Positive (engaged recipients) | Risky if unsegmented |

Nearly half of flow revenue comes from new buyers, so flows also convert new sign-ups. The best brands send fewer campaigns to tighter, engaged segments and put the time saved into their flows.

## 11.2 Lifecycle map and build order

```
  VISITOR ──sign-up──► SUBSCRIBER ──1st order──► CUSTOMER ──2nd order──► REPEAT ──► VIP
  Browse / cart /       Welcome series            Post-purchase           Replenishment   VIP perks
  checkout abandonment                            Review request          Cross-sell      Early access
                              ◄──── lapsed ──── WIN-BACK ◄──── no response ──► SUNSET → SUPPRESS
```

Abandoned cart and welcome flows produced 76% of all automated orders on Omnisend in 2025. For a brand starting from little, build in this order: abandoned checkout and cart, welcome, browse abandonment, post-purchase and reviews, back-in-stock, **replenishment** (the most important flow for our four verticals), win-back, then VIP, birthday and sunset.

## 11.3 Flow SOP specifications

| Flow | Trigger and filters | Messages and timing | Content | Incentive policy |
|---|---|---|---|---|
| **Welcome** | Joins list; exits on first order | 4 to 5: immediately, day 1 to 2, day 3 to 4, day 6 to 7, day 10 to 12 | Story, best-sellers, proof, education, founder note | First-order offer in email 1 with an expiry reminder; no stacking |
| **Abandoned checkout** | Started checkout, no order; 7-day re-entry block | 3 (+1 SMS with consent): 1 to 4 hours, 24 hours, 48 to 72 hours | Cart contents, reassurance, objection handling | Offer in the last message only, first-time buyers only |
| **Abandoned cart** | Added to cart, no checkout | 2: 2 to 4 hours, 24 hours | Product and reviews | None |
| **Browse abandonment** | Viewed product (identified); capped at 1 per 7 to 14 days | 2: 2 to 6 hours, 24 to 48 hours | Viewed item, alternatives | None |
| **Post-purchase** | Order placed or fulfilled; first-time vs. repeat split | 3 to 5 over about 30 days | Thanks, how-to, review request at 10 to 21 days after delivery, cross-sell at 21 to 30 days | Loyalty or referral, not discounts |
| **Replenishment** | Days since purchase of a consumable; exits on reorder | 2 to 3, starting about 7 days before run-out | "Running low?", one-click reorder, subscribe-and-save | Subscription discount only |
| **Back-in-stock** | Alert request; stock above threshold | 1 to 2 (+SMS) on restock | It's back; limited quantity | None |
| **Win-back** | No order in 1.5 to 2× the median days between orders | 3 over 2 to 3 weeks | What's new, best-sellers | Tiered: none, soft, then a real offer last |
| **VIP** | Top 5% to 10% by spend, or third order | Welcome, then monthly perks | Early access, exclusives | Access, not discounts |
| **Sunset** | No click, visit or order in 120 to 180 days | 1 to 2 re-permission emails | "Still want to hear from us?" | Optional |

In Omnisend's 2025 data, back-in-stock converted at 6.72% (USD 9.14 per email), welcome at 2.11% (USD 6.16) and abandoned cart at 1.72% (USD 3.59).

**Edge cases.** *Subscription customers* skip replenishment and win-back and get their own lifecycle: charge reminders, skip or swap prompts, and dunning. *Gift orders* (those with a gift message) get a "for yourself" cross-sell instead of replenishment. *Multi-SKU carts* trigger replenishment from the shortest-cycle item. *Discount-only buyers* get bundles or free-shipping thresholds rather than codes. *Canadian cart abandoners* can only be emailed with consent or an existing business relationship (CASL).

## 11.4 Campaign architecture

| Element | Standard |
|---|---|
| Cadence | 2 to 5 a week normally; up to daily in Black Friday week, for engaged tiers only |
| Segments | Engaged (clicked, visited or ordered in 30 days); warm (31 to 90 days); cool (91 to 180 days); older goes to sunset |
| Rotation | Engaged get every send; warm get 1 to 2 a week; cool get the strongest monthly send |
| Content mix | About 40% product and launches, 30% education and story, 20% social proof, 10% offers (outside peak) |
| Testing | One variable at a time, judged on clicks and placed orders, never opens |

The best-documented case for engagement-based targeting is Patrick Ta Beauty's Black Friday 2024. The brand sent nearly six times its usual volume, but to properly segmented audiences. Its unsubscribe rate fell 37%, and email drove 30% of online revenue, up from 10% the year before (Klaviyo case study).

**SMS layering.** Klaviyo SMS costs about USD 0.009 to 0.012 per US text and earns mainly through automations. Use it where speed matters: abandoned checkout, back-in-stock, shipping updates and time-limited peak offers. Keep SMS campaigns to a few a month. US marketing texts need express written consent under the TCPA, and quiet hours must be respected.

## 11.5 Scenario: flow rebuild for a USD 6M pet brand

*Illustrative.* **Before:** a one-email welcome with 10% off, an abandoned checkout flow offering 15% in every message, no replenishment, browse or win-back flows, and four full-list campaigns a week to 70,000 profiles. Email is 11% of website revenue. **Lhotse's first 90 days:** in weeks 1 to 2, rebuild engagement tiers on clicks and orders and move 24,000 dormant profiles into sunset. In weeks 2 to 4, launch a five-email welcome series (pet-type quiz, founder story, reviews, vet-backed education, then the offer) and limit the checkout discount to the last email for first-time buyers. In weeks 4 to 8, add replenishment for the three best-selling food SKUs (45-day cycle, first reminder at day 38, subscribe-and-save offer) and browse abandonment. In weeks 8 to 12, add a 90-day win-back, a "gotcha day" flow using quiz data, and 10% holdouts on welcome and replenishment. **Measure:** email share, holdout lift, discount cost per order and the Klaviyo tier after suppression. In a food-led pet brand we would expect replenishment to become a top revenue flow within one or two reorder cycles. Proving it with a holdout is what turns a trial quarter into a long retainer.

---

# 12. Subscriber Database Hygiene, List Management & ESP Cost Control

> **Bottom line:** Klaviyo bills on every active profile. Dormant subscribers and bot sign-ups therefore cost a brand twice, once on the invoice and again in inbox placement. Engagement tiers, a sunset flow, careful suppression and bot defences answer the most common owner complaint (a rising bill with flat revenue) and improve deliverability at the same time.

## 12.1 Klaviyo billing

Since 18 February 2025, Klaviyo has billed on all active profiles, and it upgrades the plan automatically when a limit is passed. Suppressed profiles leave the bill but can no longer receive email or enter flows, so suppression is a marketing decision, not just a way to save money.

| Active profiles | 1,000 | 5,000 | 10,000 | 25,000 | 50,000 | 250,000 |
|---|---|---|---|---|---|---|
| Email price per month | USD 30 | USD 100 | USD 150 | USD 400 | USD 700 | USD 2,300 |

*SendX, a secondary source. Check Klaviyo's live prices before quoting. A USD 1M to 10M brand with 25,000 to 100,000 profiles probably pays USD 400 to 1,400+ a month for email alone (our estimate).*

```
  A TYPICAL UNMANAGED LIST: 60,000 ACTIVE PROFILES (illustrative; one block ≈ 1,500)
  Engaged (≤ 30 days)   ████████                 12,000  20%  ← earns most revenue
  Warm (31–90 days)     ██████                    9,000  15%
  Cool (91–180 days)    ████                      6,000  10%
  Dormant (180+ days)   ████████████████████     30,000  50%  ← costs money, hurts placement
  Bots / invalid        ██                        3,000   5%  ← costs money, causes bounces
```

One owner described this exact pattern publicly: paying for more than 50,000 profiles while about 15,000 engaged, with flat revenue and a rising bill. Suppressing the dormant and bot segments here takes the list to about 27,000 profiles. That cuts the email bill by roughly USD 300 a month or more (our estimate), and the remaining mail goes to people who respond.

## 12.2 Engagement tiers and suppression rules

| Tier | Definition (no opens) | Treatment |
|---|---|---|
| **Engaged** | Clicked, visited or ordered in 30 days, or joined in 30 days | Every campaign |
| **Warm** | Same signals, 31 to 90 days ago | 1 to 2 campaigns a week |
| **Cool** | Same signals, 91 to 180 days ago | Strongest monthly send; targeted win-back |
| **Dormant** | Nothing in 180+ days | Sunset flow, then suppress |
| **Protected** | Ordered in 12 months, active subscriber, VIP, or open order or ticket | Never suppress automatically; keep in post-purchase and transactional mail |

**Suppress:** hard bounces and spam complainers (Klaviyo does this automatically), sunset non-responders, confirmed bots, disposable and malformed addresses, and profiles that got 3+ emails in 180 days with no click, visit or order. That is Klaviyo's cleaning guideline with opens removed.

## 12.3 Sunset policy SOP

1. **Entry:** no click, visit or order in 180 days *and* no order in 12 months. Use 270 days for long buying cycles.
2. **Re-permission:** 1 to 2 emails over 7 to 10 days, with a one-click "yes, keep me".
3. **Responders** go back to the warm tier.
4. **Non-responders** are suppressed with a reason tag (such as sunset_2026Q4), so the action can be audited and reversed.
5. **Run it continuously as a flow,** not as an annual purge.
6. **Report** the profiles removed, the tier change, and the change in click and order rates.

One manufacturer who excluded unengaged profiles and added a sunset flow publicly reported opens rising from the 45% to 55% range to 65% to 70%. Opens are imperfect, but the direction holds: mailing fewer, more engaged people improves every other metric.

## 12.4 Bots and list bombing

**List bombing** is bots flooding sign-up forms with real or fake addresses. The brand then pays for junk profiles and its welcome emails bounce or hit spam traps. Warning signs: sign-up spikes at odd hours or from one country, random-string names or URLs in name fields, high bounces on welcome email 1, and clusters of obscure domains.

**Controls:** CAPTCHA or bot protection on every form; a hidden honeypot field; double opt-in for high-risk sources (footer forms, countries the brand doesn't ship to, API sign-ups); blocking disposable domains; alerts when daily sign-ups exceed three times the trailing average; and suppressing any affected cohort. This matches Klaviyo's own guidance. **Never buy lists.** Bought lists carry spam traps and dead addresses, and one documented case bounced 12% hard on its first send.

---

# 13. Technical Email Deliverability Engineering & Authentication Protocols

> **Bottom line:** SPF, DKIM and an aligned DMARC record are the price of entry at Gmail, Yahoo and Microsoft, and all three now reject bulk mail that fails. DMARC at `p=none` meets every current mandate. Moving to `p=quarantine` and then `p=reject` is best practice that we carry out step by step, guided by report data. It should never be thrown at a prospect as an accusation. Every ICP brand is a bulk sender, and most have at least one sender (a helpdesk, a reviews app or a subscription tool) that is not aligned.

## 13.1 How authentication fits together

```
   WHAT THE RECEIVING SERVER SEES                         WHAT IT CHECKS
   From:         hello@brand.com         ◄ visible sender     DMARC: did SPF or DKIM pass AND
                                                              align with this domain?
   Return-Path:  bounces@send.brand.com  ◄ envelope sender    SPF: is this IP allowed to send
                                                              for send.brand.com?
   DKIM-Signature: d=send.brand.com; s=selector1; ...         DKIM: does the signature verify
                                                              against the key in DNS?
   ALIGNMENT (relaxed): send.brand.com and brand.com share an organizational domain → aligned
```

**SPF** checks the *envelope* sender, not the From address the customer sees. **DKIM** signs the message, and the signature usually survives forwarding. **DMARC** ties both back to the *visible* From domain through **alignment**, and tells receivers what to do with mail that fails.

## 13.2 SPF

```
brand.com.  IN TXT  "v=spf1 include:_spf.google.com include:mail.helpdesk-vendor.example ~all"
                     version  Google Workspace       a support tool sending as @brand.com  soft-fail the rest
```

| Rule | Failure it causes |
|---|---|
| **One record per hostname.** Two `v=spf1` records make SPF invalid. | Permanent error: SPF fails for every sender |
| **10 DNS-lookup limit.** `include`, `a`, `mx`, `ptr`, `exists` and `redirect` all count, including nested includes. | Permanent error, usually triggered when an eleventh app is added |
| **2 void-lookup limit.** | Permanent error |
| **SPF checks the Return-Path, not the From.** | SPF can pass while DMARC fails on alignment |
| **SPF breaks on forwarding.** | Why DKIM alignment is the more reliable way to pass DMARC |
| **Qualifiers.** `~all` is the norm, `-all` is stricter, `+all` is never acceptable. | `+all` authorizes the whole internet |
| **255-character limit per TXT string.** | Split long records into several quoted strings |

Klaviyo's branded sending domain lives on a subdomain (for example `send.brand.com`), and its DNS records cover SPF and DKIM there. Do not add Klaviyo to the root SPF record unless Klaviyo's setup screen asks for it. Shopify's own DNS records handle SPF for Shopify-sent mail.

## 13.3 DKIM

The signature header names the signing domain (`d=`) and selector (`s=`). The public key sits at `<selector>._domainkey.<d-domain>` and can be queried with `dig +short TXT selector1._domainkey.send.brand.com`, or as a CNAME when the ESP delegates the key.

| Standard | Requirement |
|---|---|
| Key length | 2048-bit RSA where supported; 1024-bit minimum |
| Alignment | `d=` is the From domain or a subdomain of it |
| Coverage | *Every* tool that sends as @brand.com: Workspace or Microsoft 365, Klaviyo, helpdesk, reviews, subscriptions |
| Rotation | ESP-managed CNAME keys rotate automatically. Rotate self-managed keys at least yearly and after vendor or admin changes. Keep the old key published for 7+ days so rotation causes no downtime. |

## 13.4 DMARC

A starter record at `_dmarc.brand.com`:

```
v=DMARC1; p=none; rua=mailto:dmarc-reports@brand.com; adkim=r; aspf=r
```

| Tag | Meaning | Default |
|---|---|---|
| `p` / `sp` | Policy for the domain / its subdomains: `none`, `quarantine`, `reject` | Start at `none` |
| `np` | Policy for subdomains that don't exist (updated standard) | `reject` once enforced |
| `rua` | Where aggregate reports go | Always set it |
| `adkim` / `aspf` | Alignment mode, relaxed (`r`) or strict (`s`) | Relaxed |
| `t` | Testing flag (`t=y`) that replaces the retired `pct` tag | Use while moving to quarantine |

**The updated DMARC standard (2026) removed `pct`.** A missing `pct=100` is not a finding. Raising it with a technical buyer tells them we are out of date.

| Phase | Record | Duration | Exit criteria |
|---|---|---|---|
| **0. Publish** | `p=none` + `rua` | Day 0 | Reports arriving |
| **1. Discover** | `p=none` | 2 to 4 weeks | Every sending source identified as legitimate or unknown |
| **2. Align** | `p=none` | 2 to 6 weeks | Every legitimate source passes aligned SPF or DKIM; about 98%+ of legitimate volume passes for two weeks in a row |
| **3. Quarantine** | `p=quarantine` (optionally `t=y` first) | 2 to 4 weeks | No legitimate failures; no reports of missing mail |
| **4. Reject** | `p=reject`; add `np=reject` | Ongoing | Weekly report review; every new tool added through a change request |

**Senders to inventory on a Shopify brand:** Google Workspace or Microsoft 365, Klaviyo, Shopify notifications and Shopify Email, the helpdesk, ReCharge, the reviews and loyalty apps, invoicing, HR and recruiting tools, and 3PL notifications. The ones that break enforcement are the ones nobody remembers.

**Why Shopify brands in particular.** Shopify rewrites the sender to shopifyemail.com when a domain has *no* DMARC record *or two* of them. Both are visible from outside, and both are clean Ascent findings. Gaps are common even at scale. dmarcian found that among the top 500 US retail domains, 31% are at `p=reject`, 15% at `quarantine` and 28% at `none`, while 13% have no record and 13% have broken records. Only 25% of the top 100 Canadian retail domains enforce DMARC.

## 13.5 Mailbox provider bulk-sender mandates

| Requirement | Gmail | Yahoo / AOL | Microsoft |
|---|---|---|---|
| Bulk threshold | About 5,000+ a day to personal Gmail, counted across the domain and its subdomains. Once reached, bulk status is permanent. | Bulk senders (no published number) | 5,000+ a day |
| SPF + DKIM | Required | Required | Required |
| DMARC | Required; `p=none` is enough; must align with From | Required, and must pass | At least `p=none`, aligned with SPF or DKIM |
| One-click unsubscribe | Required for marketing mail | Required; honour within 2 days | Expected |
| Spam rate | Below 0.1%; never 0.3% | Below 0.3% | Low complaints expected |
| Enforcement | Rejects some non-compliant mail (since Nov 2025). Above 0.3%, Gmail stops mitigation until the rate stays below 0.3% for 7 straight days. | Rejects or filters | Rejects with `550 5.7.515` (since 5 May 2025) |

**Every ICP brand is a bulk sender.** Gmail holds 54.4% of US inboxes, so one campaign to about 9,200 US profiles probably crosses Gmail's threshold (our estimate). **Rejected mail shows up as bounces** in the ESP, not in a test-inbox screenshot, so always read the bounce reasons.

## 13.6 Klaviyo sending setup

New Klaviyo accounts send from a shared IP and a shared Klaviyo domain, and inherit that domain's reputation. Gmail shows this as "via klaviyomail.com". Klaviyo requires bulk senders to set up a branded sending domain, and recommends one with DMARC for any account above 5,000 profiles. Its warning thresholds are stricter than Gmail's: it flags spam complaints above 0.05% (Gmail's line is 0.1%) and bounces above 2%. **Blocks on the shared pool are Klaviyo's to resolve,** and every Ascent scope must say so.

## 13.7 Pitch-accuracy guardrails

| Not a finding | Why |
|---|---|
| "DMARC is only p=none." | `p=none` satisfies all three providers |
| "You're missing pct=100." | `pct` has been removed from the standard |
| "No BIMI is hurting delivery." | BIMI displays a logo and has no effect on placement |
| "Promotions tab = deliverability problem." | Gmail treats Promotions as an inbox tab |
| "One seed shows spam, so you're blocked." | Seeds have no engagement history |

**Lead instead with:** no DMARC record or two records; failed alignment; the shared Klaviyo domain above 5,000 profiles; the Shopify sender rewrite; SPF over its lookup limit; missing one-click unsubscribe; transactional mail landing in spam.

## 13.8 Ascent zero-downtime delivery SOP

| Days | Workstream | Actions | Safeguard |
|---|---|---|---|
| 0 | Access and baseline | Read-only Klaviyo access; DNS or IT contact; Google Postmaster Tools verification; DMARC report mailbox; metric snapshot | No DNS changes yet |
| 1 to 3 | Inventory and quick wins | List all senders; bring SPF under 10 lookups; remove duplicate records; publish DMARC `p=none` if missing | Add records before removing any; one change at a time |
| 3 to 5 | Alignment | Branded sending domain in Klaviyo; DKIM for Workspace, helpdesk, reviews and subscriptions; confirm one-click unsubscribe | Old sending path stays live until the new one verifies |
| 5 to 10 | Hygiene | Suppress bounces, bots and dormant profiles; build engagement tiers; launch sunset flow; bot protection on forms | Suppressions tagged and reversible |
| 10 to 14 | Warm-up and repair | Start the warm-up schedule (Section 14.4); fix problem providers (Microsoft first in the UK, Canada and Australia); handover document | Flows keep sending throughout |
| Weeks 3 to 12 | Monitor and enforce | Weekly metrics; DMARC toward reject as reports allow; 30-day review; Lhotse proposal if the brand fits | Rollback plan for every DNS change |

Enterprise (A3) clients usually want their own IT team to make DNS changes. For each step, give them a change request listing the exact records, why each is needed, how to verify it and how to roll it back.

---

# 14. Inbox Placement Testing, Domain Reputation & Risk Management

> **Bottom line:** A seed test shows how a provider treats a stranger. Postmaster data shows how it treats the brand's real customers. Protect reputation by sending based on engagement, measure it with first-party signals, and reserve dedicated IPs for very large, steady senders. Average inbox rates already exceed 80%, so an 80% seed-test pass bar is a weak definition of Ascent success. Replace it with a composite scorecard.

## 14.1 The placement landscape

Validity's 2025 benchmark (based on 2024 seed data) found that 83.5% of marketing email reached the inbox, so about one message in six missed. Spam placement rose from 4.5% in Q1 to 8.6% in Q4.

| Country | Gmail share (inbox rate) | Microsoft share (inbox rate) | Yahoo share (inbox rate) | Overall inbox |
|---|---|---|---|---|
| United States | 54.4% (88.8%) | 10.8% (75.8%) | 21.8% (86.4%) | 85.0% |
| Canada | 45.5% (94.4%) | 27.9% (78.9%) | 12.2% (88.6%) | 86.7% |
| United Kingdom | 41.1% (91.8%) | 32.3% (86.9%) | 7.8% (90.2%) | 87.8% |
| Australia | 47.3% (92.6%) | 30.2% (77.7%) | 7.5% (86.4%) | 85.0% |

*Validity. No data for Ireland or NZ.* **Microsoft is the weak spot outside the US.** It holds about a third of mailboxes in Canada, the UK and Australia, and brands have reported months of Hotmail spam placement even when mailing only 30-day engaged profiles. For non-US brands, check Microsoft first.

**Gmail's Promotions tab is not spam.** Klaviyo calls it "a type of inbox", and no sender can choose which tab a message lands in. Since September 2025 Gmail has sorted Promotions by relevance, so low-engagement senders sink within the tab. The honest pitch is about visibility inside Promotions, which is an engagement and hygiene argument, not a promise to "get you out of Promotions".

## 14.2 The measurement stack

| Tool | Shows | Limits |
|---|---|---|
| Google Postmaster Tools | Gmail spam rate, compliance status | Needs enough daily Gmail volume |
| Yahoo Sender Hub | Yahoo sender data and complaints | Yahoo only |
| Microsoft SNDS | IP-level Outlook data | Only useful with a dedicated IP |
| Klaviyo reports | Bounces, complaints, engagement by provider | Opens distorted by MPP |
| DMARC aggregate reports | Every source sending as the domain | Needs a processor at scale |
| Seed tests | Where a test lands across a panel | No engagement history; panel mix skews the score |

## 14.3 Using seed tests properly

Seed accounts don't behave like real people, as Twilio SendGrid's guidance points out. Panel mix also moves the score: Microsoft and Apple seeds place around 75% to 76%, while Gmail and Yahoo seeds place around 86% to 87%. Weight the panel to the brand's actual mailbox mix, read results as a trend over several sends, and always pair them with Postmaster spam rates, bounce reasons and DMARC data. Real warning signs are spam placement at several providers at once, or order confirmations landing in spam.

**The Ascent Health Scorecard** (replacing the 80% seed bar):

| Metric | Target at 30 days | Source |
|---|---|---|
| DMARC pass on legitimate volume | 98%+ | DMARC reports |
| Gmail spam rate | Below 0.1% (aim for below 0.05%) | Postmaster Tools |
| Bounce rate | Below 1% | Klaviyo |
| Microsoft placement | Measurably better than baseline | Weighted seed trend and provider engagement |
| Transactional mail | Inbox at all major providers | Seeds and real order tests |
| One-click unsubscribe | Present on all marketing mail | Header inspection |
| Revenue per recipient | Flat or better against the same weeks last year | Klaviyo |

## 14.4 Dedicated IPs and warm-up

| | Shared IP (Klaviyo default) | Dedicated IP |
|---|---|---|
| Reputation | Pooled with other senders | The brand's alone |
| Volume needed | None | High and steady; quiet spells let it go cold |
| Cost | Included | Extra fee plus the warm-up effort |
| Main risk | Pool incidents (Klaviyo's to fix) | Every mistake is the brand's alone |
| Best for | Nearly every brand up to about USD 20M | A3 senders with large, consistent daily volume |

At Gmail, domain reputation now carries most of the weight. For almost every ICP brand, an authenticated branded domain with engagement-based sending matters far more than the IP choice. Shared pools do fail: one merchant reported a Gmail block on Klaviyo's shared IPs bouncing 22.5% and 60% of two Black Friday 2025 campaigns. Even then, the fix is usually escalating to Klaviyo and tightening targeting.

**Warm-up for a new sending domain** (modelled on Klaviyo's guidance; third-party "warming" tools have no role):

| Weeks | Campaign audience | Flows |
|---|---|---|
| 1 to 2 | Clicked or ordered in 30 days | On |
| 3 to 4 | Engaged in 60 days | On |
| 5 to 6 | Engaged in 90 days | On |
| 7 to 8 | Engaged in 120 days | On |
| 9 to 10 | Engaged in 180 days | On |

Step up only while complaints stay below 0.05% and bounces below 1%. Otherwise hold for a week. **To finish before Black Friday 2026 (27 November), warm-up had to start by about 18 September 2026. For 2027 (26 November), start by about 17 September 2027.** Brands that miss the window should stay on their current authenticated path through peak and migrate in January.

## 14.5 Incident runbook

| Incident | Signal | Severity | First 24 hours | Recovery |
|---|---|---|---|---|
| Gmail spam rate > 0.3% | Postmaster Tools | **Critical** | Campaigns to 30-day engaged only; audit recent list sources | 7 clean days, then ramp back tier by tier |
| Bounces > 2% | Klaviyo | High | Read bounce reasons; pause new sources; check forms for bots | Suppress the cohort; re-verify sources |
| Microsoft rejections (`550 5.7.515`) | Bounce reasons | High | Check SPF, DKIM, DMARC and alignment on that path | Fix, then retest |
| Shared IP blocklisted | Bounce codes; Klaviyo notice | Medium to high | Klaviyo ticket; narrow to engaged | Klaviyo moves traffic; record it in the client report |
| List bomb | Sign-up spike | Medium | CAPTCHA and double opt-in on affected forms | Suppress the cohort |
| DMARC fails after a new tool | Aggregate reports | Medium | Add DKIM or SPF for the tool | Add a change-request step |
| Pre-peak volume jump | Send plan | Preventive | Ramp up over 4 to 6 weeks | Peak SOP (Section 15.3) |

## 14.6 Validity's "Heatwave" blocklist

On 3 September 2026, Validity announced Heatwave, a blocklist of domains that use synthetic warming (networks of fake accounts trading messages, opens and replies) or cold-email setups. It reported more than a million domains at launch, with Proofpoint, Spamhaus, SURBL, Comcast and beehiiv as partners. The only source so far is Validity's own announcement, and whether Gmail or Outlook use the list is unconfirmed. Specialists have separately noted that filtering of cold email has increased. **For clients,** Klaviyo's own warm-up is the right method, and nobody should use warm-up networks. **For GrowMailers,** stop all synthetic warming on its own outreach domains now (Section 17.7). A deliverability agency whose domain is on a blocklist loses its credibility.

---

# 15. Global Retail Holidays & Regional Peak Promotional Windows

> **Bottom line:** Black Friday falls on 27 November 2026 in all six of our markets, 60 days after this document's date. The planning year runs from the early-October setup lock to the following September. Market-specific peaks such as Boxing Day, Mothering Sunday and Australia's end-of-financial-year sales shape both client calendars and GrowMailers' selling windows. In 2025 the US peak grew while the UK, Canada and New Zealand were flat or down, so outside the US, peak revenue is about taking share rather than riding growth.

## 15.1 Master calendar: October 2026 to November 2027

| Date | Event | Markets | Vertical relevance |
|---|---|---|---|
| 6 to 7 Oct 2026 | Amazon Prime Big Deal Days | All except NZ | Counter with bundles and loyalty perks, not deeper discounts |
| 12 Oct 2026 | Thanksgiving | Canada | Food and beverage, gifting |
| 27 to 30 Oct 2026 | Click Frenzy (unconfirmed; the operator was reported in liquidation) | Australia | Tentative |
| 31 Oct 2026 | Halloween | US, Canada, UK, Ireland | Confectionery; pet costumes |
| 1 Nov 2026 | UK Black Friday campaigns begin (Black Friday week is 23 to 30 Nov) | UK | Month-long UK peak |
| 11 Nov 2026 | Singles Day | All | Beauty, especially in Australia and NZ |
| 26 Nov 2026 | Thanksgiving | US | Food and beverage |
| **27 Nov 2026** | **Black Friday** | **All six** | **The biggest day for all four verticals** |
| **30 Nov 2026** | **Cyber Monday** | **All six** | |
| 1 Dec 2026 | Giving Tuesday | US | Cause-linked campaigns |
| 14 Dec 2026 | Green Monday | US | Last reliable ground-shipping push |
| 19 Dec 2026 | Super Saturday | US, UK | Last-minute gifting; e-gift cards |
| 26 Dec 2026 | Boxing Day (St Stephen's Day in Ireland) | Canada, UK, Ireland, Australia, NZ | Major sale day outside the US |
| 1 Jan 2027 | New Year | All six | Resolutions: supplements, wellness, food |
| 6 Feb 2027 | Lunar New Year | All | Food gifting |
| 14 Feb 2027 | Valentine's Day | All six | Beauty, food and beverage |
| 7 Mar 2027 | Mothering Sunday | UK, Ireland | Beauty and food gifting |
| 17 Mar 2027 | St Patrick's Day | Ireland and diaspora | Food and beverage |
| 26 to 29 Mar 2027 | Easter | All six | Chocolate, gifting |
| 9 May 2027 | Mother's Day | US, Canada, Australia, NZ | Beauty's biggest non-Q4 moment |
| June 2027 | Australian EOFY sales (financial year ends 30 June) | Australia | A month-long sales period; budgets reset 1 July |
| 20 Jun 2027 | Father's Day | US, Canada, UK, Ireland | Grooming, food and beverage |
| July 2027 (dates TBA) | Amazon Prime Day | All except NZ | Counter-program |
| Late Jul to Aug 2027 | Back-to-school | US, Canada | Lunchbox food, routines, supplements |
| 5 Sep 2027 | Father's Day | Australia, NZ | |
| **26 Nov 2027** | **Black Friday 2027** | **All six** | |

**Watch the calendar shift.** Cyber Monday moves from 1 December (2025) to 30 November (2026), so November 2026 will look stronger year on year purely because of the dates, and December weaker. Warn clients before they read too much into it.

## 15.2 Peak size in 2025 and vertical moments

| Market | Measure | 2025 result |
|---|---|---|
| United States | Cyber Week online spend / Cyber Monday / Nov to Dec total | USD 44.2B (+7.7%) / USD 14.25B (+7.1%) / USD 257.8B (+6.8%) |
| Global | Shopify merchants, Black Friday weekend | USD 14.6B (+27%) |
| United Kingdom | Black Friday week online | −1.2% |
| Canada | Black Friday card volume | −4% |
| Ireland | Black Friday online card spend (2024) | EUR 120M (+22%) |
| Australia | Black Friday weekend | Parcels +6.3%; about A$1.5B spent |
| New Zealand | Black Friday non-food spend | NZ$55.6M (−6.2%) |

*Adobe, Shopify, IMRG, Moneris, AIB, Australia Post and a New Zealand payments company.*

**Concentration is the argument for Ascent.** Cyber Week produced 17.1% of the US November to December season in 5 of its 61 days (our estimate from Adobe), and in one sample about one US brand in six took 30% or more of its yearly orders in Black Friday week. For those brands, a deliverability failure that week damages the whole year. Beauty and activewear were 2025's strongest peak categories in the US, UK and Australia.

| Vertical | Biggest moments beyond Black Friday | Program implication |
|---|---|---|
| Beauty | Valentine's Day, Mothering Sunday, Mother's Day, holiday gifting, Singles Day | Gift guides, gift-with-purchase, sets |
| Supplements | **January resolutions** (the supplement "Black Friday"), September back-to-routine | Education series; subscription offers |
| Food and beverage | Thanksgiving, holiday hampers, Easter, Lunar New Year, summer barbecue (reversed in the southern hemisphere) | Shipping cut-offs; gifting; perishability logistics |
| Pet | Holiday gifting; flea and tick season (spring and summer, reversed south of the equator); adoption anniversaries | Seasonal health flows; "gotcha day" automations |

**Regional nuances.** The UK's Black Friday runs all month, so UK segments must be live by late October. Mothering Sunday (7 March) and Mother's Day (9 May) are two months apart, so multi-market brands need two campaign tracks. Boxing Day is a major sale outside the US, and December capacity should be held for it. Australian and New Zealand summer falls over Christmas.

## 15.3 Peak-season email SOP

```
  T–12 WEEKS ── Authentication final; any new sending domain already warming (≈ mid-Sep)
  T–10 WEEKS ── List clean: sunset run, bots suppressed, engagement tiers rebuilt
  T–8  WEEKS ── Peak calendar drafted; offers agreed with finance (margin floor per SKU)
  T–6  WEEKS ── Volume ramp begins: +1 send a week to engaged and warm tiers
  T–4  WEEKS ── Segments, creative and flows locked; SMS consent list verified
  T–2  WEEKS ── QA: links, codes, one-click unsubscribe, mobile rendering, send times
  PEAK WEEK ─── Engaged first, then wider tiers; check spam rate and bounces daily
  T+1  WEEK ─── New buyers out of sale blasts and into post-purchase and review flows
  T+3  WEEKS ── Sunset peak-only sign-ups that never engage; plan January win-back
```

**The rule that prevents most peak incidents:** never let send volume jump. A list that has been quiet for months and is then blasted on Black Friday will see part of that mail land in spam. Brands that paused sending before peak have reported bounce spikes on their first sale email.

---

# 16. Go-To-Market Execution Windows & Sales Timelines

> **Bottom line:** Pitch Lhotse when budgets reset and there is time to build: January to February, and June to mid-September. From mid-October to year-end, sell only low-risk Ascent fixes and book January starts. As of 28 September 2026, GrowMailers has about three weeks of freeze-safe Ascent selling left before the Black Friday lock. The next Lhotse window opens on 4 January 2027.

## 16.1 The master sales calendar

| Window | Dates | Lead offer | Ascent scope allowed | Lhotse | Theme |
|---|---|---|---|---|---|
| **Pre-freeze sprint** | Now to 16 Oct 2026 | Ascent quick fixes | DMARC on the *current* domain; alignment; list cleaning; suppression; bot defences; spam triage | Book January starts only | "Protect peak without changing your setup" |
| **Freeze** | 16 Oct to 31 Dec 2026 | None | Emergency repairs only | Sign for January | "Let's review your peak data in January" |
| **Best window** | 4 Jan to end Feb 2027 | Lhotse | Full, including new sending domains | Full pitch | "New budget; here's what peak revealed" |
| **Steady window** | Mar to May 2027 | Both | Full | US, Canada, non-gifting brands; Australia before EOFY | "Build the system before summer" |
| **Second-best window** | Jun to mid-Sep 2027 | Both | Full; new domains warming by ~17 Sep | Aim for starts by early August | "Black Friday is won in summer" |

**Why this rhythm.** Klaviyo's own checklist says Black Friday is won in summer, with setup, segments and flows final by early October. Agencies advise hiring email partners 8 to 12 weeks before Black Friday. Most teams freeze changes in November, and onboarding takes 2 to 3 weeks. A retainer pitched in late October is almost impossible to deliver well and very easy to lose.

```
  WHERE IS TODAY RELATIVE TO BLACK FRIDAY (BF)?
   ├─ > 12 weeks before ─► USD 3M–20M and in a target vertical?
   │                        ├─ YES ─► AUS ≥ 40 ? ASCENT NOW → LHOTSE NEXT : LHOTSE-FIRST
   │                        └─ NO ──► ASCENT ONLY (USD 1–3M or USD 20M+)
   ├─ 6–12 weeks before ─► ASCENT on the current domain only; Lhotse proposals dated January
   ├─ < 6 weeks / freeze ─► NO NEW PROJECTS; emergency repairs; book January calls
   └─ January–February ──► LHOTSE, with Ascent work folded into onboarding if needed
```

## 16.2 Back-planning for Black Friday 2027

```
  JUN 2027        JUL              AUG             SEP                   OCT          NOV
  Pitch and  ──►  Contract   ──►   Onboarding ──►  Flows rebuilt; new ─► Setup lock   BF 26 Nov
  discovery       (latest: early   (2–3 weeks)     domain warming by     (early Oct)
                  August)                          ~17 Sep
```

For a Lhotse client to be fully peak-ready, the latest sensible signature date is early August. After that, pitch a January start instead.

## 16.3 Sales cycles and capacity

| Offer and buyer | Typical cycle | Implication |
|---|---|---|
| Ascent, founder (A1) | 1 to 2 weeks | Can close within the pre-freeze sprint |
| Ascent, CRM lead + VP (A2) | 2 to 3 weeks | Start by late September for October delivery |
| Ascent, enterprise with IT (A3) | 3 to 6 weeks | Best sold in January or summer. Expect a DNS-access security review. |
| Lhotse, founder (L1) | 2 to 4 weeks | Pitch in January, start in February |
| Lhotse, VP or Head of Growth (L2) | 4 to 8 weeks | Start in early January for March starts |
| Lhotse, CMO + finance (L3) | 6 to 12 weeks | Start in November or December for Q1 decisions |

*Planning assumptions; calibrate against GrowMailers' closed deals.*

```
  Accounts to audit per month = Target clients ÷ (reply rate × meeting rate × close rate)
  With ASSUMED rates of 10% × 50% × 25% and a target of 2 clients/month:
  2 ÷ 0.0125 = 160 audits a month ≈ 40 a week ≈ two researcher-days at 15–20 minutes each
```

**Weekly rhythm:** Monday, build and score about 50 accounts. Tuesday and Wednesday, run about 40 external audits and record 10 to 15 videos. Thursday, follow-ups, discovery calls and proposals. Friday, pipeline review, re-scoring, and a health check on GrowMailers' own outreach domains.

## 16.4 Market sequencing

| Period | US | UK and Ireland | Canada | Australia and NZ |
|---|---|---|---|---|
| Jan to Feb | ★★★★★ | ★★★★★ (non-gifting) | ★★★★ (CASL-compliant only) | ★★★★ |
| Mar to May | ★★★★ | ★★★ | ★★★★ | ★★★ (ready for EOFY by early May) |
| Jun to Aug | ★★★★ | ★★★★ | ★★★★ | ★★★★★ (new budgets from July) |
| Sep to mid-Oct | ★★ Ascent only | ★★ (UK peak starts 1 Nov) | ★★ | ★★ |
| Mid-Oct to Dec | Freeze | Freeze | Freeze | Freeze |

---

# 17. International Marketing Compliance & Cold Outreach Law

> **Bottom line:** Cold email to businesses is simplest in the US, which runs an opt-out regime, and in the UK when the recipient is a limited company. It is narrow in Canada and Ireland, where only published role addresses or company addresses are safe, and consent-led in Australia and New Zealand. Cold SMS is off-limits everywhere, and cold calls need screening in every market. In every country, identify GrowMailers honestly, include a postal address and a working opt-out, record where each address came from, and never buy lists.

*Research, not legal advice. Confirm each country's position with a qualified lawyer before scaling outreach there.*

## 17.1 Principles that apply everywhere

1. **Honest identity:** a named GrowMailers sender, the real company name and accurate headers.
2. **Honest subject lines** that match the content. Never put "Re:" or "Fwd:" on a first touch.
3. **Postal address and a working opt-out** in every commercial email.
4. **Fast, permanent opt-outs,** kept on one suppression list shared by every tool and teammate.
5. **Recorded provenance:** source URL and date, plus a dated screenshot for Canada, Australia and NZ.
6. **No bought lists, and no guessed or permutated addresses** in strict jurisdictions.
7. **No cold SMS, autodialled calls, AI voices or ringless voicemail** anywhere.

## 17.2 United States: CAN-SPAM and TCPA

**CAN-SPAM** covers all commercial email, including B2B, and runs on an *opt-out* basis, so prior consent is not required. Every message must still meet these rules:

| Requirement | For GrowMailers outreach |
|---|---|
| Accurate headers; honest subject line | From, Reply-To and routing identify GrowMailers; the subject reflects the body |
| Identify the message as commercial | Say clearly that the message is about GrowMailers' services |
| Valid physical postal address | A street address, a registered PO box, or a registered private mailbox |
| Clear opt-out, honoured within 10 business days | Must work for at least 30 days after sending; no fee or login; never sell or share opted-out addresses |
| Vendor liability | GrowMailers stays liable if a lead-gen vendor sends on its behalf |
| No harvesting | Scraping addresses from sites that forbid it, or generating them by guessing, is an aggravated violation |
| Penalties | More than USD 50,000 per non-compliant email (adjusted for inflation each year) |

**TCPA** governs calls and texts. Calls or texts to **mobile numbers** made with an autodialer or an artificial or prerecorded voice need prior express consent, and telemarketing needs *written* consent. **Texts count as calls**, and the FCC treats AI-generated voices as artificial. The **National Do Not Call Registry** protects residential and wireless numbers. Business landlines generally fall outside it, but founders often list a mobile as the business line, so scrub mobiles against the Registry and dial manually. Call only between **8 a.m. and 9 p.m. in the recipient's local time**, and keep an internal do-not-call list. Statutory damages are **USD 500 per violation, up to USD 1,500 if wilful**, and class actions are common. **State "mini-TCPA" laws** (Florida and Oklahoma, for example) add stricter rules.

## 17.3 United Kingdom: PECR and UK GDPR

- **Corporate subscribers** (Ltd, LLP, PLC, Scottish partnerships, government bodies) can receive B2B marketing email without consent, as long as GrowMailers identifies itself and offers an easy opt-out.
- **Individual subscribers,** including **sole traders** and some partnerships, need **consent.** Check Companies House first. If no company is registered, do not cold email.
- **UK GDPR still covers named business addresses** (jane@brand.co.uk is personal data). GrowMailers needs a written **legitimate interests assessment**, must tell each person where it got their data within one month (the first email's footer works), and must treat any objection as permanent.
- **A director's personal Gmail** probably counts as an individual and needs consent (our reading).
- **Calls:** screen against the **TPS** and **Corporate TPS**. Automated calls need consent.
- **Penalties:** since 5 February 2026, the maximum PECR fine is **£17.5 million or 4% of global turnover.**

## 17.4 Canada: CASL and the telemarketing rules

CASL is the strictest regime in our markets, and it applies to messages sent *into* Canada from anywhere, including Nepal.

- Every commercial email needs **consent** (express or implied), **sender identification** and a **working unsubscribe.**
- **Implied consent by conspicuous publication** needs **all three** of these: the person published the address (for example on the brand's site); nothing near it refuses unsolicited messages; and the message relates to their business role. The CRTC has said this gives no broad licence to email any address found online.
- **Addresses found only through enrichment tools, and personal Gmail addresses, carry no implied consent.**
- **Referral exemption:** one message is allowed after a referral from someone who has a relationship with both parties, and it must name the referrer in full.
- **Content:** sender name, mailing address, and a phone, email or web contact that stays valid for 60 days. Unsubscribes must be processed within **10 business days.**
- **The burden of proof is on the sender,** so keep a dated screenshot of where each address was published.
- **Penalties:** up to **C$10 million per violation** for a business. Recent cases against Indeed Canada, Hudson's Bay and DavidsTea all involved broken unsubscribe processes.
- **Calls:** B2B calls are exempt from the National DNCL, but GrowMailers must still **register with the DNCL operator,** keep an internal list, call only **9:00 a.m. to 9:30 p.m. on weekdays and 10:00 a.m. to 6:00 p.m. on weekends,** and identify itself. The CRTC has fined a foreign caller C$175,000.
- **Quebec:** marketing must be available in French. Write in French or put Quebec lower in the queue.

## 17.5 Ireland, Australia and New Zealand

- **Ireland:** email to a **company** is allowed unless it has objected. A **named employee address** may count as an individual needing consent, so use generic company addresses until counsel confirms otherwise. **Cold calls to mobiles need consent,** and many owners list a mobile as their business number. Each unsolicited message is a separate offence, and the Data Protection Commission closed 275 direct-marketing investigations in 2025, up 88%.
- **Australia (Spam Act 2003):** consent may be express or **inferred**. Inferred consent covers conspicuously published business addresses where the message fits the recipient's role and nothing refuses such messages. Every message needs sender identification and an unsubscribe honoured within **5 working days**. Penalties for repeat breaches can reach A$3.3 million a day. Check the Do Not Call Register before calling mobiles.
- **New Zealand (Unsolicited Electronic Messages Act 2007):** consent may be express, inferred or **deemed**. Deemed consent applies to conspicuously published business addresses, on the same terms as Australia's inferred consent. Unsubscribes must be honoured within **5 working days**.

*Our research on Australia and New Zealand is incomplete. Treat both as frameworks to confirm.*

## 17.6 Six-country comparison and pre-send checklist

| Country | Cold email to brands | Safest address | Cold calls | Opt-out deadline | Risk |
|---|---|---|---|---|---|
| United States | Allowed (opt-out regime) | Named business address | Manual dial; scrub mobiles against DNC | 10 business days | Low (email) / high (calls, texts) |
| United Kingdom | Ltd, LLP, PLC yes; sole traders need consent | Named address at a verified company, with an LIA | Screen TPS and CTPS | Promptly; objection is absolute | Medium |
| Canada | Published addresses meeting all three tests, or referrals | Published role address | DNCL registration; calling hours | 10 business days | **High** |
| Ireland | Companies yes; named staff unclear | Generic company address | No mobiles without consent | Promptly | **High** |
| Australia | Inferred consent via publication | Published role address | Check DNC Register | 5 working days | Medium to high |
| New Zealand | Deemed consent via publication | Published role address | Check before calling | 5 working days | Medium to high |

**Pre-send checklist:**

- [ ] Real operating country confirmed (not a registered-agent address)
- [ ] Address type allowed for that country
- [ ] Provenance logged (URL, date; screenshot for Canada, Australia and NZ). UK: Companies House match and LIA on file.
- [ ] Not on the global suppression list
- [ ] Named sender; honest subject line
- [ ] Footer: GrowMailers legal name, postal address, statement that this is a message about GrowMailers' services, data-source note (UK and EU), simple opt-out
- [ ] Sequence of 3 to 4 touches over about three weeks, stopping at any reply

## 17.7 GrowMailers' own sending infrastructure

A deliverability agency's own outreach is its first case study. Keep cold outreach on **separate domains**, off growmailers.com. Authenticate every outreach domain fully (SPF, DKIM and aligned DMARC, moving to enforcement). **Stop all synthetic warm-up immediately** (Heatwave and SURBL listing risk, Section 14.6). Keep volume low and human: researched, personal emails at a steady per-mailbox pace. Check blocklists and Postmaster data every week, and cap bounces at 2%.

New Shopify owners are flooded with cold pitches. Community helpers often label them scams, and they single out Gmail senders and "your store has a problem" openers. The approach that works is the opposite: a specific free fix, shown in a short screen recording, with no ask. Public "free audit" offers in forums almost never get a reply.

## 17.8 Client-side compliance (what Lhotse must respect)

| Rule | Where | Program implication |
|---|---|---|
| An abandoned checkout is not consent | Canada (CASL) | Email Canadian abandoners only with consent or an existing business relationship |
| Soft opt-in | UK (PECR) | Past customers may get marketing for similar products, with an opt-out in every message |
| Unsubscribe within 2 days / 5 working days | Yahoo / Australia and NZ | Never delay unsubscribes |
| Written consent for marketing SMS | US (TCPA) | Separate SMS consent with clear disclosure; quiet hours |
| French-language marketing | Quebec | French flows and campaigns for Quebec profiles |
| Health and supplement claims | FTC, ASA, TGA | Copy review for every health claim |

---

# 18. Actionable GTM Audit SOP, Prospecting Scripts & Qualification Playbook

> **Bottom line:** GrowMailers wins by showing, not telling. Build a precise list. Run a 15-minute non-invasive external audit. Send one specific free fix in a short personalized video. Then qualify with the prospect's own numbers. Every step below can be repeated by a researcher and will hold up in front of a technical buyer.

## 18.1 The pipeline

```
  SOURCE ─► GATE ─► SCORE ─► AUDIT ─► OUTREACH ─► DISCOVERY ─► PROPOSAL ─► CLOSE ─► ONBOARD
  Store     Hard    LFS +    15-min   Video +     Their        Ascent SOW  Signed   30-day plan
  Leads     gates   AUS      external  email      numbers →    or Lhotse            + holdouts
  (18.2)    (5.1)   (4.3)    (18.3)   (18.4–18.5) model (18.6)  (18.8)
```

## 18.2 Step 1: Build the list

| Store Leads filter | Setting |
|---|---|
| Platform and country | Shopify or Shopify Plus; US, UK, Canada, Australia, Ireland, NZ |
| Estimated monthly sales | USD 83k+ (Ascent). Lhotse: USD 250k+ for beauty and supplements, USD 333k+ for pet, USD 417k+ for food. |
| Apps to include | Klaviyo |
| Apps to exclude | Printful, Printify, Fourthwall; DSers, Zendrop, AutoDS, CJdropshipping |
| Categories | Beauty and fitness, health, food and drink, pet (apparel as secondary) |
| Post-filter screens | Registry trap (Section 6.5); marketplace-led; email agency hired in the last 6 months |

## 18.3 Step 2: The non-invasive external audit (15 to 20 minutes)

**Boundaries:** use only public DNS and emails received as an ordinary subscriber. No login attempts, no scanning, no spoofing tests, and no contact with the brand's customers.

```bash
DOMAIN=brand.com
dig +short TXT $DOMAIN | grep -i "v=spf1"     # 1. SPF: expect exactly ONE record
dig +short TXT _dmarc.$DOMAIN                 # 2. DMARC: expect exactly ONE v=DMARC1 record
dig +short MX $DOMAIN                         # 3. Mailbox host (Workspace, Microsoft 365…)
dig +short TXT send.$DOMAIN                   # 4. Sending subdomain (take it from Return-Path)
dig +short TXT <selector>._domainkey.<d-domain>   # 5. DKIM key (s= and d= from the header)
```

Count SPF lookups by hand or with any public SPF checker (the limit is 10). Then subscribe with a Gmail and an Outlook research inbox and check the following:

| Check | Where to look | A finding looks like |
|---|---|---|
| Sender label | Gmail sender line | "via klaviyomail.com", or a sender rewritten to shopifyemail.com |
| Authentication | Gmail → Show original | spf, dkim or dmarc not "pass"; `header.from` not aligned with `d=` |
| One-click unsubscribe | `List-Unsubscribe-Post` header | Missing on marketing mail |
| Welcome delivery | Arrival time and folder | More than an hour late, or in Outlook junk |
| Program depth | Mail over 14 days | One-email welcome; daily blasts to a never-clicked subscriber |
| Forms | Signup popup | No bot protection; no double opt-in on risky sources |
| Browse and cart | Browse, then start checkout while identified | No follow-up within 48 hours |

| Finding | Severity | Offer | Plain-English phrasing |
|---|---|---|---|
| No DMARC, or two records | High | Ascent | "Your domain has no DMARC record, which Gmail and Yahoo now require from bulk senders. It's a two-minute DNS fix." |
| Shared Klaviyo domain above 5,000 profiles | High | Ascent | "Your emails say 'via klaviyomail.com', so your reputation is pooled with other senders." |
| Shopify sender rewrite | High | Ascent | "Shopify is swapping your sender for shopifyemail.com because of a DMARC gap." |
| Outlook junk placement | High (UK, Canada, Australia) | Ascent | "Your welcome landed in Outlook junk, and about a third of UK inboxes are Microsoft." |
| No one-click unsubscribe / SPF over its limit | Medium | Ascent | "Gmail requires one-click unsubscribe." / "Your SPF record exceeds its lookup limit." |
| Thin flows | Medium | Lhotse | "Your welcome is one email, and there's no replenishment reminder for a 30-day product." |
| Daily full-list blasts | Medium | Lhotse | "Sending daily to people who never click is what pushes a list toward spam." |

## 18.4 Step 3: The 90-second audit video

| Time | Beat | Script |
|---|---|---|
| 0:00 to 0:10 | Hook | "Hi {{first name}}, I'm {{name}} from GrowMailers. I joined the {{Brand}} list last week, and your {{specific email or product}} is genuinely good." |
| 0:10 to 0:35 | Finding, on screen | "One thing stood out in the headers. *[show it]* This line means {{finding}}. In plain terms: {{impact}}." |
| 0:35 to 0:55 | Why now | "With Black Friday on 27 November {{or: Gmail's bulk-sender rules}}, this is the kind of thing that turns into bounces just as volume rises." |
| 0:55 to 1:15 | Free fix | "Here's the exact fix. *[show it]* Your developer can add it in minutes, and it's in the email below." |
| 1:15 to 1:30 | Soft close | "That's it, no pitch. If you want a second pair of eyes on the rest, just reply." |

Record the prospect's actual inbox or DNS output, never a generic slide, and keep it under two minutes.

## 18.5 Step 4: Outreach templates

**Template A: Ascent, to a founder (A1 or A2)**

> **Subject:** {{Brand}}'s DMARC record
>
> Hi {{first name}}, I joined the {{Brand}} list to study your welcome emails (the {{detail}} one is great) and noticed something in the headers: {{plain-English finding}}. Since last year, Gmail, Yahoo and Microsoft have been rejecting bulk mail that fails this check, so it's worth fixing before Black Friday volume. It's a small fix, and I recorded 90 seconds showing exactly what to change: {{video link}}. No strings attached. If you'd like me to look at the rest, just reply.
>
> {{Name}}, GrowMailers
>
> *GrowMailers · {{postal address}} · A one-off business message about our email services. I found your address on {{source}}. Reply "no thanks" and I won't contact you again.*

**Template B: Lhotse, to a VP Marketing or Head of Growth (L2)**

> **Subject:** replenishment at {{Brand}}
>
> Hi {{first name}}, I've been on the {{Brand}} list for two weeks. Your campaigns are sharp, but I didn't see a replenishment email for {{product}}, which is roughly a {{N}}-day product. At your size, a working replenishment and post-purchase system usually needs only 1% to 3% of monthly orders to be incremental to pay for a full retention team, and we prove it with holdout tests rather than platform attribution. Worth 20 minutes in January, once peak is behind you?
>
> {{Name}}, GrowMailers · *{{compliant footer}}*

**Template C: Enterprise Ascent, to a CRM or Retention Lead (A3)**

> **Subject:** DMARC enforcement at {{Brand}}
>
> Hi {{first name}}, quick peer note. Your DMARC is at p=none with reporting on, which is compliant, and it looks like you're partway to enforcement. {{Sender, e.g. the reviews app}} isn't aligned yet. We run zero-downtime enforcement projects: we inventory your senders, write change requests for your IT team, and step up to reject without touching peak. Happy to share our SOP either way.
>
> {{Name}}, GrowMailers · *{{compliant footer}}*

**Follow-ups:** on day 4, one line with a second finding. On day 10, a relevant benchmark. On day 21, close the loop ("I'll stop here. The fix in the video still stands."). Stop at any reply.

## 18.6 Step 5: The discovery call (30 minutes)

| Minutes | Agenda |
|---|---|
| 0 to 5 | Their goals for the next two quarters |
| 5 to 15 | Collect the numbers and build the Section 8 model live: website revenue, AOV, gross margin, monthly orders, email share and attribution window, active profiles and Klaviyo tier, blended CPA or MER, subscription share, markets |
| 15 to 22 | Walk through the audit findings; ask what they've seen (bounces, bills, spam) |
| 22 to 27 | Fit: Ascent, Lhotse or both, with the breakeven order count |
| 27 to 30 | Next step: proposal date, who decides, start window |

**Qualifying questions:** Who else weighs in, and how have you bought agency services before? What happened to email week by week last Black Friday? What would you expect to see in 90 days if this worked? Does DNS access need IT sign-off? **Red flags:** they demand guaranteed inbox rates, want a discount-heavy program regardless of margin, are mid-way through an ESP migration, have no clear decision maker, or show visible cash stress (Section 9.3).

## 18.7 Step 6: Pipeline scoring

```
  GrowMailers Opportunity Score (GOS, 0–100)
    = Fit (0–40)                ← LFS × 0.4 (Lhotse) or AUS × 0.4 (Ascent-only accounts)
    + Urgency (0–25)            ← audit severity, recent incident, proximity to peak
    + Timing (0–15)             ← inside a pitch window (Section 16.1) = 15; freeze = 0
    + Authority & access (0–20) ← decision maker engaged 20; influencer only 10; no contact 0

  ≥ 75   Priority: discovery within 7 days; proposal within 48 hours of the call
  55–74  Active nurture: second finding or benchmark; re-score monthly
  < 55   Long-term nurture or disqualify; re-score quarterly
```

| Stage | Exit criteria |
|---|---|
| S0 Identified | Passes the hard gates |
| S1 Qualified | GOS calculated; lawful contact route confirmed |
| S2 Audited | At least one specific finding recorded |
| S3 Engaged | Replied or watched the video; meeting booked |
| S4 Discovery | Numbers collected; model built; fit confirmed |
| S5 Proposal | Scope and price sent; decision date agreed |
| S6 Closed | Won: kickoff booked. Lost: reason and re-contact date logged. |

## 18.8 Proposals, scope and onboarding

**Ascent SOW:** baseline metrics, sender inventory, DNS change list with rollbacks, hygiene actions, warm-up plan, Health Scorecard targets (Section 14.3) and a 30-day review. **Lhotse proposal:** the brand's own economics, a 90-day flow and campaign plan, a holdout plan, the monthly scorecard, the scope band and fee, and a 90-day initial term. **State these exclusions explicitly:** no guaranteed inbox percentage; shared-IP blocks are Klaviyo's to resolve; ESP migrations are out of scope unless requested; DNS changes need the client's access or IT team; health claims need the client's own compliance review.

**First 30 days of a new client:**

- [ ] Kickoff: goals, KPIs, contacts, approvals
- [ ] Access: Klaviyo, Shopify (read), DNS or IT contact, Postmaster Tools, SMS platform
- [ ] Baseline snapshot; sender inventory; DMARC reporting live
- [ ] Engagement tiers rebuilt without opens; sunset flow live
- [ ] Top three flow fixes shipped; holdouts on the two highest-volume flows
- [ ] 60-day campaign calendar with peak moments flagged by market
- [ ] First monthly scorecard delivered

## 18.9 GTM engine KPIs

| KPI | Cadence |
|---|---|
| Accounts audited; audit-to-reply rate; reply-to-meeting rate | Weekly |
| Meeting-to-close rate | Monthly |
| Ascent-to-Lhotse conversion within 90 days | Quarterly |
| Lhotse retention at 6 and 12 months | Quarterly |
| Holdout-tested incremental revenue across clients, divided by fees | Quarterly |
| GrowMailers outreach domain health (bounces, blocklists, spam placement) | Weekly |

---

# Appendix A: Glossary

| Term | Meaning |
|---|---|
| Alignment | Whether the domain authenticated by SPF or DKIM matches the visible From domain |
| AOV / CPA / CAC | Average order value / ad spend per purchase (new or returning) / marketing spend per *new* customer |
| BIMI | Standard for displaying a brand logo in the inbox; no placement effect |
| CASL / PECR / TCPA | Canada's anti-spam law / UK electronic marketing rules / US telephone consumer protection law |
| Contribution | Revenue minus product, fulfilment and payment costs |
| DKIM / SPF / DMARC | Cryptographic signature / list of authorized sending servers / policy tying both to the From domain |
| ESP | Email service provider, such as Klaviyo |
| Flow / campaign | Behaviour-triggered automation / one-off send |
| Holdout | A random group deliberately not mailed, to measure true lift |
| LFS / AUS / GOS | Lhotse Fit Score / Ascent Urgency Score / GrowMailers Opportunity Score |
| LTV / MER | Lifetime contribution per customer / total revenue ÷ total marketing spend |
| MPP | Apple Mail Privacy Protection, which auto-opens email |
| Sunset flow | Re-permission, then suppression, of long-inactive profiles |
| 3PL | Third-party logistics (outsourced fulfilment) |

# Appendix B: Sources and Data Notes

**Sources:** US Census Bureau Quarterly E-Commerce Report (Q2 2026). Store Leads Shopify, Plus, app and Klaviyo counts by country, state and city (18 September 2026), https://storeleads.app/reports/shopify/US/top-stores. Klaviyo 2026 Email Benchmarks (updated 24 September 2026), https://www.klaviyo.com/products/email-marketing/benchmarks, plus Klaviyo's Q2 2026 results, help centre and Patrick Ta Beauty case study. Omnisend 2025 data (150,000 brands). Validity Email Deliverability 2025 Benchmark Report, https://www.validity.com/wp-content/uploads/2025/03/2025-Benchmark-Report-FINAL.pdf, and Validity's Heatwave announcement (3 September 2026). Google email sender guidelines FAQ, https://support.google.com/a/answer/14229414. Yahoo and Microsoft bulk-sender requirements. Triple Whale Ecommerce Benchmarks (21 September 2026), https://benchmark.triplewhalelabs.com/. Meta Q2 2026 results. ShipBob 2026 survey (416 executives). eMarketer. Litmus (July 2026). dmarcian. FIGS, Hims & Hers and Temple & Webster filings. Adobe, IMRG, Moneris, AIB and Australia Post peak results. Flypost, Level CFO, ATTN, Eightx, eCommerce Placement, Liquid Lemon and ECOM CPA guides. Glassdoor, Morgan McKinley and Indeed salary data. Regulator guidance from the FTC, FCC, ICO, CRTC, Irish Data Protection Commission, ACMA and New Zealand's Department of Internal Affairs.

**Notes:** (1) "Our estimate" and "planning assumption" figures are GrowMailers calculations; replace them with export or prospect data. (2) Vendor benchmarks (Triple Whale, Klaviyo, Omnisend, Validity) describe their own customers and are directional. (3) Platform attribution overstates causal impact, so holdouts are the reporting standard. (4) Legal summaries are research as of September 2026, not legal advice. (5) Community and review-site comments were used only to confirm pain points, not as statistics.
