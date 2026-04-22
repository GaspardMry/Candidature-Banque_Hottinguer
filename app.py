import streamlit as st
import sys
import os

# Ajouter le répertoire racine au path pour les imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data.generate_data import generate_all_series, compute_returns
from utils.styling import apply_streamlit_theme, COLORS
from components import overview, var_tab, stress_tab, greeks_tab, market_tab, risk_dashboard

# ── Configuration de la page ──────────────────────────────────────────
st.set_page_config(
    page_title="Asset:Gaspard MÉRAY",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Appliquer le thème ────────────────────────────────────────────────
apply_streamlit_theme()

# ── Génération des données (cache Streamlit) ──────────────────────────
@st.cache_data
def load_data():
    df = generate_all_series(seed=42)
    returns = compute_returns(df)
    return df, returns

df, returns = load_data()

# ── Sidebar ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style="text-align: center; padding: 20px 0;">
        <p1 style="color:{COLORS['white']}; font-family: 'Courier New'; font-size: 1.3em;">
            Asset Gaspard MÉRAY
        </h1>
        <p1 style="color:{COLORS['orange']}; font-family: 'Courier New'; font-size: 1.0em;">
        Global Analysis
        </p>
        <hr style="border-color: #30363D; margin: 15px 0;">
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background: {COLORS['bg_lighter']}; padding: 12px; border-radius: 8px; margin-bottom: 15px;">
        <p style="color: {COLORS['white']}; font-family: 'Courier New'; font-size: 0.75em; margin: 0;">
            <b style="color: {COLORS['orange']};">> PROFIL :</b> Gaspard Méray<br>
            <b style="color: {COLORS['orange']};">> STATUT :</b> Master 1 Finance, Banking & Financial Engineering, Major in Quantitative Methods<br>
            <b style="color: {COLORS['orange']};">> OBJECTIF :</b> Stage de 3 mois en tant que Risk Analyst chez Banque Hottinguer <br>
            <b style="color: {COLORS['orange']};">> ORIGINE :</b> Lasson, Normandie<br>
            <b style="color: {COLORS['orange']};">> BAC :</b> 10.25/20 <br>
            <b style="color: {COLORS['orange']};">> NEURO :</b> #Confidentiel on en parlera durant l'entretien...<br>
            <b style="color: {COLORS['orange']};">> ÉCOLE :</b> ESSCA Angers (Non-Target)
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background: {COLORS['bg_lighter']}; padding: 12px; border-radius: 8px; border: 1px solid #30363D;">
        <p style="color: {COLORS['orange']}; font-family: 'Courier New'; font-size: 0.75em; margin: 0;">
            <b style="color: {COLORS['orange']};">> THÈSE</b>
        <p style="color: {COLORS['white']}; font-family: 'Courier New'; font-size: 0.75em; margin: 0;">
            Un profil atypique est un actif à <b style="color: {COLORS['orange']};">haute convexité</b> :
            les pertes sont bornées,
            mais le potentiel de hausse est asymétriquement <b style="color: {COLORS['orange']};">positif</b>.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ── Navigation par onglets ────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Vue d'ensemble",
    "VaR & Monte Carlo",
    "Stress Tests",
    "Greeks",
    "Up/Down Market",
    "Risk Dashboard",
])

with tab1:
    overview.render(df)

with tab2:
    var_tab.render(df, returns)

with tab3:
    stress_tab.render(df)

with tab4:
    greeks_tab.render(df)

with tab5:
    market_tab.render(df, returns)

with tab6:
    risk_dashboard.render(df)
