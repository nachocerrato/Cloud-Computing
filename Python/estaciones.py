numero = int(input("Introduce un número del 1 al 4: "))

if(numero < 1 or numero > 4):
    print("Error.")
else:
    if(numero == 1):
        print("Verano")
    elif(numero == 2):
        print("Otoño")
    elif(numero == 3):
        print("Invierno")
    else:
        print("Primavera")