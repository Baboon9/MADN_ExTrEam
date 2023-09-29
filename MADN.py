import random
#Spieler Namen geben
##################
#Spieler im feld?       GOTO A
#Sonst                  GOTO B
##################
#####A Kein Spieler im feld
#würfeln
#6 prüfen
#sechs gewählt?
#spieler ins haus
#nächster spieler
##################      
#####B Spieler im feld
#Würfeln
#Ziehen
#checken
#geschlagen?            GOTO C
#Parkplatz erreicht?    GOTO D
#
#####C
#Zurück ins haus
#####D
#Ende erreicht
#alle drin?
#game Over
##############################STRUKTUREN
spielernamen = ["Tim", "Tom", "Tobias", "Lukas"]
spielerzahl = int(4)
schwierigkeitsgrad = int(1)
team1 = ["Abraham", "Jehemia", "Wolfgang", "Peter"]
team2 = ["Nicola", "Sarah", "Mike", "Kordula"]
team3 = ["Max", "Moritz", "Nils", "Nele"]
team4 = ["Lukas", "Torben", "Sascha", "Ruben"]
teams = [team1, team2, team3, team4]
#Ein zweidimensionales dict mit den Namen der Spielerfiguren. Numerisch geordnet werden so die Spieler hinterlegt 
spielerTeam = [team1,team2,team3,team4]


###############################FUNKTIONEN
def figurennamenEingeben():
    for i in range(4):
        print("Geben sie Namen oder Kürzel für ihre figuren ein:")
        figurnamen.append(input())
    return figurnamen

###############
def spieleinstellungen():
    #Frage nach Anzahl der Spieler, Schwierigkeitsgrad, den Namen der Spieler und speichere sie global ab
    
    print("Geben Sie die Spielerzahl ein.")
    spielerzahl = int(input())
    print("Geben Sie den schwierigkeitsgrad an.")
    schwierigkeitsgrad = input()
    print("Jetzt muss jeder Spieler seinen Figuren einen Namen geben.")
    for i in range(spielerzahl):
        spielernamen.append(input("Spielernamen eingeben"))
    
    #Lass jedem Spieler seine Figuren benennen

    print("Jeder Spieler muss seinen figuren einen kurzen namen, oder kürzel geben.")
    for spieler in range(spielerzahl):
        figurnamen.append(figurennamenEingeben())

def spieleinstellungenDefault():
    print("Willkommen bei Mensch Ärgere dich nicht.")
    print("Maximal 4 Spieler")
    print("Wieviele spielen mit?")
    
    while (spielerzahl == int(input())) > 4: 
        print("Maximal 4 Spieler!")
    
    spielernamen = ["","","",""]
    
    #Damit die Mitspieler identifiziert werden können
    print("Geben sie die Namen der Mitspieler an und das gewählte Team")
    for i in range(spielerzahl):
            spielernamen[i-1] = input()
   
    #Damit die richtigen Figurnamen den entsprechenden Spielern zugeordnet werden können
    for i in range(spielerzahl):
        print("Wählen sie ihr Team: 1, 2, 3, oder 4")
        wahl = input()
        spielerTeam[i] = teams[int(wahl)-1]

def spieleinstellungsausgabe():
    print("Willkommen bei Mensch ärgere dich XtReAm")
    print("Gewählter Schwierigkeitsgrad: {}".format(schwierigkeitsgrad))
    print("Folgende Mitspieler sind im Spiel und haben folgendes Team gewählt")
    for i in range(spielerzahl):
        print("Spielername")
        print(" " + spielernamen[i])
        print("Namen der Figuren")
        print(" {},{},{},{}".format(spielerTeam[i][0], spielerTeam[i][1], spielerTeam[i][2], spielerTeam[i][3]))
    

playerAtTurn = 1
figurPositions = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def startGame():
    print("Spieler {} ist an der Reihe".format(spielernamen[spielerAmZug]))
    if playerHasAllInHouse[playerAtTurn]:
        allInHouse()

def rollDice():
    dice = random.randint(1,6)
    print("Es wurde eine {} gewürfelt".format(dice))
    return dice

playerHasAllInHouse = [True, True, True, True]
def allInHouse():
    print("Es befinden sich alle Figuren im Haus")
    leftRolls = 4
    while leftRolls > 1:
        dice = rollDice()
        if(dice == 6):
            print("Welche Figur soll ins spiel")
            figureName = input()
            setInGame(dice)
            playerHasAllInHouse[playerAtTurn] = False
            break
        leftRolls = leftRolls -1
    pass

def showFigureNames(player):
    pass
def setInGame(dice, figureName):
    print("Eine Figur wurde ins Spiel gelassen.")
    print("Und zwar von spieler {}".format(playerAtTurn))
    figureToMove = 
    moveFigure(dice, figureToMove)
    

spielerAmZug = 1
def chooseFigureToMove():
    pass 
def moveFigure():
    pass
def checkFigure():
    pass
def goBackInHouse():
    pass
def endReached():
    pass
def gameOver():
    pass
def nextTurn():
    pass 

startGame()
