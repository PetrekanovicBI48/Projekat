from Kola.automobiliIO import ucitaj_kola,sacuvaj_kola
automobili=ucitaj_kola()
kljuc=['Marka','Godiste','Oprema']
def dodaj_kola():
    automobili={}
    Marka= input('Marka:')
    Godiste= int(input('Godiste:'))
    Cena=int(input('Cena:'))
    novi_automobil={
    "Marka":"VW",
    "Godiste":"2001",
    "Cena":"200",
    "Oprema":[]
    }
    novi_automobil['Marka']=Marka
    novi_automobil['Godiste']= Godiste
    novi_automobil['Cena']= Cena
    dodaj_kola= True
    while dodaj_kola:
        Oprema=input("Unesite opremu\n Unesite prazno polje da prekinete unos opreme ")
        if Oprema== '':
            dodaj_kola= False
        else:
            novi_automobil['Oprema'].append(Oprema)
    automobili.append(novi_automobil)
    sacuvaj_kola(automobili)
    print("Automobil: %s je dodaat\ngodiste:[%s]" %(novi_automobil['Marka'], novi_automobil['Godiste']))
