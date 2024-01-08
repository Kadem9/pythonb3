import random

# Je créer une fonction qui renvoie un nombre aléatoire entre 1 et 6
def lancer_de():
    return random.randint(1, 6)

# je Créeer mes joueurs
score_joueur1 = 0
score_joueur2 = 0

# je rentre le nombre de manche
nombre_de_manches = 10000

# Je créer une boucle pour chaque manche
for manche in range(nombre_de_manches):
    # Première manche : Chaque joueur tire une fois
    resultat_joueur1 = lancer_de()
    resultat_joueur2 = lancer_de()

    # Je compare les résultats
    if resultat_joueur1 > resultat_joueur2:
        score_joueur1 += 1
    elif resultat_joueur2 > resultat_joueur1:
        score_joueur2 += 1

    # Deuxième manche : Chaque joueur tire 5 fois
    valeurs_joueur1 = [lancer_de() for _ in range(5)]
    valeurs_joueur2 = [lancer_de() for _ in range(5)]

    # Jer trie les valeurs par ordre décroissant
    valeurs_joueur1.sort(reverse=True)
    valeurs_joueur2.sort(reverse=True)

    # Je compare les résultats
    if valeurs_joueur1[0] > valeurs_joueur2[0]:
        score_joueur1 += 1
    elif valeurs_joueur2[0] > valeurs_joueur1[0]:
        score_joueur2 += 1

# j'affiche les résultats
print(f"Résultats après {nombre_de_manches} manches :")
print(f"Joueur 1 a un score de {score_joueur1} points.")
print(f"Joueur 2 a un score de {score_joueur2} points.")

# je compare les scores pour déterminer le gagnant
if score_joueur1 > score_joueur2:
    print("Joueur 1 remporte la partie !")
elif score_joueur2 > score_joueur1:
    print("Joueur 2 remporte la partie !")
else:
    print("La partie est un match nul !")
