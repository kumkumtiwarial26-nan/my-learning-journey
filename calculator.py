print("Welcome,my first calculator")
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
opreations = input("enter opreations(+,-,/,*)")
if opreations == '+':
    num3 = num1+num2
    print(num3)
elif opreations == '-':
    num3 = num1-num2
    print(num3)
elif opreations == '/':
    num3 = num1/num2
    print(num3)
elif opreations == '*':
    num3 = num1*num2
    print(num3)
else:
    print("opreation not found")