#!/usr/bin/env python3
"""Generate insights.html and every post page from the POSTS list below.

To add a post: append a dict to POSTS, run this, then run
scripts/inline-partials.py, then add the new URL to sitemap.xml.
"""
import html, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = 'https://3we4.media'
DATE, DATE_HUMAN = '2026-09-21', '21 September 2026'
MAIL = 'mailto:3WE4.media@gmail.com?subject=Enquiry%20from%203we4.media'
DR = 'https://datareportal.com/reports/digital-2026-india'
PWC = 'https://www.pwc.in/industries/retail-and-consumer/global-consumer-insights-pulse-survey-india-perspective.html'

SRC_DR = f'<li>DataReportal, <a href="{DR}" target="_blank" rel="noopener">Digital 2026: India</a> (Kepios analysis; Meta and Google ad tools), October 2025.</li>'
SRC_PWC = f'<li>PwC, <a href="{PWC}" target="_blank" rel="noopener">Global Consumer Insights Pulse Survey, India perspective</a>, June 2023.</li>'

POSTS = [
 dict(
  slug='insights-social-media-asset-or-liability', label='Mindset',
  title='Social Media: Asset or Liability? Six Tests | 3WE4.media',
  desc='Most businesses run social media as an expense. Six blunt tests to tell whether yours is a liability or an asset, with sourced India numbers.',
  h1='Social media: asset or liability?<br><span class="accent">Six tests.</span>',
  card='Social media: asset or liability? Six tests.',
  body=f'''
<p class="lead">A liability costs you money and gives nothing back. An asset is something you build once that keeps working for you. Social media can be either one, and the platform has nothing to do with which. It comes down to how you run it.</p>

<h2>Your customers are already there</h2>
<p>Start with the size of the room. At the end of 2025, <strong>1.03 billion</strong> people were online in India, 70% of the population. There were <strong>500 million</strong> active social media user identities (accounts, not unique people). Instagram can reach <strong>481 million</strong> people in India with ads, and YouTube <strong>500 million</strong>.<sup><a href="#sources">1</a></sup> In a 2023 PwC survey, <strong>29%</strong> of consumers in India said they use social media to research a product before buying it.<sup><a href="#sources">2</a></sup></p>
<p>Those numbers don't say social media works for everyone. They say your customers are there whether you are or not. The only thing you choose is what they find when they look.</p>

<h2>The six tests</h2>
<p>Answer honestly. Nobody is marking you.</p>
<ol>
<li><strong>Can you say what it earned last month?</strong> In rupees, leads or enquiries. "Good reach" is not an answer. If you can't name a number a business can spend, you are paying for something you can't see.</li>
<li><strong>Does every post have a job?</strong> Get you found, earn trust, or drive a sale. If a post exists because "it's been three days", it's noise, and you are paying to produce it.</li>
<li><strong>Is one person accountable for it?</strong> Not a cousin, an intern and a freelancer each guessing. One owner who answers for results, not just for uploads.</li>
<li><strong>Would a stranger trust you in 30 seconds?</strong> Open your own profile as if you had never heard of you. Can you tell what is sold, to whom, with what proof, and how to get in touch?</li>
<li><strong>Is anything you posted last quarter still working?</strong> Assets compound. If nothing from three months ago brings anyone to you today, you are renting attention, not building it.</li>
<li><strong>Would it be the first thing cut when money is tight?</strong> Businesses cut expenses first and protect whatever brings in sales. If social media goes first, you already treat it as a liability, and it will perform like one.</li>
</ol>
<p>Fail three or more and you are running a liability. That isn't an insult. It is the default outcome when nobody sets social media up to be anything else.</p>

<h2>What turns a liability into an asset</h2>
<p>Four things, in this order:</p>
<ul>
<li><strong>A goal in money terms.</strong> Enquiries, bookings, orders. Decide it before you post anything.</li>
<li><strong>A system, not a calendar.</strong> Strategy first, then production, then distribution, all pointed at that goal. This is how we run <a href="services.html">the system</a>.</li>
<li><strong>One accountable owner.</strong> Someone who can be asked "why didn't that work?" and has an answer.</li>
<li><strong>Measurement that matches the goal.</strong> Likes measure attention. Sales measure value. Read <a href="insights-likes-are-not-revenue.html">what to measure instead of likes</a>.</li>
</ul>
<p>It doesn't start with a bigger budget. It starts with a decision to stop treating social media as decoration.</p>

<p>If you want a straight read on which one you are running, that is what a first conversation with us is for: <a href="{MAIL}">3WE4.media@gmail.com</a>. Or keep reading: <a href="insights-where-online-sales-leak.html">where online sales leak</a>.</p>

<div class="sources" id="sources">
<p>Sources</p>
<ol>
{SRC_DR}
{SRC_PWC}
</ol>
<p>The six tests and the conclusions drawn from them are our opinion, not survey findings.</p>
</div>
'''),
 dict(
  slug='insights-where-online-sales-leak', label='Diagnosis',
  title='3 Ways Your Business Loses Online Sales | 3WE4.media',
  desc="Nobody invoices you for a sale you didn't get. Three leaks between a stranger and a customer, and a free check for each one you can do today.",
  h1='Three places your business loses sales online.<br><span class="accent">How to check each one.</span>',
  card='Three places your business loses sales online.',
  body=f'''
<p class="lead">Nobody sends you an invoice for a sale you didn't get. That is why a weak online presence feels harmless: the loss is real, but it never shows up on a statement.</p>
<p>A customer has to get through three points on the way from stranger to sale, and you can lose them at any of the three. Here is each one, and how to check yours today without paying anyone.</p>

<h2>Leak 1: They never find you</h2>
<p>You don't lose this sale. You never learn it existed. Someone searched, scrolled or asked a friend, and you weren't where they looked.</p>
<p><strong>Check it:</strong></p>
<ul>
<li>Search your business name on Google, Instagram and YouTube. Do you appear on the first screen, with the right name and a profile that looks like you?</li>
<li>Search the phrase a customer would type for what you sell, plus your area. Do you appear? Who appears instead of you?</li>
<li>Read your profile description. Does it say what you sell and where, in words a customer would actually use?</li>
</ul>
<p>Why it matters: 29% of consumers in India use social media to research a product before buying it (PwC, 2023).<sup><a href="#sources">1</a></sup> If they go looking there, being findable there is not optional.</p>

<h2>Leak 2: They find you, then leave</h2>
<p>They didn't decide you were bad. They decided someone else looked safer. Trust online is judged fast, and on small things.</p>
<p><strong>Check it:</strong></p>
<ul>
<li><strong>When was your last post?</strong> A page that went quiet months ago looks like a closed business.</li>
<li><strong>Would you buy from your own feed?</strong> Look at your last nine posts. Do they show real work, real results and real people, or stock images and festival greetings?</li>
<li><strong>Is there proof?</strong> Reviews, finished work, before-and-afters, what customers say.</li>
<li><strong>Are comments and DMs answered?</strong> An unanswered question in public tells everyone else how you treat customers.</li>
</ul>

<h2>Leak 3: They trust you, and nothing happens</h2>
<p>This is the most expensive leak and the cheapest to fix, because these people already want to buy.</p>
<p><strong>Check it:</strong></p>
<ul>
<li><strong>Is there one obvious next step?</strong> Call, WhatsApp, book, visit. Not five links and a paragraph.</li>
<li><strong>Does it work?</strong> Tap your own link on a phone, right now.</li>
<li><strong>How fast do you reply?</strong> Time it. A message that waits a day is a customer who asked someone else.</li>
<li><strong>Does anyone follow up?</strong> Someone asks the price and goes quiet. Does anybody ever check back?</li>
</ul>

<h2>Fix them from the bottom up</h2>
<p>Start with Leak 3, then Leak 2, then Leak 1. There is no point paying to bring more people into a funnel that already loses the ones who arrive. This is our opinion, and it comes from simple arithmetic: turning more visitors into customers multiplies whatever traffic you have, while adding traffic without that just increases the number you lose.</p>
<p>It is also how we work. We look for the leak before we touch a camera. That is the "Diagnose" step in <a href="services.html">how we work</a>.</p>

<p>If you would rather have someone else look at yours, email <a href="{MAIL}">3WE4.media@gmail.com</a>. Or read <a href="insights-likes-are-not-revenue.html">what to measure once you have fixed them</a>.</p>

<div class="sources" id="sources">
<p>Sources</p>
<ol>
{SRC_PWC}
</ol>
<p>The three leaks, the checks and the order of fixing them are our own framework and opinion, not survey findings.</p>
</div>
'''),
 dict(
  slug='insights-likes-are-not-revenue', label='Measurement',
  title='Likes Are Not Revenue: What to Measure | 3WE4.media',
  desc='Likes and reach measure attention, not sales. The four numbers that show whether social media pays for itself, and how to track them without software.',
  h1='Likes are not revenue.<br><span class="accent">Measure this instead.</span>',
  card='Likes are not revenue. Measure this instead.',
  body=f'''
<p class="lead">Likes feel like progress. They are easy to see, they move every day, and they make a report look busy. None of them can be spent.</p>

<h2>What the usual numbers actually tell you</h2>
<ul>
<li><strong>Likes.</strong> Someone reacted. That is attention, not intent.</li>
<li><strong>Followers.</strong> A list of people who once pressed follow. Some are customers. Many are not, and some are not even people.</li>
<li><strong>Reach and impressions.</strong> How many times it was shown. Whether it changed anyone's mind is a different question.</li>
<li><strong>Views.</strong> The video played. That doesn't say whether they would buy.</li>
</ul>
<p>These numbers aren't useless. They tell you whether people noticed you. They do not tell you whether it paid.</p>

<h2>The four numbers that do</h2>
<ol>
<li><strong>Enquiries.</strong> Calls, DMs, WhatsApp messages and form fills that came because of social media, per month.</li>
<li><strong>Qualified enquiries.</strong> The ones from people who could actually buy what you sell. Ten right enquiries beat a hundred wrong ones.</li>
<li><strong>Sales from those enquiries.</strong> In rupees. This is the number that ends arguments.</li>
<li><strong>Cost per sale.</strong> Everything you spent (content, ads, tools, your own time) divided by the sales it produced. This is the ratio that tells you whether social media is an asset or an expense.</li>
</ol>

<h2>How to track them without buying software</h2>
<ul>
<li><strong>Ask every new customer how they found you</strong>, and write the answer down. It is free, and it works.</li>
<li><strong>Give social media its own way to reach you.</strong> A dedicated WhatsApp link, a separate number, or an offer code that is only ever used there.</li>
<li><strong>Tag the link in your bio.</strong> Adding a tracking tag (a UTM parameter) to the link tells your analytics which source sent the click.</li>
<li><strong>Keep one sheet.</strong> One row per enquiry: date, source, qualified yes or no, sale amount. Ten minutes a week.</li>
</ul>

<h2>What good looks like</h2>
<p>We won't give you a benchmark. It varies by business, and any number we made up would be a guess dressed as a fact. Compare yourself with yourself: this month's enquiries, sales and cost per sale against the last three months. If those are improving, it is working. If likes are climbing and those are not, you are being entertained, not paid.</p>
<p>It is also how we judge our own work, and why our results page reports leads and sales, not likes. Here is <a href="results.html">how to read our numbers</a>, including the parts we can't show you.</p>

<p>If you want help setting up the tracking, email <a href="{MAIL}">3WE4.media@gmail.com</a>. Or start from the beginning: <a href="insights-social-media-asset-or-liability.html">asset or liability, six tests</a>.</p>

<div class="sources" id="sources">
<p>Note</p>
<p>The metrics framework and advice above are our own opinion and experience. No third-party statistics are used in this post.</p>
</div>
'''),
]

ICONS = ('<link rel="icon" href="/favicon.ico" sizes="48x48">\n'
         '<link rel="icon" type="image/png" sizes="192x192" href="/assets/icon-192.png">\n'
         '<link rel="apple-touch-icon" href="/apple-touch-icon.png">')
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;700;800;900&family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">')

def read_minutes(body):
    words = len(re.sub(r'<[^>]+>', ' ', body).split())
    return max(1, round(words / 200)), words

def head(title, desc, path, og_type, ld):
    e = html.escape
    url = f'{BASE}/{path}'
    extra = ''
    if og_type == 'article':
        extra = f'\n<meta property="article:published_time" content="{DATE}T00:00:00+05:30">\n<meta property="article:author" content="3WE4.media">'
    return f'''<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">

<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="en_IN">
<meta property="og:site_name" content="3WE4.media">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/og-cover.png">
<meta property="og:image:alt" content="3WE4.media logo">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">{extra}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{BASE}/assets/og-cover.png">

{ICONS}
{FONTS}
<link rel="stylesheet" href="style.css?v=6">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
</script>
</head>'''

def crumbs(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}

def page(headhtml, main):
    return f'''{headhtml}
<body data-page="insights">

<div id="site-header-mount"></div>

<main id="main">

{main.strip()}

</main>

<div id="site-footer-mount"></div>

<script src="script.js?v=5"></script>
</body>
</html>
'''

def card(p, minutes):
    return f'''        <div class="teaser-card">
          <p class="teaser-label">{p['label']}</p>
          <h3>{p['card']}</h3>
          <p>{html.escape(p['desc'])}</p>
          <p class="post-meta"><span>{DATE_HUMAN}</span><span>{minutes} min read</span></p>
          <a class="teaser-link" href="{p['slug']}.html">Read the post</a>
        </div>'''

mins = {p['slug']: read_minutes(p['body'])[0] for p in POSTS}

# ---- individual posts
for p in POSTS:
    path = p['slug'] + '.html'
    url = f'{BASE}/{path}'
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BlogPosting", "headline": p['card'], "description": p['desc'],
         "datePublished": DATE, "dateModified": DATE, "inLanguage": "en-IN",
         "mainEntityOfPage": {"@type": "WebPage", "@id": url}, "image": f"{BASE}/assets/og-cover.png",
         "author": {"@type": "Organization", "name": "3WE4.media", "url": f"{BASE}/"},
         "publisher": {"@type": "Organization", "name": "3WE4.media", "url": f"{BASE}/",
                       "logo": {"@type": "ImageObject", "url": f"{BASE}/assets/icon-512.png"}}},
        crumbs([("Home", f"{BASE}/"), ("Insights", f"{BASE}/insights.html"), (p['card'], url)])]}
    others = [q for q in POSTS if q['slug'] != p['slug']]
    more = '\n'.join(card(q, mins[q['slug']]) for q in others)
    main = f'''  <section class="page-hero">
    <div class="wrap">
      <p class="eyebrow reveal">Insights · {p['label']}</p>
      <h1 class="section-title reveal">{p['h1']}</h1>
      <p class="post-meta reveal"><span>By 3WE4.media</span><span>{DATE_HUMAN}</span><span>{mins[p['slug']]} min read</span></p>
    </div>
  </section>

  <section class="post-body">
    <div class="wrap">
      <article class="prose">
{p['body'].strip()}
      </article>
    </div>
  </section>

  <section class="band-alt" id="keep-reading">
    <div class="wrap">
      <p class="eyebrow">Keep reading</p>
      <h2 class="section-title">More from Insights.</h2>
      <div class="teaser-grid teaser-grid-2">
{more}
      </div>
    </div>
  </section>'''
    (ROOT / path).write_text(page(head(p['title'], p['desc'], path, 'article', ld), main))

# ---- index
idx_title = 'Insights on Social Media That Sells | 3WE4.media'
idx_desc = 'Short, blunt, sourced notes on why most social media never pays and what to do about it, from a digital growth agency in Greater Noida.'
ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "CollectionPage", "name": "Insights", "url": f"{BASE}/insights.html", "description": idx_desc,
     "inLanguage": "en-IN", "isPartOf": {"@type": "WebSite", "url": f"{BASE}/", "name": "3WE4.media"}},
    crumbs([("Home", f"{BASE}/"), ("Insights", f"{BASE}/insights.html")])]}
cards = '\n'.join(card(p, mins[p['slug']]) for p in POSTS)
main = f'''  <section class="page-hero">
    <div class="wrap">
      <p class="eyebrow reveal">Insights</p>
      <h1 class="section-title reveal">Straight talk about<br><span class="accent">social media that sells.</span></h1>
      <p class="page-hero-sub reveal">Short, blunt and sourced. Why most social media never pays, how to tell where your sales are leaking, and what to measure instead of likes. No jargon, no theory.</p>
    </div>
  </section>

  <section class="band" id="posts">
    <div class="wrap">
      <div class="teaser-grid">
{cards}
      </div>
    </div>
  </section>'''
(ROOT / 'insights.html').write_text(page(head(idx_title, idx_desc, 'insights.html', 'website', ld), main))

print('wrote insights.html +', len(POSTS), 'posts')
for p in POSTS:
    m, w = read_minutes(p['body'])
    print(f"  {p['slug']}.html  {w} words, {m} min | title {len(p['title'])} chars | desc {len(p['desc'])} chars")
    assert len(p['title']) <= 62 and len(p['desc']) <= 160
assert len(idx_title) <= 62 and len(idx_desc) <= 160, (len(idx_title), len(idx_desc))
