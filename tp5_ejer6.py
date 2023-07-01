#  Realizar un programa que cargue una lista con 5 números. A continuación mostrar la suma, el
# promedio, el mayor y el menor de todos.

lista = []
suma = 0

for i in range(5):
    numero = int(input("Ingrese un número entero: "))
    while not numero.isdigit():
      numero = int(input("Ingrese un número ENTERO: "))
    lista.append(numero)
    suma += numero
    if i == 0:
       mayor = numero
       menor = numero
    else:
        if numero>mayor:
          mayor = numero
        if numero<menor:
          menor = numero

promedio = suma / len(lista)

print(lista)
print(f"Suma de todos los numeros: {suma}")
print(f"Promedio de todos los numeros: {promedio}")
print(f"Numero más grande: {mayor}")
print(f"Numero más chico: {menor}")

