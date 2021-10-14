menu = int(input("Menú \n 0.- Salir \n 1.- Conjetura Collatz \n 2.- Tabla multiplicar \n 3.- Números Pares \n Introduzca una opción \n"))

if(menu == 1):
    numero = int(input("Escribe un número positivo: "))

    while numero != 1:
        print(numero)
        if(numero%2 == 0):
            numero = numero / 2
        else:
            numero = (numero * 3) + 1
    print(numero)
elif(menu == 2):
    numero = int(input("Dime un número hostias: "))

    i = 1

    for i in range(1,11):
        print(numero, " * ", i, " = ", numero * i)
elif(menu == 3):
    num1 = int(input("Introduzca un número: "))
    num2 = int(input("Introduzca otro número: "))


    if(num1 > num2):
        print("El segundo número debe ser mayor.")
    else:
        while num1 < num2:
            if(num1%2 == 0):
                print(num1)
            num1 += 1   