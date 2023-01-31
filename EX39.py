dia = int(input('Insira o dia: '))

if dia > 30:
    dia = 30

if dia < 1:
    dia = 1

mes = int(input('Insira o mês: '))

if mes > 12:
    mes = 12

if mes < 1:
    mes = 1

quant_dias = (mes - 1) * 30 + (dia - 1)

print('*'*45)

print(f'Se passaram {quant_dias} dias desde o inicio do ano. \n')

print('*'*45)