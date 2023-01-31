quant_hora = int(input("Informe a quantidade de horas trabalhadas: \n"))
valor_hora = float(input("Informe o valor da hora: \n"))

salario_bruto = quant_hora * valor_hora
porcentagem = ""

if salario_bruto <= 900:
    salario_bruto = salario_bruto
    porcentagem = "0%"

elif salario_bruto > 900 and salario_bruto <= 1500:
    salario_bruto = salario_bruto - (salario_bruto*0.05)
    porcentagem = "5%"

elif salario_bruto > 1500 and salario_bruto <= 2500:
    salario_bruto = salario_bruto - (salario_bruto*0.10)
    porcentagem = "10%"

elif (salario_bruto > 2500):
    salario_bruto = salario_bruto - (salario_bruto*0.20)
    porcentagem = "20%"

print(f"O salário final é de {salario_bruto}: \n")
print(f"A porcentagem é de {porcentagem}: ")



