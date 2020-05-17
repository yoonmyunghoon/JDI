num1=int(input())
oper=input()
num2=int(input())

if(oper == '+'):
    print('{} + {} = {}' .format(num1, num2, num1+num2))
elif(oper == '-'):
    print('{} - {} = {}' .format(num1, num2, num1-num2))
elif(oper == '*'):
    print('{} * {} = {}' .format(num1, num2, num1*num2))
elif(oper == '/'):
    print('{0} / {1} = {2: 0.3f}' .format(num1, num2, num1/num2))
else:
    print('+, -, *, / 중에 한가지 연산자를 사용하세요.')