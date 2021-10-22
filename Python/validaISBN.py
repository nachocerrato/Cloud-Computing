numero = input("Introduzca el ISBN: ")
longitud = len(numero)
algo = 0

if(len(numero) != 9):
    if(numero.isdigit()):
        for i in range(longitud):
            letra = int(numero[i])
            posicion = i + 1
            nuevo = posicion * letra
            algo = algo + nuevo
        
        if(algo % 11 == 0):
            print("El ISBN es correcto. ")
        else:
            print("El ISBN es incorrecto. ")
    else:
        print("El ISBN debe ser numérico. ")
else:
    print("El ISBN debe tener 10 cifras. ")


#Ahora el corregido  8441513929

