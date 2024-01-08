#tp 2 : Comptage de lettres et de mots d’une chaine de caractère saisie
# Compter le nombre de voyelle d’une chaine de caractère saisie
# Compter le nombre de présence d’une lettre dans d’une chaine de caractère saisie
# Renvoyer une liste de mot à partir d’une phrase
# Vérifier la présence d’une lettre dans d’une chaine de caractère saisie
# Vérifier la présence d’un mot dans une liste (retourne sa position dans le tableau)

# Je vais créer une fonction pour chaque traitement à effectuer
# Je vais ensuite appeler ces fonctions dans la fonction principale
# Je vais ensuite afficher le résultat de la fonction principale

# Fonction qui compte le nombre de voyelle d’une chaine de caractère saisie
def comptageVoyelle(chaine):
    # je déclare une variable qui contiendra le nombre de voyelle
    nbVoyelle = 0
    # je déclare une variable qui contiendra la liste des voyelles
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    # je parcours la chaine de caractère saisie
    for lettre in chaine:
        # je vérifie si la lettre est dans la liste des voyelles
        if lettre in voyelles:
            # si la lettre est dans la liste des voyelles, j'incrémente mon compteur
            nbVoyelle += 1
    # je retourne le nombre de voyelle
    return nbVoyelle

# Fonction qui compte le nombre de présence d’une lettre dans d’une chaine de caractère saisie
def comptageLettre(chaine, lettre):
    # je déclare une variable qui contiendra le nombre de présence de la lettre
    nbLettre = 0
    # je parcours la chaine de caractère saisie
    for lettreSaisie in chaine:
        # je vérifie si la lettre saisie est égale à la lettre recherchée
        if lettreSaisie == lettre:
            # si la lettre est égale à la lettre recherchée, j'incrémente mon compteur
            nbLettre += 1
    # je retourne le nombre de présence de la lettre
    return nbLettre

# Fonction qui renvoie une liste de mot à partir d’une phrase
def listeMot(chaine):
    # je déclare une variable qui contiendra la liste des mots
    liste = []
    # je déclare une variable qui contiendra le mot en cours de traitement
    mot = ""
    # je parcours la chaine de caractère saisie
    for lettre in chaine:
        # je vérifie si la lettre est un espace
        if lettre == " ":
            # si la lettre est un espace, j'ajoute le mot dans la liste
            liste.append(mot)
            # je réinitialise la variable mot
            mot = ""
        else:
            # si la lettre n'est pas un espace, j'ajoute la lettre au mot
            mot += lettre
    # je retourne la liste des mots
    return liste

# Fonction qui vérifie la présence d’une lettre dans d’une chaine de caractère saisie
def presenceLettre(chaine, lettre):
    # je déclare une variable qui contiendra le résultat de la recherche
    presence = False
    # je parcours la chaine de caractère saisie
    for lettreSaisie in chaine:
        # je vérifie si la lettre saisie est égale à la lettre recherchée
        if lettreSaisie == lettre:
            # si la lettre est égale à la lettre recherchée, je passe la variable presence à True
            presence = True
    # je retourne le résultat de la recherche
    return presence

# Fonction qui vérifie la présence d’un mot dans une liste (retourne sa position dans le tableau)
def presenceMot(liste, mot):
    # je déclare une variable qui contiendra le résultat de la recherche
    presence = False
    # je parcours la liste
    for motListe in liste:
        # je vérifie si le mot de la liste est égale au mot recherché
        if motListe == mot:
            # si le mot est égale au mot recherché, je passe la variable presence à True
            presence = True
    # je retourne le résultat de la recherche
    return presence

# Fonction principale
def comptageLettres():
    # je demande à l'utilisateur de saisir une chaine de caractère
    chaine = input("Merci de saisir une chaine de caractère : ")
    # je déclare une variable qui contiendra le nombre de voyelle
    nbVoyelle = comptageVoyelle(chaine)
    # j'affiche le résultat
    print("Le nombre de voyelle est : ", nbVoyelle)
    # je demande à l'utilisateur de saisir une lettre
    lettre = input("Merci de saisir une lettre : ")
    # je déclare une variable qui contiendra le nombre de présence de la lettre
    nbLettre = comptageLettre(chaine, lettre)
    # j'affiche le résultat
    print("Le nombre de présence de la lettre est : ", nbLettre)
    # je déclare une variable qui contiendra la liste des mots
    liste = listeMot(chaine)
    # j'affiche le résultat
    print("La liste des mots est : ", liste)
    # je demande à l'utilisateur de saisir une lettre
    lettre = input("Merci de saisir une lettre : ")
    # je déclare une variable qui contiendra le résultat de la recherche
    presence = presenceLettre(chaine, lettre)
    # j'affiche le résultat
    print("La lettre est présente : ", presence)
    # je demande à l'utilisateur de saisir un mot
    mot = input("Merci de saisir un mot : ")
    # je déclare une variable qui contiendra le résultat de la recherche
    presence = presenceMot(liste, mot)
    # j'affiche le résultat
    print("Le mot est présent : ", presence)
    
# Appel de la fonction principale
comptageLettres()

