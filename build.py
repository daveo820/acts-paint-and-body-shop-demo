# Static page builder for the Act's Paint & Body Shop concept. Run: python3 build.py
import json
BASE = 'https://acts-paint-and-body-shop-demo.vercel.app/'  # Vercel production URL
TEL, TEL_H = '+19196806802', '(919) 680&#8209;6802'
MAP = 'https://www.google.com/maps/search/?api=1&query=Act%27s+Paint+%26+Body+Shop+304+S+Elm+St+Durham+NC+27701'
ORG = {"@context":"https://schema.org","@type":"AutoBodyShop","name":"Act's Paint & Body Shop",
 "url":BASE,"telephone":"+1-919-680-6802",
 "founder":{"@type":"Person","name":"Alfred Brunson"},
 "address":{"@type":"PostalAddress","streetAddress":"304 S Elm St","addressLocality":"Durham","addressRegion":"NC","postalCode":"27701","addressCountry":"US"},
 "geo":{"@type":"GeoCoordinates","latitude":35.987962,"longitude":-78.893233},
 "openingHours":"Mo-Fr 08:00-17:00","areaServed":"Durham, NC",
 "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.8","reviewCount":"104"}}

def K(t): return f'<p class="kicker">{t}</p>'
def DECK(h=14, cap=False, cls=''):
    d = f'<ul class="deck {cls}" style="--dh:{h}px" aria-hidden="true">' + '<li></li>'*5 + '</ul>'
    if cap: d += '<ul class="deck-cap" aria-hidden="true"><li>Metal</li><li>Primer</li><li>Base</li><li>Pearl</li><li>Clear</li></ul>'
    return d

HEAD = '''<!doctype html><html lang="en" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Act&#39;s Paint &amp; Body Shop (concept)"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}"><meta property="og:image" content="{base}og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{base}og.png">
<meta name="robots" content="noindex, nofollow"><!-- concept demo, not for indexing -->
<meta name="theme-color" content="#f7f1e6">
<link rel="preload" as="font" type="font/woff2" href="fonts/gloock-normal-400-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="fonts/hanken-grotesk-normal-400-700-latin.woff2" crossorigin>
<link rel="stylesheet" href="css/design-system.css"><link rel="stylesheet" href="css/components.css"><link rel="stylesheet" href="css/pages.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='16' fill='%239a3b22'/%3E%3Ctext x='16' y='22' font-family='Georgia' font-size='17' fill='%23fff' text-anchor='middle'%3EA%3C/text%3E%3C/svg%3E">
<script>document.documentElement.classList.replace('no-js','js-ready')</script><script type="application/ld+json">{ld}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="demo-bar">Concept by <a href="https://luminarch.pro">LuminArch</a>. Not an official Act&rsquo;s Paint &amp; Body Shop site; their domain is on hold. Reviews are real and sourced; placeholders are labeled.</div>
<header class="top"><div class="wrap nav"><a class="mark" href="index.html"><span class="mk" aria-hidden="true">A</span><span><b>Act&rsquo;s Paint &amp; Body</b><small>304 S Elm St &middot; Durham</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button><ul id="menu">{nav}</ul><a class="btn btn--brick btn--call" href="tel:{tel}"><span class="cl-full">{telh}</span><span class="cl-short">Call</span></a></div></header><main id="main">'''

FOOT = f'''</main><footer class="site-foot">{DECK(10)}<div class="wrap">
<div class="sign">
 <p class="sign-k">Scrape, dent, peeling clear coat?</p>
 <p class="sign-h">Call Pastor Al for a quote.</p>
 <a class="sign-num" href="tel:{TEL}">{TEL_H}</a>
 <p class="sign-sub">Monday to Friday, 8am to 5pm &middot; 304 S Elm St, Durham, NC 27701</p>
</div>
<div class="foot-grid">
 <p class="foot-quote">&ldquo;From the carpet to the insurance claims office.&rdquo;<span>The shop&rsquo;s own words, from its former website (archived Feb 2025)</span></p>
 <nav aria-label="Footer"><a href="services.html">Services</a><a href="reviews.html">Reviews</a><a href="about.html">About</a><a href="contact.html">Get a quote</a></nav>
</div>
<div class="foot-row"><span>Act&rsquo;s Paint &amp; Body Shop &middot; Durham, North Carolina</span><span>Concept by <a href="https://luminarch.pro">LuminArch</a></span></div></div></footer>
<script src="js/main.js"></script></body></html>'''

NAV = [('services.html','Services'),('reviews.html','Reviews'),('about.html','About'),('contact.html','Get a quote')]
def bc(*n): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":a,"item":BASE+b} for i,(a,b) in enumerate(n)]}
def page(fn, t, d, body, ld=None):
    assert 50 <= len(t) <= 60, (fn, len(t), t)
    assert 140 <= len(d) <= 160, (fn, len(d), d)
    nav = ''.join(f'<li><a href="{h}"' + (' aria-current="page"' if h == fn else '') + f'>{n}</a></li>' for h, n in NAV)
    url = BASE + ('' if fn == 'index.html' else fn)
    open(fn,'w').write(HEAD.format(t=t,d=d,url=url,base=BASE,nav=nav,ld=json.dumps(ld or [ORG]),tel=TEL,telh=TEL_H) + body + FOOT)

# Google reviews, word for word, from the Exa place page https://exa.ai/library/place/np2yylyfbwf (Google listing data, checked 9 Oct 2026). All 5 of 5.
# "..." = cut short at the source. One em dash replaced with a comma for house style (Jun 2025).
REV = [
 ('2025-08-13','Aug 2025','If your car has a scrape and you aren&rsquo;t sure where to go, this is the place!! When my car got scraped in a parking garage, I was worried about going through insurance because of my high deductible and potential rate increases. Pastor Al not only gave me an incredibly reasonable quote, he completed the job less than 48 hours after drop&#8209;off with impeccable results (and my car has a metallic tri&#8209;coat that is not easy to match!) Amazing work and amazing service at a reasonable price!! If I ever need paint or body work done again, I will be back.','Tri-coat scrape &middot; paid out of pocket'),
 ('2025-10-12','Oct 2025','Can&rsquo;t recommend this shop enough. Damaged my Land Cruiser while off roading at Uwharrie so insurance was a no go. Scheduled an estimate and discussed options. They were able to repair the panel instead of replacing it which saved me a significant amount of money. Dropped it off Monday and it was ready to go the following Friday. If you need some bodywork done for a reasonable price go check them out!','Land Cruiser &middot; panel repaired, not replaced'),
 ('2025-09-09','Sep 2025','I don&rsquo;t usually leave reviews, but I&rsquo;d be amiss not to take a moment to appreciate Pastor Al and Ms. Geneva. With an upcoming move, I needed my car done quickly. I dropped it off Thursday at 4:30 pm with a fender that needed painting, and by Friday at 1:45 pm Pastor Al called me to pick it up. Not only was my car finished early, but he also reinstalled the fender liner, glued down part of the running panel that had started to lift, and made sure the wiring for my fender blinker was accessible so I could add the light once it arrived. On top of excellent service, Pastor Al and Ms. Geneva took...','Fender paint &middot; next day'),
 ('2025-09-03','Sep 2025','About 5 years ago, I had a massive paint peeling on my trunk. Places closer to my area priced me at $1200+ to repaint the whole trunk. These guys did it for half that and did a fantastic job repainting my trunk. I am forever grateful and would absolutely recommend them for something like that.','Trunk repaint'),
 ('2025-10-09','Oct 2025','We had a wonderful experience with Acts Paint and Body Shop. Our car looks brand new! They finished it earlier than expected and did an excellent job! Thank you Pastor Al and team!','Finished early'),
 ('2025-06-10','Jun 2025','Brilliant! I recently had my rear bumper repaired at Acts Paint, and I couldn&rsquo;t be happier with the experience. The price was amazing, very reasonable compared to other quotes I received, and the repair was completed right on time. The team was professional and efficient, and the quality of the work exceeded my expectations. I strongly recommend Acts Paint to anyone looking for reliable and affordable auto body repair.','Rear bumper'),
 ('2018-07-20','Jul 2018','Incredible service! Al and Chris are wonderful people and want the best for their customers. They were quick, reasonable, and do high quality work! You can&rsquo;t even tell our Jeep doors were both smashed in after they fixed them.','Jeep doors'),
]
def rcard(r, cls=''):
    iso,d,txt,job = r
    return (f'<figure class="rcard rv {cls}"><div class="rc-top"><span>{job}</span><span class="stars" aria-label="5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</span></div>'
            f'<blockquote><p>{txt}</p></blockquote><figcaption>Google review &middot; <time datetime="{iso}">{d}</time></figcaption></figure>')

CLOCK = [('Thu 4:30 pm','Dropped off: a fender that needed paint'),('Fri 1:45 pm','Pastor Al calls: come get it'),('Under 48 hours','A metallic tri&#8209;coat matched after a garage scrape'),('Monday to Friday','A Land Cruiser panel repaired instead of replaced')]

# ---------- HOME ----------
page('index.html',"Act's Paint & Body Shop | Auto Paint and Body Repair, Durham",
 "Pastor Alfred Brunson's paint and body shop at 304 S Elm St, Durham. Paint matching, dent repair, bumpers and fenders. 4.8 stars from 104 Google reviews.", f'''
<section class="hero"><div class="wrap">
 <div class="hero-head">{K('Paint and body &middot; Durham, NC')}
  <h1>Paint and body work on South Elm Street, <em>from Pastor Al and Ms. Geneva.</em></h1>
 </div>
 <div class="dip">
  <figure class="dip-a"><img src="img/jag-sanding.webp" width="479" height="359" alt="A technician sanding the fender of a classic Jaguar roadster down to bare metal" fetchpriority="high"><figcaption><b>Before</b> Sanded to metal</figcaption></figure>
  <div class="dip-mid">{DECK(18,True,'deck--hero')}
   <p class="lede">Act&rsquo;s is a small shop with a big Google record: <b>4.8 stars from 104 reviews</b>. Customers talk about paint that matches, quotes that make sense and cars back early.</p>
   <div class="cta"><a class="btn btn--brick" href="tel:{TEL}">Call {TEL_H}</a><a class="btn btn--line" href="contact.html">Ask for a quote</a></div>
   <p class="fine">Mon to Fri, 8am to 5pm &middot; 304 S Elm St</p>
  </div>
  <figure class="dip-b"><img src="img/jag-primer.webp" width="479" height="359" alt="The same Jaguar masked and sprayed in gray primer in the paint booth" fetchpriority="high"><figcaption><b>Next</b> In primer</figcaption></figure>
 </div>
 <p class="fine dip-note">Photos: Act&rsquo;s own before and after section, from its former website (archived 2021). Low resolution; new photos would replace them.</p>
</div></section>

<section class="clock on-dark" aria-labelledby="ck-h"><div class="wrap">
 <div class="clock-head rv">{K('On the clock')}<h2 id="ck-h">What &ldquo;quick&rdquo; means here, in customers&rsquo; words.</h2></div>
 <ol class="clock-list">{''.join(f'<li class="rv"><time>{a}</time><span>{b}</span></li>' for a,b in CLOCK)}</ol>
 <p class="fine rv">Each line is from a Google review dated 2025. Not a promise; every job is different.</p>
</div></section>

<section class="pocket wrap" aria-labelledby="pk-h">
 <div class="pocket-copy rv">{K('Paying out of pocket?')}<h2 id="pk-h">A straight quote, before you decide on insurance.</h2>
  <p>Three of the reviews here skipped insurance: a high deductible, an off road dent, a peeling trunk. Each one got a quote first, then decided.</p>
  <p>The shop&rsquo;s former website said it covers &ldquo;every step of the repair process. From the carpet to the insurance claims office.&rdquo; Claim or cash, ask Pastor Al.</p>
  <a class="btn btn--brick" href="contact.html">Ask for a quote</a></div>
 {rcard(REV[3],'pocket-q')}
</section>

<section class="menu-sec wrap" aria-labelledby="sv-h">
 <div class="rv">{K('Services')}<h2 id="sv-h">The menu, from the shop&rsquo;s own list.</h2>{DECK(8)}</div>
 <ul class="svc-list">
  <li class="rv"><b>Auto painting</b><span>Panels to full trunk repaints</span></li>
  <li class="rv"><b>Paint matching</b><span>Including metallic tri&#8209;coats</span></li>
  <li class="rv"><b>Dent repair</b><span>Including paintless dent removal</span></li>
  <li class="rv"><b>Bumper repair</b><span>Front and rear</span></li>
  <li class="rv"><b>Fender repair</b><span>Paint, liners, trim</span></li>
  <li class="rv"><b>Aluminum repair</b><span>Listed by the shop</span></li>
  <li class="rv"><b>Hail damage</b><span>Listed by the shop</span></li>
  <li class="rv"><b>Estimates</b><span>Call or stop by</span></li>
 </ul>
 <a class="btn btn--line rv" href="services.html">All services</a>
</section>

<section class="voices wrap" aria-labelledby="vo-h">
 <div class="rv">{K('What customers say')}<h2 id="vo-h">104 Google reviews, 4.8 stars.</h2></div>
 <div class="voices-grid">{rcard(REV[4],'rcard--lead')}{rcard(REV[0])}{rcard(REV[5])}</div>
 <a class="btn btn--line rv" href="reviews.html">Read seven of them</a>
</section>
''', ld=[ORG, bc(('Home',''))])

# ---------- SERVICES ----------
SV = [('paint','Auto painting','Single panels to a full trunk repaint. One reviewer was quoted $1,200 and up elsewhere for a peeling trunk and paid about half here.',REV[3]),
 ('match','Paint matching','The hardest job in paint. A reviewer with a metallic tri&#8209;coat had a garage scrape matched in under 48 hours.',REV[0]),
 ('dent','Dent repair and paintless dent removal','Both are on the shop&rsquo;s own service list. One customer&rsquo;s Land Cruiser panel was repaired instead of replaced, which saved a significant amount.',REV[1]),
 ('bumper','Bumper repair','Front and rear. A June 2025 reviewer called the price very reasonable compared to other quotes.',REV[5]),
 ('fender','Fender repair','Paint, plus the small things: one customer got the fender liner reinstalled and a lifting panel glued down.',REV[2]),
 ('aluminum','Aluminum repair','On the shop&rsquo;s own service list.',None),
 ('hail','Hail damage repair','On the shop&rsquo;s own service list.',None)]
def sv(i,s):
    k,n,d,r = s
    short = (r[2] if len(r[2]) < 260 else r[2][:250].rsplit(' ',1)[0] + '...') if r else ''
    side = (f'<blockquote class="sv-q"><p>{short}</p><footer>Google review, {r[1]}</footer></blockquote>' if r else
            '<p class="note"><span class="ph">Placeholder</span> A before and after pair from a recent job of this kind.</p>')
    return f'<article id="{k}" class="sv rv"><span class="sv-n">{i+1:02d}</span><div class="sv-body"><h2>{n}</h2><p>{d}</p></div>{side}</article>'
page('services.html',"Paint, Dent and Bumper Repair Services | Act's Paint, Durham",
 "Auto painting, paint matching, dent and paintless dent repair, bumpers, fenders, aluminum and hail damage at Act's Paint & Body Shop on S Elm St in Durham.", f'''
<section class="sub"><div class="wrap">{K('Services')}<h1>From the shop&rsquo;s own list.</h1><p class="lede">Every service here was on Act&rsquo;s former website. Quotes are from Google reviews.</p>{DECK(10,True)}</div></section>
<section class="wrap svs">{''.join(sv(i,s) for i,s in enumerate(SV))}</section>
<section class="wrap band rv"><h2>Want a number before you decide?</h2><p>Call or stop by South Elm Street for an estimate.</p><a class="btn btn--brick" href="contact.html">Ask for a quote</a></section>
''', ld=[ORG, bc(('Home',''),('Services','services.html'))])

# ---------- REVIEWS ----------
page('reviews.html',"Reviews | Act's Paint & Body Shop, Body Repair Durham NC",
 "Real Google reviews for Act's Paint & Body Shop in Durham, quoted word for word with dates. 4.8 stars from 104 reviews for paint matching and body repair.", f'''
<section class="sub"><div class="wrap">{K('Reviews')}<h1>4.8 stars from 104 Google reviews.</h1><p class="lede">Seven of them, word for word, with the date each was posted.</p>{DECK(10)}</div></section>
<section class="wrap rv-list">{''.join(rcard(r) for r in REV)}</section>
<section class="wrap"><p class="note rv"><span class="ph">Placeholder</span> On the real site, a live Google reviews feed or a set Pastor Al picks. Yelp has 16 more.</p></section>
''', ld=[ORG, bc(('Home',''),('Reviews','reviews.html'))])

# ---------- ABOUT ----------
page('about.html',"About Pastor Al Brunson | Act's Paint & Body Shop, Durham",
 "Act's Paint & Body Shop is Pastor Alfred Brunson's paint and body shop at 304 S Elm St in downtown Durham. Customers name Pastor Al, Ms. Geneva and Chris.", f'''
<section class="sub"><div class="wrap">{K('About')}<h1>Pastor Al&rsquo;s shop.</h1><p class="lede">Alfred Brunson owns Act&rsquo;s. Customers call him Pastor Al.</p>{DECK(10)}</div></section>
<section class="wrap about">
 <div class="phbox rv"><p><span class="ph">Placeholder</span> Portrait of Pastor Al and Ms. Geneva at the shop door on South Elm Street.</p></div>
 <div class="about-copy rv">
  <h2>Small shop. Names you will hear.</h2>
  <p>Reviewers name Pastor Al and Ms. Geneva again and again, and a 2018 review names Al and Chris. One customer&rsquo;s car got a wash before pickup. Another got a call the next afternoon: done early.</p>
  <p class="note"><span class="ph">Placeholder</span> The story in Pastor Al&rsquo;s words: how long the shop has been here, where the name Act&rsquo;s comes from, and who does what.</p>
 </div>
</section>
<section class="wrap facts rv"><h2 class="sr">Shop facts</h2><dl>
 <div><dt>Owner</dt><dd>Pastor Alfred Brunson</dd></div>
 <div><dt>Address</dt><dd>304 S Elm St, Durham, NC 27701</dd></div>
 <div><dt>Hours</dt><dd>Mon to Fri, 8am to 5pm</dd></div>
 <div><dt>Google</dt><dd>4.8 from 104 reviews</dd></div>
</dl></section>
''', ld=[ORG, bc(('Home',''),('About','about.html'))])

# ---------- CONTACT ----------
page('contact.html',"Get a Quote | Act's Paint & Body Shop, 304 S Elm St, Durham",
 "Ask Act's Paint & Body Shop for a paint or body repair quote. Call (919) 680-6802 or stop by 304 S Elm St, Durham, NC. Open Monday to Friday, 8am to 5pm.", f'''
<section class="sub"><div class="wrap">{K('Get a quote')}<h1>Call, or stop by South Elm.</h1><p class="lede">Calling is fastest. The form shows how a photo quote request could work.</p>{DECK(10)}</div></section>
<section class="wrap contact">
 <div class="c-info rv">
  <h2>The shop</h2>
  <a class="c-big" href="tel:{TEL}">{TEL_H}</a>
  <p>304 S Elm St<br>Durham, NC 27701</p>
  <p>Monday to Friday, 8am to 5pm<br>Saturday and Sunday closed</p>
  <p><a class="tlink" href="{MAP}" rel="noopener">Directions in Google Maps</a></p>
 </div>
 <form id="qform" class="form rv" novalidate>
  <p class="note"><span class="ph">Demo form</span> Nothing is sent. On a real site this would reach the shop.</p>
  <fieldset><legend class="sr">Your details</legend>
   <div class="two"><label>Name<input name="n" autocomplete="name"></label><label>Phone<input name="p" type="tel" autocomplete="tel"></label></div>
   <div class="two"><label>Vehicle and color<input name="v"></label><label>Paying by<select name="i"><option>Not sure yet</option><option>Insurance claim</option><option>Out of pocket</option></select></label></div>
   <label>What needs fixing<textarea name="m"></textarea></label>
   <label>Photos<input name="f" type="file" accept="image/*" multiple></label>
  </fieldset>
  <button class="btn btn--brick" type="submit">Send request</button>
  <p id="qmsg" role="status"></p>
 </form>
</section>
''', ld=[ORG, bc(('Home',''),('Get a quote','contact.html'))])

page('404.html',"Page Not Found | Act's Paint & Body Shop, Durham NC Repair",
 "That page is not here. Head back to the Act's Paint & Body Shop home page, or call (919) 680-6802 for paint and body repair at 304 S Elm St in Durham, NC.", f'''
<section class="sub"><div class="wrap">{K('404')}<h1>That page is not here.</h1><p class="lede">Try the home page, or just call the shop.</p><div class="cta"><a class="btn btn--brick" href="index.html">Home</a><a class="btn btn--line" href="tel:{TEL}">Call {TEL_H}</a></div>{DECK(10)}</div></section>
''')
print('built')
