import json

datoteka="./kola/automobili.json"

def ucitaj_kola():
    with open(datoteka,encoding='utf-8') as f:
        return json.load(f)

def sacuvaj_kola(automobili):
    with open(datoteka,"w", encoding='utf-8') as f:
        json.dump(automobili,f, indent=4)