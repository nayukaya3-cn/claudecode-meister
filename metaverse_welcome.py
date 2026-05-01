"""
新入留学生ウェルカムパーティ メタバース インタビュー・ギャラリー
東千田キャンパス 2026/04/28
聞き取り・写真撮影：楠香谷
"""

import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="留学生メタバース・ギャラリー | 東千田",
    page_icon="🍁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────────────────────
# 実際のインタビューデータ（2026/04/28 ウェルカムパーティにて聴取）
# ──────────────────────────────────────────────────────────────
INTERVIEWS = [
    {
        "id": 0,
        "name": "Indonesian Students (3 people)",
        "name_ja": "インドネシア留学生 3名",
        "country": "インドネシア",
        "flag": "\U0001f1ee\U0001f1e9",
        "color": "#FF6B35",
        "glow": "#FF6B3588",
        "department": "広島大学 大学院",
        "photo": None,
        "interviewer_note": "★ 一番上の写真⭕️が楠香谷。インドネシア留学生の間に写っている。",
        "q1": "出身地はどこですか？",
        "a1": "スマトラ島でもジャワ島でもないとのこと。具体的な島名を話してくれたが、その時点でインドネシア地理の知識が不足しており、会話が深まらず終わってしまった。",
        "q2": "インタビュアー（楠香谷）の反省点",
        "a2": "「あらかじめ、留学生の出身地を予想して、地理や歴史（特に近現代史）などの知識をアップデートしておくべきでした」。スマトラ・ジャワ以外の多様な島々の歴史・文化を事前に調べていれば、もっと豊かな対話ができた。",
        "q3": "この体験から学んだこと",
        "a3": "留学生へのインタビューには「事前準備」が不可欠。相手の出身地・文化・歴史を下調べしておくことで、会話が一気に深まる。次回への大切な教訓。",
        "keywords": ["インドネシア", "出身地不明（スマトラ・ジャワ以外）", "事前準備の重要性", "地理知識", "近現代史"],
        "pos": [-4, 0, -3],
    },
    {
        "id": 1,
        "name": "Chinese Student A (Shanghai?)",
        "name_ja": "中国人留学生A（上海出身？）",
        "country": "中国",
        "flag": "\U0001f1e8\U0001f1f3",
        "color": "#FF6B6B",
        "glow": "#FF6B6B88",
        "department": "広島大学 SDS（持続可能性科学）",
        "photo": None,
        "interviewer_note": "授業開始のため急いで走って去って行った。",
        "q1": "日本での生活・アルバイトについて",
        "a1": "「日本語が弱いので、心配でアルバイトができない」とのこと。大学ではファイナンス（金融）を専攻していた。将来は日本企業に就職希望。",
        "q2": "「アントレプレナー」という概念について",
        "a2": "「アントレプレナー（起業家精神）」という言葉・概念がなかなか通じなかった。日本語の壁だけでなく、概念自体が文化的に馴染みが薄い可能性もある。興味深い発見だった。",
        "q3": "最後の様子",
        "a3": "「授業が始まる！」と気づき、急いで走って去って行った。日本の時間厳守の文化をしっかり身につけている様子。",
        "keywords": ["SDS", "ファイナンス専攻", "日本語の壁", "アルバイト不安", "日本企業就職希望", "アントレプレナー概念の壁"],
        "pos": [0, 0, -5],
    },
    {
        "id": 2,
        "name": "Chinese Student B (Guangdong?)",
        "name_ja": "中国人留学生B（広東省出身？）",
        "country": "中国",
        "flag": "\U0001f1e8\U0001f1f3",
        "color": "#4ECDC4",
        "glow": "#4ECDC488",
        "department": "広島大学 文系大学院（組織論）",
        "photo": None,
        "interviewer_note": "授業開始のため急いで走って去って行った。",
        "q1": "なぜ理系出身なのに文系大学院へ？",
        "a1": "高校では理系（化学・生物・物理が得意）だったが、数学が苦手。広島大学の文系大学院で組織論を学んでいる。日本の会社・組織に強い興味があり、日本企業への就職を希望。",
        "q2": "就職志望先と「キヤノン問題」",
        "a2": "「キヤノンに就職したい」と語った。折しもキヤノンが中国生産から撤退・史上最高水準の退職補償が話題になっていた時期（風傳媒日本語版）。この動向が志望に影響しているか、興味深い。",
        "q3": "「研究生」制度について（本人談）",
        "a3": "楠香谷が「経済学では微分を使うから数学が大変では？」と問うたところ、「半年間は研究生として勉強し、その後、本格的に大学院に進学できる」と教えてくれた。直後に走って去って行った。",
        "keywords": ["組織論", "キヤノン就職希望", "理系→文系転向", "研究生制度（6ヶ月）", "数学苦手", "キヤノン中国撤退"],
        "pos": [4, 0, -3],
    },
    {
        "id": 3,
        "name": "Chinese Student C",
        "name_ja": "中国人留学生C",
        "country": "中国",
        "flag": "\U0001f1e8\U0001f1f3",
        "color": "#A8E6CF",
        "glow": "#A8E6CF88",
        "department": "広島大学 文系大学院（行動経済学）",
        "photo": None,
        "interviewer_note": "その日は授業がなくゆっくりしていたため、写真撮影ができた！",
        "q1": "研究テーマを教えてください",
        "a1": "「インフルエンサーによる衝動購買への効果」を研究する行動経済学者。SNSのインフルエンサーが消費者の購買行動に与える心理的・経済的影響を分析している。",
        "q2": "インタビューで起きた「面白い誤解」",
        "a2": "最初、楠香谷は彼自身がインフルエンサーだと思い、フォロワー数を聞いてしまった。すると彼は困った様子に。彼は「インフルエンサー」ではなく、「インフルエンサーを研究する研究者」だったのだ。この誤解から笑いが生まれ、良い雰囲気で話が弾んだ。",
        "q3": "なぜ写真が撮れたのか",
        "a3": "その日は授業がなくゆっくりしていたため、じっくり話して写真も撮影できた。行動経済学×SNSという現代的なテーマで、高校生にも「なぜ人は衝動買いをするのか」という問いとして伝わりやすい。",
        "keywords": ["行動経済学", "インフルエンサー研究", "衝動購買", "SNS消費行動", "授業なし→写真撮影成功", "インフルエンサーとの誤解"],
        "pos": [-4, 0, 3],
    },
    {
        "id": 4,
        "name": "Japanese Law Student A (Hiroshima)",
        "name_ja": "日本人 法学部昼間主2年生A（広島出身）",
        "country": "日本",
        "flag": "\U0001f1ef\U0001f1f5",
        "color": "#DDA0DD",
        "glow": "#DDA0DD88",
        "department": "広島大学 法学部昼間主コース 2年",
        "photo": None,
        "interviewer_note": "東千田キャンパスのみで学ぶ制度について教えてくれた。",
        "q1": "東千田キャンパスだけで学べるって本当？",
        "a1": "「オンライン授業を併用すれば、教養課程であっても東広島キャンパスに通学する必要がなく、東千田キャンパスへの通学だけで大丈夫」とのこと。",
        "q2": "出身地と通学について",
        "a2": "広島出身。東千田キャンパスが市内中心部にあるため、交通アクセスが良く、通学負担が少ない。地元学生として東千田キャンパスの利便性をフルに活用している。",
        "q3": "留学生との共学について",
        "a3": "ウェルカムパーティで多くの留学生と出会い、様々な国の話を聞けた。同じキャンパスに世界中の仲間がいることが大きな刺激になっている。",
        "keywords": ["法学部", "オンライン授業活用", "東千田のみ通学OK", "広島出身", "東広島不要"],
        "pos": [0, 0, 5],
    },
    {
        "id": 5,
        "name": "Japanese Law Student B (Kansai)",
        "name_ja": "日本人 法学部昼間主2年生B（関西出身）",
        "country": "日本",
        "flag": "\U0001f1ef\U0001f1f5",
        "color": "#F7DC6F",
        "glow": "#F7DC6F88",
        "department": "広島大学 法学部昼間主コース 2年",
        "photo": None,
        "interviewer_note": "関西から広島大学法学部に進学した学生。",
        "q1": "関西から広島大学を選んだ理由は？",
        "a1": "法学部昼間主コースに進学。東千田キャンパスが広島市の中心部にあり、都市型のキャンパスライフが送れる点が魅力だった。",
        "q2": "オンライン授業活用で変わったこと",
        "a2": "「教養課程でも東千田キャンパスだけで過ごせる」という制度が、遠方からの通学負担を大幅に軽減。関西出身でも広島に定住しやすい環境が整っている。",
        "q3": "留学生との共学について",
        "a3": "同じ法学部の留学生と授業で一緒になることもある。異なる法文化・価値観を持つ仲間と議論することで、法律の見方が大きく広がった。",
        "keywords": ["法学部", "関西出身", "オンライン活用", "東千田のみ通学OK", "留学生との共学"],
        "pos": [4, 0, 3],
    },
]

# ──────────────────────────────────────────────────────────────
# グローバルCSS
# ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;700;900&family=Orbitron:wght@400;700;900&display=swap');

:root {
    --bg: #050510;
    --surface: #0d0d2b;
    --surface2: #1a1a3e;
    --accent: #7B2FBE;
    --accent2: #FF6B6B;
    --accent3: #4ECDC4;
    --gold: #FFD700;
    --text: #E8EAF0;
    --text-dim: #8892A4;
    --border: #2a2f55;
    --maple: #FF6B35;
}

html, body, [class*="css"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Noto Sans JP', sans-serif !important;
}

.main .block-container { padding-top: 0.5rem !important; max-width: 100% !important; }

.hero-title {
    background: linear-gradient(135deg, #7B2FBE, #FF6B6B, #4ECDC4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.2rem, 3vw, 2rem);
    font-weight: 900;
    letter-spacing: 3px;
    text-align: center;
    margin: 0;
}

.hero-sub {
    color: var(--text-dim);
    text-align: center;
    font-size: 0.85rem;
    margin-top: 4px;
    letter-spacing: 2px;
}

.interview-card {
    background: linear-gradient(135deg, var(--surface) 0%, var(--surface2) 100%);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 16px;
    position: relative;
    overflow: hidden;
}

.interview-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 4px; height: 100%;
    background: var(--card-color, #7B2FBE);
    border-radius: 16px 0 0 16px;
}

.card-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 14px;
}

.card-flag { font-size: 2rem; }

.card-name {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text);
}

.card-meta {
    font-size: 0.75rem;
    color: var(--text-dim);
    margin-top: 2px;
}

.note-box {
    background: rgba(255,107,53,0.12);
    border: 1px solid rgba(255,107,53,0.4);
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 0.75rem;
    color: #FF6B35;
    margin-bottom: 12px;
}

.qa-block { margin-bottom: 12px; }

.q-label {
    font-size: 0.7rem;
    color: var(--gold);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 3px;
}

.q-text { font-size: 0.82rem; color: var(--text-dim); }
.a-text {
    font-size: 0.88rem;
    color: var(--text);
    line-height: 1.7;
    border-left: 2px solid var(--accent3);
    padding-left: 10px;
    margin-top: 4px;
}

.keyword-chip {
    display: inline-block;
    background: rgba(123,47,190,0.25);
    border: 1px solid rgba(123,47,190,0.5);
    border-radius: 20px;
    padding: 2px 10px;
    font-size: 0.72rem;
    color: #B39DDB;
    margin: 2px;
}

.stat-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px;
    text-align: center;
    margin-bottom: 8px;
}

.stat-num {
    font-family: 'Orbitron', monospace;
    font-size: 1.8rem;
    font-weight: 700;
    background: linear-gradient(135deg, #7B2FBE, #4ECDC4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.stat-label { font-size: 0.72rem; color: var(--text-dim); margin-top: 2px; }

.stButton > button {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    border-radius: 8px !important;
    font-family: 'Noto Sans JP', sans-serif !important;
}

.stButton > button:hover {
    background: rgba(123,47,190,0.3) !important;
    border-color: #7B2FBE !important;
}
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────
# セッション状態
# ──────────────────────────────────────────────────────────────
if "selected_id" not in st.session_state:
    st.session_state.selected_id = None
if "view_mode" not in st.session_state:
    st.session_state.view_mode = "metaverse"

# ──────────────────────────────────────────────────────────────
# サイドバー
# ──────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<p class="hero-title" style="font-size:1rem;">🍁 留学生メタバース</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">東千田 2026.04.28</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:0.68rem;color:#FF6B35;text-align:center;">聞き取り：楠香谷</p>', unsafe_allow_html=True)
    st.divider()

    countries = list({s["country"] for s in INTERVIEWS})
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-num">{len(INTERVIEWS)}</div>
            <div class="stat-label">インタビュー数</div>
        </div>""", unsafe_allow_html=True)
    with col_b:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-num">{len(countries)}</div>
            <div class="stat-label">参加国数</div>
        </div>""", unsafe_allow_html=True)

    st.divider()

    st.markdown("**表示モード**")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🌐 メタバース", use_container_width=True):
            st.session_state.view_mode = "metaverse"
            st.rerun()
    with c2:
        if st.button("📋 一覧", use_container_width=True):
            st.session_state.view_mode = "list"
            st.rerun()

    st.divider()

    st.markdown("**インタビュー一覧**")
    for s in INTERVIEWS:
        is_active = st.session_state.selected_id == s["id"]
        bg = "rgba(123,47,190,0.3)" if is_active else "transparent"
        border = "border-left: 3px solid #7B2FBE;" if is_active else ""
        st.markdown(f"""
        <div style="background:{bg};{border} padding:8px 12px; border-radius:8px; margin-bottom:4px;">
            <span style="font-size:1.2rem;">{s['flag']}</span>
            <span style="font-size:0.82rem; margin-left:8px; color:#E8EAF0;">{s['name_ja']}</span><br>
            <span style="font-size:0.68rem; color:#8892A4; padding-left:30px;">{s['department']}</span>
        </div>""", unsafe_allow_html=True)
        if st.button("詳細を見る", key=f"nav_{s['id']}", use_container_width=True):
            st.session_state.selected_id = s["id"]
            st.session_state.view_mode = "list"
            st.rerun()

    st.divider()
    st.markdown("""
    <div style="font-size:0.7rem; color:#8892A4; text-align:center;">
    操作方法<br>
    🖱️ ドラッグ: 回転<br>
    🖱️ ホイール: ズーム<br>
    👆 ノードをクリック: 詳細表示
    </div>""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────
# Three.js メタバース HTML
# ──────────────────────────────────────────────────────────────
def build_metaverse_html(interviews: list, selected_id) -> str:
    data_json = json.dumps(interviews, ensure_ascii=False)
    selected_json = json.dumps(selected_id)

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:#050510; overflow:hidden; font-family:'Noto Sans JP',sans-serif; }}
canvas {{ display:block; }}
#overlay {{
    position:absolute; top:0; left:0; width:100%; height:100%;
    pointer-events:none;
}}
#info-panel {{
    position:absolute; right:16px; top:50%;
    transform:translateY(-50%);
    width:300px;
    background:rgba(13,13,43,0.95);
    border:1px solid #2a2f55;
    border-radius:16px;
    padding:20px;
    pointer-events:auto;
    display:none;
    backdrop-filter:blur(12px);
    max-height:80vh;
    overflow-y:auto;
}}
#info-panel::-webkit-scrollbar {{ width:4px; }}
#info-panel::-webkit-scrollbar-thumb {{ background:#7B2FBE; border-radius:4px; }}

.panel-flag {{ font-size:2.5rem; text-align:center; }}
.panel-name {{ font-size:1.05rem; font-weight:700; color:#E8EAF0; text-align:center; margin-top:6px; }}
.panel-dept {{ font-size:0.7rem; color:#8892A4; text-align:center; margin-bottom:10px; }}
.panel-note {{
    background:rgba(255,107,53,0.12);
    border:1px solid rgba(255,107,53,0.4);
    border-radius:8px; padding:6px 10px;
    font-size:0.7rem; color:#FF6B35;
    margin-bottom:10px;
}}
.panel-divider {{ border:none; border-top:1px solid #2a2f55; margin:10px 0; }}
.panel-q {{ font-size:0.65rem; color:#FFD700; letter-spacing:2px; text-transform:uppercase; margin-bottom:3px; }}
.panel-qt {{ font-size:0.76rem; color:#8892A4; margin-bottom:4px; }}
.panel-a {{
    font-size:0.8rem; color:#E8EAF0; line-height:1.7;
    border-left:2px solid #4ECDC4; padding-left:10px;
    margin-bottom:12px;
}}
.panel-kw-wrap {{ margin-top:8px; }}
.panel-kw {{
    display:inline-block;
    background:rgba(123,47,190,0.25);
    border:1px solid rgba(123,47,190,0.5);
    border-radius:20px; padding:2px 8px;
    font-size:0.65rem; color:#B39DDB; margin:2px;
}}
#close-btn {{
    position:absolute; top:12px; right:12px;
    background:rgba(255,107,107,0.2);
    border:1px solid #FF6B6B;
    color:#FF6B6B; border-radius:50%;
    width:28px; height:28px;
    cursor:pointer; font-size:14px;
    display:flex; align-items:center; justify-content:center;
    pointer-events:auto;
}}
#close-btn:hover {{ background:rgba(255,107,107,0.4); }}

#instructions {{
    position:absolute; bottom:16px; left:50%; transform:translateX(-50%);
    background:rgba(13,13,43,0.8);
    border:1px solid #2a2f55;
    border-radius:30px; padding:8px 20px;
    font-size:0.72rem; color:#8892A4;
    pointer-events:none;
    backdrop-filter:blur(8px);
    white-space:nowrap;
}}

#title-bar {{
    position:absolute; top:16px; left:50%; transform:translateX(-50%);
    text-align:center; pointer-events:none;
}}
.title-main {{
    font-family:'Orbitron',monospace; font-size:1.1rem; font-weight:900;
    background:linear-gradient(135deg,#7B2FBE,#FF6B6B,#4ECDC4);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    letter-spacing:3px;
}}
.title-sub {{ font-size:0.68rem; color:#8892A4; margin-top:2px; letter-spacing:2px; }}
.title-credit {{ font-size:0.6rem; color:#FF6B35; margin-top:2px; }}

#loading {{
    position:absolute; top:50%; left:50%;
    transform:translate(-50%,-50%);
    text-align:center; color:#7B2FBE;
    font-family:'Orbitron',monospace; font-size:1rem; letter-spacing:4px;
}}
.loading-dots::after {{
    content:''; animation: dots 1.5s steps(4,end) infinite;
}}
@keyframes dots {{
    0%,20%  {{ content: ''; }}
    40%     {{ content: '.'; }}
    60%     {{ content: '..'; }}
    80%,100%{{ content: '...'; }}
}}
</style>
</head>
<body>
<div id="loading">
    <div>METAVERSE</div>
    <div style="font-size:0.6rem;margin-top:8px;">LOADING<span class="loading-dots"></span></div>
</div>
<div id="overlay">
    <div id="title-bar">
        <div class="title-main">🍁 WELCOME PARTY METAVERSE</div>
        <div class="title-sub">東千田キャンパス 新入留学生インタビュー 2026.04.28</div>
        <div class="title-credit">聞き取り・撮影：楠香谷</div>
    </div>
    <div id="info-panel">
        <button id="close-btn" onclick="closePanel()">✕</button>
        <div id="panel-content"></div>
    </div>
    <div id="instructions">🖱️ ドラッグ: 回転 &nbsp;｜&nbsp; ホイール: ズーム &nbsp;｜&nbsp; 👆 ノードをクリック: 詳細</div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
<script>
const INTERVIEWS = {data_json};
const INIT_SELECTED = {selected_json};

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x050510);
scene.fog = new THREE.FogExp2(0x050510, 0.035);

const camera = new THREE.PerspectiveCamera(60, window.innerWidth/window.innerHeight, 0.1, 200);
camera.position.set(0, 8, 14);
camera.lookAt(0, 0, 0);

const renderer = new THREE.WebGLRenderer({{ antialias:true, alpha:true }});
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
document.body.appendChild(renderer.domElement);

scene.add(new THREE.AmbientLight(0x1a1a3e, 2));
const pointMain = new THREE.PointLight(0x7B2FBE, 3, 30);
pointMain.position.set(0, 10, 0);
scene.add(pointMain);
const pointR = new THREE.PointLight(0xFF6B35, 2, 20);
pointR.position.set(8, 4, 0); scene.add(pointR);
const pointL = new THREE.PointLight(0x4ECDC4, 2, 20);
pointL.position.set(-8, 4, 0); scene.add(pointL);

const gridHelper = new THREE.GridHelper(30, 30, 0x2a2f55, 0x1a1a3e);
gridHelper.position.y = -1.5; scene.add(gridHelper);

const floor = new THREE.Mesh(
    new THREE.PlaneGeometry(30, 30),
    new THREE.MeshStandardMaterial({{ color:0x080820, metalness:0.8, roughness:0.3 }})
);
floor.rotation.x = -Math.PI/2; floor.position.y = -1.5;
floor.receiveShadow = true; scene.add(floor);

const stage = new THREE.Mesh(
    new THREE.CylinderGeometry(2, 2, 0.2, 32),
    new THREE.MeshStandardMaterial({{ color:0x1a0a2e, metalness:0.9, roughness:0.1, emissive:0x7B2FBE, emissiveIntensity:0.15 }})
);
stage.position.y = -1.4; scene.add(stage);

const ring = new THREE.Mesh(
    new THREE.TorusGeometry(2.2, 0.03, 8, 64),
    new THREE.MeshBasicMaterial({{ color:0x7B2FBE }})
);
ring.rotation.x = Math.PI/2; ring.position.y = -1.3; scene.add(ring);

const particleCount = 600;
const pGeo = new THREE.BufferGeometry();
const pPos = new Float32Array(particleCount * 3);
const pCol = new Float32Array(particleCount * 3);
const pSpd = new Float32Array(particleCount);
const pColorList = [
    new THREE.Color(0xFF6B35), new THREE.Color(0x7B2FBE),
    new THREE.Color(0x4ECDC4), new THREE.Color(0xFFD700), new THREE.Color(0xFF6B6B),
];
for (let i = 0; i < particleCount; i++) {{
    pPos[i*3]   = (Math.random()-0.5)*40;
    pPos[i*3+1] = Math.random()*20 - 2;
    pPos[i*3+2] = (Math.random()-0.5)*40;
    pSpd[i] = 0.005 + Math.random()*0.015;
    const c = pColorList[Math.floor(Math.random()*pColorList.length)];
    pCol[i*3]=c.r; pCol[i*3+1]=c.g; pCol[i*3+2]=c.b;
}}
pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
pGeo.setAttribute('color',    new THREE.BufferAttribute(pCol, 3));
const particles = new THREE.Points(pGeo, new THREE.PointsMaterial({{
    size:0.12, vertexColors:true, transparent:true, opacity:0.8, sizeAttenuation:true,
}}));
scene.add(particles);

function makeTextSprite(text, color) {{
    const canvas = document.createElement('canvas');
    canvas.width = 256; canvas.height = 64;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0,0,256,64);
    ctx.fillStyle = color;
    ctx.font = 'bold 16px Arial';
    ctx.textAlign = 'center';
    ctx.fillText(text, 128, 42);
    const tex = new THREE.CanvasTexture(canvas);
    const sprite = new THREE.Sprite(new THREE.SpriteMaterial({{ map:tex, transparent:true }}));
    sprite.scale.set(3, 0.7, 1);
    return sprite;
}}

const nodes = [], nodeMeshes = [];
INTERVIEWS.forEach((s, i) => {{
    const color = new THREE.Color(s.color);
    const [px, py, pz] = s.pos;

    const outer = new THREE.Mesh(
        new THREE.TorusGeometry(0.75, 0.06, 8, 40),
        new THREE.MeshBasicMaterial({{ color }})
    );
    outer.position.set(px, py, pz);
    outer.rotation.x = Math.PI/4;
    scene.add(outer);

    const mesh = new THREE.Mesh(
        new THREE.SphereGeometry(0.5, 32, 32),
        new THREE.MeshStandardMaterial({{ color, metalness:0.6, roughness:0.2, emissive:color, emissiveIntensity:0.4 }})
    );
    mesh.position.set(px, py, pz);
    mesh.userData = s;
    mesh.castShadow = true;
    scene.add(mesh);
    nodeMeshes.push(mesh);

    const nodeLight = new THREE.PointLight(color, 1.5, 4);
    nodeLight.position.set(px, py, pz);
    scene.add(nodeLight);

    const label = makeTextSprite(s.flag + ' ' + s.name_ja, s.color);
    label.position.set(px, py+1.1, pz);
    scene.add(label);

    nodes.push({{ mesh, outer, label, nodeLight, baseY:py }});
}});

let isDragging = false;
let prevMouse = {{ x:0, y:0, startX:0, startY:0 }};
let spherical = {{ theta:0, phi:Math.PI/4, radius:16 }};
const camTarget = new THREE.Vector3(0,0,0);

function updateCamera() {{
    camera.position.x = camTarget.x + spherical.radius*Math.sin(spherical.phi)*Math.sin(spherical.theta);
    camera.position.y = camTarget.y + spherical.radius*Math.cos(spherical.phi);
    camera.position.z = camTarget.z + spherical.radius*Math.sin(spherical.phi)*Math.cos(spherical.theta);
    camera.lookAt(camTarget);
}}

renderer.domElement.addEventListener('mousedown', e => {{
    isDragging = true;
    prevMouse = {{ x:e.clientX, y:e.clientY, startX:e.clientX, startY:e.clientY }};
}});
window.addEventListener('mouseup', () => isDragging = false);
window.addEventListener('mousemove', e => {{
    if (!isDragging) return;
    spherical.theta -= (e.clientX - prevMouse.x) * 0.005;
    spherical.phi = Math.max(0.1, Math.min(Math.PI/2, spherical.phi + (e.clientY - prevMouse.y)*0.005));
    prevMouse.x = e.clientX; prevMouse.y = e.clientY;
    updateCamera();
}});
renderer.domElement.addEventListener('wheel', e => {{
    spherical.radius = Math.max(4, Math.min(30, spherical.radius + e.deltaY*0.02));
    updateCamera();
}});

let prevTouch = null;
renderer.domElement.addEventListener('touchstart', e => {{
    prevTouch = {{ x:e.touches[0].clientX, y:e.touches[0].clientY }};
}});
renderer.domElement.addEventListener('touchmove', e => {{
    if (!prevTouch) return;
    spherical.theta -= (e.touches[0].clientX - prevTouch.x)*0.005;
    spherical.phi = Math.max(0.1, Math.min(Math.PI/2, spherical.phi + (e.touches[0].clientY - prevTouch.y)*0.005));
    prevTouch = {{ x:e.touches[0].clientX, y:e.touches[0].clientY }};
    updateCamera(); e.preventDefault();
}}, {{ passive:false }});
renderer.domElement.addEventListener('touchend', () => {{ prevTouch = null; }});
updateCamera();

const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();
renderer.domElement.addEventListener('click', e => {{
    if (Math.abs(e.clientX - prevMouse.startX) > 5) return;
    mouse.x =  (e.clientX/window.innerWidth)*2 - 1;
    mouse.y = -(e.clientY/window.innerHeight)*2 + 1;
    raycaster.setFromCamera(mouse, camera);
    const hits = raycaster.intersectObjects(nodeMeshes);
    if (hits.length > 0) {{ showPanel(hits[0].object.userData); focusNode(hits[0].object); }}
}});

function showPanel(s) {{
    const kws = s.keywords.map(k => `<span class="panel-kw">${{k}}</span>`).join('');
    const noteHtml = s.interviewer_note
        ? `<div class="panel-note">📸 ${{s.interviewer_note}}</div>` : '';
    document.getElementById('panel-content').innerHTML = `
        <div class="panel-flag">${{s.flag}}</div>
        <div class="panel-name">${{s.name_ja}}</div>
        <div class="panel-dept">${{s.country}} · ${{s.department}}</div>
        ${{noteHtml}}
        <hr class="panel-divider">
        <div class="panel-q">Q1</div>
        <div class="panel-qt">${{s.q1}}</div>
        <div class="panel-a">${{s.a1}}</div>
        <div class="panel-q">Q2</div>
        <div class="panel-qt">${{s.q2}}</div>
        <div class="panel-a">${{s.a2}}</div>
        <div class="panel-q">Q3</div>
        <div class="panel-qt">${{s.q3}}</div>
        <div class="panel-a">${{s.a3}}</div>
        <hr class="panel-divider">
        <div class="panel-kw-wrap">${{kws}}</div>
    `;
    const panel = document.getElementById('info-panel');
    panel.style.display = 'block';
    panel.style.borderColor = s.color;
}}

function closePanel() {{
    document.getElementById('info-panel').style.display = 'none';
}}

function focusNode(mesh) {{
    const pos = mesh.position;
    spherical.theta = Math.atan2(pos.x - camTarget.x, pos.z - camTarget.z) + Math.PI;
    spherical.radius = 8;
    updateCamera();
}}

let t = 0;
function animate() {{
    requestAnimationFrame(animate);
    t += 0.01;
    nodes.forEach((n, i) => {{
        const dy = Math.sin(t + i*0.8)*0.2;
        n.mesh.position.y  = n.baseY + dy;
        n.label.position.y = n.baseY + dy + 1.1;
        n.outer.position.y = n.baseY + dy;
        n.outer.rotation.z = t*0.5 + i;
        n.outer.rotation.y = t*0.3 + i*0.5;
        n.mesh.rotation.y  = t*0.4 + i;
    }});
    ring.rotation.y = t*0.3;
    pointMain.intensity = 2.5 + Math.sin(t*2)*0.5;
    const pos = particles.geometry.attributes.position.array;
    for (let i = 0; i < particleCount; i++) {{
        pos[i*3+1] -= pSpd[i];
        pos[i*3]   += Math.sin(t*0.5 + i)*0.003;
        if (pos[i*3+1] < -2) pos[i*3+1] = 18;
    }}
    particles.geometry.attributes.position.needsUpdate = true;
    particles.rotation.y = t*0.02;
    renderer.render(scene, camera);
}}

window.addEventListener('resize', () => {{
    camera.aspect = window.innerWidth/window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}});

document.getElementById('loading').style.display = 'none';
if (INIT_SELECTED !== null) {{
    const s = INTERVIEWS.find(x => x.id === INIT_SELECTED);
    const mesh = nodeMeshes.find(m => m.userData.id === INIT_SELECTED);
    if (s && mesh) {{ showPanel(s); focusNode(mesh); }}
}}
animate();
</script>
</body>
</html>"""


# ──────────────────────────────────────────────────────────────
# メインエリア
# ──────────────────────────────────────────────────────────────
st.markdown('<p class="hero-title">🍁 新入留学生 メタバース・インタビュー・ギャラリー</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">東千田キャンパス｜新入留学生ウェルカムパーティ 2026.04.28｜聞き取り・撮影：楠香谷</p>', unsafe_allow_html=True)

if st.session_state.view_mode == "metaverse":
    html_code = build_metaverse_html(INTERVIEWS, st.session_state.selected_id)
    components.html(html_code, height=680, scrolling=False)

    if st.session_state.selected_id is not None:
        s = next(x for x in INTERVIEWS if x["id"] == st.session_state.selected_id)
        st.divider()
        st.markdown(f"### {s['flag']} {s['name_ja']} — {s['country']} · {s['department']}")
        if s.get("interviewer_note"):
            st.markdown(f'<div class="note-box">📸 {s["interviewer_note"]}</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        for col, (q, a) in zip([c1, c2, c3], [(s['q1'], s['a1']), (s['q2'], s['a2']), (s['q3'], s['a3'])]):
            with col:
                st.markdown(f"**{q}**")
                st.info(a)

else:
    st.markdown("### インタビュー一覧")
    cols = st.columns(2)
    for i, s in enumerate(INTERVIEWS):
        with cols[i % 2]:
            kw_html = " ".join(f'<span class="keyword-chip">{k}</span>' for k in s["keywords"])
            note_html = f'<div class="note-box">📸 {s["interviewer_note"]}</div>' if s.get("interviewer_note") else ""
            st.markdown(f"""
            <div class="interview-card" style="--card-color:{s['color']}">
                <div class="card-header">
                    <span class="card-flag">{s['flag']}</span>
                    <div>
                        <div class="card-name">{s['name_ja']}</div>
                        <div class="card-meta">{s['country']} · {s['department']}</div>
                    </div>
                </div>
                {note_html}
                <div class="qa-block">
                    <div class="q-label">Q1</div>
                    <div class="q-text">{s['q1']}</div>
                    <div class="a-text">{s['a1']}</div>
                </div>
                <div class="qa-block">
                    <div class="q-label">Q2</div>
                    <div class="q-text">{s['q2']}</div>
                    <div class="a-text">{s['a2']}</div>
                </div>
                <div class="qa-block">
                    <div class="q-label">Q3</div>
                    <div class="q-text">{s['q3']}</div>
                    <div class="a-text">{s['a3']}</div>
                </div>
                <div class="panel-kw-wrap">{kw_html}</div>
            </div>""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────
# フッター
# ──────────────────────────────────────────────────────────────
st.divider()
st.markdown("""
<div style="text-align:center; color:#8892A4; font-size:0.72rem; letter-spacing:2px; padding-bottom:16px;">
🍁 広島大学 東千田キャンパス ｜ 新入留学生ウェルカムパーティ 2026.04.28<br>
聞き取り・撮影：楠香谷 ｜ 研究課題：留学生の生の声への接触は、高校生の大学進学・探究学習への意欲を高めるか
</div>
""", unsafe_allow_html=True)
