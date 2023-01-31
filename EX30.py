limite_peso = 50 
multa_kg = 4.0 

peso = float(input("Informe o peso em KG de peixes pescados: \n"))

if peso > limite_peso:
    excesso = peso - limite_peso
    multa = excesso * multa_kg
    
    print("Valor da multa a ser paga: R$ \n", multa)

else:
    print("Não há multa a ser paga. \n")