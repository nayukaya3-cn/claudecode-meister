import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="中小企業リスクマネジメント・ダッシュボード",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CSS ────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;700;900&display=swap');

html, body, [class*="css"] { font-family: 'Noto Sans JP', sans-serif; }

.hero {
    background: linear-gradient(135deg, #0f4c75 0%, #1b6ca8 50%, #118ab2 100%);
    color: white; padding: 2.5rem 2rem; border-radius: 16px;
    margin-bottom: 2rem; text-align: center;
    box-shadow: 0 8px 32px rgba(17,138,178,0.3);
}
.hero h1 { font-size: 2.4rem; font-weight: 900; margin: 0 0 0.5rem 0; }
.hero p  { font-size: 1.15rem; opacity: 0.9; margin: 0; }

.alert-banner {
    background: linear-gradient(135deg, #c0392b, #e74c3c);
    color: white; padding: 1.5rem 2rem; border-radius: 12px; margin: 1rem 0;
    border-left: 6px solid #922b21;
}
.alert-banner h3 { margin: 0 0 0.5rem 0; }
.alert-banner p  { margin: 0.3rem 0; font-size: 1.05rem; }

.kpi-card {
    background: white; border: none; border-radius: 14px;
    padding: 1.5rem; text-align: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    border-top: 4px solid #1b6ca8;
}
.kpi-card .kpi-num  { font-size: 2.2rem; font-weight: 900; color: #1b6ca8; }
.kpi-card .kpi-unit { font-size: 1rem;   font-weight: 700; color: #1b6ca8; }
.kpi-card .kpi-lbl  { font-size: 0.82rem; color: #555; margin-top: 0.4rem; line-height:1.4; }

.kpi-card-red  { border-top-color: #e74c3c; }
.kpi-card-red  .kpi-num, .kpi-card-red  .kpi-unit { color: #c0392b; }
.kpi-card-grn  { border-top-color: #27ae60; }
.kpi-card-grn  .kpi-num, .kpi-card-grn  .kpi-unit { color: #1e8449; }
.kpi-card-ora  { border-top-color: #e67e22; }
.kpi-card-ora  .kpi-num, .kpi-card-ora  .kpi-unit { color: #d35400; }

.section-title {
    background: linear-gradient(90deg, #0f4c75, #1b6ca8);
    color: white; padding: 0.6rem 1.4rem; border-radius: 8px;
    font-size: 1.2rem; font-weight: 700; margin: 2rem 0 1rem 0;
    display: inline-block;
}

.insight-box {
    background: linear-gradient(135deg, #eaf4fb, #d6eaf8);
    border: 2px solid #1b6ca8; border-radius: 12px;
    padding: 1.2rem 1.5rem; margin: 1rem 0;
}
.insight-box h4 { color: #0f4c75; margin: 0 0 0.5rem 0; }

.case-card {
    background: #1a1a2e; color: white;
    border-radius: 12px; padding: 1.5rem; margin: 1rem 0;
}
.case-card h4 { color: #f39c12; margin: 0 0 0.8rem 0; font-size: 1.1rem; }

.risk-tag-high   { background:#fdecea; color:#c62828; border:1px solid #ef9a9a;
                   border-radius:6px; padding:0.2rem 0.6rem; font-size:0.8rem; font-weight:700; }
.risk-tag-mid    { background:#fff8e1; color:#e65100; border:1px solid #ffcc02;
                   border-radius:6px; padding:0.2rem 0.6rem; font-size:0.8rem; font-weight:700; }
.risk-tag-low    { background:#e8f5e9; color:#2e7d32; border:1px solid #a5d6a7;
                   border-radius:6px; padding:0.2rem 0.6rem; font-size:0.8rem; font-weight:700; }

.result-score {
    font-size: 3rem; font-weight: 900; text-align: center; padding: 1.5rem;
    border-radius: 12px; margin: 1rem 0;
}

.roadmap-step {
    background: white; border-left: 5px solid #1b6ca8;
    border-radius: 0 10px 10px 0; padding: 1rem 1.5rem; margin: 0.8rem 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.roadmap-step h4 { margin: 0 0 0.3rem 0; color: #0f4c75; }
.roadmap-step p  { margin: 0; color: #555; font-size: 0.9rem; }

.seminar-card {
    background: linear-gradient(135deg, #f8f9fa, #e9ecef);
    border: 1px solid #dee2e6; border-radius: 12px;
    padding: 1.2rem 1.5rem; margin: 0.8rem 0;
}
.seminar-card h4 { color: #0f4c75; margin: 0 0 0.4rem 0; }
</style>
""", unsafe_allow_html=True)

# ─── SIDEBAR ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🛡️ リスクマネジメント研究会")
    st.caption("（一社）広島県中小企業診断協会")
    st.divider()
    page = st.radio(
        "メニュー",
        [
            "🏠 ホーム・概要",
            "🔍 リスク自己診断",
            "📊 被害データ・統計",
            "⚔️ リスク対応マトリクス",
            "💰 保険vs貯蓄シミュレーター",
            "📰 事例研究",
            "🗺️ 対応策ロードマップ",
            "🏆 研究会の実績",
        ],
        label_visibility="collapsed",
    )
    st.divider()
    st.caption("代表：三村雅彦\n中小企業診断士 / 損保専門家\n©2026 リスクマネジメント研究会")

# ════════════════════════════════════════════════════════════════════════════
# PAGE 1 ── ホーム・概要
# ════════════════════════════════════════════════════════════════════════════
if page == "🏠 ホーム・概要":
    st.markdown("""
    <div class="hero">
        <h1>🛡️ 中小企業のためのリスクマネジメント</h1>
        <p>「備えあれば憂いなし」—— あなたの会社は、明日の危機に備えていますか？</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="alert-banner">
        <h3>⚠️ 衝撃の事実：2018年西日本豪雨</h3>
        <p>経済損失 <strong>1兆1,580億円</strong> のうち、保険でカバーされたのはわずか <strong>2,000億円（約17%）</strong></p>
        <p>残り <strong>約9,580億円（83%）</strong> は、中小企業が自力で負担するしかありませんでした。</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    kpis = [
        ("50", "%", "被災中小企業のうち<br>営業停止に追い込まれた割合", "kpi-card-red"),
        ("83", "%", "2018年豪雨損失のうち<br>保険でカバーされなかった割合", "kpi-card-red"),
        ("57", "兆円", "中小企業向け損保<br>潜在市場規模（未開拓）", "kpi-card-grn"),
        ("1,000", "万円未満", "被災中小企業の<br>物的損害の中央値", "kpi-card-ora"),
    ]
    for col, (num, unit, lbl, cls) in zip([c1, c2, c3, c4], kpis):
        col.markdown(f"""
        <div class="kpi-card {cls}">
            <div><span class="kpi-num">{num}</span><span class="kpi-unit">{unit}</span></div>
            <div class="kpi-lbl">{lbl}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── リスクマネジメントとは ──
    st.markdown('<div class="section-title">📚 リスクマネジメントとは</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([3, 2])

    with c1:
        st.markdown("""
        <div class="insight-box">
            <h4>企業が永続・成長するために欠かせない視点</h4>
            <p>企業は営利を目的とする中で、社会への寄与や発展への貢献などの社会的責任を果たさなければ、<strong>永続・成長できません。</strong></p>
            <p>環境変化や不確定な事象（＝リスク）に対応し、損失の回避・低減を図ることが、企業価値を維持・増大させる鍵です。</p>
            <hr style="border-color:#1b6ca8; margin: 0.8rem 0;">
            <p style="font-size:0.9rem;"><strong>リスクマネジメント（広義）の3要素：</strong></p>
            <table style="width:100%; font-size:0.88rem; border-collapse:collapse;">
                <tr style="background:#d6eaf8;">
                    <td style="padding:6px 10px; font-weight:700; color:#0f4c75;">① リスクマネジメント（狭義）</td>
                    <td style="padding:6px 10px;">予防・抑制を中心とした<strong>事前の対策</strong></td>
                </tr>
                <tr style="background:#ffeeba;">
                    <td style="padding:6px 10px; font-weight:700; color:#856404;">② 危機管理</td>
                    <td style="padding:6px 10px;">重大リスク発現時の<strong>迅速な初期対応</strong></td>
                </tr>
                <tr style="background:#f8d7da;">
                    <td style="padding:6px 10px; font-weight:700; color:#721c24;">③ 事業継続計画（BCP）</td>
                    <td style="padding:6px 10px;">発生後に速やかに復旧し<strong>事業を再開させる行動計画</strong></td>
                </tr>
            </table>
            <p style="font-size:0.78rem; color:#666; margin-top:0.8rem;">（中小企業庁HPより）</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        # RM Timeline
        fig = go.Figure()
        x = [0, 1, 2, 2, 3, 5]
        y = [3, 3, 3, 0, 0.5, 3]
        fig.add_trace(go.Scatter(
            x=x, y=y, mode='lines',
            line=dict(color='#ccc', width=3), showlegend=False
        ))
        # Phase backgrounds
        fig.add_vrect(x0=0, x1=2, fillcolor="#d6eaf8", opacity=0.4, line_width=0)
        fig.add_vrect(x0=2, x1=3, fillcolor="#fdecea", opacity=0.4, line_width=0)
        fig.add_vrect(x0=3, x1=5, fillcolor="#eafaf1", opacity=0.4, line_width=0)
        # Annotations
        for (xi, yi, txt, col) in [
            (1,   3.4, "①事前対策",   "#1b6ca8"),
            (2.5, 0.8, "②初期対応",   "#c0392b"),
            (4,   3.4, "③BCP・復旧",  "#27ae60"),
            (2,   1.5, "⚡事故発生",   "#e74c3c"),
        ]:
            fig.add_annotation(x=xi, y=yi, text=f"<b>{txt}</b>",
                               showarrow=False, font=dict(size=13, color=col))
        fig.add_trace(go.Scatter(
            x=[2], y=[0], mode='markers',
            marker=dict(size=16, color='#e74c3c', symbol='star'),
            showlegend=False
        ))
        fig.update_layout(
            title=dict(text="リスクマネジメントのフロー", font=dict(size=13)),
            height=260,
            xaxis=dict(showticklabels=False, showgrid=False, range=[-0.2, 5.2]),
            yaxis=dict(showticklabels=False, showgrid=False, range=[-0.5, 4]),
            plot_bgcolor='white', margin=dict(l=0, r=0, t=35, b=0),
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("""
        <div style="background:#fff3cd; padding:0.8rem; border-radius:8px; font-size:0.9rem;">
        💡 <strong>ポイント：</strong>「事故が起きてから考える」では遅い。<br>
        事前の備えが企業存続を左右します。
        </div>
        """, unsafe_allow_html=True)

    # ── リスク全体像 ──
    st.markdown('<div class="section-title">⚡ 企業を取り巻くリスクの全体像</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("純粋リスク（損失のみ発生）")
        data = {
            "リスク": ["地震・台風", "情報漏洩", "火災", "労働災害",
                       "システムダウン", "不正行為", "製造物責任", "物流停止", "交通事故"],
            "深刻度": [9, 8, 8, 7, 7, 7, 6, 6, 5]
        }
        df = pd.DataFrame(data)
        colors = ["#c0392b" if v >= 9 else "#e67e22" if v >= 7 else "#27ae60"
                  for v in df["深刻度"]]
        fig = go.Figure(go.Bar(
            x=df["深刻度"], y=df["リスク"], orientation='h',
            marker_color=colors,
            text=[f"{v}/10" for v in df["深刻度"]], textposition='outside'
        ))
        fig.update_layout(height=320, xaxis=dict(range=[0, 12]),
                          plot_bgcolor='white', margin=dict(l=0, r=50, t=5, b=0))
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.subheader("投機的リスク（近年急拡大）")
        data2 = {
            "リスク": ["財務リスク\n(貸倒・資金繰り)", "人事・労務リスク\n(雇用・財務流出)",
                       "経営・戦略リスク\n(製品開発失敗)", "社会・政治リスク\n(法制度改正)",
                       "市場リスク\n(競争激化)", "経済リスク\n(為替・金利)"],
            "影響度": [9, 8, 8, 7, 7, 6]
        }
        df2 = pd.DataFrame(data2)
        colors2 = ["#8e1a0e" if v >= 9 else "#c0392b" if v >= 8
                   else "#e67e22" if v >= 7 else "#f39c12"
                   for v in df2["影響度"]]
        fig2 = go.Figure(go.Bar(
            x=df2["影響度"], y=df2["リスク"], orientation='h',
            marker_color=colors2,
            text=[f"{v}/10" for v in df2["影響度"]], textposition='outside'
        ))
        fig2.update_layout(height=320, xaxis=dict(range=[0, 12]),
                           plot_bgcolor='white', margin=dict(l=0, r=50, t=5, b=0))
        st.plotly_chart(fig2, use_container_width=True)

    st.info("👈 左のメニューから「リスク自己診断」へ進んで、自社のリスクスコアを計算してください。")


# ════════════════════════════════════════════════════════════════════════════
# PAGE 2 ── リスク自己診断
# ════════════════════════════════════════════════════════════════════════════
elif page == "🔍 リスク自己診断":
    st.markdown('<div class="hero" style="padding:1.5rem;"><h1 style="font-size:1.8rem;">🔍 リスク自己診断ツール</h1><p>以下の質問に答えて、自社のリスクスコアを把握しましょう</p></div>', unsafe_allow_html=True)

    with st.form("risk_form"):
        st.subheader("① 基本情報")
        c1, c2, c3 = st.columns(3)
        industry = c1.selectbox("業種", ["製造業", "建設業", "卸・小売業", "飲食・宿泊業",
                                         "情報通信業", "運輸・物流業", "医療・福祉", "その他サービス業"])
        employees = c2.selectbox("従業員数", ["5人未満", "5〜20人", "21〜50人",
                                              "51〜100人", "101〜300人", "300人以上"])
        location = c3.selectbox("事業所の地域", ["北海道・東北", "関東", "中部", "近畿",
                                                  "中国・四国", "九州・沖縄"])

        st.subheader("② リスク対策の現状（各項目をチェック）")
        c1, c2 = st.columns(2)
        with c1:
            has_bcp = st.checkbox("事業継続計画（BCP）を策定している")
            has_profit_ins = st.checkbox("利益補償型保険に加入している")
            has_fire_ins = st.checkbox("火災保険・地震保険に加入している")
            has_cyber_ins = st.checkbox("サイバーリスク保険に加入している")
            has_pl_ins = st.checkbox("製造物責任保険（PL保険）に加入している")
        with c2:
            has_cyber_sec = st.checkbox("サイバーセキュリティ対策を実施している（EDR/WAF等）")
            has_risk_training = st.checkbox("従業員向けリスク教育を定期実施している")
            has_supplier_alt = st.checkbox("主要仕入先の代替先を確保している")
            has_cashflow = st.checkbox("3ヶ月以上の運転資金を手元に確保している")
            has_legal = st.checkbox("労務・法務の専門家と顧問契約を締結している")

        st.subheader("③ リスク経験")
        c1, c2 = st.columns(2)
        past_disaster = c1.checkbox("過去5年間に自然災害の被害を受けたことがある")
        past_cyber = c2.checkbox("過去3年間にサイバー攻撃・情報漏洩を経験したことがある")
        past_labor = c1.checkbox("過去3年間に労務トラブル（ハラスメント等）があった")
        single_client = c2.checkbox("売上の50%以上が1社の取引先に依存している")

        submitted = st.form_submit_button("🔍 診断結果を見る", use_container_width=True)

    if submitted:
        # Score calculation
        checks = [has_bcp, has_profit_ins, has_fire_ins, has_cyber_ins, has_pl_ins,
                  has_cyber_sec, has_risk_training, has_supplier_alt, has_cashflow, has_legal]
        risk_factors = [past_disaster, past_cyber, past_labor, single_client]
        base_score = sum(checks) * 10
        risk_penalty = sum(risk_factors) * 8
        emp_bonus = {"5人未満": -5, "5〜20人": -3, "21〜50人": 0,
                     "51〜100人": 2, "101〜300人": 4, "300人以上": 8}[employees]
        total = max(0, min(100, base_score - risk_penalty + emp_bonus))

        if total >= 70:
            level, color, msg = "優良", "#27ae60", "リスク管理体制が整っています。継続的な見直しを行いましょう。"
        elif total >= 40:
            level, color, msg = "要改善", "#e67e22", "部分的な対策は取れています。重要な穴を塞ぎましょう。"
        else:
            level, color, msg = "要緊急対策", "#c0392b", "重大なリスクにさらされています。早急な対策が必要です。"

        st.markdown(f"""
        <div class="result-score" style="background:{color}20; border:3px solid {color}; color:{color};">
            リスク対策スコア：{total} / 100点<br>
            <span style="font-size:1.4rem;">{level}</span>
        </div>
        <div class="insight-box"><h4>{msg}</h4></div>
        """, unsafe_allow_html=True)

        # Radar chart
        categories = ["BCP・事業継続", "損害保険", "サイバー対策", "人材・労務", "資金・財務"]
        bcp_s = (has_bcp * 50 + has_supplier_alt * 30 + has_cashflow * 20)
        ins_s  = (has_profit_ins * 35 + has_fire_ins * 35 + has_cyber_ins * 15 + has_pl_ins * 15)
        cyber_s = (has_cyber_sec * 60 + has_risk_training * 40)
        labor_s = (has_legal * 50 + has_risk_training * 30 + (not has_bcp) * 0 + 20)
        fin_s   = (has_cashflow * 60 + has_profit_ins * 40)
        values = [bcp_s, ins_s, cyber_s, labor_s, fin_s]

        fig = go.Figure(go.Scatterpolar(
            r=values + [values[0]],
            theta=categories + [categories[0]],
            fill='toself', fillcolor='rgba(27,108,168,0.2)',
            line=dict(color='#1b6ca8', width=2),
            name="現在のスコア"
        ))
        fig.add_trace(go.Scatterpolar(
            r=[100, 100, 100, 100, 100, 100],
            theta=categories + [categories[0]],
            fill='toself', fillcolor='rgba(0,0,0,0.03)',
            line=dict(color='#ccc', width=1, dash='dot'),
            name="目標スコア"
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True, height=380,
            title="リスク対策レーダーチャート"
        )
        st.plotly_chart(fig, use_container_width=True)

        # Priority recommendations
        st.subheader("🎯 優先すべき対策")
        recs = []
        if not has_profit_ins:
            recs.append(("🔴 緊急", "利益補償型保険への加入",
                         "被災時に操業せざるを得ない状況を防ぐ最重要対策。西日本豪雨で多くの中小企業が無保険で操業継続を余儀なくされました。"))
        if not has_bcp:
            recs.append(("🔴 緊急", "BCP（事業継続計画）の策定",
                         "災害後の復旧手順を事前に決めておくことで、被害を最小化できます。"))
        if not has_fire_ins:
            recs.append(("🟠 重要", "火災保険・地震保険の見直し",
                         "補償内容が不十分なケースが多いため、専門家による保険診断を推奨します。"))
        if not has_cyber_sec:
            recs.append(("🟠 重要", "サイバーセキュリティ対策",
                         "中小企業へのサイバー攻撃は急増中。基本的なセキュリティ対策から始めましょう。"))
        if not has_risk_training:
            recs.append(("🟡 推奨", "従業員向けリスク教育の実施",
                         "最大のリスク源は「人」。定期的な教育・訓練が事故防止に直結します。"))
        if not recs:
            recs.append(("🟢 維持", "現在の対策を継続・定期見直し",
                         "良好な対策状況です。年1回の保険内容・BCP見直しを習慣化しましょう。"))

        for tag, title, desc in recs:
            st.markdown(f"""
            <div class="roadmap-step">
                <h4>{tag} {title}</h4>
                <p>{desc}</p>
            </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# PAGE 3 ── 被害データ・統計
# ════════════════════════════════════════════════════════════════════════════
elif page == "📊 被害データ・統計":
    st.markdown('<div class="hero" style="padding:1.5rem;"><h1 style="font-size:1.8rem;">📊 データで見る中小企業の被害実態</h1><p>2019年度 中小企業白書・三菱UFJリサーチ&コンサルティング調査より</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">💥 被災時の物的損害額（災害別）</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="insight-box">
        <h4>中小企業はリスクを「実感」している</h4>
        <p>被災した中小企業のうち、<strong>物的損害が1,000万円未満の企業が半数以上</strong>を占めます。「大きな災害でないと損害は少ない」という思い込みは危険です。</p>
    </div>
    """, unsafe_allow_html=True)

    damage_data = pd.DataFrame({
        "損害額区分": ["0円", "1〜50万円未満", "50〜100万円未満",
                       "100〜500万円未満", "500〜1,000万円未満",
                       "1,000〜3,000万円未満", "3,000〜5,000万円未満",
                       "5,000万〜1億円未満", "1億円超"],
        "西日本豪雨\n(n=158)": [2.5, 19.6, 13.3, 24.7, 12.0, 10.8, 5.1, 2.5, 9.5],
        "熊本地震\n(n=108)":   [13.9, 5.6, 19.4, 11.1, 17.6, 7.4, 12.0, 0, 13.0],
        "東日本大震災\n(n=789)": [0.8, 10.5, 13.2, 21.8, 16.5, 12.9, 6.1, 6.1, 12.2],
        "その他の災害\n(n=267)": [0.4, 12.7, 11.6, 34.5, 13.9, 15.7, 3.7, 3.4, 4.1],
    })

    disasters = ["西日本豪雨\n(n=158)", "熊本地震\n(n=108)", "東日本大震災\n(n=789)", "その他の災害\n(n=267)"]
    selected = st.multiselect("表示する災害を選択", disasters, default=disasters)

    colors_d = ["#e74c3c", "#e67e22", "#3498db", "#9b59b6"]
    fig = go.Figure()
    for i, d in enumerate(disasters):
        if d in selected:
            fig.add_trace(go.Bar(
                name=d.replace("\n", " "),
                x=damage_data["損害額区分"],
                y=damage_data[d],
                marker_color=colors_d[i],
            ))
    fig.update_layout(
        barmode='group', height=420,
        xaxis_title="物的損害額", yaxis_title="割合（%）",
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#eee'),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    )
    fig.add_shape(type='line', x0=-0.5, x1=4.5, y0=0, y1=0,
                  line=dict(color='black', width=1))
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.markdown('<div class="section-title">⏱️ 従業員規模別 営業停止期間</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="alert-banner">
        <h3>🔴 注目：約50%が「営業停止せず」の真実</h3>
        <p>表面上は「営業継続できた」ように見えますが——</p>
        <p><strong>実態：利益補償型保険に加入していなかったため、「操業せざるを得なかった」のではないか？</strong></p>
        <p>保険へのアクセスをスムーズにすれば、中小企業支援・地域創生につながる可能性があります。</p>
    </div>
    """, unsafe_allow_html=True)

    stoppage_data = pd.DataFrame({
        "規模": ["21〜30人\n(n=581)", "31〜50人\n(n=707)", "51〜100人\n(n=611)", "101〜300人\n(n=292)"],
        "営業停止せず": [50.4, 50.2, 48.3, 49.3],
        "1日": [0, 7.2, 4.0, 5.6, ],
        "2〜3日": [7.2, 4.0, 5.6, 7.9],
        "1週間以内": [11.0, 10.9, 12.1, 10.6],
        "1ヶ月以内": [15.1, 13.3, 12.6, 10.3],
        "3ヶ月以内": [9.8, 12.4, 12.8, 11.0],
        "半年以内・それ以上": [2.4, 5.0, 4.4, 5.1],
    })

    # Fix data - recalculate to sum to 100
    stoppage_data2 = pd.DataFrame({
        "規模": ["21〜30人", "31〜50人", "51〜100人", "101〜300人"],
        "営業停止せず": [50.4, 50.2, 48.3, 49.3],
        "1週間以内": [18.2, 14.9, 17.7, 18.5],
        "1ヶ月以内": [15.1, 13.3, 12.6, 10.3],
        "3ヶ月以内": [9.8, 12.4, 12.8, 11.0],
        "長期（半年以上）": [6.5, 9.2, 8.6, 10.9],
    })

    stop_cols = ["営業停止せず", "1週間以内", "1ヶ月以内", "3ヶ月以内", "長期（半年以上）"]
    stop_colors = ["#27ae60", "#f39c12", "#e67e22", "#e74c3c", "#8e1a0e"]

    fig2 = go.Figure()
    for col, color in zip(stop_cols, stop_colors):
        fig2.add_trace(go.Bar(
            name=col, x=stoppage_data2["規模"], y=stoppage_data2[col],
            marker_color=color,
            text=[f"{v:.0f}%" for v in stoppage_data2[col]],
            textposition='inside', textfont=dict(color='white', size=11),
        ))
    fig2.update_layout(
        barmode='stack', height=380, plot_bgcolor='white',
        yaxis=dict(title="割合（%）", gridcolor='#eee'),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    st.markdown('<div class="section-title">🛠️ 復興時に活用したもの（企業規模別）</div>', unsafe_allow_html=True)
    recovery_data = pd.DataFrame({
        "手段": ["損害保険", "民間金融機関\nからの貸付", "国・自治体の補助金",
                  "公的金融機関\nからの貸付", "損保以外\n（その他）"],
        "21〜50人": [34.1, 18.6, 15.6, 11.7, 34.9],
        "51〜100人": [30.7, 14.9, 13.7, 11.1, 33.1],
        "101〜300人": [25.5, 13.9, 13.7, 10.5, 36.3],
    })

    fig3 = go.Figure()
    for col, color in zip(["21〜50人", "51〜100人", "101〜300人"],
                           ["#1b6ca8", "#118ab2", "#06d6a0"]):
        fig3.add_trace(go.Bar(
            name=col, x=recovery_data["手段"], y=recovery_data[col],
            marker_color=color,
        ))
    fig3.update_layout(
        barmode='group', height=380, plot_bgcolor='white',
        yaxis=dict(title="活用した割合（%）", gridcolor='#eee'),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("""
    <div class="insight-box">
        <h4>💡 重要な示唆：損害保険が最大の復興手段</h4>
        <p>規模を問わず、復興時に最も活用されたのは<strong>損害保険</strong>です。しかし活用率は高くても30〜34%程度。
        残りの70%近くは保険なしで復興に臨んでいます。</p>
        <p><strong>⇒ 保険への適切なアクセスが、中小企業の生存率を大きく左右します。</strong></p>
    </div>
    """, unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# PAGE 4 ── リスク対応マトリクス
# ════════════════════════════════════════════════════════════════════════════
elif page == "⚔️ リスク対応マトリクス":
    st.markdown('<div class="hero" style="padding:1.5rem;"><h1 style="font-size:1.8rem;">⚔️ リスク対応マトリクス</h1><p>頻度と損失規模から、最適なリスク対応策を特定する</p></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box">
        <h4>リスクの評価軸：「発生頻度」と「損失規模」</h4>
        <p>リスクをこの2軸で評価することで、最適な対応策（回避・防止・保有・移転）が決まります。</p>
    </div>
    """, unsafe_allow_html=True)

    # Risk matrix data
    risks = [
        {"name": "地震・台風", "freq": 2, "loss": 9, "strategy": "移転（保険）", "color": "#c0392b"},
        {"name": "サイバー攻撃", "freq": 6, "loss": 8, "strategy": "防止・移転", "color": "#c0392b"},
        {"name": "火災", "freq": 2, "loss": 8, "strategy": "移転（保険）", "color": "#c0392b"},
        {"name": "情報漏洩", "freq": 5, "loss": 7, "strategy": "防止・移転", "color": "#e67e22"},
        {"name": "労働災害", "freq": 4, "loss": 7, "strategy": "防止・移転", "color": "#e67e22"},
        {"name": "製造物責任", "freq": 2, "loss": 8, "strategy": "移転（PL保険）", "color": "#c0392b"},
        {"name": "交通事故", "freq": 5, "loss": 5, "strategy": "防止・軽減", "color": "#e67e22"},
        {"name": "物流停止", "freq": 3, "loss": 6, "strategy": "防止・分散", "color": "#e67e22"},
        {"name": "パワハラ", "freq": 6, "loss": 6, "strategy": "防止・軽減", "color": "#e67e22"},
        {"name": "システムダウン", "freq": 4, "loss": 6, "strategy": "防止・軽減", "color": "#e67e22"},
        {"name": "不正行為", "freq": 3, "loss": 7, "strategy": "防止・移転", "color": "#e67e22"},
        {"name": "貸し倒れ", "freq": 3, "loss": 6, "strategy": "防止・保有", "color": "#e67e22"},
        {"name": "小さなミス", "freq": 8, "loss": 2, "strategy": "保有", "color": "#27ae60"},
        {"name": "軽微なクレーム", "freq": 7, "loss": 2, "strategy": "保有・防止", "color": "#27ae60"},
    ]

    # Interactive sliders to add custom risk
    st.subheader("自社のリスクを追加してみよう")
    c1, c2, c3 = st.columns([2, 2, 2])
    custom_name = c1.text_input("リスク名を入力", placeholder="例: 主要顧客の離反")
    custom_freq = c2.slider("発生頻度（低↔高）", 1, 10, 5)
    custom_loss = c3.slider("損失規模（小↔大）", 1, 10, 5)
    if custom_name:
        risks.append({"name": custom_name, "freq": custom_freq, "loss": custom_loss,
                      "strategy": "評価中", "color": "#8e44ad"})

    # Build quadrant chart
    fig = go.Figure()

    # Quadrant backgrounds
    fig.add_shape(type='rect', x0=5, x1=10.5, y0=5, y1=10.5,
                  fillcolor='rgba(231,76,60,0.12)', line_width=0)
    fig.add_shape(type='rect', x0=-0.5, x1=5, y0=5, y1=10.5,
                  fillcolor='rgba(230,126,34,0.12)', line_width=0)
    fig.add_shape(type='rect', x0=5, x1=10.5, y0=-0.5, y1=5,
                  fillcolor='rgba(52,152,219,0.12)', line_width=0)
    fig.add_shape(type='rect', x0=-0.5, x1=5, y0=-0.5, y1=5,
                  fillcolor='rgba(39,174,96,0.12)', line_width=0)

    # Quadrant labels
    for (x, y, txt) in [
        (7.5, 9.5, "①リスクの回避\n（高頻度・大損失）"),
        (2.5, 9.5, "④リスクの移転\n（低頻度・大損失）⇒保険"),
        (7.5, 2.5, "②リスクの防止・軽減\n（高頻度・小損失）"),
        (2.5, 2.5, "③リスクの保有\n（低頻度・小損失）"),
    ]:
        fig.add_annotation(x=x, y=y, text=txt, showarrow=False,
                           font=dict(size=11, color="#333"),
                           align='center', bgcolor='rgba(255,255,255,0.7)',
                           bordercolor='#ccc', borderwidth=1)

    # Plot risks
    for r in risks:
        fig.add_trace(go.Scatter(
            x=[r["freq"]], y=[r["loss"]],
            mode='markers+text',
            marker=dict(size=22, color=r["color"], opacity=0.85,
                        line=dict(color='white', width=2)),
            text=[r["name"]],
            textposition="top center",
            textfont=dict(size=10, color="#222"),
            name=r["name"],
            hovertemplate=(f"<b>{r['name']}</b><br>発生頻度: {r['freq']}/10<br>"
                           f"損失規模: {r['loss']}/10<br>対応策: {r['strategy']}<extra></extra>"),
            showlegend=False,
        ))

    # Dividers
    fig.add_hline(y=5, line_dash='dash', line_color='gray', line_width=1.5)
    fig.add_vline(x=5, line_dash='dash', line_color='gray', line_width=1.5)

    fig.update_layout(
        height=560,
        xaxis=dict(title="損失の発生頻度 → 高", range=[-0.5, 10.5],
                   showgrid=True, gridcolor='#eee'),
        yaxis=dict(title="損失の規模 → 大", range=[-0.5, 10.5],
                   showgrid=True, gridcolor='#eee'),
        plot_bgcolor='white',
    )
    st.plotly_chart(fig, use_container_width=True)

    # Strategy table
    st.markdown('<div class="section-title">📋 リスク対応策の選び方</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    strategies = [
        ("①", "リスクの回避", "高頻度・大損失", "リスクの発生確率をゼロにする。事業そのものを変更・中止。", "#c0392b"),
        ("②", "リスクの防止・軽減", "高頻度・小損失", "事故の発生を防止し、発生した場合の損害額を軽減するための予防策。リスクの分散も有効。", "#e67e22"),
        ("③", "リスクの保有", "低頻度・小損失", "リスクそのものを抱え込む。貯蓄などで備える。", "#27ae60"),
        ("④", "リスクの移転", "低頻度・大損失", "直面するリスクを金銭的取引により第三者へ移転する。⇒ <strong>保険が最適解</strong>", "#3498db"),
    ]
    for i, (num, name, cond, desc, color) in enumerate(strategies):
        col = c1 if i % 2 == 0 else c2
        col.markdown(f"""
        <div style="background:{color}15; border-left:5px solid {color};
                    border-radius:0 10px 10px 0; padding:1rem 1.2rem; margin:0.5rem 0;">
            <h4 style="color:{color}; margin:0 0 0.3rem 0;">{num} {name} <small>（{cond}）</small></h4>
            <p style="margin:0; font-size:0.9rem;">{desc}</p>
        </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# PAGE 5 ── 保険vs貯蓄シミュレーター
# ════════════════════════════════════════════════════════════════════════════
elif page == "💰 保険vs貯蓄シミュレーター":
    st.markdown('<div class="hero" style="padding:1.5rem;"><h1 style="font-size:1.8rem;">💰 「貯蓄は三角、保険は四角」シミュレーター</h1><p>万一のとき、貯蓄だけで備えられますか？</p></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box">
        <h4>「貯蓄は三角、保険は四角」とは？</h4>
        <p>貯蓄は時間をかけてお金を積み上げる（三角形）ため、<strong>途中で事故が起きた時にカバーできない可能性があります。</strong><br>
        一方、保険は契約初日から十分な補償が受けられる（四角形）ため、<strong>不測の事故にも即座に備えられます。</strong></p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 2])

    with c1:
        st.subheader("条件設定")
        target_amount = st.number_input("備えたい金額（万円）", min_value=100, max_value=50000,
                                        value=1000, step=100)
        monthly_savings = st.number_input("月々の貯蓄額（万円）", min_value=1, max_value=500,
                                          value=10, step=1)
        monthly_premium = st.number_input("月々の保険料（万円）", min_value=0.5, max_value=50.0,
                                          value=3.0, step=0.5)
        accident_month = st.slider("事故が発生する月（契約から）", 1, 120, 24)

        years_needed = target_amount / monthly_savings / 12
        savings_at_accident = min(monthly_savings * accident_month, target_amount)
        shortage = max(0, target_amount - savings_at_accident)
        total_premium = monthly_premium * accident_month

        st.divider()
        st.metric("貯蓄で備えるのに必要な年数", f"{years_needed:.1f}年")
        st.metric("事故時の貯蓄額", f"{savings_at_accident:,.0f}万円")
        st.metric("不足額", f"{shortage:,.0f}万円",
                  delta=f"-{shortage:,.0f}万円" if shortage > 0 else "0（十分）",
                  delta_color="inverse")
        st.metric("保険の支払総額（事故まで）", f"{total_premium:.0f}万円")

    with c2:
        months = list(range(0, 121))
        savings_curve = [min(monthly_savings * m, target_amount) for m in months]
        insurance_curve = [target_amount] * 121
        premium_curve = [monthly_premium * m for m in months]

        fig = make_subplots(specs=[[{"secondary_y": False}]])

        # Savings area (triangle)
        fig.add_trace(go.Scatter(
            x=months, y=savings_curve,
            name="貯蓄残高", fill='tozeroy',
            fillcolor='rgba(52,152,219,0.2)',
            line=dict(color='#3498db', width=3),
        ))

        # Insurance flat line (square)
        fig.add_trace(go.Scatter(
            x=months, y=insurance_curve,
            name="保険補償額", fill='tozeroy',
            fillcolor='rgba(39,174,96,0.15)',
            line=dict(color='#27ae60', width=3, dash='dot'),
        ))

        # Premiums paid
        fig.add_trace(go.Scatter(
            x=months, y=premium_curve,
            name="保険料累計支払",
            line=dict(color='#e74c3c', width=2, dash='dash'),
        ))

        # Accident line
        fig.add_vline(x=accident_month, line_dash='solid', line_color='#e74c3c',
                      line_width=3, annotation_text=f"⚡事故発生（{accident_month}ヶ月目）",
                      annotation_position="top right",
                      annotation_font=dict(color='#e74c3c', size=12))

        # Shortage annotation
        if shortage > 0:
            fig.add_annotation(
                x=accident_month, y=savings_at_accident + shortage / 2,
                text=f"不足額\n{shortage:,.0f}万円",
                showarrow=True, arrowhead=2, arrowcolor='#c0392b',
                font=dict(color='#c0392b', size=12, weight='bold'),
                bgcolor='rgba(255,255,255,0.9)', bordercolor='#c0392b',
            )

        fig.update_layout(
            title=f"貯蓄 vs 保険：目標{target_amount:,}万円の備え",
            height=450, plot_bgcolor='white',
            xaxis=dict(title="経過月数（月）", gridcolor='#eee'),
            yaxis=dict(title="金額（万円）", gridcolor='#eee'),
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
        )
        st.plotly_chart(fig, use_container_width=True)

    # Cost comparison
    st.divider()
    st.subheader("💡 コスト比較：保険 vs 自己資金準備")
    c1, c2, c3 = st.columns(3)

    annual_premium = monthly_premium * 12
    c1.metric("年間保険料", f"{annual_premium:.0f}万円",
              help="月々の保険料 × 12ヶ月")
    c2.metric("保険なしで同額確保するのに必要な年数", f"{years_needed:.1f}年",
              help="目標金額 ÷ 年間貯蓄額")
    c3.metric("その間のリスク暴露期間", f"{max(0, years_needed - accident_month/12):.1f}年",
              help="備えが完成するまでの無防備な期間", delta_color="inverse")

    st.markdown("""
    <div class="alert-banner">
        <h3>⚠️ これが現実です</h3>
        <p>2018年西日本豪雨で被災した中小企業の損害額の中央値は約1,000万円。</p>
        <p>月10万円ずつ貯蓄していても、1,000万円が貯まるまでには <strong>約8年4ヶ月</strong> かかります。</p>
        <p>この間に被災した企業は、自力で損害を補填するしかありませんでした。</p>
    </div>
    """, unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# PAGE 6 ── 事例研究
# ════════════════════════════════════════════════════════════════════════════
elif page == "📰 事例研究":
    st.markdown('<div class="hero" style="padding:1.5rem;"><h1 style="font-size:1.8rem;">📰 事例研究：リスク対応の失敗と教訓</h1><p>実際に起きた事例から、リスクマネジメントの重要性を学ぶ</p></div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["① 雪印集団中毒事件", "② 明石花火大会歩道橋事件", "③ 中小企業への示唆"])

    with tab1:
        st.markdown("""
        <div class="case-card">
            <h4>🥛 雪印集団中毒事件（2000年）</h4>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**📅 事件の経緯**")
            timeline_data = {
                "時点": ["2000年6月27日", "7月1日\n（記者会見）", "7月", "2002年1月"],
                "出来事": ["大阪工場の低脂肪乳で14,780人が食中毒",
                           "社長が「俺は寝ていない」などの暴言。\n対処の判断が遅れ、隠ぺい工作も発覚",
                           "大阪工場閉鎖・経営トップ辞任\n雪印乳業は実質的に解体",
                           "雪印食品の牛肉産地偽装発覚\n⇒ 雪印食品は解散"],
            }
            for t, e in zip(timeline_data["時点"], timeline_data["出来事"]):
                st.markdown(f"""
                <div style="display:flex; margin:0.5rem 0; align-items:flex-start;">
                    <div style="background:#c0392b; color:white; padding:0.3rem 0.5rem;
                                border-radius:6px; font-size:0.8rem; font-weight:700;
                                min-width:100px; text-align:center; margin-right:1rem;">{t}</div>
                    <div style="font-size:0.9rem; padding-top:0.2rem;">{e}</div>
                </div>""", unsafe_allow_html=True)

        with c2:
            st.markdown("**⚖️ 法的・経営的帰結**")
            outcomes = [
                ("被害者数", "14,780人", "#c0392b"),
                ("刑事訴訟", "業務上過失致傷\n元工場長に禁固刑", "#e67e22"),
                ("民事訴訟", "初のPL訴訟\n和解成立", "#e67e22"),
                ("企業への影響", "ブランド完全崩壊\n会社実質解体", "#c0392b"),
            ]
            for label, value, color in outcomes:
                st.markdown(f"""
                <div style="background:{color}15; border-left:4px solid {color};
                            padding:0.7rem 1rem; border-radius:0 8px 8px 0; margin:0.5rem 0;">
                    <strong style="color:{color};">{label}</strong><br>
                    <span style="font-size:0.95rem;">{value}</span>
                </div>""", unsafe_allow_html=True)

        st.markdown("""
        <div class="alert-banner">
            <h3>🔑 リスクマネジメントの教訓</h3>
            <p>① <strong>初期対応の遅れ</strong>が最悪の結果を招いた。「通常の苦情」として処理したことで被害が拡大。</p>
            <p>② <strong>危機発生時の意思決定プロセス</strong>（誰が・何を・いつ決断するか）を事前に決めておく必要がある。</p>
            <p>③ <strong>隠ぺい</strong>は最大のリスク。誠実な情報開示が企業存続の鍵。</p>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <div class="case-card">
            <h4>🎆 明石花火大会歩道橋事件（2001年）</h4>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**📅 概要**")
            st.markdown("""
            - 2001年7月、兵庫県明石市朝霧駅の歩道橋で群衆が転倒
            - **11名死亡、247名負傷**
            - 原因：事前の警備計画の不備と群集の危険性への認識欠如
            """)
            st.markdown("**⚖️ 法的帰結**")
            st.markdown("""
            | 対象 | 判決 |
            |------|------|
            | 県警察官・警備会社社員 | **実刑** |
            | 市職員 | 執行猶予付有罪判決 |
            | 明石市・兵庫県警・警備会社 | **損害賠償5億6,800万円** |
            """)

        with c2:
            # Impact visualization
            fig = go.Figure(go.Treemap(
                labels=["総被害", "死亡", "負傷", "損害賠償\n5億6,800万円",
                        "警備業法改正", "国家公安委員会規則改正"],
                parents=["", "総被害", "総被害", "総被害", "総被害", "総被害"],
                values=[100, 11, 247, 568, 50, 50],
                marker_colors=["#1a1a2e", "#c0392b", "#e74c3c", "#e67e22", "#27ae60", "#3498db"],
            ))
            fig.update_layout(height=320, margin=dict(l=0, r=0, t=10, b=0))
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        <div class="alert-banner">
            <h3>🔑 中小企業への教訓</h3>
            <p>① 警備会社（中小企業が多い）も<strong>重大な損害賠償責任</strong>を問われた。</p>
            <p>② <strong>賠償責任保険</strong>（PL保険・賠償責任保険）がなければ、会社の存続自体が危うくなる。</p>
            <p>③ 「自分の会社には関係ない」は最大の危機：どの業種でも賠償リスクは存在する。</p>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="section-title">💡 中小企業が学ぶべきこと</div>', unsafe_allow_html=True)

        lessons = [
            ("事前の対策が全て", "危機が起きてから考えても手遅れ。BCP・リスク対策は「平時」に策定する必要があります。",
             "🔴 最重要", "#c0392b"),
            ("初期対応が命運を分ける", "最初の72時間の対応が企業の評判・存続を左右します。「誰が」「何を」「いつ」決断するか、事前に決めておきましょう。",
             "🟠 重要", "#e67e22"),
            ("保険は「移転」の手段", "大きな損害リスクは自社だけで抱え込まず、保険（第三者）に移転する。これがリスクファイナンスの基本です。",
             "🟡 実践", "#f39c12"),
            ("誠実な情報開示", "問題が発生した際の隠ぺいは最大のリスク。誠実な対応が長期的な企業価値を守ります。",
             "🟢 原則", "#27ae60"),
        ]
        for title, desc, tag, color in lessons:
            st.markdown(f"""
            <div style="background:{color}12; border:2px solid {color};
                        border-radius:12px; padding:1.2rem 1.5rem; margin:0.8rem 0;">
                <div style="display:flex; align-items:center; margin-bottom:0.5rem;">
                    <span style="background:{color}; color:white; padding:0.2rem 0.7rem;
                                 border-radius:6px; font-size:0.8rem; font-weight:700;
                                 margin-right:0.8rem;">{tag}</span>
                    <h4 style="margin:0; color:{color};">{title}</h4>
                </div>
                <p style="margin:0; font-size:0.95rem;">{desc}</p>
            </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# PAGE 7 ── 対応策ロードマップ
# ════════════════════════════════════════════════════════════════════════════
elif page == "🗺️ 対応策ロードマップ":
    st.markdown('<div class="hero" style="padding:1.5rem;"><h1 style="font-size:1.8rem;">🗺️ 中小企業のリスク対策ロードマップ</h1><p>今日から始めるリスクマネジメントの実践ステップ</p></div>', unsafe_allow_html=True)

    # Market analysis
    st.markdown('<div class="section-title">🌊 なぜ今、中小企業にリスクマネジメントが必要か</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        # Market size visualization
        fig = go.Figure(go.Bar(
            x=["大企業", "中規模企業", "小規模企業"],
            y=[50, 47, 10],
            marker_color=["#7f8c8d", "#e74c3c", "#e74c3c"],
            text=["50兆円\n（損保会社が直接対応）",
                  "47兆円\n⚠️ 開拓不十分",
                  "10兆円\n⚠️ 開拓不十分"],
            textposition='inside',
            textfont=dict(color='white', size=11),
        ))
        fig.add_annotation(
            x=1.5, y=58, text="中小企業向け市場は<br><b>ブルーオーシャン！</b>",
            showarrow=True, arrowhead=2, arrowcolor='#27ae60',
            bgcolor='#27ae60', font=dict(color='white', size=12),
        )
        fig.update_layout(
            title="損保市場規模（推計）", height=380, plot_bgcolor='white',
            yaxis=dict(title="潜在市場規模（兆円）", gridcolor='#eee'),
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.markdown("""
        <div class="insight-box" style="margin-top:0;">
            <h4>中小企業向け市場の現状と課題</h4>
            <table style="width:100%; font-size:0.88rem; border-collapse:collapse;">
                <tr style="background:#eaf4fb;">
                    <th style="padding:8px; text-align:left;">プレイヤー</th>
                    <th style="padding:8px; text-align:left;">課題</th>
                </tr>
                <tr style="border-bottom:1px solid #dee;">
                    <td style="padding:8px;"><strong>損保プロ代理店</strong></td>
                    <td style="padding:8px;">新規顧客（中小企業）の実情がわからず、二の足を踏んでいる</td>
                </tr>
                <tr style="background:#f8f9fa; border-bottom:1px solid #dee;">
                    <td style="padding:8px;"><strong>中小企業診断士</strong></td>
                    <td style="padding:8px;">中小企業との接点はあるが、保険の知識がなく提案できない</td>
                </tr>
                <tr>
                    <td style="padding:8px;"><strong>中小企業</strong></td>
                    <td style="padding:8px;">リスクは感じているが、適切な保険・対策へのアクセスがない</td>
                </tr>
            </table>
        </div>

        <div style="background:#fff3cd; border:2px solid #f39c12; border-radius:12px;
                    padding:1.2rem; margin-top:1rem;">
            <h4 style="color:#856404; margin:0 0 0.5rem 0;">🌉 研究会の役割</h4>
            <p style="margin:0; font-size:0.95rem;">
                <strong>中小企業診断士 ↔ リスクマネジメント研究会 ↔ プロ代理店</strong><br>
                この橋渡しにより、中小企業に適切なリスク対策が届く仕組みを構築します。
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Action roadmap
    st.markdown('<div class="section-title">📋 今日からできるアクションプラン</div>', unsafe_allow_html=True)

    steps = [
        ("Step 1", "リスクの洗い出し（今日〜1週間）", "#1b6ca8",
         "自社が直面している純粋リスク・投機的リスクをリストアップ。「リスク自己診断」ツールを活用してください。"),
        ("Step 2", "保険内容の現状確認（1〜2週間）", "#118ab2",
         "現在加入している保険の補償内容・金額を確認。特に利益補償型保険の有無をチェック。不明な場合はプロ代理店へ相談。"),
        ("Step 3", "優先リスクへの対策立案（1〜3ヶ月）", "#06d6a0",
         "リスクマトリクスで優先度を決め、「移転（保険）」「防止」「保有」の対策を具体化する。"),
        ("Step 4", "BCP（事業継続計画）の策定（3〜6ヶ月）", "#27ae60",
         "被災後に何日以内に事業を再開するか目標を定め、復旧手順・連絡体制を文書化する。"),
        ("Step 5", "定期的な見直しと訓練（毎年）", "#2ecc71",
         "リスク環境は変化します。年1回の保険見直し・BCP訓練を習慣化しましょう。"),
    ]

    for step, title, color, desc in steps:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; margin:0.8rem 0;">
            <div style="background:{color}; color:white; padding:0.5rem 0.8rem;
                        border-radius:8px; font-weight:900; font-size:0.9rem;
                        min-width:70px; text-align:center; margin-right:1rem;
                        box-shadow:0 2px 8px {color}50;">{step}</div>
            <div style="flex:1; background:white; border-left:4px solid {color};
                        border-radius:0 10px 10px 0; padding:0.8rem 1.2rem;
                        box-shadow:0 2px 8px rgba(0,0,0,0.08);">
                <h4 style="margin:0 0 0.3rem 0; color:#0f4c75;">{title}</h4>
                <p style="margin:0; color:#555; font-size:0.9rem;">{desc}</p>
            </div>
        </div>""", unsafe_allow_html=True)

    # BCP checklist
    st.markdown('<div class="section-title">✅ BCPチェックリスト（現状確認）</div>', unsafe_allow_html=True)

    bcp_items = [
        ("事業への影響分析", "どの業務が止まったら事業継続できないか把握している"),
        ("復旧目標時間の設定", "各業務の復旧目標時間（RTO）を設定している"),
        ("緊急連絡網の整備", "緊急時の連絡先リストと連絡手順が整備されている"),
        ("バックアップ体制", "重要データのバックアップと代替業務手順がある"),
        ("資金繰り対策", "災害時の緊急資金調達方法を準備している"),
        ("訓練の実施", "年1回以上BCP訓練を実施している"),
    ]

    checked = 0
    for title, desc in bcp_items:
        if st.checkbox(f"**{title}**：{desc}"):
            checked += 1

    progress = checked / len(bcp_items)
    st.progress(progress)
    if progress == 1.0:
        st.success(f"✅ BCP準備度：{checked}/{len(bcp_items)} — 素晴らしい！完全に備えています。")
    elif progress >= 0.5:
        st.warning(f"⚠️ BCP準備度：{checked}/{len(bcp_items)} — もう一歩。残りの項目を整備しましょう。")
    else:
        st.error(f"🔴 BCP準備度：{checked}/{len(bcp_items)} — 緊急対策が必要です。専門家に相談しましょう。")


# ════════════════════════════════════════════════════════════════════════════
# PAGE 8 ── 研究会の実績
# ════════════════════════════════════════════════════════════════════════════
elif page == "🏆 研究会の実績":
    st.markdown('<div class="hero" style="padding:1.5rem;"><h1 style="font-size:1.8rem;">🏆 リスクマネジメント研究会の実績</h1><p>（一社）広島県中小企業診断協会 リスクマネジメント研究会</p></div>', unsafe_allow_html=True)

    # 3-year plan
    st.markdown('<div class="section-title">📅 3か年計画（ホップ・ステップ・ジャンプ）</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    plans = [
        ("🐇 ホップ", "2021年度", "#1b6ca8",
         ["研究テーマの選定", "研究→アウトプット", "ビジネスモデルの検討",
          "セミナーの企画", "顧客（代理店・診断士）開拓"]),
        ("🚀 ステップ", "2022年度", "#118ab2",
         ["セミナーの実施", "日本損保協会との連携", "各地での開催実績"]),
        ("🏆 ジャンプ", "2023年度以降", "#06d6a0",
         ["研究会の法人化", "セミナーの継続実施", "更なる普及活動"]),
    ]
    for col, (phase, year, color, items) in zip([c1, c2, c3], plans):
        items_html = "".join(f"<li>{item}</li>" for item in items)
        col.markdown(f"""
        <div style="background:white; border-top:5px solid {color};
                    border-radius:12px; padding:1.5rem;
                    box-shadow:0 4px 16px rgba(0,0,0,0.1); height:100%;">
            <h3 style="color:{color}; margin:0 0 0.3rem 0;">{phase}</h3>
            <div style="font-size:0.85rem; color:#888; margin-bottom:1rem;">{year}</div>
            <ul style="margin:0; padding-left:1.2rem; font-size:0.9rem; line-height:1.8;">
                {items_html}
            </ul>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Seminar history
    st.markdown('<div class="section-title">📣 セミナー開催実績</div>', unsafe_allow_html=True)

    seminars = [
        {
            "date": "2022年3月1日",
            "title": "中小企業を取り巻くリスクを考えるセミナー",
            "org": "日本損害保険協会 中国支部",
            "format": "オンライン",
            "topics": ["自然災害リスク対策", "コロナウイルスリスク", "サイバー攻撃対策", "情報漏えい対策"],
            "color": "#1b6ca8",
        },
        {
            "date": "2022年12月1日",
            "title": "中小企業向けリスクセミナー",
            "org": "日本損害保険協会 中部支部・北陸支部",
            "format": "対面",
            "topics": ["企業を取り巻くリスク（横尾浩輝 中小企業診断士）",
                       "小規模零細企業のサイバーリスクの脅威",
                       "BCPと事業継続力強化計画（中小企業基盤整備機構）"],
            "note": "閉会挨拶：経済産業省中部経済産業局 中小企業課長",
            "color": "#118ab2",
        },
        {
            "date": "2023年3月10日",
            "title": "中小企業向けリスク対策セミナー",
            "org": "日本損害保険協会 中国支部",
            "format": "対面（約60名参加）",
            "topics": ["BCP策定によるリスク対策（広島県商工労働局）",
                       "リスク対策としての補助金の活用（中小企業診断士）",
                       "労務管理（パワハラ・セクハラ）のリスク対策（弁護士）"],
            "color": "#06d6a0",
        },
    ]

    for s in seminars:
        topics_html = "".join(f"<li style='font-size:0.88rem;'>{t}</li>" for t in s["topics"])
        note_html = f"<p style='font-size:0.82rem; color:#888; margin:0.5rem 0 0 0;'>📝 {s['note']}</p>" if "note" in s else ""
        st.markdown(f"""
        <div class="seminar-card">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap;">
                <div>
                    <span style="background:{s['color']}; color:white; padding:0.2rem 0.7rem;
                                 border-radius:6px; font-size:0.8rem;">{s['date']}</span>
                    <span style="background:#6c757d; color:white; padding:0.2rem 0.7rem;
                                 border-radius:6px; font-size:0.8rem; margin-left:0.5rem;">{s['format']}</span>
                    <h4 style="margin:0.5rem 0 0.2rem 0;">{s['title']}</h4>
                    <p style="font-size:0.9rem; color:#555; margin:0;">主催：{s['org']}</p>
                </div>
            </div>
            <ul style="margin:0.8rem 0 0 0; padding-left:1.2rem;">
                {topics_html}
            </ul>
            {note_html}
        </div>""", unsafe_allow_html=True)

    # Impact chart
    st.markdown('<div class="section-title">📈 活動の広がり</div>', unsafe_allow_html=True)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=["2021年度", "2022年度", "2023年度", "2024年度以降"],
        y=[0, 2, 3, 5],
        mode='lines+markers+text',
        text=["活動開始", "セミナー2回", "セミナー3回\n法人化", "更なる展開"],
        textposition=["bottom center", "top center", "top center", "top center"],
        marker=dict(size=16, color="#1b6ca8"),
        line=dict(color="#1b6ca8", width=3),
        fill='tozeroy', fillcolor='rgba(27,108,168,0.1)',
    ))
    fig.update_layout(
        height=300, plot_bgcolor='white',
        xaxis=dict(showgrid=False),
        yaxis=dict(title="セミナー開催数", gridcolor='#eee', range=[0, 7]),
        title="研究会活動の推移",
    )
    st.plotly_chart(fig, use_container_width=True)

    # Contact / CTA
    st.markdown("""
    <div style="background:linear-gradient(135deg, #0f4c75, #1b6ca8);
                color:white; padding:2rem; border-radius:16px; text-align:center; margin-top:1rem;">
        <h2 style="margin:0 0 0.5rem 0;">🤝 リスクマネジメントに関するご相談</h2>
        <p style="font-size:1.05rem; opacity:0.9; margin:0 0 1rem 0;">
            中小企業診断士がリスクの実態把握から対策立案まで、丁寧にサポートします。
        </p>
        <div style="background:rgba(255,255,255,0.15); padding:1rem 2rem;
                    border-radius:10px; display:inline-block;">
            <strong>（一社）広島県中小企業診断協会</strong><br>
            リスクマネジメント研究会 代表 三村雅彦<br>
            <span style="font-size:0.9rem; opacity:0.8;">中小企業診断士 / 元損害保険協会</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
