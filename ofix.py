import streamlit as str_lib

# 1. Podešavanje stranice
str_lib.set_page_config(
    page_title="OFIX - Knjigovodstveni program",
    page_icon="📊",
    layout="wide",
)

# 2. Glavni Header (Slika na vrhu)
try:
    str_lib.image("newofix.jpg", use_container_width=True)
except:
    str_lib.markdown("## **OFIX – Knjigovodstveno-kancelarijski program**")
    str_lib.markdown("#### Efikasan alat za brzo izdavanje A4 računa i evidenciju poslovanja.")

str_lib.divider()

# 3. Organizacija podataka u čist Python rečnik (Nema ponavljanja str_lib komandi!)
podaci_o_programu = {
    "Ključne funkcije": [
        "**Jednostavna baza podataka:** kupaca, artikala, dobavljača i izdatih dokumenata.",
        "**Evidencija:** stanja lagera, potraživanja i dugovanja.",
        "**Izveštaji:** automatski kreirani izveštaji po kupcu, datumu, artiklu...",
        "**Jednostavnost:** prilagođeno korisnicima bez IT predznanja.",
        "**Veoma brz:** veličina svega oko 20MB, radi i bez interneta i na starijim računarima."
    ],
    "Nudimo dve verzije OFIX-a": [
        "**STANDARD** - mogućnost odobravanja rabata na ceo iznos računa.",
        "**RABAT** - mogućnost rabata (različitog) na svaku stavku na računu.",
        "Jedina razlika između verzija je ta što RABAT verzija omogućava različit rabat za svaku stavku na računu, a STANDARD rabat na ceo iznos računa."
    ],
    "Važne napomene": [
        "Za pokretanje OFIX-a je potrebno imati instaliran **Microsoft ACCESS**.",
        "OFIX ne služi za izdavanje e-faktura.",
        "Omogućena instalacija i rad na **neograničenom broju računara**.",
        "Godinu dana **besplatne tehničke podrške** autora."
    ],
    "Način kupovine i cena": [
        "Godišnja pretplata & Trajna kupovina.",
        "**OFIX STANDARD:** **59€ / godišnje** ili **249€ / trajna licenca**.",
        "**OFIX RABAT:** **89€ / godišnje** ili **349€ / trajna licenca**.",
        "Autor pruža besplatnu tehničku podršku godinu dana (telefonom, emailom ili putem TeamViewer-a)."
    ],
    "Kontakt": [
        "Za dodatne informacije i **besplatnu** demo verziju možete nas kontaktirati:",
        "Email 1: **magicamp@bluewin.ch**",
        "Email 2: **magy@usa.com**",
        "Telefon: **063 310 850**"
    ]
}

# 4. Raspored elemenata: Koristimo Tabove za čist i moderan izgled
tab_tekst, tab_slike = str_lib.tabs(["📋 DETALJI O PROGRAMU", "🖼️ EKRANI I SLIKE"])

# Ispis tekstualnih segmenata pomoću jedne brze petlje
with tab_tekst:
    str_lib.markdown("### **O programu OFIX**")
    str_lib.markdown("**OFIX** je knjigovodstveno-kancelarijski program, namenjen za brzo i jednostavno izdavanje računa i predračuna. Idealan je alat za svakodnevnu upotrebu vlasnicima i osoblju malih i srednjih preduzeća, zanatskih, trgovinskih i uslužnih radnji, komisiona i veleprodaja.")
    
    # Petlja prolazi kroz rečnik i sama pravi naslove i stavke
    for naslov, stavke in podaci_o_programu.items():
        str_lib.markdown(f"### **{naslov}**")
        for stavka in stavke:
            # Ako stavka ne treba da ima tačku ispred (običan tekst unutar rečnika)
            if "Jedina razlika" in stavka or "Autor pruža" in stavka or "Za dodatne" in stavka or "Godišnja" in stavka:
                str_lib.markdown(stavka)
            else:
                str_lib.markdown(f"🔹 {stavka}")  # Plavi kvadrat umesto obične tačke (popravlja uočljivost BOLD-a na tamnoj temi)

# Prikaz slika u posebnoj kartici, poređane jedna pored druge (horizontalno)
with tab_slike:
    str_lib.markdown("### **Vizuelni prikaz rada u programu OFIX**")
    kol1, kol2, kol3 = str_lib.columns(3)
    
    slike = [("2.JPG", "Prikaz rada u programu"), ("3.JPG", "Kreiranje računa"), ("4.JPG", "Izgled gotovog računa spremnog za štampu")]
    kolone = [kol1, kol2, kol3]
    
    for kolona, (fajl, opis) in zip(kolone, slike):
        with kolona:
            try:
                str_lib.image(fajl, caption=opis, use_container_width=True)
            except:
                str_lib.info(f"[Slika {fajl} nedostaje]")
