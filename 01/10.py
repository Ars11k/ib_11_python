print('Вы находитесь в пещере на развилке. Вы можете пойти "налево", "направо" или "прямо". Введите одно из слов в кавычках для выбора')
ans=input()
if ans=='налево':
    print('Вы направились налево. Через некоторое время вы дошли до двух дверей. Вы выберете "левую" или "правую"?')
    ans2=input()
    if ans2=='правую':
        print('Вы смело открыли правую дверь. Но за ней вас подстерегала гигантская подземная жаба, которая проглотила вас целиком!')
    else:print('Game over')
else:
    print('Game over')
