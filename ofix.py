import streamlit as st
import base64
import os

# 1. Podešavanje stranice
st.set_page_config(
    page_title="OFIX - Knjigovodstveno-kancelarijski program",
    page_icon="📊",
    layout="wide",
)

# 2. Funkcija za pretvaranje lokalnih fajlova sa GitHub-a u bezbedan Base64 format
def ucitaj_sliku_base64(putanja_slike):
    if os.path.exists(putanja_slike):
        with open(putanja_slike, "rb") as fajl:
            podaci = fajl.read()
            return "data:image/jpeg;base64," + base64.b64encode(podaci).decode()
    return ""

# Učitavanje vašeg banera sa GitHub-a
banner_b64 = ucitaj_sliku_base64("banner.jpg")
izvor_banera = banner_b64 if banner_b64 else "https://placeholder.com"

# 3. Globalni CSS stilovi sa vašom animacijom (PC i telefon optimizacija)
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

    /* Animacija za baner preuzeta iz vašeg koda s PC optimizacijom */
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

    /* Primena animacije na baner sliku sa PC optimizacijom */
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
        padding: 1rem 1.2rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- HERO SEKCIJA: TEKST NA SAMOM VRHU ----
st.markdown(
    """
    <div class='hero-text-container'>
        <h1 style='margin-bottom: 5px; padding-bottom: 0px; font-size: 2.2rem;'>OFIX – Knjig
