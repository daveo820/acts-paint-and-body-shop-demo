# Market research: Act's Paint & Body Shop (Durham, NC)

Prepared 9 Oct 2026 for the LuminArch concept demo. Lead from Job finder, Oct 9 morning NC sweep (row 2).

## 1. Lead check

Job finder said: actspaintandbodyshop.com is on Squarespace hold. Verified before building.

| Claim | Evidence | Verdict |
|---|---|---|
| Domain on hold | RDAP (rdap.verisign.com): status "client hold", "client delete prohibited", "client transfer prohibited". Registered 4 Oct 2018, expires 4 Oct 2027, last changed 5 Oct 2026. Nameservers dns-parking.com. Google DNS (dns.google) returns NXDOMAIN. | True, the site does not resolve |
| "Squarespace" | Partly wrong. The Wayback Machine shows the last real site was a WebSite X5 build ("Created by Incredibull Designs", page title "New Project") captured as late as 17 Feb 2025. Whoever holds the registrar account put it on hold days ago (5 Oct 2026). | Premise holds; the detail is off |
| Even when it worked | The old page had a default "New Project" title, a service list and two before and after photos. No reviews, no quote path. | Weak site even at its best |
| Business is open | Google listing status Open, 4.8 from 104 reviews, reviews through Oct 2025. Yelp has 16 reviews. | Open |
| NC SOS active | Could not verify. sosnc.gov and nccompanies.com sit behind a Cloudflare check that we did not bypass, and no search snippet showed an entity. Likely a sole proprietorship or assumed name. | Unverified |
| Owner alive | Alfred Brunson ("Pastor Alfred Brunson", owner, on the shop's own former site and MapQuest). Reviews from Oct 2025 thank "Pastor Al". No obituary found. | No red flag |
| MDN Cabinets conflict | MDN is a Raleigh commercial millwork shop. No overlap. | None |

**Verdict: survives.** The domain is on registrar hold and does not resolve; the shop is busy and well reviewed.

**Caveat:** a hold placed 5 Oct 2026 is often a billing or verification issue, so Pastor Al may get the old page back on his own. Even then it is a one page "New Project" site.

## 2. Where they show up today
- Google Business Profile: 4.8 (104), Mon to Fri 8 to 5, website link points at the held domain.
- Yelp (16 reviews), MapQuest, myHomePro (estimated staff: 3), cmac (lists 9 to 5; Google and the shop's own site say 8 to 5).

## 3. Top performing collision sites (ranked)

Lighthouse 12, mobile, run from the box on 9 Oct 2026. Screenshots (desktop and phone fold) are in `research/`.

| Rank | Site | Why it ranks here | Perf | A11y | BP | SEO | LCP | Weight |
|---|---|---|---|---|---|---|---|---|
| 1 | ultracolornc.com (UltraColor, Durham) | Best independent site in the Triangle: phone in the nav, 8 estimate CTAs, reviews, a booking flow, dealer partner page | 69 | 91 | 100 | 100 | 7.7 s | 1.1 MB |
| 2 | caliber.com (national) | Gold standard flow: "Online Estimate" and "Book an Appointment" in the header, FAQ, reviews, payment options | 33 | 96 | 79 | 85 | 27.3 s | 5.9 MB |
| 3 | relentlesscollision.com (Raleigh, Durham, Cary) | Certified luxury positioning, location blocks, reviews, form on the home page | 54 | 89 | 61 | 100 | 3.9 s | 2.4 MB |
| 4 | gerbercollision.com Durham / Chapel Hill page | Location page done right: hours, map, schedule and estimate buttons | 36 | 89 | 71 | 100 | 19.6 s | 2.6 MB |
| 5 | michaeljordancollisioncenter.com (Durham) | Virtual estimate and online authorization form, facility tour | 40 | 81 | 96 | 92 | 9.5 s | 20.7 MB |
| 6 | crashchampions.com (national) | Location finder first, strong photo hero | 18 | 94 | 71 | 85 | 19.6 s | 7.2 MB |
| 7 | johnsrestorations.net (Cary) | Small independent, title tag "Home", no tel link, 287 words. What not to do | 37 | 94 | 75 | 82 | 17.6 s | 2.7 MB |

### Patterns the winners share
1. **Phone and estimate in the header.** UltraColor, Caliber and Gerber all keep a tap to call number and an estimate button visible on every page.
2. **Photo first estimates.** "Virtual Estimate" (Michael Jordan), "Online Collision Estimate" (Gerber), "Start your estimate" (Caliber). Customers expect to send pictures before they drive over.
3. **Insurance explained.** Every top site has an insurance page or FAQ. The chains sell their insurer partnerships; independents sell the customer's right to choose.
4. **Reviews near the top**, usually Google stars plus three quotes.
5. **Services as a grid of cards**, one line each, linking to detail.
6. **Hours and map** on the home page for location searches.
7. **What they get wrong:** heavy pages (5 to 20 MB), slow LCP on phones (8 to 27 s), stock photos of cars that are not theirs.

## 4. The opening
Act's reviews tell a story the big shops don't: people paying out of pocket. A high deductible, an off road dent insurance would not cover, a peeling trunk quoted at $1,200 and up elsewhere. Every top site above is built around insurance claims and DRP partners. Nobody in the set speaks to the cash customer who wants a straight quote first. That, plus fast turnaround and paint matching (a metallic tri-coat in under 48 hours), is the angle, and it is all in customers' own words.

## 5. Pitch points
1. The Google "Website" button on a 104 review listing goes nowhere today.
2. The old site's title was literally "New Project". The demo has unique titles and descriptions on every page.
3. "Paying out of pocket?" section built from three real reviews.
4. "On the clock" band: real turnaround stories with times, from reviews.
5. The demo reuses the shop's own before and after photos of a classic Jaguar, from its former site, so it already looks like theirs.

## 6. Risks and caveats
- The hold may be lifted by the owner at any time.
- The Jaguar photos are low resolution (479 px) and from 2021. Ask for new ones; get written permission before any public launch.
- Hours: Google and the shop's 2025 page say 8 to 5; cmac says 9 to 5. We used 8 to 5.
- "Since about 2003" comes only from a directory (Job finder's note). Not used.
- The shop's former site listed a cell number for Pastor Al. Not used; it is personal.
- One review (Dec 2023) calls him "Pastor Yesterday", almost certainly autocorrect. Not quoted.
- Competitor scores are one Lighthouse run each from the box; they move from run to run. Use them as a range, not a promise.
- We never claim the demo will rank or bring in calls. We show process: speed, clarity, the right to choose page, photo first estimates.
