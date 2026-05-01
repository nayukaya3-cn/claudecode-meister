"""
留学生インタビュー大作戦！ — 漫画UIバージョン
東千田キャンパス ウェルカムパーティ 2026/04/28
作：楠香谷
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="留学生インタビュー大作戦！| 漫画版",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
html, body, [class*="css"] { background: #f5f0e8 !important; }
.main .block-container { padding: 0.5rem 1rem !important; max-width: 100% !important; }
.stButton > button {
    background: #1a1a1a !important; color: #fff !important;
    border: 3px solid #1a1a1a !important; border-radius: 4px !important;
    font-weight: 900 !important; font-size: 1rem !important;
    letter-spacing: 2px !important;
}
</style>
""", unsafe_allow_html=True)


# ── SVGキャラクター生成 ──────────────────────────────────────────

def char(color: str, flag: str, expr: str = "smile",
         w: int = 70, h: int = 110, flip: bool = False) -> str:
    """シンプルなちびキャラSVGを返す"""
    exprs = {
        "smile":    ('<ellipse cx="24" cy="26" rx="5" ry="6" fill="#1a1a1a"/>'
                     '<ellipse cx="46" cy="26" rx="5" ry="6" fill="#1a1a1a"/>'
                     '<path d="M22 38 Q35 48 48 38" stroke="#1a1a1a" stroke-width="2.5" fill="none" stroke-linecap="round"/>'),
        "surprise": ('<ellipse cx="24" cy="26" rx="6" ry="8" fill="#1a1a1a"/>'
                     '<ellipse cx="46" cy="26" rx="6" ry="8" fill="#1a1a1a"/>'
                     '<ellipse cx="35" cy="40" rx="6" ry="7" fill="#1a1a1a"/>'),
        "confused": ('<ellipse cx="24" cy="26" rx="5" ry="6" fill="#1a1a1a"/>'
                     '<ellipse cx="46" cy="26" rx="5" ry="6" fill="#1a1a1a"/>'
                     '<path d="M22 38 Q29 34 35 38 Q41 42 48 38" stroke="#1a1a1a" stroke-width="2.5" fill="none" stroke-linecap="round"/>'
                     '<text x="50" y="12" font-size="14" fill="#FF6B35">？</text>'),
        "laugh":    ('<path d="M20 22 Q24 18 28 22" stroke="#1a1a1a" stroke-width="2" fill="none"/>'
                     '<path d="M42 22 Q46 18 50 22" stroke="#1a1a1a" stroke-width="2" fill="none"/>'
                     '<path d="M20 34 Q35 50 50 34" stroke="#1a1a1a" stroke-width="3" fill="none" stroke-linecap="round"/>'
                     '<text x="13" y="56" font-size="11" fill="#1a1a1a">笑</text>'),
        "sweat":    ('<ellipse cx="24" cy="26" rx="5" ry="6" fill="#1a1a1a"/>'
                     '<ellipse cx="46" cy="26" rx="5" ry="6" fill="#1a1a1a"/>'
                     '<path d="M22 38 Q35 34 48 38" stroke="#1a1a1a" stroke-width="2.5" fill="none"/>'
                     '<ellipse cx="56" cy="10" rx="4" ry="6" fill="#4fc3f7" opacity="0.8"/>'
                     '<ellipse cx="56" cy="17" rx="3" ry="4" fill="#4fc3f7" opacity="0.8"/>'),
        "run":      ('<ellipse cx="24" cy="26" rx="5" ry="6" fill="#1a1a1a"/>'
                     '<ellipse cx="46" cy="26" rx="5" ry="6" fill="#1a1a1a"/>'
                     '<path d="M22 38 Q35 44 48 38" stroke="#1a1a1a" stroke-width="2.5" fill="none" stroke-linecap="round"/>'),
        "angry":    ('<path d="M19 20 Q24 16 29 20" stroke="#1a1a1a" stroke-width="2.5" fill="none"/>'
                     '<path d="M41 20 Q46 16 51 20" stroke="#1a1a1a" stroke-width="2.5" fill="none"/>'
                     '<path d="M22 34 Q35 28 48 34" stroke="#1a1a1a" stroke-width="2.5" fill="none"/>'
                     '<text x="52" y="10" font-size="16" fill="#FF6B6B">！</text>'),
        "think":    ('<ellipse cx="24" cy="26" rx="5" ry="6" fill="#1a1a1a"/>'
                     '<ellipse cx="46" cy="26" rx="5" ry="6" fill="#1a1a1a"/>'
                     '<path d="M22 38 Q35 34 48 38" stroke="#1a1a1a" stroke-width="2.5" fill="none"/>'
                     '<text x="50" y="10" font-size="12" fill="#7B2FBE">・・・</text>'),
    }
    face_svg = exprs.get(expr, exprs["smile"])
    flip_tf = 'transform="scale(-1,1) translate(-70,0)"' if flip else ''
    body_color = color
    # lighten body color slightly
    return f"""<svg width="{w}" height="{h}" viewBox="0 0 70 110" {flip_tf}>
  <!-- head -->
  <circle cx="35" cy="30" r="25" fill="{body_color}" stroke="#1a1a1a" stroke-width="3"/>
  <!-- face -->
  {face_svg}
  <!-- flag -->
  <text x="22" y="65" font-size="20">{flag}</text>
  <!-- body -->
  <rect x="15" y="55" width="40" height="32" rx="6" fill="{body_color}" stroke="#1a1a1a" stroke-width="3"/>
  <!-- left leg -->
  <rect x="15" y="84" width="15" height="22" rx="5" fill="{body_color}" stroke="#1a1a1a" stroke-width="2.5"/>
  <!-- right leg -->
  <rect x="40" y="84" width="15" height="22" rx="5" fill="{body_color}" stroke="#1a1a1a" stroke-width="2.5"/>
</svg>"""


def char_run(color: str, flag: str) -> str:
    """走るポーズ"""
    return f"""<svg width="90" height="110" viewBox="0 0 90 110">
  <circle cx="35" cy="28" r="22" fill="{color}" stroke="#1a1a1a" stroke-width="3"/>
  <ellipse cx="26" cy="24" rx="4" ry="5" fill="#1a1a1a"/>
  <ellipse cx="44" cy="24" rx="4" ry="5" fill="#1a1a1a"/>
  <path d="M24 36 Q35 44 46 36" stroke="#1a1a1a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <text x="23" y="56" font-size="16">{flag}</text>
  <!-- leaning body -->
  <rect x="20" y="50" width="34" height="28" rx="5" fill="{color}" stroke="#1a1a1a" stroke-width="2.5"
        transform="rotate(-15 35 65)"/>
  <!-- running legs -->
  <rect x="14" y="76" width="13" height="26" rx="4" fill="{color}" stroke="#1a1a1a" stroke-width="2"
        transform="rotate(30 20 90)"/>
  <rect x="38" y="76" width="13" height="26" rx="4" fill="{color}" stroke="#1a1a1a" stroke-width="2"
        transform="rotate(-20 44 90)"/>
  <!-- speed lines -->
  <line x1="0" y1="35" x2="16" y2="38" stroke="#1a1a1a" stroke-width="1.5" opacity="0.5"/>
  <line x1="0" y1="45" x2="18" y2="46" stroke="#1a1a1a" stroke-width="1.5" opacity="0.5"/>
  <line x1="0" y1="55" x2="16" y2="54" stroke="#1a1a1a" stroke-width="1.5" opacity="0.5"/>
</svg>"""


def interviewer(expr: str = "smile", has_notepad: bool = True, flip: bool = False) -> str:
    """楠香谷（インタビュアー）"""
    exprs = {
        "smile":    '<path d="M22 38 Q35 48 48 38" stroke="#1a1a1a" stroke-width="2.5" fill="none" stroke-linecap="round"/>',
        "excited":  ('<ellipse cx="24" cy="26" rx="6" ry="7" fill="#1a1a1a"/>'
                     '<ellipse cx="46" cy="26" rx="6" ry="7" fill="#1a1a1a"/>'
                     '<path d="M22 40 Q35 50 48 40" stroke="#1a1a1a" stroke-width="2.5" fill="none" stroke-linecap="round"/>'),
        "surprised":('<ellipse cx="24" cy="26" rx="7" ry="9" fill="#1a1a1a"/>'
                     '<ellipse cx="46" cy="26" rx="7" ry="9" fill="#1a1a1a"/>'
                     '<ellipse cx="35" cy="40" rx="7" ry="8" fill="#1a1a1a"/>'),
        "reflect":  ('<path d="M20 22 Q24 18 28 22" stroke="#1a1a1a" stroke-width="2" fill="none"/>'
                     '<path d="M42 22 Q46 18 50 22" stroke="#1a1a1a" stroke-width="2" fill="none"/>'
                     '<path d="M22 36 Q29 32 35 36 Q41 40 48 36" stroke="#1a1a1a" stroke-width="2.5" fill="none"/>'),
        "determined":('<path d="M18 20 Q24 16 30 20" stroke="#1a1a1a" stroke-width="3" fill="none"/>'
                      '<path d="M40 20 Q46 16 52 20" stroke="#1a1a1a" stroke-width="3" fill="none"/>'
                      '<path d="M22 40 Q35 48 48 40" stroke="#1a1a1a" stroke-width="3" fill="none" stroke-linecap="round"/>'),
    }
    face = exprs.get(expr, exprs["smile"])
    if "ellipse" not in face and "path" not in face:
        face = ('<ellipse cx="24" cy="26" rx="5" ry="6" fill="#1a1a1a"/>'
                '<ellipse cx="46" cy="26" rx="5" ry="6" fill="#1a1a1a"/>' + face)
    notepad = """
  <rect x="46" y="58" width="22" height="28" rx="3" fill="white" stroke="#1a1a1a" stroke-width="2"/>
  <line x1="50" y1="65" x2="64" y2="65" stroke="#888" stroke-width="1.5"/>
  <line x1="50" y1="70" x2="64" y2="70" stroke="#888" stroke-width="1.5"/>
  <line x1="50" y1="75" x2="64" y2="75" stroke="#888" stroke-width="1.5"/>
  <rect x="48" y="56" width="5" height="6" rx="1" fill="#FFD700" stroke="#1a1a1a" stroke-width="1.5"/>
""" if has_notepad else ""
    flip_tf = 'transform="scale(-1,1) translate(-70,0)"' if flip else ''
    return f"""<svg width="90" height="110" viewBox="0 0 70 110" {flip_tf}>
  <circle cx="35" cy="30" r="25" fill="#FFD700" stroke="#1a1a1a" stroke-width="3"/>
  {face}
  <text x="25" y="65" font-size="14">🎤</text>
  <rect x="10" y="55" width="40" height="32" rx="6" fill="#FFD700" stroke="#1a1a1a" stroke-width="3"/>
  {notepad}
  <rect x="10" y="84" width="15" height="22" rx="5" fill="#FFD700" stroke="#1a1a1a" stroke-width="2.5"/>
  <rect x="35" y="84" width="15" height="22" rx="5" fill="#FFD700" stroke="#1a1a1a" stroke-width="2.5"/>
</svg>"""


# ── 共通HTML部品 ─────────────────────────────────────────────────

def bubble(text: str, style: str = "normal", color: str = "#fff",
           font_size: str = "0.9rem", max_width: str = "260px") -> str:
    """吹き出しHTML"""
    if style == "shout":
        return f"""<div style="background:{color};border:3px solid #1a1a1a;padding:8px 14px;
        border-radius:6px;clip-path:polygon(0 10%,4% 0,96% 0,100% 10%,100% 90%,96% 100%,4% 100%,0 90%);
        font-weight:900;font-size:{font_size};color:#1a1a1a;max-width:{max_width};
        text-align:center;line-height:1.4;">{text}</div>"""
    elif style == "think":
        return f"""<div style="background:{color};border:3px solid #1a1a1a;padding:8px 14px;
        border-radius:50%;font-size:{font_size};color:#1a1a1a;max-width:{max_width};
        text-align:center;line-height:1.5;font-weight:700;">{text}</div>"""
    elif style == "narration":
        return f"""<div style="background:#fffde7;border:3px solid #1a1a1a;padding:8px 14px;
        border-radius:0;font-size:{font_size};color:#1a1a1a;max-width:{max_width};
        line-height:1.6;font-weight:500;">{text}</div>"""
    else:
        return f"""<div style="background:{color};border:3px solid #1a1a1a;padding:8px 14px;
        border-radius:18px;font-size:{font_size};color:#1a1a1a;max-width:{max_width};
        line-height:1.6;font-weight:600;">{text}</div>"""


def sfx(text: str, color: str = "#FF6B35", size: str = "2.5rem",
        rotate: int = -8, x: int = 0) -> str:
    """擬音語・効果文字"""
    return f"""<div style="font-size:{size};font-weight:900;font-style:italic;
    color:{color};-webkit-text-stroke:3px #1a1a1a;text-shadow:4px 4px 0 #1a1a1a;
    transform:rotate({rotate}deg) translateX({x}px);display:inline-block;
    line-height:1;letter-spacing:2px;">{text}</div>"""


def narr(text: str) -> str:
    return bubble(text, style="narration", font_size="0.82rem")


def panel(content: str, bg: str = "#fff", border: str = "5px solid #1a1a1a",
          padding: str = "14px", flex: str = "1",
          min_h: str = "160px", extra_style: str = "") -> str:
    """コマ（パネル）"""
    return f"""<div style="background:{bg};border:{border};padding:{padding};
    flex:{flex};min-height:{min_h};display:flex;flex-direction:column;
    align-items:center;justify-content:center;gap:8px;position:relative;
    overflow:hidden;box-sizing:border-box;{extra_style}">{content}</div>"""


def halftone_bg(color: str = "#FFD70022") -> str:
    return f"background:{color};background-image:radial-gradient(circle,#1a1a1a11 1.5px,transparent 1.5px);background-size:12px 12px;"


def speed_lines(color: str = "#1a1a1a08") -> str:
    return f"background:conic-gradient({color} 0deg, transparent 2deg, {color} 4deg, transparent 6deg, {color} 8deg, transparent 360deg);"


# ── 各ページHTML ─────────────────────────────────────────────────

def page_cover() -> str:
    return f"""
<div class="manga-page" id="page-0">
  <div style="display:flex;flex-direction:column;height:100%;
              background:linear-gradient(160deg,#fff9f0 0%,#ffecd2 100%);
              border:6px solid #1a1a1a;position:relative;overflow:hidden;">
    <!-- speed lines bg -->
    <div style="position:absolute;inset:0;{speed_lines('#1a1a1a05')}opacity:0.5;"></div>
    <!-- top band -->
    <div style="background:#1a1a1a;color:#FFD700;text-align:center;
                padding:10px;font-size:0.75rem;letter-spacing:4px;font-weight:900;
                border-bottom:4px solid #FF6B35;">
      広島大学 東千田キャンパス ／ 2026年4月28日
    </div>
    <!-- main content -->
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;
                justify-content:center;padding:20px;gap:12px;position:relative;">
      <!-- title -->
      <div style="text-align:center;line-height:1.1;">
        <div style="font-size:2.8rem;font-weight:900;color:#1a1a1a;
                    -webkit-text-stroke:2px #1a1a1a;letter-spacing:2px;">
          留学生
        </div>
        <div style="font-size:2.2rem;font-weight:900;color:#FF6B35;
                    -webkit-text-stroke:2px #1a1a1a;letter-spacing:3px;">
          インタビュー
        </div>
        <div style="font-size:3rem;font-weight:900;color:#1a1a1a;
                    -webkit-text-stroke:2px #FF6B35;letter-spacing:2px;">
          大作戦！
        </div>
      </div>
      <!-- characters row -->
      <div style="display:flex;gap:4px;align-items:flex-end;margin:8px 0;">
        {char('#FF6B35','🇮🇩','smile',55,88)}
        {char('#FF6B6B','🇨🇳','surprised',55,88)}
        {interviewer('excited',True)}
        {char('#4ECDC4','🇨🇳','run',55,88)}
        {char('#A8E6CF','🇨🇳','laugh',55,88)}
      </div>
      <!-- sub title bubble -->
      <div style="background:#FFD700;border:4px solid #1a1a1a;border-radius:12px;
                  padding:8px 20px;font-size:0.88rem;font-weight:900;color:#1a1a1a;
                  text-align:center;line-height:1.5;">
        世界７カ国のリアルな声を届けろ！<br>
        <span style="font-size:0.72rem;font-weight:600;">ウェルカムパーティ潜入取材レポート</span>
      </div>
      <!-- author -->
      <div style="position:absolute;bottom:12px;right:16px;font-size:0.75rem;
                  font-weight:900;color:#1a1a1a;letter-spacing:2px;text-align:right;">
        聞き取り・撮影<br>楠香谷
      </div>
    </div>
    <!-- flags bottom -->
    <div style="background:#FF6B35;border-top:4px solid #1a1a1a;
                padding:6px;text-align:center;font-size:1.4rem;letter-spacing:6px;">
      🇮🇩 🇨🇳 🇨🇳 🇨🇳 🇯🇵 🇯🇵
    </div>
  </div>
</div>"""


def page_opening() -> str:
    return f"""
<div class="manga-page" id="page-1" style="display:none;">
  <div style="display:flex;flex-direction:column;height:100%;border:5px solid #1a1a1a;gap:4px;
              background:#fff;padding:4px;box-sizing:border-box;">
    <!-- row1: wide panel -->
    <div style="display:flex;gap:4px;flex:2;">
      {panel(f'''
        <div style="font-size:1.5rem;font-weight:900;color:#fff;
                    -webkit-text-stroke:1px #1a1a1a;text-shadow:3px 3px 0 #1a1a1a;
                    text-align:center;line-height:1.2;">
          広島大学<br>東千田キャンパス<br>ウェルカムパーティ！
        </div>
        <div style="display:flex;gap:2px;flex-wrap:wrap;justify-content:center;font-size:1.8rem;">
          🇮🇩🇨🇳🇻🇳🇰🇷🇪🇬🇯🇵🇧🇷🇮🇳🇲🇽🇹🇼
        </div>
        <div style="font-size:0.7rem;color:#fff;font-weight:700;letter-spacing:2px;">
          ── 世界中から新入生が集まる日 ──
        </div>
      ''', bg='linear-gradient(135deg,#1a1a2e,#16213e,#0f3460)', min_h='180px', flex='3')}
      <div style="display:flex;flex-direction:column;gap:4px;flex:1;">
        {panel(f'''
          {interviewer("excited",True)}
          {bubble("いくぞ！<br>インタビュー<br>大作戦！","shout","#FFD700","0.82rem")}
        ''', bg='#fffde7', min_h='80px')}
        {panel(f'''
          {narr("2026年4月28日。楠香谷は<br>ノートを手に会場に乗り込んだ。")}
        ''', bg='#fff9f0', min_h='80px')}
      </div>
    </div>
    <!-- row2 -->
    <div style="display:flex;gap:4px;flex:3;">
      {panel(f'''
        <div style="font-size:0.75rem;font-weight:700;color:#333;text-align:center;">
          会場には様々な国籍の留学生が！
        </div>
        <div style="display:flex;gap:6px;align-items:flex-end;">
          {char('#FF6B35','🇮🇩','smile',52,82)}
          {char('#FF6B35','🇮🇩','smile',52,82)}
          {char('#FF6B35','🇮🇩','laugh',52,82)}
        </div>
        {bubble("インドネシア<br>から来ました！","normal","#FFE4D0","0.78rem","140px")}
      ''', min_h='160px', flex='1')}
      {panel(f'''
        <div style="display:flex;gap:4px;align-items:flex-end;">
          {char('#FF6B6B','🇨🇳','smile',52,82)}
          {char('#4ECDC4','🇨🇳','think',52,82)}
          {char('#A8E6CF','🇨🇳','laugh',52,82)}
        </div>
        {bubble("中国から<br>３人来ています","normal","#FFE4E4","0.78rem","150px")}
        {sfx("ワイワイ","#4ECDC4","1.6rem",-5)}
      ''', min_h='160px', flex='1')}
      {panel(f'''
        {char('#DDA0DD','🇯🇵','smile',52,82)}
        {char('#F7DC6F','🇯🇵','smile',52,82)}
        {bubble("法学部2年生です！","normal","#F3E5F5","0.78rem","150px")}
        {narr("日本人学生も参加。<br>東千田の制度を<br>知っていた！")}
      ''', min_h='160px', flex='1')}
    </div>
    <!-- page label -->
    <div style="text-align:right;font-size:0.68rem;color:#888;padding:2px 6px;">
      ─ 第１話：いざ、パーティへ！ ─
    </div>
  </div>
</div>"""


def page_indonesia() -> str:
    return f"""
<div class="manga-page" id="page-2" style="display:none;">
  <div style="display:flex;flex-direction:column;height:100%;border:5px solid #1a1a1a;gap:4px;
              background:#fff;padding:4px;box-sizing:border-box;">
    <!-- タイトルバー -->
    <div style="background:#FF6B35;border:3px solid #1a1a1a;
                color:#fff;text-align:center;padding:6px;
                font-weight:900;font-size:1.1rem;letter-spacing:3px;">
      🇮🇩 インドネシア留学生３名との遭遇
    </div>
    <!-- row1 -->
    <div style="display:flex;gap:4px;flex:2;">
      {panel(f'''
        <div style="display:flex;gap:2px;align-items:flex-end;">
          {char('#FF6B35','🇮🇩','smile',56,90)}
          {char('#FF6B35','🇮🇩','smile',56,90)}
          {char('#FF6B35','🇮🇩','laugh',56,90)}
        </div>
        {sfx("ドドド","#FF6B35","2rem",-5)}
        {narr("写真一番上の⭕が私（楠香谷）。<br>インドネシア留学生の間に写っている。")}
      ''', bg='#fff8f0', flex='2', min_h='150px')}
      {panel(f'''
        {interviewer("excited",True,flip=True)}
        {bubble("出身地は<br>どちらですか？","shout","#FFD700","0.9rem","160px")}
      ''', flex='1', min_h='150px')}
    </div>
    <!-- row2 -->
    <div style="display:flex;gap:4px;flex:2;">
      {panel(f'''
        {char('#FF6B35','🇮🇩','smile',60,96)}
        {bubble("スマトラでも<br>ジャワでもないですよ♪","normal","#FFE4D0","0.9rem","180px")}
      ''', flex='1', min_h='140px')}
      {panel(f'''
        {interviewer("surprised",False)}
        {bubble("え…！？<br>スマトラでも<br>ジャワでも<br>ない…？","think","#fff9c4","0.88rem","160px")}
        {sfx("ガーン","#FF6B6B","2.2rem",-8)}
      ''', bg='#fffde7', flex='1', min_h='140px')}
    </div>
    <!-- row3 -->
    <div style="display:flex;gap:4px;flex:2;">
      {panel(f'''
        {narr("その時点でインドネシアの地理知識が<br>不足しており、会話が続かなかった…")}
        {sfx("シーン…","#888","1.6rem",3)}
        <div style="display:flex;gap:2px;">
          {char('#FF6B35','🇮🇩','confused',44,72)}
          {interviewer("reflect",False)}
        </div>
      ''', bg='#f5f5f5', flex='2', min_h='130px')}
      {panel(f'''
        {bubble("反省！<br>スマトラ・ジャワ以外の<br>島々の歴史を<br>事前に調べるべきだった！！","shout","#FFE4D0","0.8rem","180px")}
        {sfx("後悔","#FF6B35","1.8rem",-10)}
      ''', bg='#fff8f0', flex='1', min_h='130px')}
    </div>
    <div style="text-align:right;font-size:0.68rem;color:#888;padding:2px 6px;">
      ─ 第２話：事前準備の重要性 ─
    </div>
  </div>
</div>"""


def page_china_a() -> str:
    return f"""
<div class="manga-page" id="page-3" style="display:none;">
  <div style="display:flex;flex-direction:column;height:100%;border:5px solid #1a1a1a;gap:4px;
              background:#fff;padding:4px;box-sizing:border-box;">
    <div style="background:#FF6B6B;border:3px solid #1a1a1a;
                color:#fff;text-align:center;padding:6px;
                font-weight:900;font-size:1.1rem;letter-spacing:3px;">
      🇨🇳 中国人留学生A ── SDS・ファイナンス専攻
    </div>
    <!-- row1 -->
    <div style="display:flex;gap:4px;flex:2;">
      {panel(f'''
        {char('#FF6B6B','🇨🇳','sweat',64,100)}
        {bubble("日本語が弱くて…<br>アルバイトが<br>心配です","normal","#FFE4E4","0.9rem","170px")}
        {narr("広島大学SDS（持続可能性科学）<br>ファイナンス専攻")}
      ''', flex='3', min_h='150px')}
      {panel(f'''
        {interviewer("think",True,flip=True)}
        {bubble("日本企業に<br>就職したい<br>んですよね？","normal","#FFF9C4","0.85rem","150px")}
      ''', flex='2', min_h='150px')}
    </div>
    <!-- row2 -->
    <div style="display:flex;gap:4px;flex:2;">
      {panel(f'''
        {interviewer("excited",True)}
        {bubble("アントレプレナーって<br>知ってますか？","shout","#FFD700","0.9rem","170px")}
      ''', flex='1', min_h='130px')}
      {panel(f'''
        {char('#FF6B6B','🇨🇳','confused',64,100)}
        {sfx("？？？","#4ECDC4","2.5rem",5)}
        {bubble("…アントレ<br>プレナー…？","think","#FFE4E4","0.88rem","150px")}
      ''', bg='#fff0f0', flex='1', min_h='130px')}
    </div>
    <!-- row3: running away -->
    <div style="display:flex;gap:4px;flex:2;">
      {panel(f'''
        {narr("起業家精神（アントレプレナーシップ）という<br>概念がなかなか通じなかった…")}
        <div style="font-size:0.78rem;color:#666;font-weight:600;text-align:center;line-height:1.5;">
          言語の壁だけでなく、<br>概念自体の文化的な馴染みの違い？<br>とても興味深い発見だった。
        </div>
      ''', bg='#fff9f0', flex='2', min_h='130px')}
      {panel(f'''
        {char_run('#FF6B6B','🇨🇳')}
        {bubble("授業が<br>始まる！！","shout","#FF6B6B","1rem","140px")}
        {sfx("ダッシュ！！","#1a1a1a","1.8rem",-12)}
      ''', flex='1', min_h='130px')}
    </div>
    <div style="text-align:right;font-size:0.68rem;color:#888;padding:2px 6px;">
      ─ 第３話：「アントレプレナー」が通じない！ ─
    </div>
  </div>
</div>"""


def page_china_b() -> str:
    return f"""
<div class="manga-page" id="page-4" style="display:none;">
  <div style="display:flex;flex-direction:column;height:100%;border:5px solid #1a1a1a;gap:4px;
              background:#fff;padding:4px;box-sizing:border-box;">
    <div style="background:#4ECDC4;border:3px solid #1a1a1a;
                color:#fff;text-align:center;padding:6px;
                font-weight:900;font-size:1.1rem;letter-spacing:3px;">
      🇨🇳 中国人留学生B ── 組織論・キヤノン志望
    </div>
    <!-- row1 -->
    <div style="display:flex;gap:4px;flex:2;">
      {panel(f'''
        {char('#4ECDC4','🇨🇳','smile',64,100)}
        {bubble("キヤノンに<br>就職したい<br>んです！！","shout","#E0F7FA","1rem","170px")}
        {sfx("キラーン","#FFD700","1.8rem",-5)}
      ''', flex='1', min_h='150px')}
      {panel(f'''
        {interviewer("surprised",True,flip=True)}
        {narr("キヤノン…？<br>ちょうど中国生産撤退・<br>史上最高水準の退職補償が<br>ニュースになっていた頃。")}
        {bubble("それでも<br>キヤノンを<br>選ぶのか！？","think","#FFF9C4","0.82rem","160px")}
      ''', bg='#f9f9f9', flex='1', min_h='150px')}
    </div>
    <!-- row2 -->
    <div style="display:flex;gap:4px;flex:2;">
      {panel(f'''
        {char('#4ECDC4','🇨🇳','confused',56,88)}
        {bubble("高校は理系でした。<br>化学・生物・物理は得意。<br>でも数学は苦手で…","normal","#E0F7FA","0.85rem","190px")}
        {narr("▶ 文系大学院（組織論）へ")}
      ''', flex='2', min_h='130px')}
      {panel(f'''
        {interviewer("think",False,flip=True)}
        {bubble("経済学は<br>微分を使うから<br>大変では？","normal","#FFF9C4","0.85rem","150px")}
      ''', flex='1', min_h='130px')}
    </div>
    <!-- row3 -->
    <div style="display:flex;gap:4px;flex:2;">
      {panel(f'''
        {char('#4ECDC4','🇨🇳','smile',56,88)}
        {bubble("最初の半年間は<br>「研究生」として勉強します。<br>その後、本格的に<br>大学院に進学できますよ！","normal","#E0F7FA","0.85rem","200px")}
        {narr("▶ 研究生制度（6ヶ月）を発見！")}
      ''', flex='2', min_h='120px')}
      {panel(f'''
        {char_run('#4ECDC4','🇨🇳')}
        {bubble("あ！授業！","shout","#4ECDC4","1rem","120px")}
        {sfx("またかよ！","#FF6B35","1.6rem",-8)}
      ''', flex='1', min_h='120px')}
    </div>
    <div style="text-align:right;font-size:0.68rem;color:#888;padding:2px 6px;">
      ─ 第４話：研究生制度の秘密 ─
    </div>
  </div>
</div>"""


def page_china_c() -> str:
    return f"""
<div class="manga-page" id="page-5" style="display:none;">
  <div style="display:flex;flex-direction:column;height:100%;border:5px solid #1a1a1a;gap:4px;
              background:#fff;padding:4px;box-sizing:border-box;">
    <div style="background:#A8E6CF;border:3px solid #1a1a1a;
                color:#1a1a1a;text-align:center;padding:6px;
                font-weight:900;font-size:1.1rem;letter-spacing:3px;">
      🇨🇳 中国人留学生C ── 行動経済学・インフルエンサー研究
    </div>
    <!-- row1 -->
    <div style="display:flex;gap:4px;flex:2;">
      {panel(f'''
        {char('#A8E6CF','🇨🇳','smile',64,100)}
        {narr("その日は授業がなく<br>ゆっくりしていた。")}
        {bubble("インフルエンサーによる<br>衝動購買への効果を<br>研究しています","normal","#DCEDC8","0.88rem","200px")}
      ''', flex='2', min_h='150px')}
      {panel(f'''
        {sfx("ユルい日","#A8E6CF","1.6rem",5)}
        {interviewer("think",True,flip=True)}
        {narr("唯一ゆっくり<br>話せた！")}
      ''', bg='#f0fff4', flex='1', min_h='150px')}
    </div>
    <!-- row2: comedy moment -->
    <div style="display:flex;gap:4px;flex:3;">
      {panel(f'''
        {interviewer("excited",True)}
        {bubble("では…<br>フォロワー数は<br>何人ですか！？","shout","#FFD700","1rem","170px")}
      ''', flex='1', min_h='160px')}
      {panel(f'''
        {char('#A8E6CF','🇨🇳','confused',64,100)}
        {sfx("え？？","#FF6B35","2.8rem",5)}
        {bubble("私はインフルエンサー<br>じゃなくて…<br>インフルエンサーを<br>研究している<br>研究者です","normal","#DCEDC8","0.82rem","180px")}
      ''', bg='#f0fff4', flex='2', min_h='160px')}
    </div>
    <!-- row3: realization + photo -->
    <div style="display:flex;gap:4px;flex:2;">
      {panel(f'''
        <div style="display:flex;gap:6px;align-items:flex-end;">
          {interviewer("surprised",True)}
          {char('#A8E6CF','🇨🇳','laugh',56,88)}
        </div>
        {sfx("ドッ！","#FFD700","2rem",-5)}
        {bubble("あっそういうことか！<br>笑！！","shout","#FFF9C4","0.9rem","170px")}
      ''', flex='2', min_h='130px')}
      {panel(f'''
        {narr("授業がないから<br>写真撮影もできた！")}
        <div style="font-size:2.5rem;">📸</div>
        {sfx("パシャ！","#4ECDC4","1.8rem",-8)}
        {bubble("唯一の<br>撮影成功例","normal","#DCEDC8","0.78rem","130px")}
      ''', bg='#f0fff4', flex='1', min_h='130px')}
    </div>
    <div style="text-align:right;font-size:0.68rem;color:#888;padding:2px 6px;">
      ─ 第５話：笑いが生まれた瞬間 ─
    </div>
  </div>
</div>"""


def page_japan_epilogue() -> str:
    return f"""
<div class="manga-page" id="page-6" style="display:none;">
  <div style="display:flex;flex-direction:column;height:100%;border:5px solid #1a1a1a;gap:4px;
              background:#fff;padding:4px;box-sizing:border-box;">
    <div style="background:#DDA0DD;border:3px solid #1a1a1a;
                color:#fff;text-align:center;padding:6px;
                font-weight:900;font-size:1.1rem;letter-spacing:3px;">
      🇯🇵 日本人法学部生 ── キャンパス制度の秘密
    </div>
    <!-- row1 -->
    <div style="display:flex;gap:4px;flex:2;">
      {panel(f'''
        <div style="display:flex;gap:4px;align-items:flex-end;">
          {char('#DDA0DD','🇯🇵','smile',56,88)}
          {char('#F7DC6F','🇯🇵','smile',56,88)}
        </div>
        {narr("法学部昼間主コース2年生。<br>広島出身と関西出身のふたり。")}
      ''', flex='1', min_h='140px')}
      {panel(f'''
        {char('#DDA0DD','🇯🇵','excited',56,88)}
        {bubble("オンライン授業を使えば<br>教養課程でも<br>東千田だけで<br>通えます！","shout","#F3E5F5","0.9rem","190px")}
        {sfx("ナント！","#DDA0DD","1.8rem",-8)}
      ''', flex='2', min_h='140px')}
    </div>
    <!-- row2 -->
    <div style="display:flex;gap:4px;flex:1.5;">
      {panel(f'''
        {interviewer("surprised",True,flip=True)}
        {bubble("東広島キャンパスに<br>行かなくて<br>いいの！？","surprise","#FFF9C4","0.9rem","160px")}
      ''', flex='1', min_h='110px')}
      {panel(f'''
        {char('#F7DC6F','🇯🇵','smile',56,88)}
        {bubble("広島出身と<br>関西出身、<br>どちらもOK！","normal","#FFFDE7","0.85rem","160px")}
        {narr("都市型キャンパスの<br>大きなメリット")}
      ''', flex='1', min_h='110px')}
    </div>
    <!-- epilogue row -->
    <div style="display:flex;gap:4px;flex:3;">
      {panel(f'''
        {interviewer("reflect",True)}
        {narr("今日の反省<br>① 事前に出身地の地理・歴史を調べる<br>② 概念は言葉だけでなく例で伝える<br>③ 授業のない時間帯を狙って写真を！")}
      ''', bg='#fffde7', flex='1', min_h='150px')}
      {panel(f'''
        {interviewer("determined",True)}
        {bubble("次回こそ<br>完璧な準備で<br>臨むぞ！！","shout","#FFD700","1.1rem","160px")}
        {sfx("ガッ！","#FF6B35","2.5rem",-10)}
        {narr("── 完 ──")}
      ''', bg='#fff8f0', flex='1', min_h='150px')}
    </div>
    <div style="text-align:right;font-size:0.68rem;color:#888;padding:2px 6px;">
      ─ 最終話：次回予告あり ─
    </div>
  </div>
</div>"""


# ── 全体HTML ────────────────────────────────────────────────────

def build_manga_html() -> str:
    pages_html = (
        page_cover() +
        page_opening() +
        page_indonesia() +
        page_china_a() +
        page_china_b() +
        page_china_c() +
        page_japan_epilogue()
    )
    total = 7
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap');
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
    background: #2a2a2a;
    font-family: 'Noto Sans JP', 'Hiragino Kaku Gothic Pro', sans-serif;
    display: flex; flex-direction: column; align-items: center;
    min-height: 100vh; padding: 8px 4px;
}}
#reader-wrap {{
    width: 100%; max-width: 680px;
    display: flex; flex-direction: column; align-items: center; gap: 8px;
}}
.manga-page {{
    width: 100%;
    aspect-ratio: 3/4;
    background: #fff;
    box-shadow: 0 8px 32px rgba(0,0,0,0.6);
}}
.manga-page > div {{ height: 100%; }}
/* nav */
#nav-bar {{
    display: flex; align-items: center; gap: 12px;
    background: #1a1a1a; border-radius: 8px; padding: 8px 16px;
    width: 100%; max-width: 680px; justify-content: center;
}}
.nav-btn {{
    background: #FF6B35; border: 3px solid #fff; border-radius: 6px;
    color: #fff; font-size: 0.95rem; font-weight: 900;
    padding: 6px 18px; cursor: pointer; letter-spacing: 2px;
    transition: transform 0.1s, background 0.1s;
}}
.nav-btn:hover {{ background: #FFD700; color: #1a1a1a; transform: scale(1.05); }}
.nav-btn:disabled {{ background: #555; cursor: default; transform: none; }}
#page-counter {{
    color: #FFD700; font-weight: 900; font-size: 1rem;
    letter-spacing: 3px; font-family: monospace;
    min-width: 80px; text-align: center;
}}
#page-title {{
    color: #aaa; font-size: 0.7rem; letter-spacing: 2px;
    min-width: 160px; text-align: center;
}}
</style>
</head>
<body>
<div id="reader-wrap">
  <div id="nav-bar">
    <button class="nav-btn" id="btn-prev" onclick="prevPage()" disabled>◀ 前</button>
    <div style="display:flex;flex-direction:column;align-items:center;gap:2px;">
      <div id="page-counter">1 / {total}</div>
      <div id="page-title">表紙</div>
    </div>
    <button class="nav-btn" id="btn-next" onclick="nextPage()">次 ▶</button>
  </div>
  {pages_html}
</div>

<script>
const TITLES = [
  "表紙 — 留学生インタビュー大作戦！",
  "第１話 — いざ、パーティへ！",
  "第２話 — インドネシア留学生との遭遇",
  "第３話 — アントレプレナーが通じない！",
  "第４話 — 研究生制度の秘密",
  "第５話 — 笑いが生まれた瞬間",
  "最終話 — 次回予告あり",
];
let cur = 0;
const total = {total};

function showPage(n) {{
  document.querySelectorAll('.manga-page').forEach((p,i) => {{
    p.style.display = (i === n) ? 'block' : 'none';
  }});
  document.getElementById('page-counter').textContent = (n+1) + ' / ' + total;
  document.getElementById('page-title').textContent = TITLES[n];
  document.getElementById('btn-prev').disabled = (n === 0);
  document.getElementById('btn-next').disabled = (n === total-1);
  window.scrollTo(0,0);
  cur = n;
}}

function nextPage() {{ if (cur < total-1) showPage(cur+1); }}
function prevPage() {{ if (cur > 0) showPage(cur-1); }}

// keyboard navigation
document.addEventListener('keydown', e => {{
  if (e.key === 'ArrowRight' || e.key === 'ArrowDown') nextPage();
  if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')  prevPage();
}});

// touch swipe
let tx = 0;
document.addEventListener('touchstart', e => {{ tx = e.touches[0].clientX; }});
document.addEventListener('touchend', e => {{
  const dx = e.changedTouches[0].clientX - tx;
  if (Math.abs(dx) > 50) {{ if (dx < 0) nextPage(); else prevPage(); }}
}});

showPage(0);
</script>
</body>
</html>"""


# ── Streamlit UI ────────────────────────────────────────────────

st.markdown("""
<div style="text-align:center;background:#1a1a1a;border-radius:10px;
            padding:10px;margin-bottom:8px;">
  <span style="font-size:1.4rem;font-weight:900;color:#FFD700;letter-spacing:4px;">
    📖 留学生インタビュー大作戦！
  </span><br>
  <span style="font-size:0.75rem;color:#aaa;letter-spacing:3px;">
    漫画版 ／ 東千田キャンパス 2026.04.28 ／ 作：楠香谷
  </span>
</div>
""", unsafe_allow_html=True)

col_hint = st.columns([1, 2, 1])
with col_hint[1]:
    st.markdown("""
    <div style="text-align:center;font-size:0.75rem;color:#666;
                background:#fffde7;border:2px solid #FFD700;
                border-radius:8px;padding:6px 12px;">
    ◀▶ ボタン または ← → キー または スワイプ でページをめくる
    </div>""", unsafe_allow_html=True)

components.html(build_manga_html(), height=780, scrolling=False)

st.divider()
st.markdown("""
<div style="text-align:center;font-size:0.72rem;color:#888;letter-spacing:2px;">
🍁 広島大学 東千田キャンパス ／ 新入留学生ウェルカムパーティ 2026.04.28<br>
聞き取り・撮影：楠香谷 ／ メタバース版: <a href="http://localhost:8502" style="color:#FF6B35;">localhost:8502</a>
</div>
""", unsafe_allow_html=True)
