
respuesta = ""

while(respuesta != "n"):
    numero = int(input("Introduce un número: "))
    if(numero > 0):
        print("El número es positivo.")
    elif(numero == 0):
        print("El número es 0.")
    else:
        print("El número es negativo.")
    
    respuesta = str(input("¿Quieres continuar? (s/n) "))