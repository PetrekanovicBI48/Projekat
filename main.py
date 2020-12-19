from korisnici.korisnici import prijava,sort , menadzer_registracija, admin_registracija, prikaz_liste
from knjige.knjige import sortirane_knjige, pretrazi_knjige
from akcije.akcije import ispis_akcija,ucitaj_akcije

def meni_administrator():
    while True:
        print("\n1. Sortiranje knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("5. Registracija")
        print("6. Lista korisnika")
        print("7. Dodaj knjigu")
        print("8. Izmeni knjigu")
        print("9. Obrisi knjigu")
        print("0. Kraj")
        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            sortirane_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            ispis_akcija(akcije=ucitaj_akcije())
        elif stavka == 4:
            print("Nemate dozvolu za ovu komandu")
            meni_administrator()
        elif stavka == 5:
            admin_registracija()
        elif stavka == 6:
            sort()
        elif stavka == 7:
            print("Nemate dozvolu za ovu komandu")
            meni_menadzer()
        elif stavka == 8:
            print("Nemate dozvolu za ovu komandu")
            meni_administrator()
        elif stavka == 9:
            print("Nemate dozvolu za ovu komandu")
            meni_administrator()
        elif stavka == 0:
            return
        else:
            print("Pokusajte ponovo!")


def meni_menadzer():
    while True:
        print("\n 1. Sortiranje knjiga")
        print(" 2. Pretraga knjiga")
        print(" 3. Prikaz akcija")
        print(" 4. Pretraga akcija")
        print(" 5. Registracija")
        print(" 6. Lista korisnika")
        print(" 7. Dodaj knjigu")
        print(" 8. Izmeni knjigu")
        print(" 9. Obrisi knjigu")
        print(" 0. Kraj")
        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            sortirane_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            print("Nemate dozvolu za ovu komandu")
            meni_menadzer()
        elif stavka == 4:
            print("Nemate dozvolu za ovu komandu")
            meni_administrator()
        elif stavka == 5:
            menadzer_registracija()
        elif stavka == 6:
            prikaz_liste()
        elif stavka == 7:
            print("Nemate dozvolu za ovu komandu")
            meni_menadzer()
        elif stavka == 8:
            print("Nemate dozvolu za ovu komandu")
            meni_menadzer()
        elif stavka == 9:
            print("Nemate dozvolu za ovu komandu")
            meni_menadzer()
        elif stavka == 0:
            return
        else:
            print("Pokusajte ponovo!")


def meni_prodavac():
    while True:
        print("\n1. Sortiranje knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("5. Prodaj knjigu")
        print("6. Dodaj knjigu")
        print("7. Izmeni knjigu")
        print("8. Obrisi knjigu(logicko brisanje)")
        print("0. Kraj")
        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            sortirane_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            print("Nemate dozvolu za ovu komandu")
            meni_prodavac()
        elif stavka == 4:
            print("Nemate dozvolu za ovu komandu")
            meni_prodavac()
        elif stavka == 5:
            print("Nemate dozvolu za ovu komandu")
            meni_prodavac()
        elif stavka == 6:
            print("Nemate dozvolu za ovu komandu")
            meni_prodavac()
        elif stavka == 7:
            print("Nemate dozvolu za ovu komandu")
            meni_prodavac()
        elif stavka == 8:
            print("Nemate dozvolu za ovu komandu")
            meni_prodavac()

        elif stavka == 0:
            return
        else:
            print("Pokusajte ponovo!")


def main():
    for i in range(4):
        if i == 3:
            print("Previse neuspelih pokusaja za pprijavu!")
            exit()

        ulogovani_korisnik = prijava()
        if ulogovani_korisnik != False :
            print("Uspesna prijava!Tip korisnika:", ulogovani_korisnik['tip_korisnika'])
            if ulogovani_korisnik['tip_korisnika'] == 'Administrator':
                meni_administrator()
            elif ulogovani_korisnik['tip_korisnika'] == 'Menadzer':
                meni_menadzer()
            elif ulogovani_korisnik['tip_korisnika'] == 'Prodavac':
                meni_prodavac()
            else:
                print("Greska! Nepostojeca uloga korisnika!")


main()
