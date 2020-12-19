import getpass
import re

from korisnici.korisniciIO import ucitaj_korisnike, sacuvaj_korisnike

korisnici = ucitaj_korisnike()
n = len(korisnici)


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


def duzina_liste():
    max = '1'
    for i in range(5):
        max = len(str(korisnici[0][kljuc[i]]))
        for j in range(n - 1):
            if max < len(str(korisnici[j + 1][kljuc[i]])):
                max < len(str(korisnici[j + 1][kljuc[i]]))
            duzina[i] = max

def sort():
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
    print("-" * len(zaglavlje))

    for korisnik in korisnici:
        za_ispis = f"{korisnik['ime']:<10}" \
                   f"{korisnik['prezime']:<20}" \
                   f"{korisnik['tip_korisnika']:<20}"
        print(za_ispis)


def lista1(korisnici):
    duzina_liste()
    print('\nkorisnicko_ime', end="")
    for i in range(duzina[0] + 1):
        print(' ', end="")
    print('lozinka', end="")
    for i in range(duzina[1] + 1):
        print(' ', end="")
    print('ime', end="")
    for i in range(duzina[2] + 1):
        print(' ', end="")
    print('prezime', end="")
    for i in range(duzina[3] + 1):
        print(' ', end="")
    print('tip_korisnika', end="")
    for i in range(duzina[4] + 1):
        print(' ', end="")
    print('\n')
    for korisnik in korisnici:
        print(korisnik['korisnicko_ime'], end="")
        for i in range(duzina[0] + 9 - len(str(korisnik['korisnicko_ime']))):
            print(' ', end="")
        print(korisnik['lozinka'], end="")
        for i in range(duzina[1] + 9 - len(str(korisnik['lozinka']))):
            print(' ', end="")
        print(korisnik['ime'], end="")
        for i in range(duzina[2] + 5 - len(str(korisnik['ime']))):
            print(' ', end="")
        print(korisnik['prezime'], end="")
        for i in range(duzina[3] + 9 - len(str(korisnik['prezime']))):
            print(' ', end="")
        print(korisnik['tip_korisnika'], end="\n")
        i += 1


def admin_registracija():
    while True:
        korisnicko_ime = input("\nKorisnicko ime(upisite 'nazad' kako bi ste napustili registraciju):")
        greska = re.search(' ', korisnicko_ime)
        if greska is not None:
            print("Ime ne sme da sadrzi razmake!")
            continue
        if korisnicko_ime == '':
            print("Morate uneti ime!")
        break

    for korisnik in korisnici:
        if korisnik['korisnicko_ime'] == korisnicko_ime:
            print("Korisnicko ime je vec zauzeto.Pokusajte drugo")
            if not admin_registracija():
                return False
        if korisnicko_ime == 'nazad':
            return False
    while True:
        lozinka = getpass.getpass('lozinka')
        greska = re.search(' ', lozinka)
        if greska != None:
            print("lozinka ne sme da sadrzi razmak!")
            continue
        if lozinka == '':
            print("Niste uneli lozinku")
            continue
        break
    ime = input("ime:")
    prezime = input("prezime:")

    while True:
        tip_korisnika = input("Pristup menadzera ili prodavca(m/p):")
        if tip_korisnika != 'm' and tip_korisnika != 'p':
            print("Nemate dozvolu za izvrasavanje!!")
            continue
        break

    novi_korsinik = {
        "korisnicko_ime": "",
        "lozinka": "",
        "ime": "",
        "prezime": ""}
    novi_korsinik['korisnicko_ime']: korisnicko_ime
    novi_korsinik['lozinka']: lozinka
    novi_korsinik['ime']: ime
    novi_korsinik['prezime']: prezime

    if tip_korisnika == 'm':
        novi_korsinik['tip_korisnika'] = 'Menadzer'
    else:
        novi_korsinik['tip_korisnika'] = 'Prodavac'
    print("\n Korisnik se dodaje:")
    novi_korsinik = [novi_korsinik]
    lista1(novi_korsinik)
    while True:
        print("\nNastavite?"
              "1. Da"
              "2. Ne")
        stavka = input("Opcija:")
        if stavka == 1:
            korisnici.append(novi_korsinik)
            break
        elif stavka == 2:
            return False
        else:
            print("pogresan unos")

    sacuvaj_korisnike(korisnici)
    print("%s je dodat u korisnike bazu podaatka.Tip korisnika=[%s]" % (
    novi_korsinik['korisnicko_ime'], novi_korsinik['tip_korisnika']))
    return False


def menadzer_registracija():
    while True:
        korisnicko_ime = input("\nKorisnicko ime(upisite 'nazad' kako bi ste napustili registraciju):")
        greska = re.search(' ', korisnicko_ime)
        if greska is not None:
            print("Ime ne sme da sadrzi razmake!")
            continue
        if korisnicko_ime == '':
            print("Morate uneti ime!")
        break

    for korisnik in korisnici:
         if korisnik['korisnicko_ime'] == korisnicko_ime:
            print("Korisnicko ime je vec zauzeto.Pokusajte drugo")
            if not menadzer_registracija():
                return False
        if korisnicko_ime == 'nazad':
            return False
    while True:
        lozinka = getpass.getpass('lozinka:')
        greska = re.search(' ', lozinka)
        if greska != None:
            print("lozinka ne sme da sadrzi razmak!")
            continue
        if lozinka == '':
            print("Niste uneli lozinku")
            continue
        break
    ime = input("ime:")
    prezime = input("prezime:")

    novi_korsinik = {
        "korisnicko_ime": "",
        "lozinka": "",
        "ime": "",
        "prezime": ""}
    novi_korsinik['korisnicko_ime']: korisnicko_ime
    novi_korsinik['lozinka']: lozinka
    novi_korsinik['ime']: ime
    novi_korsinik['prezime']: prezime
    novi_korsinik['tip_korisnika']: 'Prodavac'
    novi_korsinik = [novi_korsinik]
    lista1(novi_korsinik)
    while True:
        print("\nNastavite?"
              "1. Da"
              "2. Ne")
        stavka = input("Opcija:")
        if stavka == 1:
            korisnici.append(novi_korsinik)
            break
        elif stavka == 2:
            return False
        else:
            print("pogresan unos")

    sacuvaj_korisnike(korisnici)
    print("%s je dodat u korisnike bazu podaatka.Tip korisnika=[%s]" % (novi_korsinik['korisnicko_ime'], novi_korsinik['tip_korisnika']))
    return False
