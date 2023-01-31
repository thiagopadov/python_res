produto = float(input("Digite o valor do produto. \n"))
if(produto>50):
    aumento = (0.30 * produto) + produto

else:
    aumento = (0.45 * produto) + produto

print("Valor do produto {}\n Valor com aumento do produto {}".format(produto, aumento))