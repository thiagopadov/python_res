num = int(input("Insira um número inteiro: "))
fat = 1
for i in range (num):
    fat = fat*(num-i)

print(fat) 