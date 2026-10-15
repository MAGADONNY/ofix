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
        opacity: 0; /* Osigurava da je slika sakrivena pre starta animacije */
        animation: advancedZoomBlur 2.2s cubic-bezier(0.1, 0.8, 0.2, 1) 0.5s forwards;



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
        <p style='font-size: 1.3rem; color: #e0e0e0; margin-top: 0px; margin-bottom: 0px;'>Efikasan alat za brzo izdavanje A4 računa i evidenciju poslovanja.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# ---- BANNER SLIKA SA ANIMACIJOM ----
st.markdown(
    f"""
    <div style="text-align: left;">
        <img src="{izvor_banera}" class="hero-banner-animated" style="max-width: 850px; width: 100%;">
    </div>
    """,
    unsafe_allow_html=True

)
st.markdown("<div style='margin-top: -30px;'></div>", unsafe_allow_html=True)

# ---- GLAVNI SADRŽAJ: O PROGRAMU + SLIKE SA DESNE STRANE ----
col_tekst, col_slike = st.columns([3, 2], gap="large")

with col_tekst:
    st.markdown("## O programu OFIX")
    st.write(
        "**OFIX** je knjigovodstveno-kancelarijski program, namenjen za brzo i"
        " jednostavno izdavanje računa i predračuna. Idealan je alat za"
        " svakodnevnu upotrebu vlasnicima i osoblju malih i srednjih preduzeća,"
        " zanatskih, trgovinskih i uslužnih radnji, komisiona i veleprodaja."
    )

    st.markdown("### Ključne funkcije")
    st.markdown("- 🔹 **Jednostavna baza podataka:** kupaca, artikala, dobavljača i izdatih dokumenata.")
    st.markdown("- 🔹 **Evidencija:** stanja lagera, potraživanja i dugovanja.")
    st.markdown("- 🔹 **Izveštaji:** automatski kreirani izveštaji po kupcu, datumu, artiklu...")
    st.markdown("- 🔹 **Jednostavnost:** prilagođeno korisnicima bez IT predznanja.")
    st.markdown("- 🔹 **Veoma brz:** veličina svega oko 20MB, radi i bez interneta i na starijim računarima.")

    st.info(
        "**Važne napomene:**\n\n"
        "🔸 **Microsoft ACCESS:** Potreban za pokretanje.\n\n"
        "🔸 **e-fakture:** Program ne služi za izdavanje e-faktura.\n\n"
        "🔸 **Instalacija:** Neograničen broj računara.\n\n"
        "🔸 **Podrška:** Godinu dana besplatne tehničke podrške autora."
    )
    
    st.markdown("---")
    
    # Nudimo dve verzije OFIX-a (Prebačeno ovde radi boljeg balansa prostora)
    st.markdown("## Nudimo dve verzije OFIX-a")
    c_ver1, c_ver2 = st.columns(2)
    with c_ver1:
        st.markdown("### 🔹 OFIX STANDARD")
        st.write("Mogućnost odobravanja rabata na **ceo iznos računa**.")
    with c_ver2:
        st.markdown("### 🔹 OFIX RABAT")
        st.write("Mogućnost **različitog rabata na svaku stavku** na računu.")
        
    st.markdown(
        "> *Jedina razlika između verzija je ta što RABAT verzija omogućava"
        " različit rabat za svaku stavku na računu, a STANDARD rabat na ceo iznos"
        " računa.*"
    )

with col_slike:
    st.markdown("### Prikaz programa")
  
    # Prva slika sa desne strane (Smanjena na umerenu veličinu)
    st.image(
        "1.JPG",
        caption="Glavni ekran i navigacija",
        width=280
    )

    st.markdown("---")

    # Druga slika sa desne strane (Smanjena)
    st.image(
        "2.JPG",
        caption="Izdavanje A4 računa",
        width=280
    )

    st.markdown("---")

    # Treća slika sa desne strane (Smanjena)
    st.image(
        "3.JPG",
        caption="Baza Artikla",
        width=280
    )

st.markdown("---")

# ---- CENE I LICENCE ----
st.markdown("## Način kupovine i cena")
st.write("Godišnja pretplata & Trajna kupovina. Autor pruža besplatnu tehničku podršku godinu dana (telefonom, emailom ili putem TeamViewer-a).")

price_col1, price_col2 = st.columns(2)

with price_col1:
    st.metric(label="OFIX STANDARD - Godišnja pretplata", value="59 €")
    st.metric(label="OFIX STANDARD - Trajna licenca", value="249 €")

with price_col2:
    st.metric(label="OFIX RABAT - Godišnja pretplata", value="89 €")
    st.metric(label="OFIX RABAT - Trajna licenca", value="349 €")

st.markdown("---")

# ---- DEMO PREUZIMANJE I KONTAKT FORMA ----
col_demo, col_kontakt = st.columns(2, gap="large")

with col_demo:
    st.markdown("## Preuzmite Demo Verziju")
    st.write("Isprobajte besplatno OFIX program i uverite se u jednostavnost korišćenja.")
  
    st.download_button(
        label="📥 Preuzmi Besplatni Demo (20MB)",
        data=b"Demo verzija fajl placeholder",
        file_name="OFIX_Demo_Setup.exe",
        mime="application/octet-stream",
    )

with col_kontakt:
    st.markdown("## Kontaktirajte nas")
    st.write("Imate pitanje ili želite da naručite licencu?")

    with st.form("kontakt_forma"):
        ime = st.text_input("Vaše ime / Naziv firme")
        email = st.text_input("Vaš Email")
        poruka = st.text_area("Poruka")
        poslato = st.form_submit_button("Pošalji poruku")
    
        if poslato:
            st.success("Hvala! Vaša poruka je uspešno poslata.")

    st.markdown("---")
    st.markdown("🔹 **Email 1:** magicamp@bluewin.ch")
    st.markdown("🔹 **Email 2:** magy@usa.com")
    st.markdown("🔹 **Telefon:** 063 310 850")
