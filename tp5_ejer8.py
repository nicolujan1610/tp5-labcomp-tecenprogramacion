#Desarrollar un programa que cargue una lista con 5 palabras. La salida del programa debe
#mostrar la palabra más larga y la más corta que fueron ingresadas por el usuario.

lista = []

for i in range(5):
  palabra = input(f"Ingrese la palabra {i+1}: ")
  lista.append(palabra)

palabraMasLarga = lista[0]
palabraMasCorta = lista[0]

for palabra in lista:
  if len(palabraMasLarga)<len(palabra):
    palabraMasLarga = palabra
  if len(palabraMasCorta)>len(palabra):
    palabraMasCorta = palabra

print(lista)
print(f"Palabra más larga: {palabraMasLarga} ({len(palabraMasLarga)})")
print(f"Palabra más corta: {palabraMasCorta} ({len(palabraMasCorta)})")

