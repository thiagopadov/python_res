conta = int(input("Insira o número da conta: \n"))
saldo = 0
credito = float(input("O valor creditado foi de R$ "))
debito = float(input("O valor retirado foi de R$ "))

saldo_atual= saldo+(credito-debito)
print("O saldo atual é de R$", saldo_atual)
if saldo_atual >=0:
    print("Saldo positivo.")

else:
    print("Saldo negativo.")
