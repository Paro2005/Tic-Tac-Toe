feld = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]   #Eine Liste in der die Figuren eingetragen werden.
spieler = "x"                   #Eine Variable mit x oder o, um im Feld die Figur einzutragen.
zaehler = int(0)                #Eine Variable mit einer Zahl, die verhindert, dass man mehr als 9 Züge macht.
zahlen = 0


def counter():

    
    if spieler == ("x"):
        xlesen = open('x.txt','r')
        counterx = xlesen.read()
        counterx = int(counterx)
        xschreiben = open('x.txt','w')
        counterx = counterx + 1
        xschreiben.write(str(counterx))
        xschreiben.close
    else:
        olesen = open('o.txt','r')
        countero = olesen.read()
        countero = int(countero)
        oschreiben = open('o.txt','w')
        countero = countero + 1
        oschreiben.write(str(countero))
        oschreiben.close

    print("\nSpieler x=", counterx, "     Spieler o =", countero, "\n")

def feld_drucken():
    """
    Die Funktion, die das Tic-Tac-Toe Feld immer wieder aktualisiert anzeigt.
    :return:
    """
    global feld
    print(" ")
    print(" ", feld[7], " ¦ ", feld[8], " ¦ ", feld[9])
    print("  --    --    --")
    print(" ", feld[4], " ¦ ", feld[5], " ¦ ", feld[6])
    print("  --    --    --")
    print(" ", feld[1], " ¦ ", feld[2], " ¦ ", feld[3])
def feld_proben():
    """
    Diese Funktion prüft nach jedem Zug, ob auf dem ausgewähltenn Feld schon eine Figur ist.
    :return:
    """
    global zahlen
    while feld[zahlen] == ("x") or feld[zahlen] == ("o"):
        print("\nAuf diesem Feld ist schon eine Figur.\n")
        zahlen = int(input("Spieler " + spieler + ". Auf welches Feld willst du eine Figur legen? "))
    else:
        print(" ")
def xodero_eintragen():
    """
    Diese Funktion ersetzt das Feld mit der entsprechenden Figur und wechselt gerade den Spieler.
    :return:
    """
    global spieler
    if spieler == ("x"):
        feld[zahlen] = ("x")
    else:
        feld[zahlen] = ("o")
def initialisierung_abfragen():
    """
    Diese Funktion startet das Prgram und fragt nach ob man ein Spiel spielen will.
    :return:
    """
    global starten
    starten = input("Willst du ein Spiel starten? Ja[j] Nein[n] ")
    while starten != "j" or starten != "n":
        if starten == "j":
            feld_drucken()
            print("\n................................................\n")
            break
        elif starten == "n":
            exit()
        else:
            print("Falsche Eingabe! ")
            starten = input("Willst du ein Spiel starten? Ja[j] Nein[n] ")
def gewinn_proben(spieler, zaehler):
    """
    Diese Funktion prüft nach jedem Zug, ob ein Spieler gewonnen hat.
    :return:
    """
    if feld[7] == spieler and feld[8] == spieler and feld[9] == spieler:
        print("\nSpieler " + spieler, ", du hast gewonnen!")
        zaehler = zaehler + 7
    elif feld[4] == spieler and feld[5] == spieler and feld[6] == spieler:
        print("\nSpieler " + spieler + ", du hast gewonnen!")
        zaehler = zaehler + 7
    elif feld[1] == spieler and feld[2] == spieler and feld[3] == spieler:
        print("\nSpieler " + spieler + ", du hast gewonnen!")
        zaehler = zaehler + 7
    elif feld[1] == spieler and feld[5] == spieler and feld[9] == spieler:
        print("\nSpieler " + spieler + ", du hast gewonnen!")
        zaehler = zaehler + 7
    elif feld[7] == spieler and feld[5] == spieler and feld[3] == spieler:
        print("\nSpieler " + spieler + ", du hast gewonnen!")
        zaehler = zaehler + 7
    elif feld[7] == spieler and feld[4] == spieler and feld[1] == spieler:
        print("\nSpieler " + spieler + ", du hast gewonnen!")
        zaehler = zaehler + 7
    elif feld[8] == spieler and feld[5] == spieler and feld[2] == spieler:
        print("\nSpieler " + spieler + ", du hast gewonnen!")
        zaehler = zaehler + 7
    elif feld[9] == spieler and feld[6] == spieler and feld[3] == spieler:
        print("\nSpieler " + spieler + ", du hast gewonnen!")
        zaehler = zaehler + 7
    else:
        print("\n................................................\n")
    return zaehler
def spieler_wechseln():
    """
        Diese Funktion wechselt den Spieler von x zu o oder von o zu x.
        :return:
        """
    global spieler
    if spieler == ("x"):
        spieler = ("o")
    else:
        spieler = ("x")


print("Tic-Tac-Toe\n")
initialisierung_abfragen()
while starten == "j":
    while zaehler < 9:
        zahlen = input("Spieler " + spieler + ". Auf welches Feld willst du eine Figur legen? ")
        try:
            zahlen = int(zahlen)
        except ValueError:
            print("\nFalsche Eingabe!\n")
        else:
            if zahlen >= 1 and zahlen <= 9:
                zaehler = zaehler + 1
                feld_proben()
                xodero_eintragen()
                feld_drucken()
                zaehler = gewinn_proben(spieler, zaehler)
                spieler_wechseln()
            else:
                print("\nFalsche Eingabe!\n")
    counter()
    
    zaehler = 0
    feld = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    initialisierung_abfragen()
    spieler_wechseln()
exit()

# Testinnnngggg