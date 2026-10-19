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

# 3. Globalni CSS stilovi sa vašom animacijom (PC i telefon optimizacija + Stil za cene/licence box-ove)
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

    /* Stil za naglašavanje box-ova cena i licenci */
    .price-box {
        background-color: rgba(28, 131, 225, 0.04);
        border: 2px solid #1f77b4;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 10px;
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

    # ---- UKLOPLJEN BOX: NUDIMO DVE VERZIJE OFIX-a ----
    st.markdown("### Nudimo dve verzije OFIX-a")
    
    c_ver1, c_ver2 = st.columns(2, gap="medium")

    with c_ver1:
        st.markdown("#### 🔹 OFIX STANDARD")
        st.caption("Standardni model fakturisanja")
        st.write("Mogućnost odobravanja rabata na **ceo iznos računa**.")

    with c_ver2:
        st.markdown("#### 🔹 OFIX RABAT")
        st.caption("Napredni model fakturisanja")
        st.write("Mogućnost **različitog rabata na svaku stavku** na računu.")

    st.info(
        "💡 **Napomena:** Jedina razlika između verzija je ta što RABAT verzija "
        "omogućava različit rabat za svaku stavku na računu, a STANDARD rabat na ceo iznos računa.\n\n"
        "🔸 **Podrška:** Za obe verzije besplatna tehnička podrška autora."
    )

# ----- BLOK SLIKE DESNO  -----
with col_slike:
    st.markdown("### Prikaz programa")
  
    st.image("1.JPG", caption="Glavni ekran i navigacija", use_container_width=True)
    st.image("2.JPG", caption="Forma baze artikala", use_container_width=True)
    st.image("3.JPG", caption="Forma za kreiranje računa", use_container_width=True)
    st.image("4.JPG", caption="Izgled gotovog računa", use_container_width=True)

st.markdown("---")

# ---- CENE I LICENCE ----
st.markdown("## Način kupovine i cena")
st.write("Godišnja pretplata & Trajna kupovina. Autor pruža besplatnu tehničku podršku godinu dana (telefonom, emailom ili putem TeamViewer-a).")
st.write("")

price_col1, price_col2 = st.columns(2, gap="large")

with price_col1:
    st.markdown(
        """
        <div class="price-box">
            <h3>🏷️ OFIX STANDARD</h3>
            <p style="color: #A9A9A9; font-size: 0.9rem; margin-top: -10px;">Za standardno fakturisanje na ceo račun</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    m1, m2 = st.columns(2)
    with m1:
        st.metric(label="Godišnja pretplata", value="59 €")
    with m2:
        st.metric(label="Trajna licenca", value="249 €")

with price_col2:
    st.markdown(
        """
        <div class="price-box">
            <h3>🏷️ OFIX RABAT</h3>
            <p style="color: #A9A9A9; font-size: 0.9rem; margin-top: -10px;">Za napredno fakturisanje po pojedinačnim stavkama</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    m3, m4 = st.columns(2)
    with m3:
        st.metric(label="Godišnja pretplata", value="89 €")
    with m4:
        st.metric(label="Trajna licenca", value="349 €")

st.markdown("---")

# ---- DEMO PREUZIMANJE I KONTAKT FORMA ----
col_demo, col_kontakt = st.columns(2, gap="large")

with col_demo:
    st.markdown("## Preuzmite Demo Verziju")
    st.write("Isprobajte besplatno OFIX program i uverite se u jednostavnost korišćenja.")
    st.write("")
  
    st.download_button(
        label="📥 Preuzmi Besplatni Demo (20MB)",
        data=b"Demo verzija fajl placeholder",
        file_name="OFIX_Demo_Setup.exe",
        mime="application/octet-stream",
        use_container_width=True
    )

with col_kontakt:
    st.markdown("## Kontaktirajte nas")
    st.write("Imate pitanje ili želite da naručite licencu?")

    with st.form("kontakt_forma"):
        ime = st.text_input("Vaše ime / Naziv firme")
        email = st.text_input("Vaš Email")
        poruka = st.text_area("Poruka")
        poslato = st.form_submit_button
