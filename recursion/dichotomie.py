def dichotomie(t,x,p=0):
    if x in t:
        if t[p] < x:
            p = p + (len(t)-p)//2
            return dichotomie(t,x,p)
        elif t[p] > x:
            t = t[:p]
            p = p//2
            return dichotomie(t,x,p)
        elif t[p] == x:
            return p
    else:
        return -1

def main():
    print("Entrer la taille de la liste d'entiers triés par ordre croissant : ")
    size_list = input()
    my_list = [i for i in range(1,int(size_list)+1,2)]
    print(my_list)
    print("Entrer la valeur de l'entier à rechercher")
    x = input()
    position = dichotomie(my_list,int(x))
    print("la position de %d est %d" % (int(x),position))

main()