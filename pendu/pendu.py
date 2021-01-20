# import de la librairie random pour la gestion aléatoire d'une liste
import random

# fonction qui récupère la liste des étapes du pendu :
def get_array_from_file(filepath,separator,size=0):
    file = open(filepath,"r")
    rows_array = file.read().split(separator)
    file.close()
    if int(size) > 0:
        rows_array = [i for i in rows_array if len(i)==size]
    return rows_array

# fonction qui affiche la lettre cachée dans le mot à deviner :
def display_hidden_letter(local_hidden_letters,local_word):
    hidden_word = ""
    for i in local_word:
        if i in local_hidden_letters:
            hidden_word += i.upper() + ' '
        else:
            hidden_word += '_ '
    print(hidden_word)

# fonction booleenne qui permet de savoir si le joueur souhaite ou non continuer la partie
def replay():
    print("Voulez - vous continuez la partie : \noui ( o ) ou non ( n ) ?")
    reponse = input()
    return reponse == 'o'

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
def main_pendu():

    error_count = 0
    hidden_letters = []
    str_word_size = ""

    logger.info("Starting application pendu")

    logger.info("Reading word size")
    while(not str_word_size.isdigit() or int(str_word_size)==0):
        if not str_word_size=="":
            logger.error("Error in word size !!!")           
        print("Entrez le nombre de lettres : ")
        str_word_size = input()

    word_size = int(str_word_size)
    logger.info("Getting word size OK")

    words_array = get_array_from_file("mots.txt",'\n',word_size)
    logger.info("Reading file mots.txt")
    word = random.choice(words_array)

    while(word_size > 0):
        print("Tappez une lettre :")
        letter = input().lower()
        if ( len(letter) == 1 ) and letter[0].isalpha():
            if letter in word:
                logger.info("letter " + letter + "in word " + word)
                hidden_letters.append(letter)
                display_hidden_letter(hidden_letters,word)
                word_size = len(word) - len(hidden_letters)
                if word_size == 0:
                    print("Partie gagnée !!!")
                    logger.info("Game won")
                    break
            else:
                logger.error("Error : Letter " + letter + " not in word " + word + " Printing pendu")
                print(pendu_array[error_count])
                error_count += 1
                if error_count == 5:
                    print("Partie perdue !!!")
                    logger.info("Game loss")
                    break
        else:
            logger.error("Error in format of the letter")

    if replay(): main_pendu()

logger = get_logger()

logger.info("Reading file pendu.txt")
pendu_array = get_array_from_file("pendu.txt",'.')

main_pendu()