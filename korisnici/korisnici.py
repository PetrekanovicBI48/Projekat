from korisnici.korisniciIO import ucitaj_korisnike, sacuvaj_korisnike
from util import unos_sa_proverom

def prijava():
    korisnici = ucitaj_korisnike()
    korisncko_ime = input("korisnicko ime: ")
    lozinka = input("loznika: ")

    for korisnik in korisnici:
        if korisnik['korisnicko_ime'] == korisncko_ime and korisnik['lozinka'] == lozinka:
            return korisnik
    return None

duzina = [1, 1, 1, 1, 1]
kljuc = ['korisnicko_ime', 'lozinka', 'ime', 'prezime', 'tip_korisnika']


def sort():
    korisnici = ucitaj_korisnike()
    while True:
        print("\n Sortiraj po:"
              "\n1. Imenu"
              "\n2. Prezimenu"
              "\n3. Tipu korisnika"
              "\n0. Nazad")
        stavka = int(input("Izaberite opciju:"))

        if stavka == 1:
            sorter = 'ime'
            break
        elif stavka == 2:
            sorter = 'prezime'
            break
        elif stavka == 3:
            sorter = 'tip_korisnika'
            break
        elif stavka == 0:
            return False
        else:
            print("Pogresan unos!")

    if sorter == 'ime':
        korisnici.sort(key=lambda korisnici: korisnici.get('ime'))

    elif sorter == 'prezime':
        korisnici.sort(key=lambda korisnici: korisnici.get('prezime'))

    elif sorter == 'tip_korisnika':
        korisnici.sort(key=lambda korisnici: korisnici.get('tip_korisnika'))

    ispis_korisnika(korisnici)


def ispis_korisnika(korisnici):
    zaglavlje = f"{'ime':<10}" \
                f"{'prezime':<20}" \
                f"{'tip_korisnika':<20}"

    print(zaglavlje)
    print("<*>" * len(zaglavlje))

    for korisnik in korisnici:
        za_ispis = f"{korisnik['ime']:<10}" \
                   f"{korisnik['prezime']:<20}" \
                   f"{korisnik['tip_korisnika']:<20}"
        print(za_ispis)


def registracija():
    korisnici = ucitaj_korisnike()
    while True:
        korisnicko_ime = unos_sa_proverom("\nKorisnicko ime(upisite 'nazad' kako bi ste napustili registraciju): ",
                                          "Korisnicko ime")
        if korisnicko_ime == 'nazad':
            return

        postojece_korisnicko_ime = False
        for korisnik in korisnici:
            if korisnik['korisnicko_ime'] == korisnicko_ime:
                postojece_korisnicko_ime = True
                print("Korisnicko ime je vec zauzeto. Pokusajte drugo!")
                break

        if postojece_korisnicko_ime == False:
            break

    lozinka = unos_sa_proverom("Lozinka: ", "Lozinka")
    ime = input("Ime:")
    prezime = input("Prezime:")

    while True:
        tip_korisnika = input("Pristup menadzera ili prodavca(m/p):")
        if tip_korisnika == 'm' or tip_korisnika == 'p':
            break
        else:
            print("Pogresan tip korisnika! Pokusajte ponovo!")

    novi_korsinik = {}
    novi_korsinik['korisnicko_ime'] = korisnicko_ime
    novi_korsinik['lozinka'] = lozinka
    novi_korsinik['ime'] = ime
    novi_korsinik['prezime'] = prezime

    if tip_korisnika == 'm':
        novi_korsinik['tip_korisnika'] = 'Menadzer'
    else:
        novi_korsinik['tip_korisnika'] = 'Prodavac'
    print("\n Korisnik se dodaje:")

    ispis_korisnika([novi_korsinik])

    korisnici.append(novi_korsinik)
    sacuvaj_korisnike(korisnici)
    print("%s je dodat u korisnike bazu podaatka.Tip korisnika=[%s]" % (novi_korsinik['korisnicko_ime'], novi_korsinik['tip_korisnika']))
