import streamlit as str_lib  # Možeš koristiti i samo 'import streamlit as st'

# Podešavanje stranice (naslov u browser tabu)
str_lib.set_page_config(
    page_title="OFIX - Knjigovodstveni program",
    page_icon="📊",
    layout="wide",
)

# --- 1. GORNJI DEO (HEADER) ZA GLAVNU SLIKU ---
str_lib.title("OFIX – Knjigovodstveno-kancelarijsko rešenje")
str_lib.write(
    "Vaš svakodnevni alat za brzo izdavanje računa i evidenciju poslovanja."
)

# Zameni 'glavna_slika.png' nazivom svoje slike u repozitorijumu (ili ostavi prazno ako je nemaš još uvek)
try:
  str_lib.image(
      "glavna_slika.png",
      use_container_width=True,
      caption="Glavni ekran programa OFIX",
  )
except:
  str_lib.info(
      "[Ovde će se prikazati glavna slika headera kada je dodate u GitHub"
      " repo]"
  )

str_lib.write("---")  # Horizontalna linija za razdvajanje

# --- 2. GLAVNI SADRŽAJ: LEVO TEKST, DESNO 3 SLIKE JEDNA ISPOD DRUGE ---

# Delimo stranicu na 2 glavne kolone: leva šira (za tekst), desna uža (za 3 slike)
kolona_tekst, kolona_slike = str_lib.columns([2, 1])

with kolona_tekst:
  str_lib.header("O programu OFIX")
  str_lib.write("""
        **OFIX** je knjigovodstveno-kancelarijsko rešenje, namenjeno za brzo i jednostavno izdavanje računa i predračuna. 
        Idealan je alat za svakodnevnu upotrebu vlasnicima i osoblju malih i srednjih preduzeća, zanatskih, trgovinskih i uslužnih radnji, komisiona i veleprodaja.

        ### Ključne funkcije:
        * **Jednostavna baza podataka:** kupaca, artikala, dobavljača i izdatih dokumenata.
        * **Evidencija:** stanja lagera, potraživanja i dugovanja.
        * **Izveštaji:** automatski kreirani izveštaji po kupcu i datumu.
        * **Jednostavnost:** prilagođeno korisnicima bez IT predznanja.

        ### Važne napomene:
        * OFIX ne služi za izdavanje e-faktura.
        * Nije zamena za knjigovođu niti štampa knjige.
        * Predstavlja efikasan poslovni alat za internu evidenciju i brže poslovanje.
        * Optimizovano za rad na neograničenom broju računara.
        * Uz program se dobija godina dana besplatne tehničke podrške autora.

        ### Kontaktirajte nas:
        Za dodatne informacije i prezentaciju, obratite nam se putem email-a:
        * magicamp@bluewin.ch
        * magy@usa.com
    """)

with kolona_slike:
  str_lib.subheader("Galerija / Detalji")

  # 3 slike jedna ispod druge sa desne strane
  slike_nazivi = [
      "slika1.png",
      "slika2.png",
      "slika3.png",
  ]  # Zameni sa svojim nazivima fajlova
  for i, naziv in enumerate(slike_nazivi, start=1):
    try:
      str_lib.image(
          naziv, use_container_width=True, caption=f"Detalj {i}"
      )
    except:
      str_lib.text(f"[Slika {i} - dodajte u repo: {naziv}]")

# Podnožje stranice
str_lib.write("---")
str_lib.caption(
    "© 2026 OFIX by Magicomp. Sva prava zadržana."
)
