login = input()
vvod = '@'
mail = input()
if vvod in login:
    print('Некорректный логин')
elif vvod not in mail:
    print('Некорректный адрес')
else:
    print('OK')