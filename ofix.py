import streamlit as str_lib

# 1. Podešavanje stranice i strukture
str_lib.set_page_config(
    page_title="OFIX - Knjigovodstveni program",
    page_icon="📊",
    layout="wide",
)

# 2. Glavni naslov i podnaslov aplikacije
str_lib.title("OFIX – Knjigovodstveno-kancelarijski program")
str_lib.subheader("Efikasan alat za brzo izdavanje A4 računa i evidenciju poslovanja.")

# 3. Glavna slika (Header)
try:
    str_lib.image("newofix.jpg", use_container_width=True)
except:
    str_lib.info("[Glavna slika 'newofix.jpg' će se prikazati kada je dodate u GitHub]")

str_lib.divider()  # Čista Streamlit linija za razdvajanje

# 4. Podela na kolone (Tekst levo, Slike desno)
kolona_tekst, kolona_slike = str_lib.columns([2, 1])

# --- LEVA KOLONA: SADRŽAJ I INFORMACIJE ---
with kolona_tekst:
    str_lib.header("O programu OFIX")
    
    # Prvi pasus - isticanje reči OFIX preko čistog markdown parametra
    str_lib.markdown("**OFIX** je knjigovodstveno-kancelarijski program, namenjen za brzo i jednostavno izdavanje računa i predračuna.")
    str_lib.markdown("Idealan je alat za svakodnevnu upotrebu vlasnicima i osoblju malih i srednjih preduzeća, zanatskih, trgovinskih i uslužnih radnji, komisiona i veleprodaja.")
    
    # Sekcija: Ključne funkcije
    str_lib.subheader("Ključne funkcije")
    str_lib.markdown("- **Jednostavna baza podataka:** kupaca, artikala, dobavljača i izdatih dokumenata.")
    str_lib.markdown("- **Evidencija:** stanja lagera, potraživanja i dugovanja.")
    str_lib.markdown("- **Izveštaji:** automatski kreirani izveštaji po kupcu, datumu, artiklu...")
    str_lib.markdown("- **Jednostavnost:** prilagođeno korisnicima bez IT predznanja.")
    str_lib.markdown("- **Veoma brz:** veličina svega oko 20MB, radi i bez interneta i na starijim računarima.")
    
    # Sekcija: Verzije
    str_lib.subheader("Nudimo dve verzije OFIX-a")
    str_lib.markdown("- **STANDARD** - mogućnost odobravanja rabata na ceo iznos računa.")
    str_lib.markdown("- **RABAT** - mogućnost rabata (različitog) na svaku stavku na računu.")
    str_lib.markdown("Jedina razlika između verzija je ta što RABAT verzija omogućava različit rabat za svaku stavku na računu, a STANDARD rabat na ceo iznos računa.")
    
    # Sekcija: Važne napomene
    str_lib.subheader("Važne napomene")
    str_lib.markdown("- Za pokretanje OFIX-a je potrebno imati instaliran **Microsoft ACCESS**.")
    str_lib.markdown("- OFIX ne služi za izdavanje e-faktura.")
    str_lib.markdown("- Omogućena instalacija i rad na **neograničenom broju računara**.")
    str_lib.markdown("- Godinu dana **besplatne tehničke podrške** autora.")
    
    # Sekcija: Kupovina i cena
    str_lib.subheader("Način kupovine i cena")
    str_lib.markdown("- Godišnja pretplata & Trajna kupovina.")
    str_lib.markdown("- **OFIX STANDARD:** **59€ / godišnje** ili **249€ / trajna licenca**.")
    str_lib.markdown("- **OFIX RABAT:** **89€ / godišnje** ili **349€ / trajna licenca**.")
    str_lib.markdown("Autor pruža besplatnu tehničku podršku godinu dana (telefonom, emailom ili putem TeamViewer-a).")
    
    # Sekcija: Kontakt
    str_lib.subheader("Kontakt")
    str_lib.markdown("Za dodatne informacije i **besplatnu** demo verziju možete nas kontaktirati:")
    str_lib.markdown("- Email 1: **magicamp@bluewin.ch**")
    str_lib.markdown("- Email 2: **magy@usa.com**")
    str_lib.markdown("- Telefon: **063 310 850**")

# --- DESNA KOLONA: SLIKE PROGRAMA ---
with kolona_slike:
    str_lib.header("Ekran programa")
    
    try:
        str_lib.image("2.JPG", caption="Prikaz rada u programu", use_container_width=True)
        str_lib.image("3.JPG", caption="Kreiranje računa", use_container_width=True)
        str_lib.image("4.JPG", caption="Izgled gotovog računa spremnog za štampu", use_container_width=True)
    except:
        str_lib.info("[Dodajte slike '2.JPG', '3.JPG' i '4.JPG' u GitHub da se prikažu ovde]")
