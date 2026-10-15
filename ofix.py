import streamlit as st

# Podešavanje stranice
st.set_page_config(
    page_title="OFIX - Knjigovodstveno-kancelarijski program",
    page_icon="📊",
    layout="wide",
)

# ---- HERO SEKCIJA ----
st.markdown("## OFIX – Knjigovodstveno-kancelarijski program")
st.subheader("Efikasan alat za brzo izdavanje A4 računa i evidenciju poslovanja.")

st.markdown("---")

# ---- O PROGRAMU + SLIKE SA DESNE STRANE ----
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

with col_slike:
  st.markdown("### Prikaz programa")
  
  # Prva slika sa desne strane
  # Prva slika sa desne strane
st.image(
    "1.JPG",
    caption="Glavni ekran i navigacija",
    use_container_width=True
)

st.markdown("---")

# Druga slika sa desne strane
st.image(
    "2.JPG",
    caption="Izdavanje A4 računa",
    use_container_width=True  # Promenjeno sa use_column_width na use_container_width
)

st.markdown("---")

# Treća slika sa desne strane (Mora biti u istom bloku/indentaciji kao i prve dve)
st.image(
    "3.JPG",
    caption="Baza Artikla",
    use_container_width=True
)


st.markdown("---")

# ---- VERZIJE PROGRAMA ----
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
