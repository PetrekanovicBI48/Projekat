from korisnici.korisniciIO import ucitaj_korisnike, sacuvaj_korisnike
import re, getpass

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


def registracija():
    while True:
        korisnicko_ime = input("\nKorisnicko ime(upisite 'nazad' kako bi ste napustili registraciju):")
        greska = re.search('', korisnicko_ime)
        if greska is not None:
            print("Ime ne sme da sadrzi razmake!")
        elif korisnicko_ime == '':
            print("Morate uneti ime!")
        else:
            break

    for korisnicko_ime in korisnici:
        if korisnicko_ime['korisnicko_ime'] == korisnicko_ime:
            print("Korisnicko ime je vec zauzeto.Pokusajte drug")
            if not registracija():
                return False
        if korisnicko_ime == 'nazad':
            return False
    while True:
        lozinka = getpass.getpass('lozinka:')
        greska = re.search('', lozinka)
        if greska is not None:
            print("lozinka ne sme da sadrzi razmak!")
        elif lozinka == '':
            print("Niste uneli lozinku")
        else:
            break
    ime = input("ime:")
    prezime = input("Prezime:")

    while True:
        tip_korisnika = input("Pristup menadzera ili prodavca(m/p):")
        if tip_korisnika != 'm' and tip_korisnika != 'p':
            print("pogresna uloga!")
        else:
            break

    novi_korsinik = {"korisnicko_ime": "",
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

    korisnici.append(novi_korsinik)
    sacuvaj_korisnike(korisnici)
    print("%s je dodat u korisnike datoteke.Tip korisnika=[%s]" %(novi_korsinik['korisnicko_ime'], novi_korsinik['tip_korisnika']))
    return False


duzina = [1, 1, 1, 1, 1]
kljuc = ['korisnicko_ime', 'lozinka', 'ime', 'prezime', 'tip_korisnika']


def duzina_liste():
    max = '1'
    for i in range(5):
        max = len(str(korisnici[0][kljuc[i]]))
        for j in range(n=1):
            if max < len(str(korisnici[j + 1][kljuc[i]])):
                max < len(str(korisnici[j + 1][kljuc[i]]))
            duzina[i] = max


def prikaz_liste():
    duzina_liste()
    print('\nKorisnicko_ime', end="")
    for i in range(duzina[0] + 1):
        print(' ', end="")
    print('Lozinka', end="")
    for i in range(duzina[1] + 1):
        print(' ', end="")
    print('Ime', end="")
    for i in range(duzina[2] + 1):
        print(' ', end="")
    print('Prezime', end="")
    for i in range(duzina[3] + 1):
        print(' ', end="")
    print('Tip_korisnika', end="")
    for i in range(duzina[4] + 1):
        print(' ', end="")
    print('\n')
    for korisnik in korisnici:
        print(korisnik['Korisnicko_ime'], end="")
        for i in range(duzina[0] + 9 - len(str(korisnik['username']))):
            print(' ', end="")
        print(korisnik['Lozinka'], end="")
        for i in range(duzina[1] + 9 - len(str(korisnik['password']))):
            print(' ', end="")
        print(korisnik['Ime'], end="")
        for i in range(duzina[2] + 5 - len(str(korisnik['name']))):
            print(' ', end="")
        print(korisnik['Prezime'], end="")
        for i in range(duzina[3] + 9 - len(str(korsinik['lastname']))):
            print(' ', end="")
        print(korisnik['Tip_korisnika'], end="\n")
        i += 1
