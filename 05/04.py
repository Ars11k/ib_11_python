number=int(input())
for i in range(number):
    lens=input()
    if 'Кот' in lens or 'кот' in lens:
        print('Мяу')
        break
    else:
        print("НЕТ")

