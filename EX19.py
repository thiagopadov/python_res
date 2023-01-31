lado1 = float(input("Insira o lado 1 do triângulo"))
lado2 = float(input("Insira o lado 2 do triângulo"))
lado3 = float(input("Insira o lado 3 do triângulo"))



if lado1 == lado2 and lado1 == lado3:
    print("Triangulo equilátero.")

elif lado1 == lado2:
    print("Triangulo isósceles.")

elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("Triangulo escaleno.")

