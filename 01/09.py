print('Введите логин')
login=input()
print('Введите адрес резервной электронной почты')
mail=input()
if '@' in login:
    print('Некорректный логин')
elif not'@' in mail:
    print('Некорректный адрес электронной почты')
else:
    print('OK')
