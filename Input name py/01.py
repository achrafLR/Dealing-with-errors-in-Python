try:
    name = input('Enter your name : ')
    if (name == ''):
        raise ValueError('name is empty')
    if (name.strip() == ''):
        raise ValueError('the name contains just the spaces')
    if (set(name).intersection("0123456789") != set()):
        raise ValueError('the name contains numbers')
except ValueError as e:
    print(f'Problem : {e} ')