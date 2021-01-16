import random

# fonction qui récupère la liste des étapes du pendu :
def get_array_from_file(filepath,separator):
    file = open(filepath,"r")
    rows_array = file.read().split(separator)
    file.close()
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
    
    word = random.choice(words_array)
    word_size = len(word)

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
words_array = ["test","orange","chambre","sport"]

main_pendu()