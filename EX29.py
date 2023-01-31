#Para homens: (72.7*h) - 58​
#Para mulheres: (62.1*h) - 44.7​

altura = float(input('Digite a altura: \n'))
sexo = input('Digite Homem ou Mulher: \n')

sexo = sexo.lower()

if sexo == 'homem':
    calc = (72.7*altura) - 58
if sexo == 'mulher':
    calc = (62.1*altura) - 44.7

print(f'O seu peso ideal é {calc} e seu sexo é: {sexo}.')   



