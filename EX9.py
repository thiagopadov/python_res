nome_aluno = str(input("Digite o nome do aluno: \n"))
disciplina = input("Digite a disciplina: \n")
prova_1 = float(input("Digite a nota da prova 1: \n"))
prova_2 = float(input("Digite a nota da prova 2: \n"))
prova_3 = float(input("Digite o nota da prova 3: \n"))

media = (prova_1+prova_2+prova_3)/3

if media >= 6:
    print(f"O aluno está aprovado com média: {media}")
else:
    print(f"O aluno está reprovado com média: {media}")
