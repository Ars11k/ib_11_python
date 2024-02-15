num=float(input())
num2=float(input())
oper=input()
if oper=='+':
    print(num+num2)
elif oper=='-':
    print(num-num2)
elif oper=='*':
    print(num*num2)
elif oper=='/':
    if num2 !=0:
        print(num/num2)
    else:
        print('888888')
else:
    print('888888')
