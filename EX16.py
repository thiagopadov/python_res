#Faça um programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Primeiro número. "))
num2 = int(input("Segundo número. "))
num3 = int(input("Terceiro número. "))

if num1 < num2 and num1 < num3:
    print(f"{num1} é menor do que {num2} e {num3}")

elif num1 > num2 and num1 > num3:
    print(f"{num1} é maior do que {num2} e {num3}")
