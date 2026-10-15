import streamlit as st

# Podešavanje stranice
st.set_page_config(
    page_title="OFIX - Knjigovodstveno-kancelarijski program",
    page_icon="📊",
    layout="wide",
)

# ---- HERO SEKCIJA ----
st.title("OFIX – Knjigovodstveno-kancelarijski program")
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
  st.image(
      "https://via.placeholder.com/600x400.png?text=OFIX+-+Glavni+meni",
      caption="Glavni ekran i navigacija",
      use_container_width=True,
  )

  st.markdown("---")

  # Druga slika sa desne strane
  st.image
