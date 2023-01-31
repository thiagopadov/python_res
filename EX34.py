preco_litro = 0

litros_vendidos = float(input('Digite a quantidade de litros vendidos: '))
tipo_combustivel = input('Digite o tipo de combustível (A-álcool, G-gasolina): ')

valor_alcool = 1.90
valor_gasolina = 2.50

desc_alcool = 0.03
desc_alcool = 0.05
desc_gasolina = 0.04
desc_gasolina = 0.06

if tipo_combustivel == 'A':
    preco_litro = valor_alcool
    if litros_vendidos <= 20:
        desconto = desc_alcool
    else:
        desconto = desc_alcool

elif tipo_combustivel == 'G':
    preco_litro = valor_gasolina
    if litros_vendidos <= 20:
        desconto = desc_gasolina

    else:
        desconto = desc_gasolina

valor_pagar = litros_vendidos * preco_litro * (1 - desconto)

print('*'*50)
print(f'Valor a pagar: R$ {valor_pagar}')
print('*'*50)