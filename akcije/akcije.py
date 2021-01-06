from akcije.akcijeIO import ucitaj_akcije,sacuvaj_akcije
from datetime import date
from knjige.knjige import ucitaj_knjige
from util import unos_sa_proverom
akcije = ucitaj_akcije()
n = len(akcije)
knjige = ucitaj_knjige()


kljuc = ['naslov','autor','kategorija','sifra','datum_vazenja','nova_cena']

def ispis_table(akcije, show_valid):
    for akcija in akcije:
        if str(date.today()) < akcija["datum_vazenja"] or show_valid == False:
            zaglavlje = f"{'sifra':<10}" \
                    f"{'naslov':<20}" \
                    f"{'stara cena':^20}" \
                    f"{'nova cena':^20}" \
                    f"{'datum vazenja':^20}"

            print(zaglavlje)
            print("-" * len(zaglavlje))
            for i in range(0, len(akcije)):
                for j in range(0, len(akcije[i]['artikli'])):
                    za_ispis = f"{akcije[i]['sifra']:<10}" \
                           f"{akcije[i]['artikli'][j]['naslov']:<20}" \
                           f"{akcije[i]['artikli'][j]['cena']:^20}" \
                           f"{akcije[i]['nova_cena']:^20}" \
                           f"{akcije[i]['datum_vazenja']:^20}"

                    print(za_ispis)

def pretraga_akcija_string(kljuc, vrednost):
    akcije = ucitaj_akcije()
    filtrirane_akcije = []
    if kljuc=='sifra' or kljuc=="nova cena" or kljuc=='datum_vazenja':

        for akcija in akcije:
            if vrednost.lower() in akcija[kljuc].lower():
                filtrirane_akcije.append(akcija)
    else:
        for akcija in akcije:
            for artikal in akcija['artikli']:
                if artikal[kljuc].lower() ==vrednost.lower():
                    filtrirane_akcije.append(akcija)
    return filtrirane_akcije


def pretraga_akcija_jednakost(kljuc, vrednost):
    akcije = ucitaj_akcije()
    filtritane_akcije = []

    for akcija in akcije:
        if vrednost == akcija[kljuc]:
            filtritane_akcije.append(akcija)
        return filtritane_akcije

def sortiranje_akcija(kljuc):
    for i in range(len(akcije)):
        for j in range(len(akcije)):
            if akcije[i][kljuc] < akcije[j][kljuc]:
                temp = akcije[i]
                akcije[i] = akcije[j]
                akcije[j] = temp

def sortirane_akcije():
    while True:
        print("\nSortiraj po"
              "\n1. sifri"
              "\n2. datum vazenja"
              "\n0. nazad")
        stavka = int(input("Opcija:"))
        if stavka == 1:
            sortiranje_akcija('sifra')
            #ispis_table(akcije, show_valid=False)
        elif stavka == 2:
            sortiranje_akcija('datum_vazenja')
            #ispis_table(akcije, show_valid=False)
        elif stavka == 0:
            return False
        else:
            print("pogresan unos!")
        ispis_table(akcije, show_valid=False)

def pretraga_akcija():
    show_valid = False
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
        akcije =pretraga_akcija_string("naslov", naslov)
    elif stavka == 3:
        autor = input("Unesite autora: ")
        akcije = pretraga_akcija_string('autor', autor)
    elif stavka == 4:
        kategorija = input("Unesite kategoriju:")
        akcije = pretraga_akcija_string('kategorija', kategorija)
    elif stavka==0:
        return
    else:
        print("Pogresan unos, pokusajte ponovo!")
    ispis_table(akcije,show_valid)
def dodavanje_akcije():
    nova_akcija={
        "sifra:":1,
        "artikli":[],
        "nova cena":1111.1,
        "datum_vazenja":"12.06.2021"
    }
    sifra= akcije[-1]['sifra']
    nova_akcija['sifra']=sifra+1
    dodavanje_knjige= True
    while (dodavanje_knjige):
        sifra=unos_sa_proverom("unesite sifru('nazad' za povratak,'benz' za prekid unosa knjiga)\nsifra:")
        if sifra=='nazad':
            return
        elif sifra == 'benz':
            dodavanje_knjige= False
        else:
            for knjiga in knjige:
                if knjiga['sifra']==int(sifra):
                    nova_cena = input("\nUnesi novu cenu knjige: ")
                    knjiga['nova cena'] = nova_cena
                    nova_akcija['artikli'].append(knjiga)
        datum_vazenja = input("\nUnesi datum vazenja akije: ")
        nova_akcija['datum_vazenja'] = datum_vazenja
        akcije.append(nova_akcija)
        sacuvaj_akcije(akcije)
        print('Nova akcija je dodata u bazu podataka. Sifra akcije=[%s]' % (nova_akcija['sifra']))