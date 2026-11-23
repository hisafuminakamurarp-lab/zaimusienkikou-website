"""財務支援機構サイトの静的HTMLを生成する（共通ヘッダー/フッターを各ページへ展開）。
出力先は第1引数のディレクトリ。"""
import sys, os

OUT = sys.argv[1]
SITE = "https://zaimusienkikou-website.vercel.app"
NAME = "一般社団法人 中小企業財務支援機構"
TEL = "03-6766-8441"
# お問い合わせの受付先（Apps Script ウェブアプリのURL）。空ならFormspreeのみに送る
GAS_URL = ""
MOBILE = "070-8521-9870"
ADDR = "〒161-0034 東京都新宿区上落合2丁目21番10号"

MARK = '<svg class="logo-mark" viewBox="0 0 178 187" aria-hidden="true"><path class="g" fill="#b69355" d="M16 0h69l-10 17H26zM93 0h69l-10 17h-49zM16 147h146v14H16z"/><path fill="currentColor" d="M30 17h41v130H30zM107 17h41v130h-41zM0 169h178v18H0z"/></svg>'

NAV_ITEMS = [("services.html", "提供サービス"), ("services.html#experts", "専門家紹介"), ("column.html", "コラム"), ("about.html", "法人概要")]


def head(title, desc, path):
    full = f"{title}｜{NAME}" if title else NAME
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{full}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{path}">
<meta property="og:site_name" content="{NAME}">
<meta name="format-detection" content="telephone=no">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="canonical" href="{SITE}/{path}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Noto+Serif+JP:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
"""


ACT = ' class="active"'


def nav(active):
    links = "\n".join(
        f'    <li><a href="{h}"{ACT if h == active else ""}>{t}</a></li>' for h, t in NAV_ITEMS)
    mlinks = "\n".join(f'  <a href="{h}">{t}</a>' for h, t in NAV_ITEMS)
    return f"""<header class="nav">
  <a href="index.html" class="nav-logo" aria-label="{NAME} トップへ">
    {MARK}
    <span class="logo-text"><small>一般社団法人</small><b>中小企業財務支援機構</b></span>
  </a>
  <ul class="nav-links">
{links}
    <li><a href="contact.html" class="nav-cta">お問い合わせ</a></li>
  </ul>
  <button class="hamburger" id="ham" aria-label="メニューを開く" aria-expanded="false" aria-controls="mobileMenu"><span></span><span></span><span></span></button>
</header>
<nav class="mobile-menu" id="mobileMenu" aria-label="モバイルメニュー">
  <a href="index.html">トップ</a>
{mlinks}
  <a href="contact.html" class="nav-cta">お問い合わせ</a>
</nav>
"""


FOOT = f"""<footer class="footer">
  <div class="footer-inner">
    <div class="footer-brand">
      <div class="footer-logo">{MARK}<span class="logo-text"><small>一般社団法人</small><b>中小企業財務支援機構</b></span></div>
      <p>{ADDR}<br>TEL <a href="tel:{TEL}">{TEL}</a>（平日 10:00〜18:00）</p>
    </div>
    <ul class="footer-links">
      <li><a href="index.html">トップ</a></li>
      <li><a href="services.html">提供サービス</a></li>
      <li><a href="services.html#experts">専門家紹介窓口</a></li>
      <li><a href="column.html">コラム</a></li>
      <li><a href="about.html">法人概要</a></li>
      <li><a href="contact.html">お問い合わせ</a></li>
      <li><a href="privacy.html">プライバシーポリシー</a></li>
      <li><a href="policy.html">サイトのご利用について</a></li>
    </ul>
  </div>
  <p class="copyright">© <span id="year">2026</span> {NAME} All Rights Reserved.</p>
</footer>
<script src="assets/site.js"></script>
"""


def cta():
    return f"""<section class="cta">
  <div class="container">
    <div class="section-label">Contact</div>
    <h2>まずは、お気軽にご相談ください</h2>
    <p>「何から相談すればいいかわからない」という段階でも大丈夫です。<br>お問い合わせ・ご相談は無料です。</p>
    <a href="contact.html" class="cta-btn">お問い合わせはこちら →</a>
    <p class="cta-tel">お電話でのご相談<a href="tel:{TEL}">{TEL}</a>平日 10:00〜18:00</p>
  </div>
</section>
"""


def page_hero(label, title, lead, crumb):
    return f"""<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="index.html">トップ</a>　／　{crumb}</p>
    <div class="section-label">{label}</div>
    <h1>{title}</h1>
    <div class="gold-divider"></div>
    <p>{lead}</p>
  </div>
</section>
"""


def write(name, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(body)


EXPERTS = [
    ("税理士", "税務申告・決算・税務調査への対応など、税務全般の専門家。"),
    ("公認会計士", "財務諸表の分析・資金調達・事業計画など、財務の専門家。"),
    ("社会保険労務士", "社会保険・労働保険の手続き、就業規則や労務管理の専門家。"),
    ("助成金・補助金", "活用できる制度の洗い出しから申請準備までを支援する専門家。"),
    ("節税対策", "事業の状況に合わせた節税の考え方・手法を提案する専門家。"),
]
EXPERT_HTML = "\n".join(f'    <div class="expert"><h3>{n}</h3><p>{d}</p></div>' for n, d in EXPERTS)

STEPS = f"""  <div class="steps reveal">
    <div class="step"><div class="step-num">01</div><h3>ご相談・お問い合わせ</h3><p>フォームまたはお電話で、いまのお困りごとをお聞かせください。</p></div>
    <div class="step"><div class="step-num">02</div><h3>状況の整理</h3><p>課題と目的を整理し、どの分野の専門家が必要かを一緒に確認します。</p></div>
    <div class="step"><div class="step-num">03</div><h3>専門家のご紹介</h3><p>提携先の中から目的に合った専門家をご紹介し、相談を始められるようにします。</p></div>
  </div>"""

EXPERT_NOTE = '<p class="note">※税務代理・税務書類の作成・個別の税務相談、社会保険・労働保険の手続き代行などの専門業務は、ご紹介する各専門家が行います。当機構はこれらの業務を行いません。</p>'

# ---------------- index ----------------
FAQ = [
    ("相談に費用はかかりますか？", "お問い合わせ・ご相談は無料です。専門家へ正式にご依頼いただく場合の費用は、ご依頼前に各専門家からご案内します。"),
    ("どのような相談ができますか？", "税金・財務・コストの見直し、法人化のタイミングや形態、制度の活用など、事業のお金と仕組みにかかわるご相談を幅広くお受けしています。内容に応じて、適した専門家もご紹介します。"),
    ("個人事業主でも相談できますか？", "はい。個人事業主・フリーランスの方から小規模法人の経営者の方まで、規模を問わずご相談いただけます。"),
    ("まだ相談内容がまとまっていなくても大丈夫ですか？", "大丈夫です。「何から手をつければいいかわからない」という段階から、状況の整理をお手伝いします。"),
]
FAQ_HTML = "\n".join(f"""    <div class="faq-item">
      <button class="faq-q" aria-expanded="false"><span><span class="q">Q</span>{q}</span><span class="faq-icon">+</span></button>
      <div class="faq-a"><p>{a}</p></div>
    </div>""" for q, a in FAQ)

index = head("", "中小企業・個人事業主の経営の土台づくりを支援する一般社団法人。税務・財務・制度の情報提供、財務・コスト相談、法人化支援、税理士・公認会計士・社労士などの専門家紹介を行っています。", "") + nav("") + f"""<main>
<section class="hero">
  <div class="hero-inner">
    <div class="hero-left">
      <div class="badge">{NAME}</div>
      <h1>経営の不安を、<br><em>仕組み</em>でなくす。</h1>
      <p class="hero-catch">中小企業の経営インフラをつくる</p>
      <p class="hero-sub">税務・社会保険・法務・財務。<br>複雑で負担の大きいバックオフィス業務を、一人で抱えていませんか？<br>事業に集中できる環境を仕組みで整え、安心して挑戦を続けられる状態を支援します。</p>
      <div class="btn-row">
        <a href="contact.html" class="btn btn-primary">無料で相談する →</a>
        <a href="services.html" class="btn btn-secondary">サービスを見る</a>
      </div>
    </div>
    <div class="hero-card">
      <div class="card-label">SUPPORT AREAS</div>
      <div class="card-title">3つの支援領域</div>
      <a class="area-row" href="services.html#information"><span class="area-num">01</span><div><h3>情報提供</h3><p>税金・法律・制度・経営知識を体系的にお届け</p></div></a>
      <a class="area-row" href="services.html#finance"><span class="area-num">02</span><div><h3>財務・コスト相談</h3><p>税金対策・財務の可視化・固定費の見直し</p></div></a>
      <a class="area-row" href="services.html#growth"><span class="area-num">03</span><div><h3>法人化支援・専門家紹介</h3><p>法人化の判断から、目的に合った専門家へ</p></div></a>
      <a href="services.html" class="btn btn-gold">サービス内容を詳しく見る →</a>
    </div>
  </div>
</section>

<section class="navy">
  <div class="container">
    <div class="section-label">Problem</div>
    <h2 class="section-title">こんなお悩みはありませんか？</h2>
    <div class="gold-divider"></div>
    <p class="section-sub">中小企業・個人事業主の多くが、本業以外の負担を一人で抱えています。</p>
    <div class="problem-grid reveal">
      <div class="problem-card"><div class="num">01</div><h3>税金・固定費の負担が重い</h3><p>売上が伸びても手元に残らない。どこを見直せばいいのかがわからない。</p></div>
      <div class="problem-card"><div class="num">02</div><h3>情報が多すぎて判断できない</h3><p>制度や法律の情報が分散していて、自分に関係あるものが見つけにくい。</p></div>
      <div class="problem-card"><div class="num">03</div><h3>信頼できる相談先がない</h3><p>誰に何を相談すればいいのか、専門家をどう選べばいいのかがわからない。</p></div>
      <div class="problem-card"><div class="num">04</div><h3>経営の判断を一人で抱えている</h3><p>法人化や資金繰りなど、大事な判断を相談できる相手がいない。</p></div>
    </div>
    <div class="answer reveal">
      <p>中小企業財務支援機構は、<em>情報・財務・専門家ネットワーク</em>で<br>その負担を仕組みで軽くします。</p>
      <a href="services.html" class="btn btn-gold">支援内容を見る →</a>
    </div>
  </div>
</section>

<section class="bg-off">
  <div class="container">
    <div class="section-label">Services</div>
    <h2 class="section-title">3つの支援領域</h2>
    <div class="gold-divider"></div>
    <p class="section-sub">情報・財務・事業構造のすべてにわたり、中小企業の経営の土台を整えます。</p>
    <div class="card-grid cols-3 reveal">
      <a class="card" href="services.html#information"><div class="card-num">01 ─ INFORMATION</div><h3>中小企業に必要な知識を、まとめて発信</h3><p>税金・法律・社会制度・経営知識など、事業の継続に必要な情報を体系的に整理してお届けします。</p><span class="more">詳しく見る →</span></a>
      <a class="card" href="services.html#finance"><div class="card-num">02 ─ FINANCE</div><h3>財務・コストの負担を軽くする</h3><p>税金対策・財務状況の可視化・固定費の見直しなど、お金まわりの課題に具体的な相談窓口を提供します。</p><span class="more">詳しく見る →</span></a>
      <a class="card" href="services.html#growth"><div class="card-num">03 ─ GROWTH</div><h3>事業成長フェーズの構造支援</h3><p>法人化のタイミングや形態の判断から、税理士・公認会計士・社労士などの専門家紹介までつなぎます。</p><span class="more">詳しく見る →</span></a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-label">For Whom</div>
    <h2 class="section-title">こんな方のための団体です</h2>
    <div class="gold-divider"></div>
    <p class="section-sub">個人事業主から、従業員を抱える中小企業まで。規模や業種を問わず、経営の土台づくりを支援します。</p>
    <div class="card-grid cols-2 reveal">
      <div class="card hover"><div class="card-num">CASE 01</div><h3>個人事業主・フリーランス</h3><p>税金や経費の負担、将来への不安を抱えながら、ほぼ一人で事業を続けている方。</p></div>
      <div class="card hover"><div class="card-num">CASE 02</div><h3>中小企業の経営者・役員</h3><p>資金繰り・税負担・人事労務など、経営課題が多岐にわたり、判断の相談相手がほしい会社。</p></div>
      <div class="card hover"><div class="card-num">CASE 03</div><h3>管理部門の体制を整えたい会社</h3><p>専任の総務・経理がいない、または少人数で回していて、制度改正や専門的な判断に外部の知見がほしい会社。</p></div>
      <div class="card hover"><div class="card-num">CASE 04</div><h3>法人化・事業拡大を検討している方</h3><p>法人化のタイミング、拠点や事業の拡大など、次のステージに向けて判断材料と専門家の力がほしい方。</p></div>
    </div>
  </div>
</section>

<section class="bg-pale" id="experts">
  <div class="container">
    <div class="section-label">Experts</div>
    <h2 class="section-title">専門家紹介窓口</h2>
    <div class="gold-divider"></div>
    <p class="section-sub">「誰に相談すればいいかわからない」をなくすために。税務・財務・労務・制度活用の専門家を、当機構が窓口となってご紹介します。</p>
    <div class="expert-grid reveal">
{EXPERT_HTML}
    </div>
{STEPS}
    <div class="btn-row" style="margin-top:36px"><a href="services.html#experts" class="btn btn-primary">紹介窓口について詳しく →</a></div>
  </div>
</section>

<section>
  <div class="container">
    <div class="center">
      <div class="section-label">FAQ</div>
      <h2 class="section-title">よくあるご質問</h2>
      <div class="gold-divider"></div>
    </div>
    <div class="faq-list">
{FAQ_HTML}
    </div>
  </div>
</section>

{cta()}</main>
{FOOT}</body>
</html>
"""
write("index.html", index)

# ---------------- services ----------------
def sv(items):
    return "\n".join(f'        <div class="sv-item"><div><h3>{h}</h3><p>{p}</p></div></div>' for h, p in items)

def tags(ts):
    return "".join(f'<span class="tag">{t}</span>' for t in ts)

services = head("提供サービス", "情報提供・財務とコストの相談・法人化支援と専門家紹介。中小企業財務支援機構の3つの支援領域と専門家紹介窓口のご案内です。", "services.html") + nav("services.html") + page_hero(
    "Services", "3つの支援領域", "情報・財務・事業構造のすべてにわたり、中小企業の経営の土台を整えます。", "提供サービス") + f"""<main>
<section>
  <div class="container">
    <div class="service reveal" id="information">
      <div>
        <div class="service-num">01</div>
        <div class="service-cat">Information</div>
        <h2>中小企業に必要な知識を、<br>まとめて発信</h2>
        <p>税金・法律・社会制度・フリーランス関連情報・経営知識など、事業の継続に必要な情報を体系的に整理してお届けします。情報収集にかかる時間とコストを、本業に集中させてください。</p>
        <p>制度改正やフリーランス保護法など、中小企業に影響する動向をいち早くキャッチアップし、わかりやすく解説します。</p>
        <div class="tags">{tags(["税金","法律","社会制度","フリーランス","経営知識","制度改正"])}</div>
      </div>
      <div class="service-visual">
{sv([("税金・節税の基礎知識","所得税・消費税・法人税の仕組みと対策を解説"),("法律・契約リスクへの備え","フリーランス保護法・下請法・契約書の注意点"),("社会制度の活用ガイド","補助金・助成金・各種給付制度の最新情報"),("経営知識のアップデート","資金繰り・財務管理・事業計画の基礎")])}
      </div>
    </div>

    <div class="service reverse reveal" id="finance">
      <div>
        <div class="service-num">02</div>
        <div class="service-cat">Finance</div>
        <h2>財務・コストの<br>負担を軽くする</h2>
        <p>コスト削減・財務改善・税金対策など、お金まわりの課題に対して具体的な相談窓口を提供します。</p>
        <p>現状の数字を一緒に整理し、どこから手をつければよいかを明確にします。</p>
        <div class="tags">{tags(["コスト削減","財務改善","税金対策"])}</div>
      </div>
      <div class="service-visual">
{sv([("税金対策の個別相談","青色申告・経費処理・小規模企業共済の活用"),("財務状況の可視化支援","キャッシュフロー・損益の把握と改善提案"),("固定費・変動費の見直し","事業コスト全体の構造的な削減サポート")])}
      </div>
    </div>

    <div class="service reveal" id="growth">
      <div>
        <div class="service-num">03</div>
        <div class="service-cat">Growth</div>
        <h2>事業成長フェーズの<br>構造支援</h2>
        <p>法人化の相談・事業構造のアドバイスから、税理士・公認会計士・社労士などの専門家紹介まで。次のステージへ進むときに必要な専門家ネットワークへおつなぎします。</p>
        <p>「いつ法人化すべきか」「どの形態が合っているか」など、個別の状況に合わせて判断の材料をご提供します。</p>
        <div class="tags">{tags(["法人化","事業構造","専門家紹介"])}</div>
      </div>
      <div class="service-visual">
{sv([("法人化タイミングの相談","売上・税負担・事業規模から適した時期を検討"),("法人形態の選択支援","株式会社・合同会社・一般社団法人の比較"),("専門家のご紹介","税理士・公認会計士・社労士・助成金/補助金・節税対策の専門家へ"),("事業構造のアドバイス","個人から法人への移行後の報酬設計・体制づくり")])}
      </div>
    </div>
  </div>
</section>

<section class="bg-pale" id="experts">
  <div class="container">
    <div class="section-label">Experts</div>
    <h2 class="section-title">専門家紹介窓口</h2>
    <div class="gold-divider"></div>
    <p class="section-sub">「誰に相談すればいいかわからない」をなくすために。税務・財務・労務・制度活用の専門家を、当機構が窓口となってご紹介します。ご相談内容を伺ったうえで、目的に合った専門家へおつなぎします。</p>
    <div class="expert-grid reveal">
{EXPERT_HTML}
    </div>
{STEPS}
    {EXPERT_NOTE}
  </div>
</section>

{cta()}</main>
{FOOT}</body>
</html>
"""
write("services.html", services)

# ---------------- about ----------------
about = head("法人概要", "一般社団法人 中小企業財務支援機構の法人概要・所在地・アクセスのご案内です。", "about.html") + nav("about.html") + page_hero(
    "About", "法人概要", "中小企業・個人事業主が安心して事業に集中できるよう、経営の土台づくりを支援しています。", "法人概要") + f"""<main>
<section>
  <div class="container narrow">
    <div class="section-label">Company</div>
    <h2 class="section-title">基本情報</h2>
    <div class="gold-divider"></div>
    <table class="info-table reveal">
      <tr><th>法人名</th><td>{NAME}</td></tr>
      <tr><th>設立</th><td>2024年11月14日</td></tr>
      <tr><th>代表者</th><td>代表理事　中村 尚史</td></tr>
      <tr><th>所在地</th><td>〒161-0034<br>東京都新宿区上落合2丁目21番10号</td></tr>
      <tr><th>電話番号</th><td><a href="tel:{TEL}" style="text-decoration:none">{TEL}</a>（平日 10:00〜18:00）</td></tr>
      <tr><th>事業内容</th><td><ul><li>中小企業・個人事業主向けの情報提供</li><li>財務・コストに関する相談</li><li>法人化に関する相談・支援</li><li>専門家（税理士・公認会計士・社会保険労務士 等）の紹介</li></ul></td></tr>
      <tr><th>取引銀行</th><td>住信SBIネット銀行</td></tr>
    </table>
  </div>
</section>

<section class="bg-off">
  <div class="container narrow">
    <div class="section-label">Access</div>
    <h2 class="section-title">アクセス</h2>
    <div class="gold-divider"></div>
    <p class="section-sub">{ADDR}</p>
    <iframe class="map" title="所在地の地図" src="https://maps.google.com/maps?q=東京都新宿区上落合2丁目21番10号&t=&z=17&ie=UTF8&iwloc=&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    <ul class="access">
      <li>都営大江戸線「<strong>中井駅</strong>」徒歩1分</li>
      <li>西武新宿線「<strong>中井駅</strong>」徒歩3分</li>
      <li>東京メトロ東西線「<strong>落合駅</strong>」4番出口 徒歩6分</li>
    </ul>
  </div>
</section>

{cta()}</main>
{FOOT}</body>
</html>
"""
write("about.html", about)

# ---------------- contact ----------------
contact = head("お問い合わせ", "一般社団法人 中小企業財務支援機構へのお問い合わせ・無料相談はこちらから。2営業日以内にご連絡します。", "contact.html") + nav("") + page_hero(
    "Contact", "お問い合わせ", "ご相談・お問い合わせは、下記フォームよりお気軽にどうぞ。内容を確認のうえ、2営業日以内にご連絡します。", "お問い合わせ") + f"""<main>
<section class="bg-off">
  <div class="container narrow">
    <div class="form-card">
      <div class="section-label">Form</div>
      <h2 class="section-title" style="font-size:24px">お問い合わせ・無料相談</h2>
      <div class="gold-divider"></div>
      <p class="section-sub" style="margin-bottom:32px">サービス内容やご自身の状況に合った相談など、どんなことでもお気軽にご連絡ください。</p>
      <form id="inquiryForm" novalidate>
        <input type="hidden" name="_subject" value="【中小企業財務支援機構】お問い合わせ・無料相談">
        <div class="hp-field" aria-hidden="true"><label>ウェブサイト<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
        <div class="form-row">
          <div class="form-group"><label for="f-name">お名前<span class="req">必須</span></label><input id="f-name" name="お名前" type="text" placeholder="山田 太郎" autocomplete="name" required></div>
          <div class="form-group"><label for="f-kana">フリガナ<span class="opt">任意</span></label><input id="f-kana" name="フリガナ" type="text" placeholder="ヤマダ タロウ"></div>
        </div>
        <div class="form-row">
          <div class="form-group"><label for="f-email">メールアドレス<span class="req">必須</span></label><input id="f-email" name="email" type="email" placeholder="example@mail.com" autocomplete="email" required></div>
          <div class="form-group"><label for="f-tel">電話番号<span class="opt">任意</span></label><input id="f-tel" name="電話番号" type="tel" placeholder="090-0000-0000" autocomplete="tel"></div>
        </div>
        <div class="form-row">
          <div class="form-group"><label for="f-type">事業形態<span class="req">必須</span></label>
            <select id="f-type" name="事業形態" required>
              <option value="">選択してください</option>
              <option>個人事業主・フリーランス</option>
              <option>法人（経営者・役員）</option>
              <option>法人（管理部門のご担当者）</option>
              <option>法人化を検討中</option>
              <option>その他</option>
            </select></div>
          <div class="form-group"><label for="f-kind">お問い合わせ種別<span class="opt">任意</span></label>
            <select id="f-kind" name="お問い合わせ種別">
              <option value="">選択してください</option>
              <option>コスト削減について</option>
              <option>財務・税金相談について</option>
              <option>法人化について</option>
              <option>専門家（士業）の紹介について</option>
              <option>情報提供サービスについて</option>
              <option>その他</option>
            </select></div>
        </div>
        <div class="form-group"><label for="f-body">ご相談内容<span class="req">必須</span></label><textarea id="f-body" name="ご相談内容" placeholder="ご質問・ご相談内容をご自由にお書きください" required></textarea></div>
        <label class="consent"><input type="checkbox" id="f-agree" required><span><a href="privacy.html" target="_blank">プライバシーポリシー</a>に同意のうえ送信します</span></label>
        <button type="submit" class="btn btn-primary">送信する</button>
        <p class="form-error" id="formError" role="alert"></p>
      </form>
    </div>
  </div>
</section>

<section>
  <div class="container narrow center">
    <div class="section-label">Direct Contact</div>
    <h2 class="section-title">お電話でのご相談</h2>
    <div class="gold-divider"></div>
    <div class="card-grid cols-2" style="margin-top:32px;text-align:left">
      <div class="card"><div class="card-num">OFFICE</div><h3><a href="tel:{TEL}" style="text-decoration:none">{TEL}</a></h3><p>法人代表番号</p></div>
      <div class="card"><div class="card-num">DIRECT</div><h3><a href="tel:{MOBILE}" style="text-decoration:none">{MOBILE}</a></h3><p>代表直通</p></div>
    </div>
    <p class="note">受付時間：平日 10:00〜18:00（土日祝・年末年始を除く）</p>
  </div>
</section>
</main>
{FOOT}<script>
(function(){{
  // 送信先: Google Apps Script（スプレッドシート記録＋メール・Slack通知）。失敗時は Formspree に送る
  var GAS_URL='{GAS_URL}';
  var FORMSPREE_URL='https://formspree.io/f/xqeweppw';
  async function sendToGas(data){{
    var params=new URLSearchParams();
    data.forEach(function(v,k){{params.append(k,v);}});
    params.append('page',location.href);
    var res=await fetch(GAS_URL,{{method:'POST',body:params}});
    var json=await res.json();
    if(!json.ok)throw new Error(json.error||'gas');
  }}
  async function sendToFormspree(data){{
    var res=await fetch(FORMSPREE_URL,{{method:'POST',body:data,headers:{{'Accept':'application/json'}}}});
    if(!res.ok)throw new Error('status '+res.status);
  }}
  var form=document.getElementById('inquiryForm');
  var err=document.getElementById('formError');
  function showError(msg){{err.textContent=msg;err.style.display='block';}}
  form.addEventListener('submit',async function(e){{
    e.preventDefault();
    err.style.display='none';
    if(!form.checkValidity()){{
      var bad=form.querySelector(':invalid');
      if(bad&&bad.id==='f-agree'){{showError('プライバシーポリシーへの同意にチェックを入れてください。');}}
      else{{showError('必須項目（お名前・メールアドレス・事業形態・ご相談内容）を正しく入力してください。');}}
      if(bad)bad.focus();
      return;
    }}
    var btn=form.querySelector('button[type="submit"]');
    btn.textContent='送信中...';btn.disabled=true;
    try{{
      var data=new FormData(form);
      if(GAS_URL){{
        try{{await sendToGas(data);}}
        catch(gasErr){{await sendToFormspree(data);}}
      }}else{{
        await sendToFormspree(data);
      }}
      location.href='thanks.html';
    }}catch(_){{
      btn.textContent='送信する';btn.disabled=false;
      showError('送信に失敗しました。お手数ですが、お電話（{TEL}）にてお問い合わせください。');
    }}
  }});
}})();
</script>
</body>
</html>
"""
write("contact.html", contact)

# ---------------- thanks ----------------
thanks = head("送信完了", "お問い合わせを受け付けました。", "thanks.html").replace("<head>", '<head>\n<meta name="robots" content="noindex">') + nav("") + f"""<main>
<section class="thanks">
  <div>
    <div class="thanks-mark">✓</div>
    <div class="section-label">Thank you</div>
    <h1 class="section-title">送信が完了しました</h1>
    <div class="gold-divider" style="margin-left:auto;margin-right:auto"></div>
    <p class="section-sub" style="margin:0 auto 36px">お問い合わせいただき、ありがとうございます。<br>内容を確認のうえ、2営業日以内にご連絡いたします。</p>
    <a href="index.html" class="btn btn-primary">トップページに戻る</a>
  </div>
</section>
</main>
{FOOT}</body>
</html>
"""
write("thanks.html", thanks)

# ---------------- privacy ----------------
# 外部サービスの記載は、Apps Script 受付を使っているか（GAS_URL）で切り替える
FORM_SERVICES = ("お問い合わせフォームの内容は、Google LLC（米国）が提供する Google Apps Script・Google スプレッドシート・Gmail を利用して記録・通知し、担当者への連絡に Slack Technologies, LLC（米国）が提供する Slack を利用しています。これらのサービスが利用できない場合に限り、米国の事業者が提供するフォーム送信サービス「Formspree」を経由して届きます。"
                 if GAS_URL else
                 "お問い合わせフォームの送信には、米国の事業者が提供するフォーム送信サービス「Formspree」を利用しており、入力内容は同社のサーバーを経由して当機構へ届きます。")
privacy = head("プライバシーポリシー", "一般社団法人 中小企業財務支援機構の個人情報の取り扱いについて。", "privacy.html") + nav("") + page_hero(
    "Privacy Policy", "プライバシーポリシー", "当機構における個人情報の取り扱いについてご案内します。", "プライバシーポリシー") + f"""<main>
<section>
  <div class="legal">
    <p>{NAME}（以下「当機構」といいます）は、個人情報の保護に関する法律その他の関係法令を遵守し、お預かりする個人情報を以下のとおり適切に取り扱います。</p>

    <h2>1. 取得する個人情報</h2>
    <p>当機構は、お問い合わせフォーム・お電話・面談等を通じて、次の情報を取得します。</p>
    <ul><li>氏名・フリガナ</li><li>メールアドレス・電話番号</li><li>事業形態・ご相談内容など、ご本人が入力・提供された情報</li></ul>

    <h2>2. 利用目的</h2>
    <p>取得した個人情報は、次の目的の範囲内で利用します。</p>
    <ol><li>お問い合わせ・ご相談への回答およびご連絡</li><li>当機構の事業（情報提供・相談・法人化支援・専門家紹介）の実施</li><li>ご本人の同意を得たうえでの、提携する専門家のご紹介</li><li>当機構の活動に関するご案内</li><li>上記に付随する業務</li></ol>

    <h2>3. 第三者への提供</h2>
    <p>当機構は、次の場合を除き、ご本人の同意なく個人情報を第三者に提供しません。</p>
    <ol><li>専門家をご紹介する際に、ご本人の同意を得て、紹介に必要な範囲の情報を提供する場合</li><li>法令に基づく場合</li><li>人の生命・身体・財産の保護のために必要で、ご本人の同意を得ることが困難な場合</li><li>その他、法令で認められている場合</li></ol>

    <h2>4. 業務の委託と外部サービスの利用</h2>
    <p>当機構は、利用目的の達成に必要な範囲で、個人情報の取り扱いを外部に委託することがあります。その際は委託先を適切に監督します。</p>
    <p>{FORM_SERVICES}米国の個人情報保護制度については、個人情報保護委員会のウェブサイトで公表されている情報をご参照ください。</p>

    <h2>5. 安全管理措置</h2>
    <p>当機構は、個人情報の漏えい・滅失・毀損を防止するため、アクセス権限の管理など必要かつ適切な安全管理措置を講じます。</p>

    <h2>6. 開示等のご請求</h2>
    <p>ご本人から、ご自身の個人情報の利用目的の通知・開示・訂正・追加・削除・利用停止・第三者提供の停止のご請求があった場合は、ご本人であることを確認したうえで、法令に従い遅滞なく対応します。下記の窓口までご連絡ください。</p>

    <h2>7. アクセス情報・外部コンテンツ</h2>
    <p>当サイトでは、表示のために Google Fonts（フォント）および Google マップ（地図）を読み込んでいます。これらの提供元が、閲覧者のIPアドレス等の情報を取得する場合があります。取り扱いは各提供元のプライバシーポリシーに従います。</p>

    <h2>8. 本ポリシーの変更</h2>
    <p>当機構は、法令の改正や事業内容の変更に応じて、本ポリシーを改定することがあります。改定後の内容は、当サイトに掲載した時点から効力を生じます。</p>

    <h2>9. お問い合わせ窓口</h2>
    <div class="box">
      <p>{NAME}　個人情報お問い合わせ窓口<br>{ADDR}<br>TEL：{TEL}（平日 10:00〜18:00）<br>お問い合わせフォーム：<a href="contact.html" class="text-link">こちら</a></p>
    </div>

    <p class="meta">制定日：2026年11月24日<br>{NAME}　代表理事　中村 尚史</p>
  </div>
</section>
</main>
{FOOT}</body>
</html>
"""
write("privacy.html", privacy)

# ---------------- policy ----------------
policy = head("サイトのご利用について", "一般社団法人 中小企業財務支援機構ウェブサイトのご利用条件・免責事項。", "policy.html") + nav("") + page_hero(
    "Site Policy", "サイトのご利用について", "当サイトをご利用いただく際の条件・免責事項です。ご利用の前にご確認ください。", "サイトのご利用について") + f"""<main>
<section>
  <div class="legal">
    <h2>掲載情報について</h2>
    <p>当サイトに掲載している情報は、一般的な情報提供を目的としたものです。税務・法務・労務などに関する個別の判断については、税理士・弁護士・社会保険労務士などの専門家にご相談ください。当機構は、税理士法・弁護士法・社会保険労務士法などで専門家に限られている業務は行いません。</p>
    <p>掲載情報の正確性には十分注意していますが、法令・制度の改正等により内容が最新でない場合があります。</p>

    <h2>免責事項</h2>
    <p>当サイトの情報を利用したことにより生じたいかなる損害についても、当機構は責任を負いかねます。また、当サイトは予告なく内容の変更・公開の中止を行うことがあります。</p>
    <p>当機構がご紹介する専門家との契約は、ご相談者さまと各専門家との間で締結されるものです。専門家の業務の内容・結果については、各専門家が責任を負います。</p>

    <h2>著作権</h2>
    <p>当サイトに掲載している文章・画像・デザイン等の著作権は、当機構または正当な権利者に帰属します。私的使用など法令で認められる場合を除き、無断での転載・複製・改変はご遠慮ください。</p>

    <h2>リンクについて</h2>
    <p>当サイトへのリンクは、原則として自由です。ただし、当サイトの内容を誤認させる形でのリンクや、公序良俗に反するサイトからのリンクはお断りします。当サイトからリンクしている外部サイトの内容について、当機構は責任を負いません。</p>

    <h2>推奨環境</h2>
    <p>Google Chrome・Safari・Microsoft Edge・Firefox の最新版でのご利用を推奨しています。</p>

    <h2>個人情報の取り扱い</h2>
    <p>個人情報の取り扱いについては、<a href="privacy.html" class="text-link">プライバシーポリシー</a>をご確認ください。</p>

    <p class="meta">制定日：2026年11月24日<br>{NAME}</p>
  </div>
</section>
</main>
{FOOT}</body>
</html>
"""
write("policy.html", policy)

# ---------------- column (Coming Soon) ----------------
COLUMN_CATS = [
    ("Tax", "税金・節税の基礎", "所得税・消費税・法人税の仕組み、青色申告や小規模企業共済の活用など。"),
    ("Finance", "財務・資金繰り", "キャッシュフローの見方、固定費の見直し、資金調達の基本など。"),
    ("Support", "補助金・助成金・制度", "中小企業が使える制度の探し方と、制度改正のポイントを解説。"),
    ("Growth", "法人化・法律・契約", "法人化の判断基準、フリーランス保護法、契約書の注意点など。"),
]
CAT_CHIPS = "".join(f'<span class="tag">{c[1]}</span>' for c in COLUMN_CATS)
CAT_CARDS = "\n".join(f'      <div class="col-card"><div class="col-thumb"><span>{en}</span></div><div class="col-body"><div class="card-num">{jp}</div><h3>Coming Soon｜近日公開</h3><p>{d}</p></div></div>' for en, jp, d in COLUMN_CATS)
column = head("コラム", "中小企業・個人事業主の経営に役立つ、税金・財務・制度・法人化の情報を発信するコラムです（近日公開）。", "column.html").replace("<head>", '<head>\n<meta name="robots" content="noindex">') + nav("column.html") + page_hero(
    "Column", "経営に役立つ情報を、<br>わかりやすく発信。", "税金や財務、使える制度、法人化のことまで。中小企業・個人事業主の経営に必要な知識を、専門的な内容もかみ砕いて定期的にお届けします。", "コラム") + f"""<main>
<section>
  <div class="container">
    <div class="soon-badge">Coming Soon｜近日公開</div>
    <div class="section-label">Categories</div>
    <h2 class="section-title">こんなテーマでお届けします</h2>
    <div class="gold-divider"></div>
    <div class="tags" style="margin-bottom:8px">{CAT_CHIPS}</div>
    <div class="col-grid reveal">
{CAT_CARDS}
    </div>
    <p class="note">記事は準備が整いしだい、順次公開します。掲載内容は一般的な情報提供を目的としたもので、個別の税務・法律の判断は専門家にご相談ください。</p>
  </div>
</section>

{cta()}</main>
{FOOT}</body>
</html>
"""
write("column.html", column)

# ---------------- 404 / robots / sitemap ----------------
nf = head("ページが見つかりません", "お探しのページは見つかりませんでした。", "404.html").replace("<head>", '<head>\n<meta name="robots" content="noindex">') + nav("") + f"""<main>
<section class="thanks">
  <div>
    <div class="section-label">404 Not Found</div>
    <h1 class="section-title">ページが見つかりません</h1>
    <div class="gold-divider" style="margin-left:auto;margin-right:auto"></div>
    <p class="section-sub" style="margin:0 auto 36px">お探しのページは移動または削除された可能性があります。</p>
    <a href="index.html" class="btn btn-primary">トップページに戻る</a>
  </div>
</section>
</main>
{FOOT}</body>
</html>
"""
write("404.html", nf)

write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
urls = ["", "services.html", "about.html", "contact.html", "privacy.html", "policy.html"]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
      "".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>2026-11-24</lastmod></url>\n" for u in urls) + "</urlset>\n")
print("built")
