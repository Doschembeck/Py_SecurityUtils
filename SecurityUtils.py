# coding=utf-8
import random
from math import pi, log

def getSurfaceOfCarre(cote):
    print(cote ** 2)
def getSurfaceOfRectangle(longueur, largeur):
    print(longueur * largeur)
def getSurfaceOfTriangle(base, hauteur):
    print((base * hauteur) / 2)
def getSurfaceOfDisque(rayon):
    print((pi * rayon) ** 2)
def getVolumeOfCube(cote):
    print(cote ** 3)
def getVolumeOfRectangle(longueur, largeur, hauteur):
    print(longueur * largeur * hauteur)
def getVolumeOfCone(rayon, hauteur):
    print((pi * rayon ** 2 * hauteur) / 3)
def getVolumeOfCylindre(hauteur, rayon):
    print(pi * rayon ** 2 * hauteur)
def getPriceTTC(prixHT, taxe=20):
    print(prixHT * (1 + (float(taxe) / 100)))
def getPriceHT(prixTTC, taxe=20):
    print(prixTTC / (1 + (float(taxe) / 100)))
def bissextil(yearEnter):
    year1 = False
    year2 = False
    year3 = False
    year4 = False

    if yearEnter % 4 == 0:
        year1 = True
    else:
        print ("Ce n'est pas une année bissextile !")

    if yearEnter % 100 != 0:
        year3 = True
    else:
        year2 = False
        print ("Ce n'est pas une année bissextile !")

    if yearEnter % 400 == 0:
        year4 = True

    if year1 and year3 and year4:
        print ("C'est une année bissextile !")
def paireOrImpaire():
    while (True):

        print("")

        chiffre = raw_input("Entrer un nombre : ")

        if chiffre.lower() == "n":
            break

        if long(chiffre) % 2 == 0:
            print("Le nombre est paire")
        else:
            print("Le nombre est impaire")
def hauteurParcourue(nbrMarche, hauteurOfMarche):
    toilette = 5
    semaine = 7

    result = (((nbrMarche * 2) * toilette) * semaine) * hauteurOfMarche

    print("Pour %s marches de %s m, il parcourt %s mètres par semaines." % (nbrMarche, hauteurOfMarche, result))
def countLoosePoints(vPoule, vChien, vVache, vAmis):
    soldeDePoints = 100
    pPoule = 1
    pChien = 3
    pVache = 5
    pAmis = 10

    calculPoints = (vPoule * pPoule) + (vChien * pChien) + (vVache * pVache) + (vAmis * pAmis)

    soldeDePoints -= calculPoints

    print("Il a perdu  %s points, il lui reste donc %s" % (calculPoints, soldeDePoints))
def nbrPremier(input):
    nombre = input("Entrer un nombre supérieur à 1 : ")

    for i in range(2, nombre + 1):
        if nombre % i == 0:
            print("%s  est un diviseur de : %s" % (i, nombre))
        else:
            print("C'est un nombre premier")

    v = 0

    for i in range(100, 301, 10):
        (9 + (170 / i) * 60)
def print_voyelle(mot):
    voyelles = "aeiouy"

    for lettre in mot:

        if str(lettre).lower() in voyelles:
            print (lettre)
        else:
            print ("*")
def print_consonne(mot):
    consonnes = "zrtpqsdfghjklmwxcvbn"

    for lettre in mot:

        if str(lettre).lower() in consonnes:
            print (lettre)
        else:
            print ("*")

def checkPowerPasswordInBits(password):
    useAlphMin = False
    useAlphMaj = False
    useNumber = False
    useSpec = False

    ALPHABET_MIN = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
    ALPHABET_MAJ = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z"]
    CHARACTERS_SPECIAL = ["/", ",", "&", "@", "?", ";", ":",
                     "%", "$", "*", "^", ".", "[", "]", "<", ">"]
    NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    alphabetGlobal = []

    for lettre in password:
        if not useAlphMaj and lettre in ALPHABET_MAJ:
            alphabetGlobal += ALPHABET_MAJ
            useAlphMaj = True

        elif not useAlphMin and lettre in ALPHABET_MIN:
            alphabetGlobal += ALPHABET_MIN
            useAlphMin = True

        elif not useSpec and lettre in CHARACTERS_SPECIAL:
            alphabetGlobal += CHARACTERS_SPECIAL
            useSpec = True

        elif not useNumber and lettre in NUMBERS:
            alphabetGlobal += NUMBERS
            useNumber = True

        elif not lettre in alphabetGlobal:
            print("Caractére inconnu !")

    force = len(alphabetGlobal) ** len(password)

    # print("longueur du mot de passe = %s" % (len(password)))
    # print("Longueur de l'alphabet global = %s" % (len(alphabetGlobal)))

    return int(log(force, 2))
def levelSecurity(passBits):
    if passBits <= 64:
        print ("Le mot de passe est très faible !")

    if 64 < passBits <= 80:
        print ("Le mot de passe est faible !")
    if 80 < passBits <= 100:
        print ("Le mot de passe est moyen ")
    if passBits > 100:
        print "Le mot de passe est fort !"
def generatePassword(nbrcaracteres, majUtility=True, minUtility=True, specUtility=False, numbersUtility=True):
    ALPHABET_MIN = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
    ALPHABET_MAJ = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z"]
    ALPHABET_SPEC = ["/", ",", "&", "@", "?", ";", ":",
                          "%", "$", "*", "^", ".", "[", "]", "<", ">"]
    ALPHABET_NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    AlphabetGlobal = []
    password = []

    for i in range(nbrcaracteres):
        password.append(str(i))

    indexFree = range(nbrcaracteres)

    if not majUtility and not minUtility and not specUtility and not numbersUtility:
        return "Erreur : Vous n'avez pas rentrer de parametres."
    elif nbrcaracteres < 4:
        return "Erreur : La longueur du mot de passe doit faire minimum 4 caracteres."

    else:
        # ==========================================
        # Ajoute a l'alphabet global les alphabets selectionnés
        # ==========================================

        if majUtility:
            AlphabetGlobal += ALPHABET_MAJ
            index = random.choice(indexFree)
            indexFree.remove(index)
            password[index] = random.choice(ALPHABET_MAJ)

        if minUtility:
            AlphabetGlobal += ALPHABET_MIN
            index = random.choice(indexFree)
            indexFree.remove(index)
            password[index] = random.choice(ALPHABET_MIN)

        if specUtility:
            AlphabetGlobal += ALPHABET_SPEC
            index = random.choice(indexFree)
            indexFree.remove(index)
            password[index] = random.choice(ALPHABET_SPEC)

        if numbersUtility:
            AlphabetGlobal += ALPHABET_NUMBERS
            index = random.choice(indexFree)
            indexFree.remove(index)
            password[index] = random.choice(ALPHABET_NUMBERS)


        # Genere un mot de passe aléatoire
        for i in range(nbrcaracteres):
            if(i in indexFree):
                password[i] = random.choice(AlphabetGlobal)

    return "".join(password)

def bruteForcePassWord(secretPassWord):
    
    testPass = "aaaa"
    
    if(secretPassWord == testPass):
        print("Mot de passe cracké !")