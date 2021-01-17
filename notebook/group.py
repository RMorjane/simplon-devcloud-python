# COMMENTEZ CHAQUE LIGNE DE CE SCRIPT EN EXPLIQUANT CE QU'ELLE FAIT ET POURQUOI

# EXPLIQUEZ CE QUE FAIT RANDOM.SAMPLE ET LES ALTERNATIVES QUI EXISTENT EN CHERCHANT SUR INTERNET

# EXPLIQUEZ LE %S DU PRINT, QUELS SONT LES AUTRES POSSIBILITES

# EXPLIQUEZ LE BUT DE CE SCRIPT

# CORRIGEZ LES ERREURS DE CE SCRIPT

# RAJOUTER AU SCRIPT UNE PARTIE QUI AFFICHE TOUS LES NOMS

# FAITES EN SORTE QUE LE RESULTAT RESSEMBLE A
    # GROUP #1:  ['nameX', 'nameX']
    # GROUP #2:  ['nameX', 'nameX']
    # GROUP #3:  ['nameX', 'nameX']
    
# MODIFIEZ LE PRINT POUR REVENIR A LA LIGNE AVANT D'AFFICHER LES GROUPES

# MODIFIEZ LE SCRIPT POUR SELECTIONNER UN A UN LES MEMBRES DE LA LISTE "selected"

# MODIFIEZ LE SCRIPT PRECEDANT POUR OBTENIR LE MEME FONCTIONNEMENT SANS AVOIR A DETERMINER LE NOMBRE DE GROUPES
# INDICE: TOUT SE PASSE SUR LA LISTE NAMES
# INDICE: PENSER A WHILE

# TRANSPOSER CE CODE DANS UN FICHIER .PY ET TROUVER COMMENT L'EXECUTER DEPUIS UN TERMINAL

# importe toutes les fonctions de la classe random
import random

# déclaration et initialisation des variables indicées name
name1 = 'name1'
name2 = 'name2'
name3 = 'name3'
name4 = 'name4'
name5 = 'name5'
name6 = 'name6'

# déclaration et initialisation d'un tableau names
names = [name1, name2, name3, name4, name5, name6]

# affichage de tous les noms du tableau names
print(names,"\n")

# déclaration et initialisation de la variable entière nb_groups
nb_groups = 3

# déclaration et calcul de la variable max_nb_groups
# len(names) : taille du tableau names
max_nb_groups = int(len(names) / nb_groups)

# pour i allant de 1 à nb_groups
# for i in range(1,nb_groups + 1): # erreur

i = 1
size_names = len(names)

while(size_names > 0):

    # crée un tableau selected contenant k items choisis au hasard dans le tableau names
    selected = random.sample(names, max_nb_groups)
    
    # affiche l'indice i et le contenu du tableau selected
    print("GROUP #%s :" % (i))
    for elem in selected:
        print(elem)
        
    print()
    
    #size_names = size_names - max_nb_groups
    i = i + 1
    
    # pour tout élément sel du tableau selected
    for sel in selected:
        # supprimer l'élémént sélectionné du tableau names
        names.remove(sel)
        
    size_names = len(names)
        
print(names)
