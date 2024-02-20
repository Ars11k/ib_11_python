password=input()
password2=input()
if len(password)<8:
    print('Короткий')
elif password!=password2:
    print('Различаются')
else:
    print('OK')