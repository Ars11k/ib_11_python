print('Вы любите спорт?')
answer =input()
print('Вы учитесь в школе?')
answer2 =input()
if answer and answer2!='да' or'нет':
    print('Eror')
    exit()
if 'да' in answer:
    print('Молодец! Спорт - это жизнь')
else:
    print('Займись спортом!')
    exit()
if 'да' in answer2:
    print('Учись хорошо!')
else:
    print('Значит универ')


