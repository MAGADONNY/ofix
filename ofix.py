import streamlit as str_lib  # Možeš koristiti i samo 'import streamlit as st'

# Podešavanje stranice (naslov u browser tabu)
str_lib.set_page_config(
    page_title="OFIX - Knjigovodstveni program",
    page_icon="📊",
    layout="wide",
)

# ---CSS BLOK ---
str_lib.markdown(
    """
    <style>
    .block-container {
        padding-top: 1.5rem; 
    }
    </style>
""",
    unsafe_allow_html=True,
    )

# --- 1. GORNJI DEO (HEADER) ZA GLAVNU SLIKU ---
str_lib.markdown("## OFIX – Knjigovodstveno-kancelarijski program")
str_lib.write(
    "#### Efikasan alat za brzo izdavanje A4 računa i evidenciju poslovanja."
)

# ----- 'glavna_slika ------
try:
  str_lib.image(
      "newofix.jpg",
      use_container_width=True,
      #caption="Glavni ekran programa OFIX",
  )
except:
  str_lib.info(
      "[Ovde će se prikazati glavna slika headera kada je dodate u GitHub"
      " repo]"
  )

str_lib.write("---")  # Horizontalna linija za razdvajanje

# --- 2. GLAVNI SADRŽAJ: ---

kolona_tekst, kolona_slike = str_lib.columns([2, 1])

with kolona_tekst:
  str_lib.header("O programu OFIX")
  str_lib.write("""
**OFIX** je knjigovodstveno-kancelarijski program, namenjen za brzo i jednostavno izdavanje računa i predračuna.  
Idealan je alat za svakodnevnu upotrebu vlasnicima i osoblju malih i srednjih preduzeća, zanatskih, trgovinskih i uslužnih radnji, komisiona i veleprodaja.

        ### Ključne funkcije:
        * **Jednostavna baza podataka:** kupaca, artikala, dobavljača i izdatih dokumenata.
        * **Evidencija:** stanja lagera, potraživanja i dugovanja.
        * **Izveštaji:** automatski kreirani izveštaji po kupcu, datumu, artiklu...
        * **Jednostavnost:** prilagođeno korisnicima bez IT predznanja.
        * **Veoma brz velicina svega oko 20MB, radi i bez interneta i na starijim racunarima

        ### Nudimo dve Verzije OFIX-a:
        * **STANDARD** -  mogucnost odobravanja rabata na ceo iznos racuna
        * **RABAT** - mogucnost rabata (razlicitog) na svaku stavku na racunu.  
          Jedina razlika izmedju verzija je ta sto RABAT verzija omogucava razlicit rabat za **svaku stavku** na racunu a STANDARD rabat na ceo iznos racuna.

        ### Važne napomene:
        * Za pokretanje OFIX-a je potrebno imati instaliran **Microsoft ACCESS** (vise informacija)
        * OFIX ne služi za izdavanje e-faktura.
        * Omogucena instalacija i rad na neograničenom broju računara.
        * Godinu dana besplatne tehničke podrške autora.

        ### Nacin kupovine i cena:
        * Godisnja preplata & Trajna kupovina
        * OFIX STANDARD 59€/godisnje. ili 249€/trajna licenca
        * OFIX RABAT 89€/godisnje ili 349€/trajna licenca.  
Autor pruza besplatnu tehnicku podrsku godinu dana {Telefonom, emailom ili putem TeamViewer-a)

        ### Kontakt:
        Za dodatne informacije i **besplatnu** demo verziju mozete nas kontaktirati:
        * magicamp@bluewin.ch
        * magy@usa.com
        * Tel. 063 310 850
    """)

with kolona_slike:
  str_lib.subheader("Galerija")

  # 3 slike jedna ispod druge sa desne strane
  slike_nazivi = [
      "2.JPG",
      "3.JPG",
      "4.JPG",
  ]  
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
