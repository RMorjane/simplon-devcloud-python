def decomposer(n):

    d = int('1' + (len(str(n)) - 1)*'0')
    q = int(n // d)
    r = int(n % d)
    print("(",q," X ",d,") + ",end="")

    if r > 0: decomposer(r)

decomposer(1998)