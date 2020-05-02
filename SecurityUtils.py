# coding=utf-8
import random
from math import pi, log

ALPHABET_MIN = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z"]
ALPHABET_MAJ = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
ALPHABET_SPEC = ["/", ",", "&", "@", "?", ";", ":",
                 "%", "$", "*", "^", ".", "[", "]", "<", ">"]
ALPHABET_NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def checkPowerPasswordInBits(password):
    useAlphMin = False
    useAlphMaj = False
    useNumber = False
    useSpec = False

    alphabetGlobal = []

    for lettre in password:
        if not useAlphMaj and lettre in ALPHABET_MAJ:
            alphabetGlobal += ALPHABET_MAJ
            useAlphMaj = True

        elif not useAlphMin and lettre in ALPHABET_MIN:
            alphabetGlobal += ALPHABET_MIN
            useAlphMin = True

        elif not useSpec and lettre in ALPHABET_SPEC:
            alphabetGlobal += ALPHABET_SPEC
            useSpec = True

        elif not useNumber and lettre in ALPHABET_NUMBERS:
            alphabetGlobal += ALPHABET_NUMBERS
            useNumber = True

        elif not lettre in alphabetGlobal:
            print("Caractére inconnu !")

    force = len(alphabetGlobal) ** len(password)

    # print("longueur du mot de passe = %s" % (len(password)))
    # print("Longueur de l'alphabet global = %s" % (len(alphabetGlobal)))

    return int(log(force, 2))


def levelSecurity(passBits):
    if passBits <= 64:
        print("Le mot de passe est très faible !")

    if 64 < passBits <= 80:
        print("Le mot de passe est faible !")
    if 80 < passBits <= 100:
        print("Le mot de passe est moyen ")
    if passBits > 100:
        print("Le mot de passe est fort !")


def generatePassword(nbrcaracteres, majUtility=True, minUtility=True, specUtility=False, numbersUtility=True):
    AlphabetGlobal = []
    password = []
    indexFree = []

    for i in range(nbrcaracteres):
        password.append(str(i))
        indexFree.append(i)

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
            if (i in indexFree):
                password[i] = random.choice(AlphabetGlobal)

    return "".join(password)


def bruteForcePassWord(secretPassWord, lenOfPass=0):
    # Method alphabetic
    lenOfPass = len(secretPassWord)

    completeList = []
    result = ""

    for current in range(lenOfPass):
        a = [i for i in ALPHABET_MIN]
        for y in range(current):
            a = [x + i for i in ALPHABET_MIN for x in a]

        completeList += a
        print(a)
        if (secretPassWord == a): return a

    return completeList

result = bruteForcePassWord("v")

print(result)
