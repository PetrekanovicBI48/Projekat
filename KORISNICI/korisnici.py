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


def admin_registracija():
    while True:
        korisnicko_ime = input("\nKorisnicko ime(upisite 'nazad' kako bi ste napustili registraciju):")
        if korisnicko_ime !='':
            greska = re.search(' ', korisnicko_ime)
            if greska == None:
                break
            else:
                print("korisnicko ime ne sme da sadrzi razmake,pokusajte opet!")
                if admin_registracija()== False:
                    return False
        else:
            print("niste uneli korisnicko ime!")
            if admin_registracija()==False:
                return False
    print("test")
    for korisnik in korisnici:
        if korisnik['korisnicko_ime'] == korisnicko_ime:
            print("Korisnicko ime je vec zauzeto.Pokusajte drugo")
            if not admin_registracija():
                return False
        if korisnicko_ime == 'nazad':
            return False
    print("test")
    while True:
        lozinka = input("unesite lozinku")
        if lozinka != '':
            greska = re.search(' ', korisnicko_ime)
            if greska == None:
                break
            else:
                print("Sifra ne sme da sadrzi razmake,pokusajte opet!")
                if admin_registracija() == False:
                    return False
        else:
            print("niste uneli sifru!")
            if admin_registracija() == False:
                return False
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
    ispis_korisnika(novi_korsinik)
    while True:
        print("\nNastavite?"
              "\n1. Da"
              "\n2. Ne")
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


def menadzer_registracija():
    while True:
        korisnicko_ime = input("\nKorisnicko ime(upisite 'nazad' kako bi ste napustili registraciju):")
        if korisnicko_ime != '':
            greska = re.search(' ', korisnicko_ime)
            if greska== None:
                break
            else:
                print("Ime ne sme da sadrzi razmake!")
                if menadzer_registracija()==False:
                    return False
        else:
            print("Morate uneti ime!")
            if menadzer_registracija()==False:
                return False

    for korisnik in korisnici:
         if korisnik['korisnicko_ime'] == korisnicko_ime:
            print("Korisnicko ime je vec zauzeto. Pokusajte drugo!")
            if not menadzer_registracija():
                return False
         if korisnicko_ime == 'nazad':
            return False
    while True:
        lozinka = input('lozinka:')
        if korisnicko_ime != '':
            greska = re.search(' ', korisnicko_ime)
            if greska== None:
                break
            else:
                print("sifra ne sme da sadrzi razmake!")
                if menadzer_registracija()==False:
                    return False
        else:
            print("Morate uneti sifru!")
            if menadzer_registracija()==False:
                return False

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
    ispis_korisnika(novi_korsinik)
    sacuvaj_korisnike(korisnici)
    print("%s je dodat u korisnike bazu podaatka.Tip korisnika=[%s]" % (novi_korsinik['korisnicko_ime'], novi_korsinik['tip_korisnika']))
    return False
