from racun.racunIO import ucitaj_racun, sacuvaj_racun
from knjige.knjigeIO import ucitaj_knjige
from akcije.akcijeIO import ucitaj_akcije
from datetime import datetime

racuni = ucitaj_racun()
knjige = ucitaj_knjige()
akcije = ucitaj_akcije()


def prodaja_knjige(ulogovani_korisnik):
    now = datetime.now()
    novi_racun = {
        "sifra": 666,
        "prodavac": ulogovani_korisnik['korisnicko_ime'],
        "datum_vreme": "2020-12-27T18:16:25.925653",
        "artikli": [], "akcije": [],
        "cena": 0.0
    }
    novi_racun['sifra'] = racuni[-1]['sifra'] + 1
    unos_artikala = True
    while(unos_artikala):
        sifra = input("\n Unesi sifru knjige ili akcije (unesi 'nazad' za povratak u meni, unesi 'x' za prekid unosa knjiga):")
        if sifra == 'nazad':
            return
        elif sifra == 'x':
            unos_artikala = False
        else:
            for knjiga in knjige:
                if knjiga['sifra'] == int(sifra) and knjiga['obrisano']=="False":
                    kolicina = input("\n Unesi kolicinu:")
                    knjiga['kolicina'] = kolicina
                    novi_racun['artikli'].append(knjiga)
                    novi_racun['cena'] += knjiga['cena']*int(kolicina)
                    continue
            for akcija in akcije:
                if akcija['sifra'] == int(sifra):
                    kolicina = input("\n Unesi kolicinu:")
                    akcija['kolicina'] = kolicina
                    novi_racun['akcije'].append(akcija)
                    for artikal in akcija['artikli']:
                        novi_racun['cena'] += float(artikal['nova cena'])*int(kolicina)
    ispis_knjiga_racun(novi_racun)
    ispis_akcija_racun(novi_racun)
    a = True
    while a:
        print('\nZelite li da nastavite kupovinu?\n1. Da\n2. Odustani')
        stavka = int(input('Unesite odgovor:'))
        if stavka == 1:
            novi_racun['datum_vreme'] = now.strftime("%d.%m.%Y. %H:%M:%S")
            racuni.append(novi_racun)
            sacuvaj_racun(racuni)
            pravljenje_racuna(novi_racun)
            a = False
        elif stavka == 2:
            return False
        else:
            print('Uneli ste pogresnu opciju. Pokusajte ponovo.')

def pravljenje_racuna(racun):
    ispis_zaglavlja(racun)
    ispis_knjiga_racun(racun)
    ispis_akcija_racun(racun)
    ispis_racun_ukupno(racun)

def ispis_zaglavlja(racun):
    print('sifra racuna: ', racun['sifra'])
    print('prodavac: ',racun['prodavac'])
    print('datum i vreme: ',datetime.now().isoformat())
    print('__'*20)

def ispis_knjiga_racun(racun):
    if racun['artikli']!=[]:
        zaglavlje = f"{'artikli':<20}" \
                    f"{'cena':<20}" \
                    f"{'kolicina':<20}"

        print(zaglavlje)
        print("-" * len(zaglavlje))

        for knjiga in racun['artikli']:
            za_ispis = f"{knjiga['naslov']:<20}" \
                       f"{knjiga['cena']:^20}" \
                       f"{knjiga['kolicina']:^20}"
            print(za_ispis)
        print("-" * len(zaglavlje))

def ispis_akcija_racun(racun):
    if racun['akcije'] != []:
        zaglavlje = f"{'artikli':<20}" \
                    f"{'cena':<20}" \
                    f"{'kolicina':<20}"

        print(zaglavlje)
        print("-" * len(zaglavlje))
        for akcija in racun['akcije']:
            for artikal in akcija['artikli']:
                za_ispis = f"{artikal['naslov']:<20}" \
                           f"{artikal['nova cena']:<20}" \
                           f"{akcija['kolicina']:<20}"
                print(za_ispis)
        print("-" * len(zaglavlje))

def ispis_racun_ukupno(racun):
    print("Ukupno: ", racun['cena'])



def kraj_kupovine():
    racuni = ucitaj_racun()
    racun = pravljenje_racuna()
    print('\nKnjige koje su odabrane su:')
    ispis_knjiga_racun(racuni)
    ispis_akcija_racun(racuni)
    while True:
        print('\nZelite li da nastavite?\n1. Da\n2. Odustani')
        stavka = input('Unesite:')
        if stavka == '1':
            racuni.append(racun)
            break
        elif stavka == '2':
            return False
        else:
            print('Pogresan unos.')
    racun.sacuvaj_racun(racuni)
    print('Prodaja zavrsena. Izvolite racun:')
    print(racun)
    return False

def izvestaj_ukupna_prodaja():
    recnik ={}
    for knjiga in knjige:
        recnik[knjiga['naslov']] = 0
    for racun in racuni:
        for artikal in racun['artikli']:
            recnik[artikal['naslov']]+=int(artikal['kolicina'])
        for akcije in racun['akcije']:
            for artikal in akcije['artikli']:
                recnik[artikal['naslov']]+=int(akcije['kolicina'])
    print(recnik)

def izvestaj_prodaja_akcija():
    recnik ={}
    for akcija in akcije:
        recnik[akcija['sifra']] = 0
    for racun in racuni:
        for akcija in racun['akcije']:
            recnik[akcija['sifra']]+=int(akcija['kolicina'])
    print(recnik)

def izvestaj_autor():
    autor = input("Unesi ime autora: ")
    recnik = {}
    for knjiga in knjige:
        if knjiga['autor'].lower() == autor.lower():
            recnik[knjiga['naslov']] = 0
    for racun in racuni:
        for artikal in racun['artikli']:
            if artikal['naslov'] in recnik.keys():
                recnik[artikal['naslov']] +=int(artikal['kolicina'])
        for akcija in racun['akcije']:
            for artikal in akcija['artikli']:
                if artikal['naslov'] in recnik.keys():
                    recnik[artikal['naslov']]+=int(akcija['kolicina'])
    print(recnik)