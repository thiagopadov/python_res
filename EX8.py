valor_gasolina = float(input("Digite o valor da gasolina: \n"))
valor_km = float(input("Digite a distância que será percorrida: \n"))
consumo = float(input("Digite o consumo do veiculo: \n"))
litros_gasolina = valor_km/consumo
valor_viagem = litros_gasolina*valor_gasolina

print("O valor gasto da viagem é: \n", valor_viagem)
