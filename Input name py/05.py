while True:
    try:
        a = int(input('a ? '))
        b = int(input('b ? '))

        print(f"{a} / {b} = {a / b}")
            
    except (ValueError, ZeroDivisionError) as v:
        print('Warning (Error) : ', v)
    except Exception as e:
        print('Warning : ', e)
    else:
        print("Great,you don't Haven't any error")
    finally:
        print('Thank you for used my apps')