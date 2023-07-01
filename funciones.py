def verificarNumero(strNum):
  isNegative = False
  if strNum.startswith('-'):
    strNum = strNum[1:]
    isNegative = True
    
  if strNum.isdigit():
    numFinal = int(strNum)
    if isNegative:
      return numFinal*(-1)
    else:
      return numFinal
  else:
    if "." in strNum:
      numPartido = strNum.split(".")
      if numPartido[0].isdigit() and numPartido[1].isdigit():
        numPartido = f"{numPartido[0]}.{numPartido[1]}"
        numFinal = float(numPartido)
        if isNegative:
          return numFinal*(-1)
        else:
          return numFinal
    else:
      return False

def pedirNumeroYVerificar(text):
  num1 = input(text)
  numVerificado = verificarNumero(num1)

  while not numVerificado:
    num1 = input(text)
    numVerificado = verificarNumero(num1)
    
  return numVerificado