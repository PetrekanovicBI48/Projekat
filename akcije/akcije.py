from akcije.akcijeIO import ucitaj_akcije
from knjige.knjige import ucitaj_knjige, sacuvaj_knjige

akcije = ucitaj_akcije()
n = len(akcije)
knjige = ucitaj_knjige()

kljuc = ['sifra', 'autor', 'kategorija', 'cena']


def pretraga_akcija_string(kljuc, vrednost):
    akcije = ucitaj_akcije()
    filtrirane_akcije = []

    for akcija in akcije:
        if vrednost.lower() in akcija[kljuc].lower():
            filtrirane_akcije.append(akcija)
    return filtrirane_akcije


def pretraga_akcija_jednakost(kljuc,vrednost):
    akcije=ucitaj_akcije()
    filtritane_akcije=[]

    for akcija in akcije:
        if vrednost==akcija[kljuc]:
            filtritane_akcije.append(akcija)
        return filtritane_akcije

def sort():
    while True:
        print("\nSortiraj po"
              "\n1. sifri"
              "\n2. datum vazenja"
              "\n0. nazad")
        stavka = input("Opcija:")
        if stavka == 1:
            sorter = 'sifra'
            break
        elif stavka == 2:
            sorter = 'datum_vazenja'
            break
        elif stavka == 0:
            return False
        else:
            print("pogresan unos!")

    if sorter == 'sifra':
        akcije.sort(key=lambda akcije: akcije.get('sifra'))
    if sorter == 'datum_vazenja':
        akcije.sort(key=lambda akcije: akcije.get('datum_vazenja'))
    ispis_akcija(akcije)


def pretrazi_akcija():
    print("\n1. Pretraga po sifri")
    print("2. Pretraga po naslovu")
    print("3. Pretraga po autoru")
    print("4. Pretraga po kategoriji")
    print("0. Napusti pretragu")
    stavka = int(input("Izaberite stavku: "))
    akcije = []
    if stavka == 1:
        sifra = int(input("Unesite sifru: "))
        akcije = pretraga_akcija_jednakost("sifra", sifra)
    elif stavka == 2:
        naslov = input("Unesite nalsov: ")
        akcije = pretraga_akcija_string("artikli", naslov)
    elif stavka == 3:
        datum_vazenja = input("Unesite datum vazenja: ")
        akcije = pretraga_akcija_jednakost("datum_vazenja", datum_vazenja)
    elif stavka == 4:
        kategorija = input("Unesite kategoriju:")
        akcije = pretraga_akcija_string('kategorija', kategorija)
    elif stavka == 0:
        return
    else:
        print("Pogresan unos")


    ispis_akcija(akcije)


def ispis_akcija(akcije):
    zaglavlje = f"{'sifra':<10}" \
                f"{'naslov':<20}" \
                f"{'autor':^20}"\
                f"{'kategorija':^20}"

    print(zaglavlje)
    print("-" * len(zaglavlje))

    for akcija in akcije:
        za_ispis = f"{akcija['sifra']:<10}" \
                   f"{akcija['naziv']:<20}" \
                   f"{akcija['autor']:^20}"\
                   f"{akcija['kategorija']:^20}"

        print(za_ispis)


def registracija_akcija():
    for akcija in akcije:
        sifra = akcija['sifra']
    sifra += 1
    naslov = input('naslov:')
    autor = input('autor:')
    isbn = input('isbn:')
    izdavac = input('izdavac:')
    godina = int(input('godina:'))
    cena = float(input('cena'))
    broj_strana = int(input('broj strana:'))
    kategorija = input('kategorija:')
    nova_knjiga = {
        "sifra": 3,
        "naslov": "Knjiga 1",
        "autor": "Pera Peric",
        "isbn": "1312312312312",
        "izdavac": "Vulkan",
        "broj strana": "231",
        "godina": 2020,
        "cena": 650.0,
        "kategorija": "Roman"
    }
    nova_knjiga['sifra'] = sifra
    nova_knjiga['naslov'] = naslov
    nova_knjiga['autor'] = autor
    nova_knjiga['isbn'] = isbn
    nova_knjiga['izdavac'] = izdavac
    nova_knjiga['broj strana'] = broj_strana
    nova_knjiga['godina'] = godina
    nova_knjiga['cena'] = cena
    nova_knjiga['kategorija'] = kategorija

    knjige.append(nova_knjiga)
    sacuvaj_knjige(knjige)
    print('%s je dodata u bazu podataka. Knjiga sifra=[%s]' % (nova_knjiga['naslov'], nova_knjiga['sifra']))
    return False
