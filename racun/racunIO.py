import json

datoteka="./datoteke/racun.json"

def ucitaj_racun():
    with open(datoteka, encoding='utf-8') as f:
        return json.load(f)

def sacuvaj_racun(novi_racun):
    with open(datoteka,"w",encoding='utf-8') as f:
        json.dump(novi_racun,f,ensure_ascii=False,indent=4)