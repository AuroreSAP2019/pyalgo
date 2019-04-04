"""
@name manip_tableau.py
@author Aélion
@version 1.0.0
    Algorithmique spécifique sur les collections 
    """


"""
getLowerof function
return the lowest value of two params 
"""
def getLowerOf(firstVal, secondVal):
    if firstVal < secondVal:
        return firstVal
    else:
        return secondVal

"""
getGreaterOf function
return the greater value of two params 
"""
def getGreaterOf(firstVal, secondVal):
    if firstVal > secondVal:
        return firstVal
    else:
        return secondVal

"""
 compare function
 @param firstVal First value to compare
 @param secondVal Second value to compare 
 @param howTo Mode de comparaison souhaité 
 @return greater or lower value of two depends on desc param
"""
def compare(firstVal, secondVal, desc=True):
    if (desc):
        return getLowerOf(firstVal, secondVal)

    return getGreaterOf(firstVal, secondVal)

"""
min function
@param anArray The array from which i want to get the min value
@return theMin value of anArray

    ALGORITHME
    FONCTION min(anArray: Tableau)
        theMin: Entier <- anArray[0]
        POUR indice: Entier DE 0 A longueur(tableau) INC 1
            SI theMin < tableau[indice]
            ALORS
                theMin <- tableau[indice]
            FIN SI
        FIN POUR
        RETOURNE theMin
    FIN FONCTION
"""
def min(anArray):
    theMin = anArray[0] # Récupère la première valeur de mon tableau
    print("Minimum au départ : ", theMin) # On attend dans l'exemple que ce soit 15 qui s'affiche

    indice = 0
    for value in anArray[1:]:
        print("Occurrence [", indice, "] : compare => ", theMin, " et ", value)
        theMin = compare(theMin, value, True)
        print("===> Occurrence [", indice, "] : le plus petit des deux est :", theMin)
        indice = indice + 1
        

    return theMin
"""
max function
@param anArray The array from which i want to get the max value
@return theMax value of anArray
"""
def max(anArray):
    theMax = anArray[0]
    for value in anArray[1:]:
        theMax = compare(theMax, value, False)

    return theMax 


    



# Déclaration du tableau de démonstration 
monTablo = [15, 3, 25, 12, 7, -15]

# More complex loop with condition 
for indice, val in enumerate(monTablo): # Boucle pour parcourir chacun des éléments du tableau
    if monTablo[indice] % 2 == 0: # Est ce que la valeur lue est paire ?
        print ("Multiplication du chiffre pair à l'indice", indice, " : ", monTablo[indice] * 2)

# Find a min (boucle)
print("Valeur minimum de monTablo : ", min(monTablo))
print ("And the max is :", max(monTablo))

