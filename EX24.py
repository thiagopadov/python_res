#Duas fatias de queijo = 50g cada/ presunto 50g/ hamburguer 100g
quantidade_s = int(input("Digite a quantidade que desejas: \n"))

queijo = 50 * 2
hamburguer = 100
presunto = 50

kg_queijo = queijo / 1000 * quantidade_s
kg_hamburguer = hamburguer / 1000 * quantidade_s
kg_presunto = presunto / 1000 * quantidade_s

total_kg = kg_queijo + kg_hamburguer + kg_presunto

print(f"A quantidade de queijo sairá em: {kg_queijo:.2f}Kg \n")
print(f"A quantidade hamburguer sairá em {kg_hamburguer:.2f}Kg \n")
print(f"A quantidade do presunto sairá em {kg_presunto:.2f}Kg \n")
print(f"O total sairá em: {total_kg:.2f}Kg \n")

