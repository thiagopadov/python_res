aluno = 0
sexo = 0
st_fisico = 0
total_m = 0
masc = 0
bom = 0
cont = 0

while aluno < 3:
    aluno = aluno+1
    matricula = float(input("Digite o número da matricula. \n"))
    sexo = input("Digite o sexo. \n").upper()
    if sexo == "F":
        altura = float(input("Digite a altura. \n"))
        if altura >= 170:
            cont += 1
    if sexo == "M":
        masc = masc+ 1
        st_fisico = int(input("Qual seu status físico? 1-RUIM/2-REGULAR/3-BOM? \n"))
        if st_fisico == 3:
            bom += 1

if masc > 0:
    total_m = (100 * bom) / masc

print(f"-----------------------------------------------------------------------------------------")
print(f"A quantidade de alunos do sexo feminino com altura superior a 170 cm é de {cont} \n ")
print(f"A % de alunos do sexo masculino cujo status é BOM é de {total_m}. \n")
print(f"-----------------------------------------------------------------------------------------")