# j'importe le module datetime qui permet de manipuler les dates comme vu dans le cours
import datetime

# je récupère la date du jour
date = datetime.datetime.now()
annee_en_cours = date.year

# je demande à l'utilisateur de saisir son année de naissance
anneeSaisie = input("Merci d'entrer votre année de naissance : ")

# je convertis la saisie en entier
anneeSaisie = int(anneeSaisie)

# je calcule l'age de l'utilisateur
age = annee_en_cours - anneeSaisie

# j'affiche le résultat
print("votre age est : ", age)

# je calcule ensuite son age en mois en multipliant son age par 12
ageMois = age * 12
print("votre age en mois est : ", ageMois)

# je calcule ensuite son age en jours en multipliant son age par 365 et en ajoutant 5 jours pour les années bissextiles
ageJours = age * 365 + 5
print("votre age en jours est : ", ageJours)

# je calcule ensuite son age en semaine en multipliant son age par 52 puis en divisant ageEnJours par 7
ageSemaine = age * 52
ageSemaine = int(ageJours / 7) # je convertis le résultat en entier pour ne pas avoir de virgule
print("votre age en semaine est : ", ageSemaine)
