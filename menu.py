import jocs


def main():
    sortir = False

    while sortir == False:
        print("")
        print("BENVINGUT AL MINI ARCADE")
        print("1. Jugar a Pedra, Paper, Tisora")
        print("2. Jugar a Endevinar el Numero")
        print("S. Sortir")

        opcio = input("Tria una opcio: ").upper()

        if opcio == "1":
            jocs.janken()
        elif opcio == "2":
            jocs.nana()
        elif opcio == "S":
            print("Gracies per jugar al Mini Arcade <3")
            sortir = True
        else:
            print("Opcio incorrecta, tria 1, 2 o S.")


main()