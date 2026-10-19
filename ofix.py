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

# ----- DIJALOG ZAN OTVARANJE SLIKA NA TABLETU/TELEFONU -----
@st.dialog("Prikaz slike u velikom formatu")
def prikazi_veliku_sliku(putanja_slike, naslov):
    st.image(putanja_slike, caption=naslov, use_container_width=True)

# ----- BLOK SLIKE DESNO (OPTIMIZOVANO ZA TABLET I TELEFON) -----
with col_slike:
    st.markdown("### Prikaz programa")
  
    # Slika 1
    st.image("1.JPG", caption="Glavni ekran i navigacija", use_container_width=True)
    if st.button("🔍 Uvećaj sliku 1", key="btn1", use_container_width=True):
        prikazi_veliku_sliku("1.JPG", "Glavni ekran i navigacija")
    st.write("")

    # Slika 2
    st.image("2.JPG", caption="Forma baze artikala", use_container_width=True)
    if st.button("🔍 Uvećaj sliku 2", key="btn2", use_container_width=True):
        prikazi_veliku_sliku("2.JPG", "Forma baze artikala")
    st.write("")

    # Slika 3
    st.image("3.JPG", caption="Forma za kreiranje računa", use_container_width=True)
    if st.button("🔍 Uvećaj sliku 3", key="btn3", use_container_width=True):
        prikazi_veliku_sliku("3.JPG", "Forma za kreiranje računa")
    st.write("")

    # Slika 4
    st.image("4.JPG", caption="Izgled gotovog računa", use_container_width=True)
    if st.button("🔍 Uvećaj sliku 4", key="btn4", use_container_width=True):
        prikazi_veliku_sliku("4.JPG", "Izgled gotovog računa")

st.markdown("---")

# ---- CENE I LICENCE ----
st.markdown("## Način kupovine i cena")
st.write("Godišnja pretplata & Trajna kupovina. Autor pruža besplatnu tehničku podršku godinu dana (telefonom, emailom ili putem TeamViewer-a).")
st.write("")

price_col1, price_col2 = st.columns(2, gap="large")

with price_col1:
    st.markdown(
        """
        <div class="price-card-blue">
            <h3 style="margin-bottom: 0px; margin-top: 0px;">🏷️ OFIX STANDARD</h3>
            <p style="color: #A9A9A9; font-size: 0.9rem; margin-top: 2px; margin-bottom: 0px;">Za standardno fakturisanje na ceo račun</p>
            <div class="price-grid">
                <div class="price-item">
                    <div class="price-label">Godišnja pretplata</div>
                    <div class="price-value">59 €</div>
                </div>
                <div class="price-item">
                    <div class="price-label">Trajna licenca</div>
                    <div class="price-value">249 €</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with price_col2:
    st.markdown(
        """
        <div class="price-card-blue">
            <h3 style="margin-bottom: 0px; margin-top: 0px;">🏷️ OFIX RABAT</h3>
            <p style="color: #A9A9A9; font-size: 0.9rem; margin-top: 2px; margin-bottom: 0px;">Za napredno fakturisanje po pojedinačnim stavkama</p>
            <div class="price-grid">
                <div class="price-item">
                    <div class="price-label">Godišnja pretplata</div>
                    <div class="price-value">89 €</div>
                </div>
                <div class="price-item">
                    <div class="price-label">Trajna licenca</div>
                    <div class="price-value">349 €</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

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
        poslato = st.form_submit_button("Pošalji poruku", use_container_width=True)
    
        if poslato:
            st.success("Hvala! Vaša poruka je uspešno poslata.")

    st.markdown("---")
    st.markdown("🔹 **Email 1:** magicamp@bluewin.ch")
    st.markdown("🔹 **Email 2:** magy@usa.com")
    st.markdown("🔹 **Telefon:** 063 310 850")
