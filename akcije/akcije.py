from akcije.akcijeIO import ucitaj_akcije,sacuvaj_akcije

akcije=ucitaj_akcije()
n=len(akcije)

kljuc=['sifra','artikli','datum_vazenja']
def pretraga_akcija_string(kljuc, vrednost):
    akcije = ucitaj_akcije()
    f_akcije = []

    for akcija in akcije:
        if vrednost.lower() in akcija[kljuc].lower():
            f_akcije.append(akcija)

    return f_akcije


def pretraga_akcija_jednakost(kljuc, vrednost):
    akcije = ucitaj_akcije()
    f_akcije = []

    for akcija in akcije:
        if vrednost == akcije[kljuc]:
            f_akcije.append(akcija)

    return f_akcije


def pretrazi_akcija():
    print("\n1. Pretraga po sifri")
    print("2. Pretraga po artiklu")
    print("3. Pretraga po datumu vazenja")
    print("0. Napusti pretragu")
    stavka = int(input("Izaberite stavku: "))
    akcije = []
    if stavka == 1:
        sifra = int(input("Unesite sifru: "))
        akcije = pretraga_akcija_jednakost("sifra", sifra)
    elif stavka == 2:
        artikli = input("Unesite nalsov: ")
        akcije = pretraga_akcija_string("artikli", artikli)
    elif stavka == 3:
        datum_vazenja = input("Unesite datum vazenja: ")
        akcije = pretraga_akcija_jednakost("datum_vazenja", datum_vazenja)
    elif stavka==0:
        return
    else:
        print("Pogresan unos")

    ispis_akcija(akcije)

def ispis_akcija(akcije):
    zaglavlje = f"{'sifra':<10}" \
               f"{'artikli':<20}" \
               f"{'Datum vazenja':^20}"

    print(zaglavlje)
    print("-"*len(zaglavlje))

    for akcija in akcije:
        za_ispis = f"{akcija['sifra']:<10}" \
                   f"{akcija['artikli']:<20}" \
                   f"{akcija['datum_vazenja']:^20}"
        print(za_ispis)
