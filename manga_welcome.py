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
html, body, [class*="css"] { background: #2a2a2a !important; }
.main .block-container {
    padding: 0.3rem 0.5rem !important;
    max-width: 100% !important;
}
</style>
""", unsafe_allow_html=True)


# ── SVGキャラクター（コンパクト版） ─────────────────────────────

def char(color: str, flag: str, expr: str = "smile",
         w: int = 44, h: int = 70, flip: bool = False) -> str:
    faces = {
        "smile":     ('<ellipse cx="17" cy="16" rx="3" ry="3.5" fill="#111"/>'
                      '<ellipse cx="28" cy="16" rx="3" ry="3.5" fill="#111"/>'
                      '<path d="M15 23 Q22.5 30 30 23" stroke="#111" stroke-width="2" fill="none" stroke-linecap="round"/>'),
        "surprise":  ('<ellipse cx="17" cy="16" rx="4" ry="5" fill="#111"/>'
                      '<ellipse cx="28" cy="16" rx="4" ry="5" fill="#111"/>'
                      '<ellipse cx="22.5" cy="25" rx="4" ry="5" fill="#111"/>'),
        "confused":  ('<ellipse cx="17" cy="16" rx="3" ry="3.5" fill="#111"/>'
                      '<ellipse cx="28" cy="16" rx="3" ry="3.5" fill="#111"/>'
                      '<path d="M15 23 Q18 20 22 23 Q26 26 30 23" stroke="#111" stroke-width="2" fill="none"/>'
                      '<text x="31" y="8" font-size="9" fill="#FF6B35">？</text>'),
        "laugh":     ('<path d="M13 13 Q17 10 21 13" stroke="#111" stroke-width="1.5" fill="none"/>'
                      '<path d="M24 13 Q28 10 32 13" stroke="#111" stroke-width="1.5" fill="none"/>'
                      '<path d="M14 21 Q22.5 32 31 21" stroke="#111" stroke-width="2.5" fill="none" stroke-linecap="round"/>'),
        "sweat":     ('<ellipse cx="17" cy="16" rx="3" ry="3.5" fill="#111"/>'
                      '<ellipse cx="28" cy="16" rx="3" ry="3.5" fill="#111"/>'
                      '<path d="M15 23 Q22.5 20 30 23" stroke="#111" stroke-width="2" fill="none"/>'
                      '<ellipse cx="36" cy="6" rx="2.5" ry="4" fill="#4fc3f7" opacity="0.85"/>'),
        "think":     ('<ellipse cx="17" cy="16" rx="3" ry="3.5" fill="#111"/>'
                      '<ellipse cx="28" cy="16" rx="3" ry="3.5" fill="#111"/>'
                      '<path d="M15 23 Q22.5 20 30 23" stroke="#111" stroke-width="2" fill="none"/>'
                      '<text x="31" y="8" font-size="8" fill="#7B2FBE">…</text>'),
        "angry":     ('<path d="M13 11 Q17 8 21 11" stroke="#111" stroke-width="2" fill="none"/>'
                      '<path d="M24 11 Q28 8 32 11" stroke="#111" stroke-width="2" fill="none"/>'
                      '<path d="M15 23 Q22.5 19 30 23" stroke="#111" stroke-width="2" fill="none"/>'),
        "excited":   ('<ellipse cx="17" cy="16" rx="4" ry="4.5" fill="#111"/>'
                      '<ellipse cx="28" cy="16" rx="4" ry="4.5" fill="#111"/>'
                      '<path d="M14 24 Q22.5 32 31 24" stroke="#111" stroke-width="2.5" fill="none" stroke-linecap="round"/>'),
        "determined":('<path d="M12 12 Q17 9 22 12" stroke="#111" stroke-width="2.5" fill="none"/>'
                      '<path d="M23 12 Q28 9 33 12" stroke="#111" stroke-width="2.5" fill="none"/>'
                      '<path d="M14 24 Q22.5 31 31 24" stroke="#111" stroke-width="2.5" fill="none" stroke-linecap="round"/>'),
        "reflect":   ('<path d="M13 14 Q17 11 21 14" stroke="#111" stroke-width="1.5" fill="none"/>'
                      '<path d="M24 14 Q28 11 32 14" stroke="#111" stroke-width="1.5" fill="none"/>'
                      '<path d="M15 23 Q19 19 22.5 22 Q26 25 30 23" stroke="#111" stroke-width="2" fill="none"/>'),
    }
    face = faces.get(expr, faces["smile"])
    tf = f'transform="scale(-1,1) translate(-{w},0)"' if flip else ""
    return f"""<svg width="{w}" height="{h}" viewBox="0 0 45 72" {tf}>
  <circle cx="22" cy="19" r="16" fill="{color}" stroke="#111" stroke-width="2.5"/>
  {face}
  <text x="13" y="41" font-size="14">{flag}</text>
  <rect x="9" y="35" width="26" height="21" rx="4" fill="{color}" stroke="#111" stroke-width="2.5"/>
  <rect x="9" y="53" width="10" height="15" rx="3" fill="{color}" stroke="#111" stroke-width="2"/>
  <rect x="26" y="53" width="10" height="15" rx="3" fill="{color}" stroke="#111" stroke-width="2"/>
</svg>"""


def char_run(color: str, flag: str, w: int = 55, h: int = 70) -> str:
    return f"""<svg width="{w}" height="{h}" viewBox="0 0 58 72">
  <circle cx="22" cy="18" r="14" fill="{color}" stroke="#111" stroke-width="2.5"/>
  <ellipse cx="16" cy="15" rx="3" ry="3.5" fill="#111"/>
  <ellipse cx="27" cy="15" rx="3" ry="3.5" fill="#111"/>
  <path d="M14 22 Q22 28 30 22" stroke="#111" stroke-width="2" fill="none" stroke-linecap="round"/>
  <text x="13" y="40" font-size="13">{flag}</text>
  <rect x="9" y="33" width="24" height="18" rx="4" fill="{color}" stroke="#111" stroke-width="2.5"
        transform="rotate(-15 21 42)"/>
  <rect x="8" y="50" width="10" height="18" rx="3" fill="{color}" stroke="#111" stroke-width="2"
        transform="rotate(25 13 60)"/>
  <rect x="28" y="50" width="10" height="18" rx="3" fill="{color}" stroke="#111" stroke-width="2"
        transform="rotate(-20 33 60)"/>
  <line x1="0" y1="22" x2="9" y2="24" stroke="#111" stroke-width="1.5" opacity="0.4"/>
  <line x1="0" y1="30" x2="9" y2="31" stroke="#111" stroke-width="1.5" opacity="0.4"/>
  <line x1="0" y1="38" x2="9" y2="38" stroke="#111" stroke-width="1.5" opacity="0.4"/>
</svg>"""


def interviewer(expr: str = "smile", has_notepad: bool = True,
                flip: bool = False, w: int = 48, h: int = 70) -> str:
    faces = {
        "smile":      '<path d="M14 23 Q22 30 30 23" stroke="#111" stroke-width="2" fill="none" stroke-linecap="round"/>',
        "excited":    ('<ellipse cx="16" cy="16" rx="4" ry="4.5" fill="#111"/>'
                       '<ellipse cx="28" cy="16" rx="4" ry="4.5" fill="#111"/>'
                       '<path d="M13 25 Q22 33 31 25" stroke="#111" stroke-width="2.5" fill="none" stroke-linecap="round"/>'),
        "surprised":  ('<ellipse cx="16" cy="16" rx="5" ry="6" fill="#111"/>'
                       '<ellipse cx="28" cy="16" rx="5" ry="6" fill="#111"/>'
                       '<ellipse cx="22" cy="26" rx="5" ry="5.5" fill="#111"/>'),
        "reflect":    ('<path d="M13 14 Q17 11 21 14" stroke="#111" stroke-width="1.5" fill="none"/>'
                       '<path d="M23 14 Q27 11 31 14" stroke="#111" stroke-width="1.5" fill="none"/>'
                       '<path d="M14 23 Q18 19 22 22 Q26 25 30 23" stroke="#111" stroke-width="2" fill="none"/>'),
        "think":      ('<ellipse cx="16" cy="16" rx="3.5" ry="4" fill="#111"/>'
                       '<ellipse cx="28" cy="16" rx="3.5" ry="4" fill="#111"/>'
                       '<path d="M14 23 Q22 20 30 23" stroke="#111" stroke-width="2" fill="none"/>'
                       '<text x="31" y="8" font-size="9" fill="#7B2FBE">…</text>'),
        "determined": ('<path d="M12 11 Q16 8 20 11" stroke="#111" stroke-width="2.5" fill="none"/>'
                       '<path d="M24 11 Q28 8 32 11" stroke="#111" stroke-width="2.5" fill="none"/>'
                       '<path d="M13 24 Q22 31 31 24" stroke="#111" stroke-width="2.5" fill="none" stroke-linecap="round"/>'),
    }
    face = faces.get(expr, faces["smile"])
    if "ellipse" not in face and "path" not in face:
        face = ('<ellipse cx="16" cy="16" rx="3.5" ry="4" fill="#111"/>'
                '<ellipse cx="28" cy="16" rx="3.5" ry="4" fill="#111"/>' + face)
    np = """<rect x="30" y="36" width="14" height="18" rx="2" fill="white" stroke="#111" stroke-width="1.5"/>
  <line x1="32" y1="41" x2="42" y2="41" stroke="#aaa" stroke-width="1"/>
  <line x1="32" y1="45" x2="42" y2="45" stroke="#aaa" stroke-width="1"/>
  <line x1="32" y1="49" x2="42" y2="49" stroke="#aaa" stroke-width="1"/>
  <rect x="31" y="35" width="4" height="4" rx="1" fill="#FFD700" stroke="#111" stroke-width="1"/>""" if has_notepad else ""
    tf = f'transform="scale(-1,1) translate(-{w},0)"' if flip else ""
    return f"""<svg width="{w}" height="{h}" viewBox="0 0 45 72" {tf}>
  <circle cx="22" cy="19" r="15" fill="#FFD700" stroke="#111" stroke-width="2.5"/>
  {face}
  <text x="15" y="41" font-size="12">🎤</text>
  <rect x="8" y="35" width="26" height="21" rx="4" fill="#FFD700" stroke="#111" stroke-width="2.5"/>
  {np}
  <rect x="8" y="53" width="10" height="15" rx="3" fill="#FFD700" stroke="#111" stroke-width="2"/>
  <rect x="26" y="53" width="10" height="15" rx="3" fill="#FFD700" stroke="#111" stroke-width="2"/>
</svg>"""


# ── HTML部品 ─────────────────────────────────────────────────────

def bub(text: str, style: str = "normal", color: str = "#fff",
        fs: str = "0.74rem", mw: str = "200px") -> str:
    if style == "shout":
        return (f'<div style="background:{color};border:2.5px solid #111;padding:5px 10px;'
                f'clip-path:polygon(0 12%,3% 0,97% 0,100% 12%,100% 88%,97% 100%,3% 100%,0 88%);'
                f'font-weight:900;font-size:{fs};color:#111;max-width:{mw};'
                f'text-align:center;line-height:1.35;">{text}</div>')
    elif style == "think":
        return (f'<div style="background:{color};border:2.5px solid #111;padding:5px 10px;'
                f'border-radius:50%;font-size:{fs};color:#111;max-width:{mw};'
                f'text-align:center;line-height:1.4;font-weight:700;">{text}</div>')
    elif style == "narr":
        return (f'<div style="background:#fffde7;border:2.5px solid #111;padding:5px 10px;'
                f'border-radius:0;font-size:{fs};color:#111;max-width:{mw};'
                f'line-height:1.5;font-weight:500;">{text}</div>')
    else:
        return (f'<div style="background:{color};border:2.5px solid #111;padding:5px 10px;'
                f'border-radius:14px;font-size:{fs};color:#111;max-width:{mw};'
                f'line-height:1.5;font-weight:600;">{text}</div>')


def sfx(text: str, color: str = "#FF6B35", size: str = "1.6rem",
        rot: int = -8) -> str:
    return (f'<div style="font-size:{size};font-weight:900;font-style:italic;'
            f'color:{color};-webkit-text-stroke:2px #111;text-shadow:3px 3px 0 #111;'
            f'transform:rotate({rot}deg);display:inline-block;line-height:1;">{text}</div>')


def pnl(content: str, bg: str = "#fff", flex: str = "1",
        extra: str = "") -> str:
    return (f'<div style="background:{bg};border:3.5px solid #111;padding:8px 6px;'
            f'flex:{flex};display:flex;flex-direction:column;'
            f'align-items:center;justify-content:center;gap:5px;'
            f'box-sizing:border-box;{extra}">{content}</div>')


def row(*panels: str, flex: str = "1") -> str:
    inner = "".join(panels)
    return f'<div style="display:flex;gap:3px;">{inner}</div>'


def pg(pid: int, title_bg: str, title_text: str, body: str,
       sub: str = "") -> str:
    display = "flex" if pid == 0 else "none"
    return f"""<div class="manga-page" id="page-{pid}" style="display:{display};">
  <div style="background:#111;color:#fff;font-size:0.75rem;font-weight:900;
              letter-spacing:3px;text-align:center;padding:5px 8px;
              border-bottom:3px solid {title_bg};flex-shrink:0;">
    {title_text}
  </div>
  <div style="display:flex;flex-direction:column;gap:3px;padding:3px;">
    {body}
  </div>
  <div style="text-align:right;font-size:0.6rem;color:#888;
              padding:2px 6px;background:#fff;">
    {sub}
  </div>
</div>"""


# ── ページ定義 ───────────────────────────────────────────────────

def page0() -> str:   # 表紙
    body = f"""
  <div style="flex:1;min-height:0;background:linear-gradient(160deg,#fff9f0,#ffecd2);
              border:3.5px solid #111;display:flex;flex-direction:column;
              align-items:center;justify-content:center;gap:8px;padding:10px;overflow:hidden;">
    <div style="text-align:center;line-height:1.1;">
      <div style="font-size:2.2rem;font-weight:900;color:#111;letter-spacing:2px;">留学生</div>
      <div style="font-size:1.8rem;font-weight:900;color:#FF6B35;
                  -webkit-text-stroke:1px #111;letter-spacing:3px;">インタビュー</div>
      <div style="font-size:2.4rem;font-weight:900;color:#111;letter-spacing:2px;">大作戦！</div>
    </div>
    <div style="display:flex;gap:2px;align-items:flex-end;">
      {char('#FF6B35','🇮🇩','smile',40,64)}
      {char('#FF6B6B','🇨🇳','surprised',40,64)}
      {interviewer('excited',True,False,44,64)}
      {char('#4ECDC4','🇨🇳','laugh',40,64)}
      {char('#A8E6CF','🇨🇳','smile',40,64)}
    </div>
    <div style="background:#FFD700;border:3px solid #111;border-radius:10px;
                padding:6px 16px;font-size:0.78rem;font-weight:900;color:#111;text-align:center;">
      世界の声を届けろ！ウェルカムパーティ潜入取材<br>
      <span style="font-size:0.65rem;font-weight:600;">聞き取り・撮影：楠香谷</span>
    </div>
    <div style="font-size:1.2rem;letter-spacing:6px;">🇮🇩 🇨🇳 🇨🇳 🇨🇳 🇯🇵 🇯🇵</div>
  </div>"""
    return pg(0, "#FF6B35",
              "📖 広島大学 東千田キャンパス ／ 2026年4月28日",
              body, "── 表 紙 ──")


def page1() -> str:   # 第1話
    body = (
        row(
            pnl(f'''
              <div style="font-size:1rem;font-weight:900;color:#fff;text-align:center;
                          text-shadow:2px 2px 0 #111;line-height:1.2;">
                広島大学 東千田<br>ウェルカムパーティ！
              </div>
              <div style="font-size:1.4rem;letter-spacing:4px;">🌏🎉🌍</div>
              <div style="font-size:0.65rem;color:#ccc;letter-spacing:2px;">世界中から新入生が集まる日</div>
            ''', bg='linear-gradient(135deg,#1a1a2e,#16213e)', flex="2"),
            pnl(f'''
              {interviewer("excited", True, False, 44, 66)}
              {bub("いくぞ！<br>大作戦！","shout","#FFD700","0.78rem","130px")}
            ''', bg="#fffde7", flex="1"),
            flex="2"
        ) +
        row(
            pnl(f'''
              <div style="display:flex;gap:3px;align-items:flex-end;">
                {char('#FF6B35','🇮🇩','smile',38,60)}
                {char('#FF6B35','🇮🇩','smile',38,60)}
                {char('#FF6B35','🇮🇩','laugh',38,60)}
              </div>
              {bub("インドネシアから！","normal","#FFE4D0","0.72rem","140px")}
            ''', flex="1"),
            pnl(f'''
              <div style="display:flex;gap:2px;align-items:flex-end;">
                {char('#FF6B6B','🇨🇳','smile',38,60)}
                {char('#4ECDC4','🇨🇳','think',38,60)}
                {char('#A8E6CF','🇨🇳','laugh',38,60)}
              </div>
              {bub("中国から３人！","normal","#FFE4E4","0.72rem","130px")}
              {sfx("ワイワイ","#4ECDC4","1.2rem",-3)}
            ''', flex="1"),
            pnl(f'''
              {char('#DDA0DD','🇯🇵','smile',38,60)}
              {char('#F7DC6F','🇯🇵','smile',38,60)}
              {bub("法学部2年生！","normal","#F3E5F5","0.72rem","120px")}
            ''', flex="1"),
            flex="2"
        )
    )
    return pg(1, "#4ECDC4", "第１話 ── いざ、パーティへ！", body, "── 第１話 ──")


def page2() -> str:   # 第2話：インドネシア
    body = (
        row(
            pnl(f'''
              <div style="display:flex;gap:2px;align-items:flex-end;">
                {char('#FF6B35','🇮🇩','smile',40,64)}
                {char('#FF6B35','🇮🇩','smile',40,64)}
                {char('#FF6B35','🇮🇩','laugh',40,64)}
              </div>
              {sfx("ドドド","#FF6B35","1.4rem",-3)}
              {bub("★写真⭕が楠香谷。<br>インドネシア留学生の間","narr","#fff","0.68rem","160px")}
            ''', bg="#fff8f0", flex="2"),
            pnl(f'''
              {interviewer("excited", True, True, 44, 66)}
              {bub("出身地は<br>どちらですか？","shout","#FFD700","0.8rem","130px")}
            ''', flex="1"),
            flex="2"
        ) +
        row(
            pnl(f'''
              {char('#FF6B35','🇮🇩','smile',44,68)}
              {bub("スマトラでも<br>ジャワでも<br>ないですよ♪","normal","#FFE4D0","0.78rem","150px")}
            ''', flex="1"),
            pnl(f'''
              {interviewer("surprised", False, False, 44, 66)}
              {sfx("ガーン","#FF6B6B","1.8rem",-8)}
              {bub("え…！スマトラでも<br>ジャワでもない…？","think","#fff9c4","0.75rem","150px")}
            ''', bg="#fffde7", flex="1"),
            flex="2"
        ) +
        row(
            pnl(f'''
              {bub("知識不足で会話が続かなかった…","narr","","0.72rem","180px")}
              {sfx("シーン…","#888","1.2rem",3)}
            ''', bg="#f5f5f5", flex="2"),
            pnl(f'''
              {bub("反省！<br>出身地を事前に<br>調べるべきだった！","shout","#FFE4D0","0.75rem","140px")}
              {sfx("後悔","#FF6B35","1.4rem",-8)}
            ''', bg="#fff8f0", flex="1"),
            flex="1"
        )
    )
    return pg(2, "#FF6B35", "🇮🇩 第２話 ── インドネシア留学生３名との遭遇",
              body, "── 第２話：事前準備の重要性 ──")


def page3() -> str:   # 第3話：中国人A
    body = (
        row(
            pnl(f'''
              {char('#FF6B6B','🇨🇳','sweat',46,70)}
              {bub("日本語が弱くて<br>アルバイトが<br>心配です…","normal","#FFE4E4","0.78rem","155px")}
              {bub("SDS・ファイナンス専攻","narr","","0.65rem","150px")}
            ''', flex="2"),
            pnl(f'''
              {interviewer("think", True, True, 44, 66)}
              {bub("日本企業に<br>就職したいんですよね","normal","#FFF9C4","0.75rem","130px")}
            ''', flex="1"),
            flex="2"
        ) +
        row(
            pnl(f'''
              {interviewer("excited", True, False, 44, 66)}
              {bub("アントレプレナーって<br>知ってますか？","shout","#FFD700","0.8rem","150px")}
            ''', flex="1"),
            pnl(f'''
              {char('#FF6B6B','🇨🇳','confused',46,70)}
              {sfx("？？？","#4ECDC4","2rem",5)}
              {bub("…アントレ<br>プレナー…？","think","#FFE4E4","0.78rem","130px")}
            ''', bg="#fff0f0", flex="1"),
            flex="2"
        ) +
        row(
            pnl(f'''
              {bub("起業家精神という概念がなかなか通じなかった。<br>言語だけでなく文化的馴染みの差かも？","narr","","0.7rem","200px")}
            ''', bg="#fff9f0", flex="2"),
            pnl(f'''
              {char_run('#FF6B6B','🇨🇳',50,66)}
              {bub("授業が始まる！","shout","#FF6B6B","0.82rem","120px")}
              {sfx("ダッシュ！","#111","1.3rem",-10)}
            ''', flex="1"),
            flex="1"
        )
    )
    return pg(3, "#FF6B6B", "🇨🇳 第３話 ── アントレプレナーが通じない！",
              body, "── 第３話 ──")


def page4() -> str:   # 第4話：中国人B
    body = (
        row(
            pnl(f'''
              {char('#4ECDC4','🇨🇳','smile',46,70)}
              {bub("キヤノンに<br>就職したいです！","shout","#E0F7FA","0.85rem","155px")}
              {sfx("キラーン","#FFD700","1.3rem",-3)}
            ''', flex="1"),
            pnl(f'''
              {interviewer("surprised", True, True, 44, 66)}
              {bub("キヤノン…！中国撤退の<br>ニュースが出ていた頃なのに","think","#FFF9C4","0.72rem","150px")}
            ''', bg="#f9f9f9", flex="1"),
            flex="2"
        ) +
        row(
            pnl(f'''
              {char('#4ECDC4','🇨🇳','confused',42,66)}
              {bub("高校は理系でしたが<br>数学が苦手で…<br>組織論を専攻中","normal","#E0F7FA","0.75rem","160px")}
            ''', flex="2"),
            pnl(f'''
              {interviewer("think", False, True, 40, 62)}
              {bub("微分を使う経済学は<br>大変では？","normal","#FFF9C4","0.72rem","120px")}
            ''', flex="1"),
            flex="2"
        ) +
        row(
            pnl(f'''
              {char('#4ECDC4','🇨🇳','smile',42,66)}
              {bub("最初の半年は研究生として学んで<br>その後、本格入学できます！","normal","#E0F7FA","0.75rem","190px")}
              {bub("▶研究生制度（６ヶ月）を発見！","narr","","0.65rem","170px")}
            ''', flex="2"),
            pnl(f'''
              {char_run('#4ECDC4','🇨🇳',50,66)}
              {bub("また授業！","shout","#4ECDC4","0.8rem","110px")}
              {sfx("またか！","#FF6B35","1.2rem",-6)}
            ''', flex="1"),
            flex="1"
        )
    )
    return pg(4, "#4ECDC4", "🇨🇳 第４話 ── キヤノン志望と研究生制度の秘密",
              body, "── 第４話 ──")


def page5() -> str:   # 第5話：中国人C
    body = (
        row(
            pnl(f'''
              {char('#A8E6CF','🇨🇳','smile',46,70)}
              {bub("インフルエンサーによる<br>衝動購買の効果を<br>研究しています","normal","#DCEDC8","0.78rem","175px")}
              {bub("その日は授業がなく<br>ゆっくりしていた","narr","","0.65rem","150px")}
            ''', flex="2"),
            pnl(f'''
              {sfx("ユルい日","#A8E6CF","1.3rem",3)}
              {interviewer("think", True, True, 44, 66)}
              {bub("珍しい！<br>ゆっくり話せる！","think","#FFF9C4","0.72rem","120px")}
            ''', bg="#f0fff4", flex="1"),
            flex="2"
        ) +
        row(
            pnl(f'''
              {interviewer("excited", True, False, 44, 66)}
              {bub("フォロワー数は<br>何人ですか！？","shout","#FFD700","0.85rem","145px")}
            ''', flex="1"),
            pnl(f'''
              {char('#A8E6CF','🇨🇳','confused',46,70)}
              {sfx("え？？","#FF6B35","2rem",5)}
              {bub("私はインフルエンサー<br>じゃなく研究者です","normal","#DCEDC8","0.75rem","155px")}
            ''', bg="#f0fff4", flex="2"),
            flex="2"
        ) +
        row(
            pnl(f'''
              <div style="display:flex;gap:4px;align-items:flex-end;">
                {interviewer("surprised", True, False, 40, 62)}
                {char('#A8E6CF','🇨🇳','laugh',40,62)}
              </div>
              {sfx("ドッ！","#FFD700","1.6rem",-4)}
              {bub("笑いが生まれた！","shout","#FFF9C4","0.75rem","140px")}
            ''', flex="2"),
            pnl(f'''
              <div style="font-size:1.8rem;">📸</div>
              {sfx("パシャ！","#4ECDC4","1.4rem",-6)}
              {bub("唯一の<br>撮影成功！","normal","#DCEDC8","0.72rem","110px")}
            ''', bg="#f0fff4", flex="1"),
            flex="1"
        )
    )
    return pg(5, "#A8E6CF", "🇨🇳 第５話 ── 笑いが生まれた瞬間",
              body, "── 第５話 ──")


def page6() -> str:   # 最終話
    body = (
        row(
            pnl(f'''
              <div style="display:flex;gap:3px;align-items:flex-end;">
                {char('#DDA0DD','🇯🇵','smile',42,66)}
                {char('#F7DC6F','🇯🇵','smile',42,66)}
              </div>
              {bub("法学部昼間主2年生。<br>広島出身と関西出身。","narr","","0.7rem","170px")}
            ''', flex="1"),
            pnl(f'''
              {char('#DDA0DD','🇯🇵','excited',44,68)}
              {bub("オンライン授業で<br>東千田だけに<br>通えます！","shout","#F3E5F5","0.82rem","150px")}
              {sfx("ナント！","#DDA0DD","1.3rem",-5)}
            ''', flex="2"),
            flex="2"
        ) +
        row(
            pnl(f'''
              {interviewer("surprised", False, True, 44, 66)}
              {bub("東広島に<br>行かなくて<br>いいの！？","think","#FFF9C4","0.8rem","130px")}
            ''', flex="1"),
            pnl(f'''
              {char('#F7DC6F','🇯🇵','smile',44,68)}
              {bub("関西出身でも<br>東千田だけで<br>OK！","normal","#FFFDE7","0.8rem","130px")}
              {bub("都市型キャンパスの強み","narr","","0.65rem","130px")}
            ''', flex="1"),
            flex="2"
        ) +
        row(
            pnl(f'''
              {interviewer("reflect", True, False, 40, 62)}
              {bub("反省①出身地を事前調査<br>反省②概念は例で伝える<br>反省③授業のない時間を狙う","narr","","0.7rem","190px")}
            ''', bg="#fffde7", flex="1"),
            pnl(f'''
              {interviewer("determined", True, False, 44, 66)}
              {bub("次回こそ<br>完璧な準備で！","shout","#FFD700","0.85rem","130px")}
              {sfx("ガッ！","#FF6B35","2rem",-8)}
              <div style="font-size:0.75rem;font-weight:900;color:#111;">── 完 ──</div>
            ''', bg="#fff8f0", flex="1"),
            flex="1"
        )
    )
    return pg(6, "#DDA0DD", "🇯🇵 最終話 ── 日本人学生＆次回予告",
              body, "── 最終話 ──")


# ── メインHTML組み立て ───────────────────────────────────────────

TITLES = [
    "表紙 — 留学生インタビュー大作戦！",
    "第１話 — いざ、パーティへ！",
    "第２話 — インドネシア留学生との遭遇",
    "第３話 — アントレプレナーが通じない！",
    "第４話 — キヤノン志望と研究生制度",
    "第５話 — 笑いが生まれた瞬間",
    "最終話 — 日本人学生＆次回予告",
]
TOTAL = 7


def build_manga_html() -> str:
    pages_html = (page0() + page1() + page2() +
                  page3() + page4() + page5() + page6())

    titles_js = str(TITLES).replace("'", '"')

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap');
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

html, body {{
    height: 100%;
    overflow: hidden;
    font-family: 'Noto Sans JP', 'Hiragino Kaku Gothic Pro', sans-serif;
    background: #1a1a1a;
    display: flex;
    flex-direction: column;
}}

/* ── ナビバー ── */
#nav-bar {{
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    background: #111;
    padding: 6px 10px;
    border-bottom: 3px solid #FF6B35;
}}
.nav-btn {{
    background: #FF6B35;
    border: 2.5px solid #fff;
    border-radius: 5px;
    color: #fff;
    font-size: 0.85rem;
    font-weight: 900;
    padding: 5px 16px;
    cursor: pointer;
    letter-spacing: 2px;
    transition: background 0.15s, transform 0.1s;
}}
.nav-btn:hover  {{ background: #FFD700; color: #111; transform: scale(1.05); }}
.nav-btn:disabled {{ background: #444; cursor: default; transform: none; }}
#page-info {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1px;
    min-width: 170px;
}}
#page-counter {{
    color: #FFD700;
    font-weight: 900;
    font-size: 0.9rem;
    letter-spacing: 3px;
    font-family: monospace;
}}
#page-title {{
    color: #aaa;
    font-size: 0.62rem;
    letter-spacing: 1px;
    text-align: center;
}}

/* ── ページエリア ── */
#page-area {{
    flex: 1;
    min-height: 0;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding: 3px;
    overflow-y: auto;
    overflow-x: hidden;
}}
#page-area::-webkit-scrollbar {{ width: 5px; }}
#page-area::-webkit-scrollbar-track {{ background: #222; }}
#page-area::-webkit-scrollbar-thumb {{ background: #FF6B35; border-radius: 4px; }}

/* ── 各漫画ページ ── */
.manga-page {{
    width: 100%;
    max-width: 700px;
    display: flex;
    flex-direction: column;
    background: #fff;
    border: 4px solid #111;
    overflow: visible;
    box-shadow: 0 6px 24px rgba(0,0,0,0.6);
    flex-shrink: 0;
}}
</style>
</head>
<body>

<div id="nav-bar">
  <button class="nav-btn" id="btn-prev" onclick="prevPage()" disabled>◀ 前</button>
  <div id="page-info">
    <div id="page-counter">1 / {TOTAL}</div>
    <div id="page-title">{TITLES[0]}</div>
  </div>
  <button class="nav-btn" id="btn-next" onclick="nextPage()">次 ▶</button>
</div>

<div id="page-area">
  {pages_html}
</div>

<script>
const TITLES = {titles_js};
let cur = 0;
const total = {TOTAL};

function showPage(n) {{
  document.querySelectorAll('.manga-page').forEach((p, i) => {{
    p.style.display = (i === n) ? 'flex' : 'none';
  }});
  document.getElementById('page-counter').textContent = (n + 1) + ' / ' + total;
  document.getElementById('page-title').textContent = TITLES[n];
  document.getElementById('btn-prev').disabled = (n === 0);
  document.getElementById('btn-next').disabled = (n === total - 1);
  document.getElementById('page-area').scrollTop = 0;
  cur = n;
}}

function nextPage() {{ if (cur < total - 1) showPage(cur + 1); }}
function prevPage() {{ if (cur > 0) showPage(cur - 1); }}

document.addEventListener('keydown', e => {{
  if (e.key === 'ArrowRight' || e.key === 'ArrowDown') nextPage();
  if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')  prevPage();
}});

let tx = 0;
document.addEventListener('touchstart', e => {{ tx = e.touches[0].clientX; }});
document.addEventListener('touchend', e => {{
  const dx = e.changedTouches[0].clientX - tx;
  if (Math.abs(dx) > 50) {{ dx < 0 ? nextPage() : prevPage(); }}
}});

showPage(0);
</script>
</body>
</html>"""


# ── Streamlit ────────────────────────────────────────────────────

components.html(build_manga_html(), height=740, scrolling=False)
