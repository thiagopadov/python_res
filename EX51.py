#51- Ler diversos números e exibir qual foi a soma. O valor -999 é o código de fim da entrada.
#WHILE = ENQUANTO

num = 0
soma = 0

#Enquanto o num for diferente de -999, a soma vai adicionando números para no final após o -999 ser inserido, o sistema irá printar a soma total dos números na tela
# o ! (Diferente) serve como função de limitador para o código 
while num != -999:
    soma = soma + num
    num = int(input('Digite o número inteiro: '))
print(soma)