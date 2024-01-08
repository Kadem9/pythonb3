# Gestionnaire de liste de mots
# ajoute un mot si il n’est pas présent dans un tableau
# Le supprime si il est déjà présent
# Renvoie le tableau si on écrit « tableau »
# Arrête le programme si on écrit « stop »

# Je crée une liste vide pour stocker les mots
liste_de_mots = []

# Je crée une boucle infinie pour demander à l'utilisateur d'entrer une action
while True:
    
    action = input("Veuillez entrer une action (ajouter/supprimer/tableau/stop) : ")

    # Je vérifie quelle action a été entrée
    # Si l'action est "ajouter", j'ajoute un mot à la liste
    if action == "ajouter":
        
        mot_a_ajouter = input("Entrez le mot à ajouter : ")
        
        # Je fais des vérifs pour être sur que le mot n'y est pas déjà
        if mot_a_ajouter not in liste_de_mots:
            # si le mot n'est pas présent dans la liste, je l'ajoute
            liste_de_mots.append(mot_a_ajouter)
            # le f avant la chaine de caractère permet d'insérer des variables dans la chaine
            # source : https://docs.python.org/fr/3/tutorial/inputoutput.html
            print(f"Le mot '{mot_a_ajouter}' a été ajouté à la liste.")
        else:
            # si le mot est déjà présent dans la liste, j'affiche un msg d'erreur
            print(f"Le mot '{mot_a_ajouter}' est déjà présent dans la liste.")

    # Si l'action est "supprimer", je supprime un mot de la liste
    elif action == "supprimer":
        
        mot_a_supprimer = input("Entrez le mot à supprimer : ")
        
        # Je fais des vérifs pour être sur que le mot est présent
        if mot_a_supprimer in liste_de_mots:
            # Je supprime le mot de la liste
            liste_de_mots.remove(mot_a_supprimer)
            print(f"Le mot '{mot_a_supprimer}' a été supprimé de la liste.")
        else:
            print(f"Le mot '{mot_a_supprimer}' n'est pas présent dans la liste.")

    # Si l'action est "tableau", j'affiche la liste complète des mots
    elif action == "tableau":
        
        print("Liste des mots :")
        for mot in liste_de_mots:
            print(mot)

    # Si l'action est "stop", j'arrête le programme
    elif action == "stop":
        print("Programme terminé.")
        break

    # Si l'action n'existe pas, je met un msg d'erreur
    else:
        print("Action non valide. Veuillez entrer 'ajouter', 'supprimer', 'tableau' ou 'stop'.")
