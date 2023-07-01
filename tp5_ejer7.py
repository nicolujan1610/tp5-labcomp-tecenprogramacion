#Escribir un programa que cargue una lista de 20 números enteros aleatorios entre -10 y 10 para
#luego muestre la cantidad de números positivos, negativos y ceros que hay en el arreglo

import random

lista = []

positivos = 0
negativos = 0
ceros = 0

for i in range(20):
    numero = random.randint(-10,10)
    lista.append(numero)
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros +=1

print(lista)
print(f"cantidad de ceros: {ceros}")
print(f"cantidad de negativos: {negativos}")
print(f"cantidad de positivos: {positivos}")
