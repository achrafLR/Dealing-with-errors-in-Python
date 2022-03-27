while True:
    def fact(n):
        if n < 0:
            raise ArithmeticError("Il faut donner un entier positif. Attention.")
        if n == 0:
            return 1
        return n * fact(n - 1)
    try:
        n = int(input('Entrez un nombre : '))
        print(fact(n))
    except ArithmeticError:
        print(ArithmeticError)
    except:
        print('Veuillez entrer un nombre.')