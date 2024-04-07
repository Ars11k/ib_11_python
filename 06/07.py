number=int(input())
country='Евразия'
country2='Остазия'
for i in range(number):
    lens=input()
    if 'С кем война?' in lens:
        print(country)
    elif 'С кем мир' in lens:
        print(country2)
    elif 'Меняем' in lens:
        country, country2=country2, country


