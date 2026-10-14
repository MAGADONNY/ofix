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
str_lib.markdown("#### Efikasan alat za brzo izdavanje A4 računa i evidenciju poslovanja.")

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

str_lib.markdown("---")  # Horizontalna linija za razdvajanje

# --- 2. GLAVNI SADRŽAJ: ---

# Linija 49: Vraćamo tačnu proporciju kolona (tekst širi, slike desno)
kolona_tekst, kolona_slike = str_lib.columns([2, 1])

with kolona_tekst:
    str_lib.markdown("## O programu OFIX")
    
    # Prvi pasus
    str_lib.markdown("**OFIX** je knjigovodstveno-kancelarijski program, namenjen za brzo i jednostavno izdavanje računa i predračuna.  \nIdealan je alat za svakodnevnu upotrebu vlasnicima i osoblju malih i srednjih preduzeća, zanatskih, trgovinskih i uslužnih radnji, komisiona i veleprodaja.")

    # Ključne funkcije
    str_lib.markdown("### Ključne funkcije:")
    str_lib.markdown("* **Jednostavna baza podataka:** kupaca, artikala, dobavljača i izdatih dokumenata.")
    str_lib.markdown("* **Evidencija:** stanja lageru, potraživanja i dugovanja.")
    str_lib.markdown("* **Izveštaji:** automatski kreirani izveštaji po kupcu, datumu, artiklu...")
    str_lib.markdown("* **Jednostavnost:** prilagođeno korisnicima bez IT predznanja.")
    str_lib.markdown("* **Veoma brz:** velicina svega oko 20MB, radi i bez interneta i na starijim racunarima.")

    # Verzije
    str_lib.markdown("### Nudimo dve Verzije OFIX-a:")
    str_lib.markdown("* **STANDARD** - mogucnost odobravanja rabata na ceo iznos racuna.")
    str_lib.markdown("* **RABAT** - mogucnost rabata (razlicitog) na svaku stavku na racunu.")
    str_lib.markdown("Jedina razlika izmedju verzija je ta sto RABAT verzija omogucava razlicit rabat za svaku stavku na racunu a STANDARD rabat na ceo iznos racuna.")

    # Važne napomene
    str_lib.markdown("### Važne napomene:")
    str_lib.markdown("* Za pokretanje OFIX-a je potrebno imati instaliran **Microsoft ACCESS** (vise informacija).")
    str_lib.markdown("* OFIX ne služi za izdavanje e-faktura.")
    str_lib.markdown("* Omogucena instalacija i rad na **neograničenom broju računara**.")
    str_lib.markdown("* Godinu dana **besplatne tehničke podrške** autora.")

    # Cene
    str_lib.markdown("### Nacin kupovine i cena:")
    str_lib.markdown("* Godisnja preplata & Trajna kupovina.")
    str_lib.markdown("* **OFIX STANDARD** **59€/godisnje** ili **249€/trajna licenca**.")
    str_lib.markdown("* **OFIX RABAT** **89€/godisnje** ili **349€/trajna licenca**.")
    str_lib.markdown("Autor pruza besplatnu tehnicku podrsku godinu dana (Telefonom, emailom ili putem TeamViewer-a).")

    # Kontakt
    str_lib.markdown("### Kontakt:")
    str_lib.markdown("Za dodatne informacije i **besplatnu** demo verziju mozete nas kontaktirati:")
    str_lib.markdown("* **magicamp@bluewin.ch**")
    str_lib.markdown("* **magy@usa.com**")
    str_lib.markdown("* Tel. **063 310 850**")


# --- 3. SEGMENT SA DESNE STRANE ZA SLIKE ---
with kolona_slike:
    str_lib.markdown("## Ekran programa")
    
    try:
        str_lib.image("2.JPG", caption="Prikaz rada u programu", use_container_width=True)
        str_lib.image("3.JPG", caption="Kreiranje računa", use_container_width=True)
        str_lib.image("4.JPG", caption="Izgled gotovog računa spremnog za stampu", use_container_width=True)
    except:
        str_lib.info("[Dodajte slike 2.JPG, 3.JPG i 4.JPG u GitHub repo da se prikažu ovde]")
