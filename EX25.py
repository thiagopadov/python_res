p = 10.0
m = 12.0
g = 15.0
ped_p = int(input("Digite a quantidade de camisetas P: "))
ped_m = int(input("Digite a quantidade de camisetas M: "))
ped_g = int(input("Digite a quantidade de camisetas G: "))

ped_total = (ped_p * p) + (ped_m * m) + (ped_g * g)

print(f"A quantidade de camisetas P solicitadas foram de: {ped_p} \n ")
print(f"A quantidade de camisetas M solicitadas foram de: {ped_m} \n ")
print(f"A quantidade de camisetas G solicitadas foram de: {ped_g} \n ")

print(f"O valor total de pedidos solicitados é de R${ped_total:.2f} ")
