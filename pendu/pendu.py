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

# fonction qui récupère la chaine de carractère tapé par le user :
def get_input_letter():
    print("Tappez une lettre :")
    local_letter = input()
    return local_letter.lower()

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

def main_pendu():

    error_count = 0
    hidden_letters = []
    str_word_size = ""

    while(not str_word_size.isdigit()):
        print("Entrez le nombre de lettres : ")
        str_word_size = input()

    word_size = int(str_word_size)
    words_array = get_array_from_file("mots.txt",'\n',word_size)
    word = random.choice(words_array)

    while(word_size > 0):
        letter = get_input_letter()
        if ( len(letter) == 1 ) and letter[0].isalpha():
            if letter in word:
                hidden_letters.append(letter)
                display_hidden_letter(hidden_letters,word)
                word_size = len(word) - len(hidden_letters)
                if word_size == 0:
                    print("Partie gagnée !!!\n")
                    break
            else:
                print(pendu_array[error_count])
                error_count += 1
                if error_count == 5:
                    if error_count == 5: print("Partie perdue !!!\n")
                    break

    if replay(): main_pendu()

pendu_array = get_array_from_file("pendu.txt",'.')

main_pendu()