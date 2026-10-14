import streamlit as str_lib

# 1. Podešavanje stranice
str_lib.set_page_config(
    page_title="OFIX - Knjigovodstveni program",
    page_icon="📊",
    layout="wide",
)

# 2. GLAVNA SLIKA (HEADER) NA SAMOM VRHU
try:
    str_lib.image("newofix.jpg", use_container_width=True)
except:
    str_lib.title("OFIX – Knjigovodstveno-kancelarijski program")
    str_lib.subheader("Efikasan alat za brzo izdavanje A4 računa i evidenciju poslovanja.")

str_lib.divider()

# 3. GALERIJA: Prostor za 3 slike programa poređane horizontalno
str_lib.subheader("Pogledajte izgled i rad u programu")
kol1, kol2, kol3 = str_lib.columns(3)

ekrani = [
    ("2.JPG", "Prikaz rada u programu"),
    ("3.JPG", "Kreiranje računa"),
    ("4.JPG", "Izgled gotovog računa spremnog za štampu")
]

for kolona, (fajl, opis) in zip([kol1, kol2, kol3], ekrani):
    with kolona:
        try:
            str_lib.image(fajl, caption=opis, use_container_width=True)
        except:
            str_lib.info(f"[Nedostaje slika {fajl}]")

str_lib.divider()

# 4. ČISTA DATA STRUKTURA: Sav tekst je spakovan na jedno mesto bez ikakvog ponavljanja komandi
sadrzaj_sajta = [
    {
        "sekcija": "O programu OFIX",
        "tekst": "OFIX je knjigovodstveno-kancelarijski program, namenjen za brzo i jednostavno izdavanje računa i predračuna. Idealan je alat za svakodnevnu upotrebu vlasnicima i osoblju malih i srednjih preduzeća, zanatskih, trgovinskih i uslužnih radnji, komisiona i veleprodaja.",
        "stavke": []
    },
    {
        "sekcija": "Ključne funkcije",
        "tekst": "",
        "stavke": [
            ("Jednostavna baza podataka", "kupaca, artikala, dobavljača i izdatih dokumenata."),
            ("Evidencija", "stanja lagera, potraživanja i dugovanja."),
            ("Izveštaji", "automatski kreirani izveštaji po kupcu, datumu, artiklu..."),
            ("Jednostavnost", "prilagođeno korisnicima bez IT predznanja."),
            ("Veoma brz", "veličina svega oko 20MB, radi i bez interneta i na starijim računarima.")
        ]
    },
    {
        "sekcija": "Nudimo dve verzije OFIX-a",
        "tekst": "Jedina razlika između verzija je ta što RABAT verzija omogućava različit rabat za svaku stavku na računu, a STANDARD rabat na ceo iznos računa.",
        "stavke": [
            ("STANDARD", "mogućnost odobravanja rabata na ceo iznos računa."),
            ("RABAT", "mogućnost rabata (različitog) na svaku stavku na računu.")
        ]
    },
    {
        "sekcija": "Važne napomene",
        "tekst": "",
        "stavke": [
            ("Microsoft ACCESS", "Za pokretanje OFIX-a je potrebno imati instaliran ovaj program (više informacija)."),
            ("e-fakture", "OFIX ne služi za izdavanje e-faktura."),
            ("Instalacija", "Omogućena instalacija i rad na neograničenom broju računara."),
            ("Tehnička podrška", "Godinu dana besplatne tehničke podrške autora.")
        ]
    },
    {
        "sekcija": "Način kupovine i cena",
        "tekst": "U ponudi su godišnja pretplata i trajna kupovina. Autor pruža besplatnu tehničku podršku godinu dana (telefonom, emailom ili putem TeamViewer-a).",
        "stavke": [
            ("OFIX STANDARD", "59€ / godišnje ili 249€ / trajna licenca."),
            ("OFIX RABAT", "89€ / godišnje ili 349€ / trajna licenca.")
        ]
    },
    {
        "sekcija": "Kontakt",
        "tekst": "Za dodatne informacije i besplatnu demo verziju možete nas kontaktirati:",
        "stavke": [
            ("Email 1", "magicamp@bluewin.ch"),
            ("Email 2", "magy@usa.com"),
            ("Telefon", "063 310 850")
        ]
    }
]

# 5. AUTOMATSKI ISPIS: Jedna jedina petlja koja sama generiše kompletan sajt i garantuje BOLD font
for grupa in sadrzaj_sajta:
    str_lib.subheader(grupa["sekcija"])
    
    if grupa["tekst"]:
        str_lib.write(grupa["tekst"])
        
    for stavka in grupa["stavke"]:
        # Razdvajamo naslov stavke i opis, pa ih spajamo. 
        # Streamlit-ov .write() sa više argumenata garantovano generiše čist i vidljiv bold!
        str_lib.write(f"🔹 **{stavka[0]}:**", stavka[1])
