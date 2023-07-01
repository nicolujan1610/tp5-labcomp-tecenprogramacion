# Escribir una función que indique si una palabra es un palíndromo (si se lee igual en un sentido u
# otro)

def esPalindromo(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False
