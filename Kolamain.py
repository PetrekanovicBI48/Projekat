from Kola.kola import dodaj_kola
def main():
    while True:
        print('1. Dodavanje auta')
        print('2. Pretraga automobila')
        print('0. Kraj!')

        stavka = input("\nIzaberite stavku:")
        if stavka == '1':
                dodaj_kola()
        elif stavka == '2':
           pass
        elif stavka == '0':
            return False
        else:
            print("Pokusajte ponvo")


main()
