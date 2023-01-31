nome = input("Digite seu nome: \n")
idade = int(input("Digite sua idade: \n"))

if idade <= 2:
    print("{} Está com {} e pela idade é considerado um bebê. \n".format(nome, idade))

if idade >= 3 and idade <= 11:
    print("{} Está com {} e pela idade é considerado uma criança. \n".format(nome, idade))

if idade >= 12 and idade <= 21:
    print("{} Está com {} e pela idade é considerado um jovem. \n".format(nome, idade))

if idade >= 22 and idade <= 64:
    print("{} Está com {} e pela idade é considerado um adulto. \n".format(nome, idade))

if idade >= 65 and idade <= 100:
    print("{} Está com {} e pela idade é considerado um idoso. \n" .format(nome, idade))

if idade >= 101:
    print("{} Está com {} e pela idade é considerado muito velhinho. \n".format(nome, idade))



