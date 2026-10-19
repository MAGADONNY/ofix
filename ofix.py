import streamlit as st
import base64
import os

# 1. Podešavanje stranice
st.set_page_config(
    page_title="OFIX - Knjigovodstveno-kancelarijski program",
    page_icon="📊",
    layout="wide",
)

# 2. Funkcija za pretvaranje lokalnih fajlova u Base64 format za prikaz
def ucitaj_sliku_base64(putanja_slike):
    if os.path.exists(putanja_slike):
        ext = putanja_slike.split(".")[-1].lower()
        mime_type = "image/png" if ext == "png" else "image/jpeg"
        with open(putanja_slike, "rb") as fajl:
            podaci = fajl.read()
            return f"data:{mime_type};base64," + base64.b64encode(podaci).decode()
    return ""

# Učitavanje banera
banner_b64 = ucitaj_sliku_base64("banner.jpg")
izvor_banera = banner_b64 if banner_b64 else "https://placeholder.com"

# 3. Globalni CSS stilovi
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 0rem !important;
    }

    /* Kontejner za naslov i podnaslov */
    .hero-text-container {
        margin-top: 0px; 
        margin-bottom: 25px;
    }

    /* Animacija za baner */
    @keyframes advancedZoomBlur {
        0% {
            transform: scale(1.08);
            filter: blur(5px) brightness(0.6);
            opacity: 0;
        }
        100% {
            transform: scale(1.0);
            filter: blur(0px) brightness(1.0);
            opacity: 1;
        }
    }

    .hero-banner-animated {
        max-width: 800px;
        width: 100%;
        height: auto;
        border-radius: 6px;
        opacity: 0; 
        animation: advancedZoomBlur 2.2s cubic-bezier(0.1, 0.8, 0.2, 1) 0.5s forwards;
    }

    /* Plavi stil za box-ove sa cijenama */
    .price-card-blue {
        background-color: rgba(28, 131, 225, 0.1);
        border-left: 5px solid #1f77b4;
        border-top: 1px solid rgba(31, 119, 180, 0.3);
        border-right: 1px solid rgba(31, 119, 180, 0.3);
        border-bottom: 1px solid rgba(31, 119, 180, 0.3);
        padding: 1.2rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }

    .price-grid {
        display: flex;
        justify-content: space-between;
        margin-top: 15px;
        padding-top: 10px;
        border-top: 1px dashed rgba(31, 119, 180, 0.3);
    }

    .price-item {
        flex: 1;
    }

    .price-label {
        font-size: 0.85rem;
        color: #A9A9A9;
        margin-bottom: 2px;
    }

    .price-value {
        font-size: 1.8rem;
        font-weight: bold;
        color: #1f77b4;
    }

    /* Bojenje Download dugmeta u upečatljivu plavu boju */
    div.stDownloadButton > button {
        background-color: #1f77b4 !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 1.05rem !important;
        padding: 0.6rem 1rem !important;
        border-radius: 0.5rem !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        transition: all 0.3s ease !important;
    }

    div.stDownloadButton > button:hover {
        background-color: #155d8d !important;
        box-shadow: 0 6px 12px rgba(31, 119, 180, 0.3) !important;
        transform: translateY(-2px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- HERO SEKCIJA: TEKST NA SAMOM VRHU ----
st.markdown(
    """
    <div class='hero-text-container'>
        <h1 style='margin-bottom: 5px; padding-bottom: 0px; font-size: 2.2rem;'>OFIX – Knjigovodstveno-kancelarijski program</h1>
        <p style='font-size: 1.3rem; color: #A9A9A9; margin-top: 0px; margin-bottom: 0px;'>Efikasan alat za brzo izdavanje A4 računa i evidenciju poslovanja.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# ---- BANNER SLIKA SA ANIMACIJOM ----
st.markdown(
    f"""
    <div style="text-align: left;">
        <img src="{izvor_banera}" class="hero-banner-animated" style="max-width: 980px; width: 100%;">
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("<div style='margin-top: -30px;'></div>", unsafe_allow_html=True)

# ---- GLAVNI SADRŽAJ: BALANSIRANA DVA STUBA ----
col_tekst, col_slike = st.columns([1.3, 0.8], gap="large")

with col_tekst:
    st.markdown("## O programu OFIX")
    st.write(
        "**OFIX** je knjigovodstveno-kancelarijski program, namenjen za brzo i"
        " jednostavno izdavanje računa i predračuna. Idealan je alat za"
        " svakodnevnu upotrebu vlasnicima i osoblju malih i srednjih preduzeća,"
        " zanatskih, trgovinskih i uslužnih radnji, komisiona i veleprodaja."
    )

    # ------------ BLOK FUNKCIJE -------
    st.markdown("### Ključne funkcije")
    st.markdown(
        """
        <div style="background-color: rgba(28, 131, 225, 0.1); padding: 1rem; border-radius: 0.5rem; border-left: 5px solid #1f77b4;">
            🔹 <b>Baza podataka:</b> kupaca, artikala, dobavljača, dokumenata<br>
            🔹 <b>Evidencija:</b> stanja lagera, potraživanja i dugovanja.<br>
            🔹 <b>Izveštaji:</b> automatski izveštaji po kupcu, datumu, artiklu<br>
            🔹 <b>Jednostavnost:</b> prilagođeno korisnicima bez IT predznanja<br>
            🔹 <b>Veoma brz:</b> veličina 20MB, radi i bez interneta i na starijim računarima
        </div><br>
        """,
        unsafe_allow_html=True
    )

    # ---- BOX NAPOMENE ----
    st.markdown("### Napomene")
    st.markdown(
        """
        🔸 **Microsoft ACCESS:** Potreban za pokretanje.<br>
        🔸 **e-fakture:** Program ne služi za izdavanje e-faktura.<br>
        🔸 **Instalacija:** Neograničen broj računara.<br>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # ----
