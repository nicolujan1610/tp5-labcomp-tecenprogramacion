from funciones import pedirNumeroYVerificar

print("A continuación ingrese 3 números y mostrare el mayor")

num1 = pedirNumeroYVerificar("Ingrese primer número: ")
num2 = pedirNumeroYVerificar("Ingrese segundo número: ")
num3 = pedirNumeroYVerificar("Ingrese tercer número: ")

mayor = num1

if num2 > mayor:
  mayor = num2
if num3 > mayor:
  mayor = num3

print(f"El número más grande es: {mayor}")