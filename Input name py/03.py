while True:
    try:
        a = int(input('a ? '))
        b = int(input('b ? '))

        print(f"{a} / {b} = {a / b}")
            
    except ValueError as v:
        print('Warning (ValueError) : ', v)
    except ZeroDivisionError as z:
        print('Warning : ', z)
    except Exception as e:
        print('Warning : ', e)
