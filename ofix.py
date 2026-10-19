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

    /* Okvir za sekciju sa dve verzije */
    .versions-card-blue {
        background-color: rgba(28, 131, 225, 0.04);
        border: 2px solid #1f77b4;
        padding: 1.2rem;
        border-radius: 0.8rem;
        margin-bottom: 1.5rem;
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
        <p style='font-size: 1.3rem; color: #A9A9A9; margin-top: 0px; margin-bottom: 0px;'>Efikasan alat za brzo izdavanje A4 računa i evidenciju poslovanja
