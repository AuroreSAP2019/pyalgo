"""
@name rendu_monnaie.py
@author Aélion
@version 0.0.1
A poor coins counter
Use // to get an interger division
Use % to get rest of int div 
Use input() function to get a user entry 
"""


somme = 400
print ("Vous devez", somme, "€")
billet100 = somme // 100
rendu100 = somme % 100
billet50 = rendu100 // 50
rendu50 = rendu100 % 50
billet20 = rendu50 // 20
rendu20 = rendu50 % 20
billet10 = rendu20 // 10
rendu10 = rendu20 % 10
billet5 = rendu10 // 5
rendu5 = rendu10 % 5
piece2 = rendu5 // 2
rendu2 = rendu5 % 2
piece1 = rendu2 // 1
rendu1 = rendu2 % 1

print (billet100,billet50,billet20,billet10,billet5,piece2,piece1)
print ("Rendu")
print (billet100, "x100€")
print (billet50, "x50€")
print (billet20, "x20€")
print (billet10, "x10€")
print (billet5, "x5€")
print (piece2, "x2€")
print (piece1, "x1€")

