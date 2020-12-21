import re


def unos_sa_proverom(poruka, naziv_unosa="Unos"):
    while True:
        unos = input(poruka)
        if unos != '':
            greska = re.search(' ', unos)
            if greska == None:
                return unos
            else:
                print(f"{naziv_unosa} ne sme da sadrzi razmake!")
        else:
            print(f"{naziv_unosa} ne sme biti prazan!")

