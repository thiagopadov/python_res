salario = float(input("Digite o salário do colaborador: "))

if salario <= 280:
    salario_atual = salario+(salario*0.2)
    print(f"O aumento do salário foi de 20%, seu salário é de {salario_atual}")

elif salario > 280 and salario <= 700:
    salario_atual = salario+(salario*0.15)
    print(f"O aumento do salário foi de 15%, seu novo salário é de {salario_atual}")

elif salario > 700 and salario <= 1500:
    salario_atual = salario+(salario*0.20)
    print(f"O aumento do salário foi de 20%, seu novo salário é de {salario_atual}")

elif salario > 1500:
    salario_atual = salario+(salario*0.05)
    print(f"O aumento do salário foi de 5%, seu novo salário é de {salario_atual}")

