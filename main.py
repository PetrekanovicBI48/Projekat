
from korisnici.korisnici import prijava
from knjige.knjiga import prikazi_knjige
from knjige.knjiga import pretrazi_knjige

def meni_administrator():
    while True:
        print("\n1. Prikaz knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("10. Kraj")
        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 10:
            return
        else:
            print("Pokusajte ponovo!")


def main():
    ulogovani_korisnik = prijava()

    if ulogovani_korisnik is not None:
        if ulogovani_korisnik['tip_korisnika'] == 'Administrator':
            meni_administrator()
        elif ulogovani_korisnik['tip_korisnika'] == 'Menadzer':
            pass
        elif ulogovani_korisnik['tip_korisnika'] == 'Prodavac':
            pass
        else:
            print("Greska! Nepostojeca uloga korisnika!")

main()