from akcije.akcijeIO import ucitaj_akcije
from knjige.knjigeIO import ucitaj_knjige
from datetime import date
from beautifultable import BeautifulTable

akcije = ucitaj_akcije()
knjige = ucitaj_knjige()
n = len(akcije)
kljuc = ['sifra', 'naslov', 'autor', 'kateogrija', 'artikli','datum_vazenja']
print("1111"
      "1")


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
                           f"{akcije[i]['nova cena']:^20}" \
                           f"{akcije[i]['datum_vazenja']:^20}"

                    print(za_ispis)
ispis_table(akcije, show_valid=False)
