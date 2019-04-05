"""
Créer un algorithme permettant de créer aléatoirement un mot de passe devant respecter des contraintes exposées. 

"""
listeMaj = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "H", "I", "J", "K"]
listeMin = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n"]
listeNb = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
listePonct = ["?", "/", "(", "&", ")", "!", ";", "^"]


import random

# Déclaration la longueur de MDP
passwordLenght = random.randint(8, 12)
print (passwordLenght)

# Choix des 3 premiers caractères constituant le MDP
nbAlEntier = random.randint(0, 13)
maj = listeMaj[nbAlEntier]
print (maj)

nbAlEntier = random.randint(0, 9)
numChif = listeNb[nbAlEntier]
print (numChif)

nbAlEntier = random.randint(0, 7)
ponc = listePonct[nbAlEntier]

password = [maj, numChif, ponc]

# Remplissage de la fin du MDP 
while len (password) < passwordLenght:
    kelBoite = random.randint(0, 3)
    if kelBoite == 0:
        bigBox = listeMaj
    if kelBoite == 1:
        bigBox = listeMin
    if kelBoite == 2:
        bigBox = listeNb 
    if kelBoite == 3:
        bigBox = listePonct
    nbAlEntier = random.randint(0, len (bigBox)-1)
    password.append(bigBox[nbAlEntier])
    print (password)

# Mélanger les caractères    
random.shuffle(password)
print(password)

# Afficher mon MDP sous forme de chaine de caractères
print("".join(password))

