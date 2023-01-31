nome = input("nome do aluno: \n")
disciplina = input("nome da disciplina\n")
nota1 = float(input("primeira nota: \n "))
nota2 = float(input("segunda nota: \n"))
nota3 = float(input("terceira nota: \n"))

media = (nota1+nota2+nota3)/3
if(media>=6):
    print(f"As notas foram: {nota1}, {nota2} e {nota3} Media do aluno {nome} foi {media:.1f}, foi o suficiente para passar.")

else:
    print(f"As notas foram: {nota1}, {nota2} e {nota3} Media do aluno {nome} foi {media:.1f}, NÃO foi o suficiente para a aprovação.")
