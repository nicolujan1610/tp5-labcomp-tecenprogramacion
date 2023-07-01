from funciones import pedirNumeroYVerificar

def sumar(a,b):
  return a+b

numero1 = pedirNumeroYVerificar("Ingresar primer numero: ")
numero2 = pedirNumeroYVerificar("Ingresar segundo numero: ")

res = sumar(numero1, numero2)
print(f"{numero1} + {numero2} = {res}")
