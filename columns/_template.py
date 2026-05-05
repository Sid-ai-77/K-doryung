# -*- coding: utf-8 -*-
"""Generate 9 K-Doryung editorial columns from a shared template."""

from pathlib import Path

OUT_DIR = Path(r"D:\\업무_개인_사업\\K-doryung\\columns")

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} — K-Doryung Editorial</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<style>
  :root{{--paper:#FBFAF6;--ink:#111;--ink-soft:#2A2A2A;--ink-muted:#6B6B6B;--accent:#7A1F1F;--rule:#1A1A1A;--serif:'Cormorant Garamond',Georgia,serif;--sans:'Inter',-apple-system,sans-serif}}
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{background:var(--paper);color:var(--ink);font-family:var(--serif);font-size:18px;line-height:1.65;-webkit-font-smoothing:antialiased}}
  .mast{{border-bottom:1px solid var(--rule);padding:18px 28px;display:flex;align-items:center;justify-content:space-between;font-family:var(--sans)}}
  .mast .brand{{font-family:var(--serif);font-style:italic;font-size:20px}}
  .mast a.back{{font-size:11px;letter-spacing:0.18em;text-transform:uppercase;color:var(--ink-muted);text-decoration:none}}
  .hero{{position:relative;width:100%;aspect-ratio:16/10;max-height:60vh;overflow:hidden}}
  .hero img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
  .hero-caption{{padding:28px 22px 22px;border-bottom:1px solid var(--rule)}}
  .kicker{{font-family:var(--sans);font-weight:600;font-size:10px;letter-spacing:0.28em;text-transform:uppercase;color:var(--accent);margin-bottom:10px}}
  h1.headline{{font-family:var(--serif);font-weight:600;font-size:32px;line-height:1.1;letter-spacing:-0.005em;color:var(--ink);margin-bottom:12px;max-width:none}}
  .deck{{font-family:var(--serif);font-style:italic;font-size:16px;line-height:1.55;color:var(--ink-soft)}}
  .byline{{padding:14px 22px;font-family:var(--sans);font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:var(--ink-muted);border-bottom:1px solid var(--rule);display:flex;flex-direction:column;gap:6px}}
  .byline strong{{color:var(--ink);font-weight:600}}
  .article{{max-width:720px;margin:36px auto 0;padding:0 22px 80px}}
  .article p{{margin-bottom:18px;font-size:16px;line-height:1.65;color:var(--ink-soft)}}
  .article h2{{font-family:var(--serif);font-weight:600;font-size:22px;letter-spacing:-0.005em;margin:30px 0 10px;color:var(--ink)}}
  .article h2::before{{content:'';display:block;width:32px;height:2px;background:var(--accent);margin-bottom:12px}}
  .pull{{margin:32px 0;padding:22px 0 18px;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);text-align:center}}
  .pull blockquote{{margin:0;font-family:var(--serif);font-style:italic;font-weight:500;font-size:20px;line-height:1.4;letter-spacing:-0.005em;color:var(--ink);max-width:24ch;margin:0 auto}}
  .pull cite{{display:block;margin-top:12px;font-family:var(--sans);font-style:normal;font-size:11px;letter-spacing:0.22em;text-transform:uppercase;color:var(--ink-muted)}}
  figure{{margin:30px 0}}
  figure img{{width:100%;height:auto;display:block;aspect-ratio:16/10;object-fit:cover}}
  figure figcaption{{font-family:var(--sans);font-size:11px;letter-spacing:0.18em;text-transform:uppercase;color:var(--ink-muted);text-align:center;margin-top:12px}}
  .ifyougo{{margin:30px auto;border:1px solid var(--rule);padding:22px;background:#F1ECE1}}
  .ifyougo .label{{font-family:var(--sans);font-weight:700;font-size:11px;letter-spacing:0.28em;text-transform:uppercase;color:var(--accent);margin-bottom:10px}}
  .ifyougo h3{{font-family:var(--serif);font-size:22px;font-weight:600;margin-bottom:14px;letter-spacing:-0.005em}}
  .ifyougo dt{{font-family:var(--sans);font-size:11px;letter-spacing:0.18em;text-transform:uppercase;font-weight:700;margin-top:10px;color:var(--ink)}}
  .ifyougo dd{{font-size:15px;line-height:1.55;color:var(--ink-soft);margin-top:3px}}
  .credits{{border-top:1px solid var(--rule);padding:20px 22px 40px;font-family:var(--sans);font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:var(--ink-muted);line-height:1.7}}
  @media (min-width:768px){{
    body{{font-size:18px}}
    .article{{margin-top:48px}}
    h1.headline{{font-size:48px}}
    .deck{{font-size:20px}}
    .article p{{font-size:18px}}
    .article h2{{font-size:28px}}
    .pull blockquote{{font-size:26px}}
  }}
</style>
</head>
<body>
<header class="mast">
  <div class="brand">The Wanderer&rsquo;s Notebook</div>
  <a class="back" href="../index.html">&larr; Back</a>
</header>
<section class="hero"><img src="{img}" alt=""></section>
<section class="hero-caption">
  <div class="kicker">{kicker}</div>
  <h1 class="headline">{title}</h1>
  <p class="deck">{deck}</p>
</section>
<div class="byline">
  <span>By <strong>The Editor</strong></span>
  <span>{location}</span>
  <span>Field Notes, Spring 2026</span>
</div>
<article class="article">
{body}
</article>
<aside class="ifyougo">
  <div class="label">If You Go</div>
  <h3>{ify_h3}</h3>
  <dl>
{ify_dl}
  </dl>
</aside>
<div class="credits">
  Story by The Editor &middot; Photographs via Unsplash, used under the Unsplash License.<br>
  The Wanderer&rsquo;s Notebook &middot; Set in Cormorant Garamond &amp; Inter.
</div>
</body>
</html>
"""

def dl(items):
    return "\n".join(f"    <dt>{k}</dt><dd>{v}</dd>" for k, v in items)

COLUMNS = [
    {
        "slug": "insadong-gil",
        "type": "long",
        "title": "The Slow Streets of Insadong-gil",
        "kicker": "Editor's Notebook · Jongno-gu",
        "deck": "A pedestrian lane where ink, paper and tea outnumber phones, and where every shopkeeper still folds your purchase by hand.",
        "img": "https://images.unsplash.com/photo-1742734703252-25ef2a605d33?auto=format&fit=crop&w=2200&q=80",
        "location": "Insadong-gil · Jongno-gu, Seoul",
        "body": (
            "<p>Insadong-gil is a single, mostly straight pedestrian lane in central Seoul that has been pretending to be quaint for almost a hundred years and, somehow, has actually become so. Walk in from the south end, by Anguk Station, and the first thing the city does is hand you back to a slower clock.</p>"
            "<p>The lane is famously the place to find calligraphy brushes, mulberry paper, traditional tea, and a hundred small ceramic studios you could happily disappear into for an afternoon. Most of the buildings are low — by Seoul standards, comically so — and a number of them are old hanok converted into shops without losing the floor heat.</p>"
            "<h2>What to look for</h2>"
            "<p>The first rule of Insadong is to leave the main lane. The interesting work is up the side alleys: paper-makers feeding cotton pulp through hand-rolled trays, brush-makers tying ox-tail hair onto bamboo, tiny tea houses that ask you to remove your shoes and lower your voice. Insadong rewards anyone willing to climb half a flight of stairs.</p>"
            "<p>Second rule: spend money on something useless. A folded paper crane, a single brush you will not use for years, a pot of ssanghwacha you will sip in your hotel and remember. Insadong's economy is built on the small, considered purchase.</p>"
            "<div class=\"pull\"><blockquote>&ldquo;Insadong is what a city looks like when it remembers its grandparents.&rdquo;</blockquote><cite>&mdash; Field note, 3:14 p.m.</cite></div>"
            "<h2>How to walk it</h2>"
            "<p>Anguk Station, Line 3, Exit 6. Walk south, past the donuts and the matcha-everything shops at the top of the lane (these are recent and tourist-priced; nothing wrong with them, just don't think they are Insadong). Within a hundred metres, real shops begin. Take any side alley you find appealing. You will not get lost.</p>"
            "<p>Doryung says: &ldquo;In a hundred and ninety years I have bought one brush from this lane every spring. The shopkeepers no longer recognise me, but the brushes still know my hand.&rdquo;</p>"
        ),
        "ify_h3": "Insadong-gil · Practical Notes",
        "ify": [
            ("Getting there", "Anguk Station, Seoul Metro Line 3, Exit 6. Five minutes on foot."),
            ("Best time", "Weekday mornings or after 5 p.m. The lane is busiest 1–4 p.m."),
            ("What to buy", "Brushes (붓), mulberry paper (한지), pottery, ssanghwacha tea."),
            ("Pair it with", "Bukchon Hanok Village (10 min walk north) or Jogyesa Temple (5 min west)."),
            ("One small ritual", "Drink one cup of tea sitting on the floor. Most teahouses still expect it."),
        ],
    },
    {
        "slug": "cheonggyecheon",
        "type": "long",
        "title": "Cheonggyecheon — Where the City Comes Up for Air",
        "kicker": "Editor's Notebook · Jung-gu",
        "deck": "A river was buried under a highway, then unburied by a city that decided it preferred the water. Take the stairs down.",
        "img": "https://images.unsplash.com/photo-1687779176476-55920ac3f400?auto=format&fit=crop&w=2200&q=80",
        "location": "Cheonggyecheon · Jung-gu, Seoul",
        "body": (
            "<p>For most of the twentieth century, Cheonggyecheon was a stream the city was politely ignoring. Then it was a covered sewer. Then a six-lane elevated highway ran above it. Then, in 2005, the city tore the highway down, dug the stream back up, and built a six-kilometre walking path along its banks. It was widely considered insane at the time. It is now considered the best decision Seoul has made in fifty years.</p>"
            "<p>The stream begins at Cheonggye Plaza, just south of Gwanghwamun, and runs east through the heart of the old city before joining the Han River. The path is one storey below street level, which is the secret of the place: when you descend the stairs, the noise of Seoul drops by a factor of ten.</p>"
            "<h2>What you'll find</h2>"
            "<p>Stepping stones every few hundred metres. Murals along the embankment walls. Office workers eating cup ramyun on the rocks at lunchtime. Couples in rental hanbok pretending the path is a film set. In summer, kids splash in the shallows. In winter, paper lanterns are strung along the water for the festival, and the whole stream glows.</p>"
            "<h2>How to walk it</h2>"
            "<p>Most visitors walk the first kilometre and turn back. That is enough — the western stretch by Cheonggye Plaza is the most photogenic. If you have time, push east toward Dongdaemun: the stream gets quieter, the bridges older, and you start to share it with locals on bicycles instead of tour groups.</p>"
            "<div class=\"pull\"><blockquote>&ldquo;A river that was buried for forty years has earned the right to be loud about coming back.&rdquo;</blockquote><cite>&mdash; Field note, dusk</cite></div>"
            "<p>Doryung says: &ldquo;I was here when this stream was a stream the first time. I was here when they paved it. I was here when they unpaved it. Of the three, the unpaving was the kindest. Korea is sometimes very good at admitting it was wrong.&rdquo;</p>"
        ),
        "ify_h3": "Cheonggyecheon · Practical Notes",
        "ify": [
            ("Getting there", "City Hall Station (Line 1/2) Exit 4, or Gwanghwamun (Line 5) Exit 5. Stairs down to the path are at every bridge."),
            ("Best time", "Late afternoon for golden light; after dark for the lanterns."),
            ("Length", "6 km total. The first 1.5 km west of Dongdaemun is the most scenic."),
            ("Free", "Always. No ticket booth."),
            ("Bring", "Soft shoes — stones are slippery — and a thermos in winter."),
        ],
    },
    {
        "slug": "subway-five-steps",
        "type": "short",
        "title": "Five Steps to Survive the Seoul Subway",
        "kicker": "Field Note · Transit",
        "deck": "A T-money card, two taps, and the calmest underground in Asia. Do not let Google Maps route you here.",
        "img": "https://images.unsplash.com/photo-1679212843220-b36bf01ff859?auto=format&fit=crop&w=2200&q=80",
        "location": "Seoul Metropolitan Subway",
        "body": (
            "<p>The Seoul subway is, unhelpfully for first-time visitors, almost too good. Trains run every two to four minutes; stations are clean enough to eat off; signs are in English; emergency staff actually answer phones. The only thing standing between you and the entire city is a small plastic card.</p>"
            "<h2>The five steps</h2>"
            "<p><strong>1. Buy a T-money card.</strong> Any convenience store sells one for ₩2,500. Say <em>&ldquo;T-money juseyo&rdquo;</em>.<br>"
            "<strong>2. Top up.</strong> ₩10,000 is plenty for a busy day. The cashier will load the card for you. No app, no account, no email.<br>"
            "<strong>3. Tap in.</strong> Touch the card to the gate sensor. Walk through.<br>"
            "<strong>4. Tap out.</strong> Yes, again, on exit. Skipping this step charges you the maximum fare.<br>"
            "<strong>5. Use Naver Map or Kakao Map.</strong> Google Maps does not route Korean transit well. The two Korean apps are free, in English, and accurate to the second.</p>"
            "<h2>One thing nobody tells you</h2>"
            "<p>If you accidentally exit the wrong station, you can re-enter through the same gate within 15 minutes for free. Useful when the station is large and you walked the wrong way.</p>"
            "<div class=\"pull\"><blockquote>&ldquo;The first time you tap out and the gate hums green, you become a Seoul resident for thirty seconds.&rdquo;</blockquote><cite>&mdash; Field note</cite></div>"
        ),
        "ify_h3": "Seoul Subway · Practical Notes",
        "ify": [
            ("Card", "T-money. ₩2,500 deposit. Recharge at any station kiosk."),
            ("Apps", "Naver Map or Kakao Map. Both have English."),
            ("Hours", "First train ~05:30, last ~midnight. Less frequent on weekends."),
            ("Refund", "Any subway info desk will refund your remaining balance plus ₩500 of deposit."),
            ("Doryung's tip", "On long rides, sit in the priority seats only if no one over 60 is standing. Always."),
        ],
    },
    {
        "slug": "gwangjang-bindaetteok",
        "type": "short",
        "title": "The Gwangjang Bindaetteok Gospel",
        "kicker": "Field Note · Eat",
        "deck": "A market, a low table, an aunt who never lets you leave hungry, and ten thousand won between you and a story.",
        "img": "https://images.unsplash.com/photo-1583224944844-5b268c057b72?auto=format&fit=crop&w=2200&q=80",
        "location": "Gwangjang Market · Jongno-gu, Seoul",
        "body": (
            "<p>Gwangjang Market is one of the oldest food markets in Korea, and it has decided, after a hundred years of practice, that it is mostly here for one thing: <em>bindaetteok</em>, a fat green-mung-bean pancake fried in pig fat until the edges are crisp and the centre still gives. You eat it standing up, or seated on a plastic stool at one of the long communal counters that line the central aisles.</p>"
            "<h2>How it goes</h2>"
            "<p>You point. The aunt nods. A pancake, fresh from the pan, is dropped in front of you with a small dish of soy-vinegar dipping sauce and a paper cup of yellow makgeolli. Six thousand won. You sit. You eat. You watch the aunt pour batter onto the next pan with one hand while making change with the other. By the time you finish, you understand why this market has lasted a century.</p>"
            "<h2>Order this too</h2>"
            "<p>If you have room: <em>mayak gimbap</em> (the &ldquo;narcotic&rdquo; mini gimbap, dipped in mustard soy), <em>jeon</em> (any savoury pancake; pick by smell), and a small bowl of <em>kalguksu</em> (knife-cut noodles in anchovy broth). All under ₩7,000 each. None of them will let you down.</p>"
            "<div class=\"pull\"><blockquote>&ldquo;Bindaetteok is what a hundred years of frying tastes like. Pay the six thousand won.&rdquo;</blockquote><cite>&mdash; Field note, lunch</cite></div>"
            "<p>Doryung says: &ldquo;The aunts at this market knew my grandfather, my father, and me. None of them recognise me now, which is the kindest thing about a market.&rdquo;</p>"
        ),
        "ify_h3": "Gwangjang Market · Practical Notes",
        "ify": [
            ("Getting there", "Jongno 5-ga Station (Line 1) Exit 8. One minute on foot."),
            ("Hours", "Most stalls 09:00 – 22:00. Bindaetteok aunts work until they run out of batter."),
            ("Cash", "Many stalls now take card; bring ₩30,000 cash anyway."),
            ("Eat first", "Bindaetteok at the centre aisle. Walk the rest after."),
            ("Avoid", "Saturday lunch. The market is excellent at every other hour."),
        ],
    },
    {
        "slug": "banana-milk-hack",
        "type": "short",
        "title": "The Banana-Milk Hack: Korea's Viral Convenience-Store Coffee",
        "kicker": "Field Note · Trend",
        "deck": "A noisy yellow bottle, an ice cup, and one shot of espresso. Three thousand won and you understand the country.",
        "img": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=2200&q=80",
        "location": "Any CU / GS25 / 7-Eleven, Korea",
        "body": (
            "<p>The drink, as it has spread across TikTok and Instagram, has many names — <em>banana latte</em>, <em>Korean banana milk coffee</em>, <em>Binggrae hack</em>. In Korea it has no name at all, because everyone has been doing it since they were small. It is simply what you make with the things in front of you when you stop at a convenience store and want coffee that tastes like a memory.</p>"
            "<h2>The recipe</h2>"
            "<p>Three things, all from the same convenience store fridge:</p>"
            "<p><strong>1.</strong> One bottle of Binggrae banana-flavoured milk (the noisy yellow conical bottle, on the market since 1974).<br>"
            "<strong>2.</strong> One ice cup (₩1,000, on the chilled shelf next to the milk).<br>"
            "<strong>3.</strong> One small canned iced espresso, or a shot from the in-store machine.</p>"
            "<p>Pour the banana milk into the ice cup. Pour the espresso on top. Stir twice. Drink. Total cost: about ₩3,000. Total preparation time: under a minute. Total joy: surprisingly large.</p>"
            "<h2>Why it works</h2>"
            "<p>Banana milk in Korea is not banana-flavoured-syrup-on-milk; it is whole milk with a small amount of real banana juice and just enough sugar to make a child suspicious. Combined with the bitterness of espresso, it tastes like a banana cream pie crossed with an Italian café — which is, by any measure, an upgrade on either of them.</p>"
            "<div class=\"pull\"><blockquote>&ldquo;The yellow bottle, the cold cup, and a shot. Nothing else. Korea in a sip.&rdquo;</blockquote><cite>&mdash; Field note, 2 p.m.</cite></div>"
            "<p>Doryung says: &ldquo;In a hundred and ninety years I have drunk a great deal of tea. I admit, on the record, that this drink is also good. Bring me one of the yellow bottles.&rdquo;</p>"
        ),
        "ify_h3": "Banana-Milk Coffee · Practical Notes",
        "ify": [
            ("Where", "Any CU, GS25, 7-Eleven, eMart24, or Ministop."),
            ("Cost", "₩3,000 ± a few hundred won."),
            ("Best time", "After lunch, before a museum, on a hot day."),
            ("Variation", "Some Koreans prefer one shot of T.O.P canned coffee instead of espresso."),
            ("Doryung's tip", "Drink it standing outside the store with the bag still in your hand. That is the correct mood."),
        ],
    },
    {
        "slug": "hanbok-free-palace",
        "type": "short",
        "title": "Why Hanbok Is Free at the Palace",
        "kicker": "Field Note · Tradition",
        "deck": "Korea offers entry to four royal palaces at no cost — if you arrive in hanbok. Almost no one outside Korea knows.",
        "img": "https://images.unsplash.com/photo-1674154083287-c36a5b34050a?auto=format&fit=crop&w=2200&q=80",
        "location": "Four royal palaces · Central Seoul",
        "body": (
            "<p>It is one of the most generous tourism gestures any city in Asia offers, and it is almost entirely unknown outside Korea: visitors wearing <em>hanbok</em> — the traditional Korean dress — are admitted to all four major Joseon-dynasty palaces in Seoul free of charge. No queue, no ticket, no questions. You walk up in hanbok, the guard nods you through.</p>"
            "<h2>How to actually do it</h2>"
            "<p>Cluster around Anguk Station and you will find dozens of <em>hanbok</em> rental shops. Two hours costs roughly ₩15,000 to ₩30,000, depending on the shop's vintage and how elaborate you'd like the dress to be. They do your hair too, often included in the price. You are then yours for the next two hours, free to walk into Gyeongbokgung, Changdeokgung, Changgyeonggung, and Deoksugung at no extra cost.</p>"
            "<h2>What's worth knowing</h2>"
            "<p>The palaces all close on different days — typically Tuesday for Gyeongbokgung, Monday for Changdeokgung. Pick your day carefully. The hanbok shops are open every day, but the cost-saving trick only works if you can actually enter a palace.</p>"
            "<div class=\"pull\"><blockquote>&ldquo;A piece of cloth older than the building lets you in for nothing. Korea has a sense of humour about its own past.&rdquo;</blockquote><cite>&mdash; Field note</cite></div>"
        ),
        "ify_h3": "Hanbok at the Palace · Practical Notes",
        "ify": [
            ("Where to rent", "Hanbok shops near Anguk Station (Line 3, Exit 2)."),
            ("Cost", "₩15,000–₩30,000 for 2 hours; hair styling usually included."),
            ("Free entry to", "Gyeongbokgung, Changdeokgung, Changgyeonggung, Deoksugung."),
            ("Closed days", "Gyeongbokgung: Tue. Changdeokgung: Mon. Plan accordingly."),
            ("Doryung's tip", "Pick a hanbok with deep pockets — they don't always have them, and you'll want them."),
        ],
    },
    {
        "slug": "han-river-after-dark",
        "type": "short",
        "title": "Han River After Dark",
        "kicker": "Field Note · Outdoors",
        "deck": "A mat, a chimaek, a slow bridge that changes color, and a city that, just for an evening, agrees to stop hurrying.",
        "img": "https://images.unsplash.com/photo-1611410873756-63d72ad1b732?auto=format&fit=crop&w=2200&q=80",
        "location": "Han River parks · Seoul",
        "body": (
            "<p>Seoul has eleven public riverside parks along the Han, all of them free, all of them unfussy, and all of them best after sunset. Yeouido is the most famous; Banpo is the showiest (the Rainbow Fountain on the bridge runs at 8 and 9 p.m. on summer nights); Ttukseom is where the locals actually go.</p>"
            "<h2>How a Han River evening goes</h2>"
            "<p>Step one: convenience store. Buy a small mat (₩3,000), a beer, and either a small bag of fried chicken or — far more correctly — order one to be delivered to your spot in the park. Yes, the chicken comes to the river. Yes, this is normal. Yes, you can pay by card.</p>"
            "<p>Step two: spread the mat. Anywhere along the path, on the grass, near a bridge. Step three: do nothing for the next two hours. The river will do the work for you.</p>"
            "<div class=\"pull\"><blockquote>&ldquo;Bring chimaek if you must. The bridges light at dusk and the geese have opinions.&rdquo;</blockquote><cite>&mdash; Doryung</cite></div>"
            "<h2>One thing you'd miss</h2>"
            "<p>At Banpo, walk down to the riverbank under the bridge a few minutes before the fountain show begins. The view from underneath is better than the view from the road. Locals know.</p>"
        ),
        "ify_h3": "Han River After Dark · Practical Notes",
        "ify": [
            ("Best parks", "Yeouido (busy), Banpo (fountain), Ttukseom (local)."),
            ("Getting there", "Yeouido: Line 5 Yeouinaru Exit 3. Banpo: Line 3/7/9 Express Bus Terminal."),
            ("Chicken delivery", "Order via the Yogiyo or Baemin app. They will ask which mat you're on."),
            ("Fountain", "Banpo: 8 and 9 p.m. on summer evenings. Free."),
            ("Doryung's tip", "Pack a small mat in your suitcase. You will use it more than you expect."),
        ],
    },
    {
        "slug": "buamdong-painters",
        "type": "short",
        "title": "Buam-dong: Where the Painters Hid",
        "kicker": "Field Note · Walk",
        "deck": "A steep, quiet hill behind the palace where painters and poets disappeared when the city below grew too loud.",
        "img": "https://images.unsplash.com/photo-1773149660396-21c22230cd6c?auto=format&fit=crop&w=2200&q=80",
        "location": "Buam-dong · Jongno-gu, Seoul",
        "body": (
            "<p>Buam-dong is a small residential village hidden behind Bugaksan, north of Gyeongbokgung. For most of the twentieth century it was where painters, sculptors, and poets moved when the city grew too noisy. The atmosphere they made survives. The streets are narrow, mostly one car wide, the houses are low, and the cafés are run by people who would clearly rather be reading than serving you a cappuccino.</p>"
            "<h2>What it's good for</h2>"
            "<p>Walking. Drinking coffee very slowly in a window. Looking at small galleries that open and close on a schedule even the owners can't fully predict. There is no list of attractions; the neighbourhood itself is the attraction.</p>"
            "<h2>How to walk it</h2>"
            "<p>Take Bus 7212 or 1020 from Gwanghwamun to the Buam-dong stop. Get off, look uphill, and start walking. Within ten minutes you will be near Baeksasil Valley — a small wooded ravine with a stream, a stone wall, and almost always one painter sketching in it. After lunch, descend back to the palace area on foot through the wall path; it takes about forty minutes and the view of Seoul as you come down is worth the entire morning.</p>"
            "<div class=\"pull\"><blockquote>&ldquo;The painters and poets fled here when the city grew loud. The steep lanes are still patient.&rdquo;</blockquote><cite>&mdash; Doryung</cite></div>"
        ),
        "ify_h3": "Buam-dong · Practical Notes",
        "ify": [
            ("Getting there", "Bus 7212 or 1020 from Gwanghwamun (15 min) to Buam-dong stop."),
            ("Best time", "Weekday mid-morning. Cafés open ~11; the village empties by 6 p.m."),
            ("Pair it with", "Baeksasil Valley walk · Seoul City Wall trail back to Gyeongbokgung."),
            ("Bring", "Walking shoes; the streets are steep."),
            ("Doryung's tip", "Order at the smallest café. They make the best coffee."),
        ],
    },
    {
        "slug": "ten-words",
        "type": "short",
        "title": "The Ten Words You Actually Need",
        "kicker": "Field Note · Language",
        "deck": "A market vendor, a cab driver, and a pharmacist all want the same ten words from you. Here they are.",
        "img": "https://images.unsplash.com/photo-1620041786470-616bc1224fb6?auto=format&fit=crop&w=2200&q=80",
        "location": "Korean, anywhere",
        "body": (
            "<p>You do not need to learn Korean to enjoy Korea. You do not even need to learn ten words. But ten words will get you smiles for free, and one or two of them will save your life on a wet Tuesday in Insadong when you cannot find a pharmacy.</p>"
            "<h2>The ten</h2>"
            "<p><strong>1. 안녕하세요</strong> <em>(annyeonghaseyo)</em> — Hello. The most useful word in Korean. Use it on every doorstep.<br>"
            "<strong>2. 감사합니다</strong> <em>(gamsahamnida)</em> — Thank you. Use it more than you think you should.<br>"
            "<strong>3. 죄송합니다</strong> <em>(joesonghamnida)</em> — Sorry / excuse me. Useful in crowded markets.<br>"
            "<strong>4. 네 / 아니요</strong> <em>(ne / aniyo)</em> — Yes / no.<br>"
            "<strong>5. 얼마예요?</strong> <em>(eolmayeyo?)</em> — How much is it?<br>"
            "<strong>6. 이거 주세요</strong> <em>(igeo juseyo)</em> — This one, please. Point and say this.<br>"
            "<strong>7. 화장실 어디예요?</strong> <em>(hwajangsil odiyeyo?)</em> — Where is the bathroom?<br>"
            "<strong>8. 도와주세요</strong> <em>(dowajuseyo)</em> — Help me.<br>"
            "<strong>9. 맛있어요</strong> <em>(masisseoyo)</em> — Delicious. Say this when food arrives.<br>"
            "<strong>10. 괜찮아요</strong> <em>(gwaenchanayo)</em> — It's okay / I'm fine. The most Korean word in this list.</p>"
            "<div class=\"pull\"><blockquote>&ldquo;Ten words and a smile go a long way in a country that has heard worse.&rdquo;</blockquote><cite>&mdash; Doryung</cite></div>"
            "<h2>One bonus word</h2>"
            "<p><strong>커피 한 잔 주세요</strong> <em>(keopi han jan juseyo)</em> — One cup of coffee, please. Useful approximately four times a day.</p>"
        ),
        "ify_h3": "The Ten Words · Practical Notes",
        "ify": [
            ("Where to practice", "Convenience stores, market stalls, taxi rides — low stakes, high warmth."),
            ("Pronunciation", "Korean is mostly pronounced exactly as written; the romanization in this list works."),
            ("If you forget", "Bow slightly and smile. It covers most gaps."),
            ("Doryung's tip", "Use 안녕하세요 to enter a shop. Use 감사합니다 to leave one. Everything in between is bonus."),
        ],
    },
]


def main():
    for col in COLUMNS:
        body = col["body"]
        ify_dl = dl(col["ify"])
        html = TEMPLATE.format(
            title=col["title"],
            kicker=col["kicker"],
            deck=col["deck"],
            img=col["img"],
            location=col["location"],
            body=body,
            ify_h3=col["ify_h3"],
            ify_dl=ify_dl,
        )
        out = OUT_DIR / f"{col['slug']}.html"
        out.write_text(html, encoding="utf-8")
        print(out, len(html))


if __name__ == "__main__":
    main()
