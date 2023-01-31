soma = 0
mult = 1

for s in range(0,5):
    num = float(input('Digite o número'))
    soma = soma + num
    
    print('*'*50)
    print(f'A soma dos números digitados foram de {soma}. \n')
    print(f'A média dos números digitados foram de {soma/5}. \n')
    print('*'*50)