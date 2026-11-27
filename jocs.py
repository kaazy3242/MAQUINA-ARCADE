import random
from robot import robot


def janken():
    r = robot()
    
    print("--- PEDRA, PAPER, TISORA ---")
    print("1. El primer que arribi a 3 victories")
    print("2. Al millor de 5 rondes")
    
    mode = input("Tria una opcio (1 o 2): ")
    while mode != "1" and mode != "2":
        print("Opcio incorrecta")
        mode = input("Tria una opcio (1 o 2): ")

    punts_usuari = 0
    punts_robot = 0
    rondes = 0
    acabat = False

    while acabat == False:
        rondes = rondes + 1
        print("")
        print("Ronda", rondes)
        print("Marcador -> Tu:", punts_usuari, "Robot:", punts_robot)

        usuari = input("Tria (pedra, paper, tisora): ").lower()
        while usuari != "pedra" and usuari != "paper" and usuari != "tisora":
            print("Has d'escriure pedra, paper o tisora")
            usuari = input("Tria (pedra, paper, tisora): ").lower()

        maquina = r.playing()
        print("El robot ha tret:", maquina)

        if usuari == maquina:
            print("Empat!")
        elif usuari == "pedra" and maquina == "tisora":
            print("Has guanyat la ronda")
            punts_usuari = punts_usuari + 1
        elif usuari == "paper" and maquina == "pedra":
            print("Has guanyat la ronda")
            punts_usuari = punts_usuari + 1
        elif usuari == "tisora" and maquina == "paper":
            print("Has guanyat la ronda")
            punts_usuari = punts_usuari + 1
        else:
            print("Guanya el robot")
            punts_robot = punts_robot + 1

        if mode == "1":
            if punts_usuari == 3 or punts_robot == 3:
                acabat = True
        
        if mode == "2":
            if punts_usuari == 3 or punts_robot == 3:
                acabat = True
            elif rondes >= 5 and punts_usuari != punts_robot:
                acabat = True

    print("")
    print("RESULTAT FINAL:")
    print("Tu:", punts_usuari, "- Robot:", punts_robot)
    if punts_usuari > punts_robot:
        print("Has guanyat la partida")
    else:
        print("Ha guanyat el robot")


def nana():
    secret = random.randint(1, 100)
    intents = 0
    encertat = False

    print("--- ENDEVINA EL NUMERO ---")
    print("He pensat un numero del 1 al 100")

    while encertat == False:
        num_txt = input("Digues un numero: ")
        
        if num_txt.isdigit():
            num = int(num_txt)
            if num >= 1 and num <= 100:
                intents = intents + 1
                if num > secret:
                    print("Massa alt")
                elif num < secret:
                    print("Massa baix")
                else:
                    print("L'has encertat en", intents, "intents")
                    encertat = True
            else:
                print("El numero ha d'estar entre 1 i 100")
        else:
            print("Aixo no es un numero")