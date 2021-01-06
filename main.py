from korisnici.korisnici import prijava, sort, registracija
from knjige.knjige import sortirane_knjige, pretrazi_knjige,brisanje_knjige, registracija_knjiga,izmena_knjiga
from akcije.akcije import pretraga_akcija,sortirane_akcije,dodavanje_akcije
from racun.racun import prodaja_knjige,izvestaj_autor

def meni_administrator():
    while True:
        print("\n1. Sortiranje knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz svih akcija")
        print("4. Pretraga akcija")
        print("5. Registracija korisnika")
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
            sortirane_akcije()
        elif stavka == 4:
            pretraga_akcija()
        elif stavka == 5:
            registracija()
        elif stavka == 6:
            sort()
        elif stavka == 7:
            registracija_knjiga()
        elif stavka == 8:
            izmena_knjiga()
        elif stavka == 9:
            brisanje_knjige()
        elif stavka == 0:
            return
        else:
            print("Pokusajte ponovo!")


def meni_menadzer():
    while True:
        print("\n 1. Sortiranje knjiga")
        print(" 2. Pretraga knjiga")
        print(" 3. Prikaz svih akcija")
        print(" 4. Pretraga akcija")
        print(" 5. Registracija akcija")
        print(" 6. Registracija korisnika")
        print(" 7. Lista korisnika")
        print(" 8. Kreiraj izvestaj")
        print(" 0. Kraj")
        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            sortirane_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            sortirane_akcije()
        elif stavka == 4:
            pretraga_akcija()
        elif stavka == 5:
            dodavanje_akcije()
        elif stavka == 6:
            registracija()
        elif stavka == 7:
            sort()
        elif stavka == 8:
            izvestaj_autor()
        elif stavka == 0:
            return
        else:
            print("Pokusajte ponovo!")


def meni_prodavac():
    while True:
        print("\n1. Sortiranje knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz svih akcija")
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
            sortirane_akcije()
        elif stavka == 4:
            pretraga_akcija()
        elif stavka == 5:
            prodaja_knjige(ulogovani_korisnik=True)
        elif stavka == 6:
            registracija_knjiga()
        elif stavka == 7:
            izmena_knjiga()
        elif stavka == 8:
            brisanje_knjige()
        elif stavka == 0:
            return
        else:
            print("Pokusajte ponovo!")


def main():
    global ulogovani_korisnik
    for i in range(4):
        if i == 3 and ulogovani_korisnik == None:
            print("Previse neuspelih pokusaja za pprijavu!")
            exit()

        ulogovani_korisnik = prijava()
        if ulogovani_korisnik != None :
            print("Uspesna prijava!\nDobrodosli:", ulogovani_korisnik['ime'],ulogovani_korisnik['prezime'],"!\nTip korisnika:", ulogovani_korisnik['tip_korisnika'])
            if ulogovani_korisnik['tip_korisnika'] == 'Administrator':
                meni_administrator()
            elif ulogovani_korisnik['tip_korisnika'] == 'Menadzer':
                meni_menadzer()
            elif ulogovani_korisnik['tip_korisnika'] == 'Prodavac':
                meni_prodavac()
            else:
                print("Greska! Nepostojeca uloga korisnika!")


main()
