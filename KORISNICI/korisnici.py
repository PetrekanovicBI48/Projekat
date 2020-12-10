from korisnici.korisniciIO import ucitaj_korisnike, sacuvaj_korisnike
import re,getpass
korisnici = ucitaj_korisnike()
z=len(korisnici)
def prijava():
    korisnici = ucitaj_korisnike()
    korisncko_ime = input("korisnicko ime: ")
    lozinka = input("loznika: ")

    for korisnik in korisnici:
        if korisnik['korisnicko_ime'] == korisncko_ime and korisnik['lozinka'] == lozinka:
            return korisnik
            printf("Dobrodosli!")
    return None
def registracija():
    while True:
        korisnicko_ime= input("Korisnicko ime(upisite 'nazad' kako bi ste napustili registraciju):")
        greska=re.search('',korisnicko_ime)
        if(greska !=''):
            print("Ime ne sme da sadrzi razmake!")
        elif (korisnicko_ime ==''):
            print("Morate uneti ime!")
        else:
            break

    for korisnicko_ime in korisnici:
        if(korisnicko_ime['korisnicko_ime']==korisnicko_ime):
            print("Korisnicko ime je vec zauzeto.Pokusajte drug")
            if (registracija()== False):
                return False
        if(korisnicko_ime=='nazad'):
            return False
    while True:
        lozinka=getpass.getpass('lozinka:')
        greska=re.search('',lozinka)
        if(greska != None):
            print("lozinka ne sme da sadrzi razmak!")
        elif(lozinka==''):
            print("Niste uneli lozinku")
        else:
            break
    ime=input("ime:")
    prezime=input("Prezime:")

    while True:
        tip_korisnika=input("Pristup menadzera ili prodavca(m/p):")
        if(tip_korisnika !='m' and tip_korisnika !='p'):
            print("pogresna uloga!")
        else:
            break

        novi_korsinik={
        "korisnicko_ime": "",
        "lozinka": "",
        "ime": "",
        "prezime": "",
        }

        novi_korsinik['korisnicko_ime']=korisnicko_ime
        novi_korsinik['lozinka']=lozinka
        novi_korsinik['ime']= ime
        novi_korsinik['prezime']=prezime

        if(tip_korisnika=='m'):
            novi_korsinik['uloga']='Menadzer'
        else:
            novi_korsinik['uloga']='Prodavac'

        korisnici.append(novi_korsinik)
        sacuvaj_korisnike(korisnici)
        print("%s je dodat u korisnike datoteke.Tip korisnika=[%s]" %(novi_korsinik['korisnicko_ime'],novi_korsinik['tip_korisnika']))
        return False

    duzina=[1,1,1,1,1]
    kljuc=['korisnicko_ime','lozinka','ime','prezime','tip_korisnika']
    

