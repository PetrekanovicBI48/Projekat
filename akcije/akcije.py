from akcije.akcijeIO import ucitaj_akcije,sacuvaj_akcije
from knjige.knjige import ucitaj_knjige,sacuvaj_knjige
akcije=ucitaj_akcije()
n=len(akcije)
knjige=ucitaj_knjige()

kljuc=['sifra','autor','kategorija']
def pretraga_akcija_arikli(artikli):
    string=''
    i=0
    for artikal in akcije['artikal']:
        string+=artikal['naslov']
        try:
            if akcije['artikli'][i+1]!=None:
                string+='\n'
        except IndexError:
            break
        i+=1
    return string


def pretraga_akcija_cena(akcije):
    string=''
    i=0

    for artikal in akcije['artikli']:
        string+=str(artikal['cena'])
        try:
            if akcije['akcije'][i+1]!=None:
                string+='\n'
        except IndexError:
            break
        i+=1

    return string

def sort():
    while True:
        print("\nSortiraj po"
              "\n1. sifri"
              "\n2. datum vazenja"
              "\n0. nazad")
        stavka= input("Opcija:")
        if stavka== 1:
            sorter='sifra'
            break
        elif stavka==2:
            sorter='datum_vazenja'
            break
        elif stavka==0:
            return False
        else:
            print("pogresan unos!")

    if sorter=='sifra':
        akcije.sort(key=lambda akcije:akcije.get('sifra'))
    if sorter=='datum_vazenja':
        akcije.sort(key=lambda akcije:akcije.get('datum_vazenja'))
    ispis_akcija(akcije)

def pretrazi_akcija():
    print("\n1. Pretraga po sifri")
    print("2. Pretraga po artiklu")
    print("3. Pretraga po datumu vazenja")
    print("0. Napusti pretragu")
    stavka = int(input("Izaberite stavku: "))
    akcije = []
    if stavka == 1:
        sifra = int(input("Unesite sifru: "))
        akcije = pretraga_akcija_arikli("sifra", sifra)
    elif stavka == 2:
        artikli = input("Unesite nalsov: ")
        akcije = pre("artikli", artikli)
    elif stavka == 3:
        datum_vazenja = input("Unesite datum vazenja: ")
        akcije = pret("datum_vazenja", datum_vazenja)
    elif stavka==0:
        return
    else:
        print("Pogresan unos")

    ispis_akcija(akcije)

def ispis_akcija(akcije):
    zaglavlje = f"{'sifra':<10}" \
               f"{'naziv':<20}" \
               f"{'Datum vazenja':^20}"

    print(zaglavlje)
    print("-"*len(zaglavlje))

    for akcija in akcije:
        za_ispis = f"{akcija['sifra']:<10}" \
                   f"{akcija['naziv']:<20}" \
                   f"{akcija['datum_vazenja']:^20}"
        print(za_ispis)
def  registracija_akcija():
    for akcija in akcije:
        sifra=akcija['sifra']
    sifra+=1
    naslov=input('naslov:')
    autor=input('autor:')
    isbn=input('isbn:')
    izdavac=input('izdavac:')
    godina=int(input('godina:'))
    cena=float(input('cena'))
    broj_strana=int(input('broj strana:'))
    kategorija=input('kategorija:')
    nova_knjiga={
        "sifra": 3,
        "naslov": "Knjiga 1",
        "autor": "Pera Peric",
        "isbn": "1312312312312",
        "izdavac": "Vulkan",
        "broj strana": "231",
        "godina": 2020,
        "cena": 650.0,
        "kategorija": "Roman"
    }
    nova_knjiga['sifra'] = sifra
    nova_knjiga['naslov']= naslov
    nova_knjiga['autor']=autor
    nova_knjiga['isbn']=isbn
    nova_knjiga['izdavac']=izdavac
    nova_knjiga['broj strana']=broj_strana
    nova_knjiga['godina']=godina
    nova_knjiga['cena']=cena
    nova_knjiga['kategorija']=kategorija

    knjige.append(nova_knjiga)
    sacuvaj_knjige(knjige)
    print('%s je dodata u bazu podataka. Knjiga sifra=[%s]' %(nova_knjiga['naslov'], nova_knjiga['sifra']))
    return False
