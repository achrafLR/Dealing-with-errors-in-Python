while True:
    try:
        a = int(input('a ? '))
        b = int(input('b ? '))

        print(f"{a} / {b} = {a / b}")
            
    except Exception as e:
        print('Warning : ', e)
