# AJOUTEZ UNE FONCTION POUR CHAQUE EXERCICE

import sys

'''
exo1:
function that takes two lists as inputs and returns a list that contains only the elements 
that are common between the lists (without duplicates)

exo2:
function that takes a list and a number and checks whether a specified value is
contained in the list. whats the best type to return ?

exo3:
function that takes a string and calculate the number of digits and letters. 
Choose the best return type, hint: dict

exo4:
function that takes as inputs a number and a list and adds my_nb to the end of the list. 
return list

exo5:
function that takes as inputs a number and a list and adds my_nb to the beggining of the list. 
return list

exo6:
function that takes as inputs a number and a list and adds my_nb either to the 
beginning or end of the list depending on an input specified by the user

exo7:
function that takes as inputs a number and a list and checks whether all numbers of the list
are greater than a certain number. whats the best return type ?

exo8:
function that gets OS name, platform and release information. what inputs do we need here ?
use package os

''' 

def exo1(list_array):
    my_list1 = str(list_array[0]).split(' ')
    my_list2  = str(list_array[1]).split(' ')
    print(my_list1)
    print(my_list2)
    new_list = my_list1 + my_list2
    new_list = set(new_list).difference([n for n in new_list if new_list.count(n) >=3 or new_list.count(n)==1])
    print("new common list without duplicates : ",new_list)

def exo2(list_array):
    my_list = str(list_array[0]).split(' ')
    my_nb = str(list_array[2])
    exist = True if my_list.count(my_nb) else False
    print("my list : ",my_list)
    print("my number : ",my_nb)
    print("is contains : ",exist)

def getCountOf( my_str ):
    l_count = 0
    d_count = 0
    for i in my_str:
        try:
            int(i)
            d_count += 1
        except:
            l_count += 1
    dict_counts = {"digits": d_count , "letters": l_count}
    return dict_counts

def exo3(list_array):
    my_str = str(list_array[3])
    print("my string : ",my_str)
    my_counts = getCountOf(my_str)
    print("my string contains ",my_counts["digits"]," digits and ",my_counts["letters"]," letters")

def exo4(list_array):
    my_list = str(list_array[4]).split(' ')
    my_nb = int(str(list_array[5]))
    print("my list : ",my_list)
    print("my number : ",my_nb) 
    my_list.append(my_nb)   
    print("new list after adding the number at the end of the list : ",my_list)

def exo5(list_array):
    my_list = str(list_array[4]).split(' ')
    my_nb = int(str(list_array[5]))
    print("my list : ",my_list)
    print("my number : ",my_nb)
    my_list.insert(0,my_nb)
    print("new list after adding the number at the beginning of the list : ",my_list)

def exo6(list_array):
    my_list = str(list_array[4]).split(' ')
    my_nb = int(str(list_array[5]))
    print("my list : ",my_list)
    print("my number : ",my_nb)
    print("position:\n1-beginning\n2-end")
    position = input()
    if int(position)==1:
        exo5( [my_nb , my_list] )
    else:
        if int(position)==2:
            exo4( [my_nb , my_list] )

def exo7(list_array):
    my_list = str(list_array[4]).split(' ')
    my_nb = int(str(list_array[6]))
    print("my list : ",my_list)
    print("my number : ",my_nb)
    is_greater = True
    for i in my_list:
        is_greater &= i > my_nb
    if is_greater:
        print("All numbers of the list are greater than ",my_nb)
    else:
        print("All numbers of the list are not greater than ",my_nb)

def getOsInfo():
    import os
    import platform
    os_info = {
        "os_name": os.name,
        "platform": platform.platform(),
        "release": platform.release()       
    }
    return os_info

def exo8(list_array=[]):
    os_infos = getOsInfo()
    for key in os_infos:
        print(os_infos.get(key))

def readFile(filename):
    file = open(filename,"r")
    line = file.read()
    #print(line)
    array_list = line.split('\n')
    #print(array_list)
    file.close()
    return array_list

dict_exos = {1: exo1, 2: exo2, 3: exo3, 4: exo4, 5: exo5, 6: exo6, 7: exo7, 8: exo8}

try:

    my_str = sys.argv[1] # récupère la valeur de l'argument passé dans le terminal
    #print(my_str)

    key_exo = int(my_str[-1:]) # récupère le dernier élément de la chaine contenu dans l'argument du terminal
    #print(key_exo)

    filename = sys.argv[2] # récupère le nom du fichier text contenant les inputs
    my_args = readFile(filename) # retourne une liste de chaines récupérée ligne par ligne du fichier texte

    dict_exos.get(key_exo)(my_args) # appel implicite à la faction correspondant au numéro de l'exo récupéré en argument

except:

    print("Veuillez saisir un numéro d'exercice valide svp !!!")