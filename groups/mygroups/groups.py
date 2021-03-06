# reprendre l'exo groupe
# 1 - logique : répartir en groupe
# 2 - lire le fichier texte d'entrée avec tous les noms
# 3 - Rajouter les logs (print -> log.txt)
# 4 - Ecrire le résultat des outputs dans un fichier json
# 5 - Packager l'application pour éxecuter l'application grace à une commande 'make_groups'

# fonction permettant de récupérer la liste des noms à partir d'un fichier texte :

def get_names_from_file(filepath):
    try:
        file = open(filepath,"r")
        names = file.read().split('\n')
        file.close()
        logger.info("Reading file " + filepath + " OK")
        return names
    except:
        logger.error("Error in openning file " + filepath)
        return []


def get_groups_from_names( local_names , nb_groups ):

    import random

    dict_groups = {}
    max_nb_groups = int(len(local_names) / nb_groups)
    size_names = len(local_names)
    i = 1

    print("\nVoici la nouvelle répartion de groupes:\n")

    while(size_names > 0):

        # crée un tableau selected contenant k items choisis au hasard dans le tableau names
        selected = random.sample(local_names, max_nb_groups)

        # affiche l'indice i et le contenu du tableau selected
        print("GROUP #%s :" % (i))
        for elem in selected:
            print(elem)            
        print()

        # ajoute la liste des noms sélectionnés dans le dictionnaire dict_groups
        dict_groups[i] = selected
        
        #size_names = size_names - max_nb_groups
        i = i + 1
        
        # pour tout élément sel du tableau selected
        for sel in selected:
            # supprimer l'élémént sélectionné du tableau names
            local_names.remove(sel)

        # met à jour la taille de la liste local_names    
        size_names = len(local_names)

    return dict_groups


def write_json_result( local_dict_groups , json_filepath ):

    import json

    str_response = ""

    try:
        with open(json_filepath,'w') as file:
            json.dump(local_dict_groups,file,indent=4,ensure_ascii=False,sort_keys=True)
            str_response = json.dumps(local_dict_groups)
            logger.info("Generation json file " + json_filepath + " OK")
    except:
        logger.error("Error in generating json file " + json_filepath)

    return str_response

# fonction qui retourne le logger
def get_logger():

    import logging
 
    from logging.handlers import RotatingFileHandler
 
    # création de l'objet logger qui va nous servir à écrire dans les logs
    logger = logging.getLogger()
    # on met le niveau du logger à DEBUG, comme ça il écrit tout
    logger.setLevel(logging.DEBUG)
    
    # création d'un formateur qui va ajouter le temps, le niveau
    # de chaque message quand on écrira un message dans le log
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

    # création d'un handler qui va rediriger une écriture du log vers
    # un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
    file_handler = RotatingFileHandler('log.txt', 'a', 1000000, 1)

    # on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
    # créé précédement et on ajoute ce handler au logger
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # création d'un second handler qui va rediriger chaque écriture de log
    # sur la console
    # stream_handler = logging.StreamHandler()
    # stream_handler.setLevel(logging.DEBUG)
    # logger.addHandler(stream_handler)

    return logger

# programme principal
def main():

    logger.info("Starting application groups")

    print("Entrez le chemin du fichier contenant tous les noms :")
    filepath = input()

    my_names = get_names_from_file(filepath)
    logger.info("Getting names from file " + filepath + " OK")

    str_nb_groups = ""
    while( not str_nb_groups.isdigit() or ( int(str_nb_groups)==0 or int(str_nb_groups)>len(my_names) ) ):
        if not str_nb_groups == "":
            logger.error("Error in groups size")
        print("Entrez le nombre de nombre de groupes :")
        str_nb_groups = input()

    nb_groups = int(str_nb_groups)

    logger.info("Getting groups size OK")

    my_groups = get_groups_from_names(my_names,nb_groups)
    logger.info("Getting groups from names OK")

    write_json_result(my_groups,"resultat.json")

    logger.exception("Exception : number of groups entered is not int type")

    print("Voulez - vous créer une nouvelle répartition : \noui ( o ) ou non ( n ) ?")
    reponse = input()
    if reponse == 'o': main()

logger = get_logger()

#main() appel de cette méthode pour tester l'application