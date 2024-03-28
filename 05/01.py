number=int(input())
number2=int(input())
for x in range(number, number2+1):
    if x%3!=0 and x%5!=0:
        print(x)
    elif x%5==0:
        print('Buzz')
    elif x%3:
        print('Fizz')
    else:
        print('FizzBuzz')