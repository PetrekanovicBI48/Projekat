
from korisnici.korisnici import prijava
from knjige.knjige import prikazi_knjige
from knjige.knjige import pretrazi_knjige

def meni_administrator():
    while True:
        print("\n1. Prikaz knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("5. Registracija")
        print("6. Lista korisnika")
        print("7. Dodaj knjigu")
        print("8. Izmeni knjigu")
        print("9. Obrisi knjigu")
        print("10. Odjavi se")
        print("0. Kraj")
        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            prikazi_knjige()
        elif stavka == 4:
            prikazi_knjige()
        elif stavka == 0:
            return
        else:
            print("Pokusajte ponovo!")


def main():
    for i in range (4):
        if(i==3):
            print("Previse neuspelih pokusaja za pprijavu!")
            return 0

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