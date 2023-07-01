# Realizar un programa que pida al usuario que ingrese una palabra y muestre cuantas vocales y
# consonantes tiene.
palabra = input("Inserte una palabra: ")
vocales = 0
consonantes = 0

for letra in palabra:
    if letra in "AEIOUaeiou":
      vocales += 1
    else:
      consonantes += 1
  
print(f"Vocales: {vocales}  ")
print(f"Consonantes: {consonantes}")