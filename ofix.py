import streamlit as str_lib

# 1. Podešavanje stranice za maksimalnu estetiku
str_lib.set_page_config(
    page_title="OFIX - Knjigovodstveni program",
    page_icon="📊",
    layout="wide",
)

# 2. TEKST NA SAMOM VRHU STRANICE (IZNAD SLIKE)
str_lib.title(":blue[OFIX – Knjigovodstveno-kancelarijski program]")
str_lib.subheader("Efikasan alat za brzo izdavanje A4 računa i evidenciju poslovanja.")

# 3. Glavna slika na vrhu (Header) ispod teksta
try:
    str_lib.image("newofix.jpg", use_container_width=True)
except:
    str_lib.info("[Glavna slika 'newofix.jpg' trenutno nije dostupna na GitHub-u]")

str_lib.divider()

# 4. Kreiranje polja: Popravljena linija dodavanjem [2, 1] unutar zagrada columns()
kolona_tekst, kolona_slike = str_lib.columns([2, 1])

# --- DESNA KOLONA: 3 SLIKE VERTIKALNO ---
with kolona_slike:
    str_lib.markdown("### :blue[Ekrani programa]")
    slike_lista = [
        ("2.JPG", "Prikaz rada u programu"),
        ("3.JPG", "Kreiranje računa"),
        ("4.JPG", "Izgled gotovog računa spreman za štampu")
    ]
    for fajl, opis in slike_lista:
        try:
            str_lib.image(fajl, caption=opis, use_container_width=True)
            str_lib.write("")  # Razmak između slika
        except:
            str_lib.info(f"[Slika {fajl} nedostaje]")

# --- LEVA KOLONA: STRUKTURIRANI SADRŽAJ ---
with kolona_tekst:
    str_lib.markdown("## :blue[O programu OFIX]")
    str_lib.markdown("OFIX je knjigovodstveno-kancelarijski program, namenjen za brzo i jednostavno izdavanje računa i predračuna. Idealan je alat za svakodnevnu upotrebu vlasnicima i osoblju malih i srednjih preduzeća, zanatskih, trgovinskih i uslužnih radnji, komisiona i veleprodaja.")
    
    # Podaci spakovani u čist Python rečnik
    sajt_data = {
        "Ključne funkcije": [
            ("Jednostavna baza podataka", "kupaca, artikala, dobavljača i izdatih dokumenata."),
            ("Evidencija", "stanja lagera, potraživanja i dugovanja."),
            ("Izveštaji", "automatski kreirani izveštaji po kupcu, datumu, artiklu..."),
            ("Jednostavnost", "prilagođeno korisnicima bez IT predznanja."),
            ("Veoma brz", "veličina svega oko 20MB, radi i bez interneta i na starijim računarima.")
        ],
        "Nudimo dve verzije OFIX-a": [
            ("STANDARD", "mogućnost odobravanja rabata na ceo iznos računa."),
            ("RABAT", "mogućnost rabata (različitog) na svaku stavku na računu."),
            ("Napomena", "Jedina razlika između verzija je ta što RABAT verzija omogućava različit rabat za svaku stavku na računu, a STANDARD rabat na ceo iznos računa.")
        ],
        "Važne napomene": [
            ("Microsoft ACCESS", "Za pokretanje OFIX-a je potrebno imati instaliran ovaj program (više informacija)."),
            ("e-fakture", "OFIX ne služi za izdavanje e-faktura."),
            ("Instalacija", "Omogućena instalacija i rad na neograničenom broju računara."),
            ("Tehnička podrška", "Godinu dana besplatne tehničke podrške autora.")
        ],
        "Način kupovine i cena": [
            ("Modeli", "Godišnja pretplata & Trajna kupovina."),
            ("OFIX STANDARD", "59€ / godišnje ili 249€ / trajna licenca."),
            ("OFIX RABAT", "89€ / godišnje ili 349€ / trajna licenca."),
            ("Podrška", "Autor pruža besplatnu tehničke podršku godinu dana (telefonom, emailom ili putem TeamViewer-a).")
        ],
        "Kontakt": [
            ("Upiti", "Za dodatne informacije i besplatnu demo verziju možete nas kontaktirati:"),
            ("Email 1", "magicamp@bluewin.ch"),
            ("Email 2", "magy@usa.com"),
            ("Telefon", "063 310 850")
        ]
    }

    # Ispis kroz čiste i standardne Streamlit stringove
    for sekcija, stavke in sajt_data.items():
        str_lib.markdown(f"### :blue[{sekcija}]")
        
        for kljuc, vrednost in stavke:
            if kljuc in ["Napomena", "Modeli", "Podrška", "Upiti"]:
                str_lib.write(vrednost)
            else:
                str_lib.write(f"🔹 :blue[{kljuc}]: {vrednost}")
