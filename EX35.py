preco_kg = 0

tipo_carne = input('Qual carne deseja? ')
quantidade = float(input('Quantos quilos de carne precisa? '))
resposta = int(input('O pagamento será realizado com cartão Tabajara? 1-SIM / 2-NÃO. \n'))


preco_file = 34.90
preco_alcatra = 44.90
preco_picanha = 66.90


preco_acima_file = 35.80
preco_acima_alcatra = 46.80
preco_acima_picanha = 67.80


desconto_tabajara = 0.95

if tipo_carne == 'File Duplo':
    if quantidade <= 5:
        preco_kg = preco_file
    else:
        preco_kg = preco_acima_file
elif tipo_carne == 'Alcatra':
    if quantidade <= 5:
        preco_kg = preco_alcatra
    else:
        preco_kg = preco_acima_alcatra
elif tipo_carne == 'Picanha':
    if quantidade <= 5:
        preco_kg = preco_picanha
    else:
        preco_kg = preco_acima_picanha

valor_total = quantidade * preco_kg
desconto = 0
if resposta == 1:
    desconto = valor_total * desconto_tabajara
valor_pagar = valor_total - desconto

print("Tipo de carne:", tipo_carne)
print("Quantidade de carne: Kg", quantidade)
print("Preço total: R$ ", valor_total)
print("Tipo de pagamento:", resposta)
print("Desconto: R$ ", desconto)
print("Valor a pagar: R$ ", valor_pagar)