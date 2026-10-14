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
  str_lib.markdown("""
**OFIX** je knjigovodstveno-kancelarijski program, namenjen za brzo i jednostavno izdavanje računa i predračuna.  
Idealan je alat za svakodnevnu upotrebu vlasnicima i osoblju malih i srednjih preduzeća, zanatskih, trgovinskih i uslužnih radnji, komisiona i veleprodaja.  

        ### Ključne funkcije:
* **Jednostavna baza podataka:** kupaca, artikala, dobavljača i izdatih dokumenata.
* **Evidencija:** stanja lagera, potraživanja i dugovanja.
* **Izveštaji:** automatski kreirani izveštaji po kupcu, datumu, artiklu...
* **Jednostavnost:** prilagođeno korisnicima bez IT predznanja.
* **Veoma brz:** veličina svega oko 20MB, radi i bez interneta i na starijim računarima.

### Nudimo dve Verzije OFIX-a:
* **STANDARD** - mogućnost odobravanja rabata na ceo iznos računa.
* **RABAT** - mogućnost rabata (različitog) na svaku stavku na računu.  
Jedina razlika između verzija je ta što RABAT verzija omogućava različit rabat za svaku stavku na računu, a STANDARD rabat na ceo iznos računa.

### Važne napomene:
* Za pokretanje OFIX-a je potrebno imati instaliran Microsoft ACCESS (više informacija).
* OFIX ne služi za izdavanje e-faktura.
* Omogućena instalacija i rad na neograničenom broju računara.
* Godinu dana besplatne tehničke podrške autora.

### Način kupovine i cena:
* Godišnja pretplata & Trajna kupovina
* OFIX STANDARD 59€/godišnje ili 249€/trajna licenca
* OFIX RABAT 89€/godišnje ili 349€/trajna licenca  
Autor pruža besplatnu tehničku podršku godinu dana (Telefonom, emailom ili putem TeamViewer-a).

### Kontakt:
Za dodatne informacije i **besplatnu** demo verziju možete nas kontaktirati:
* magicamp@bluewin.ch
* magy@usa.com
* Tel. 063 310 850
