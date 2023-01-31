#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.​
num = int(input('Digite um número inteiro: '))
soma = 0
maior = num
menor = num
#Enquanto o número for menor que -999 continua no looping
while num != -999:
    soma = soma + num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    num = int(input('Digite um número inteiro: '))
print('A soma total é: ',soma)
print('O número maior é: ',maior)
print('O número menor é: ',menor)