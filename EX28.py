# faça um programa que peça 2 números inteiros e um número real. Calcule e mostre: 
# O produto do dobro do primeiro com metade do segundo.
# A soma do triplo do primeiro com o terceiro.​
# O terceiro elevado ao cubo.​

n1 = int(input("Número inteiro: \n"))
n2 = int(input("Outro número inteiro: \n"))
n3 = float(input('Número real: \n'))

soma1 = (2*n1) + (n2/2)
soma2 = (3*n1) + (n3)
soma3 = (n3**3)

print(soma1,soma2,soma3)