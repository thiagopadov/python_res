num1 = float(input('Digite o primeiro numero. \n'))
num2 = float(input('Digite o segundo numero. \n'))
op   = input('Digite a operação desejada: \n')
if op == '+':
    result = num1 + num2

elif op == '-':
    result = num1 - num2

elif op == '*':
    result = num1 * num2

elif op == '/':
    result = num1 / num2

if num1 % 2 == 0:

    print('O número é par. \n')

else:

    print('O número é impar. \n')
    