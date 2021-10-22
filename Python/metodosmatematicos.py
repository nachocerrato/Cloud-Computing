

def sumaNumeros(num1, num2):
    num3 = num1 + num2
    return num3

def restaNumeros(num1, num2):
    num3 = num1 - num2
    return num3

def divideNumeros(num1, num2):
    num3 = num1 / num2
    return num3

def multiNumeros(num1, num2):
    num3 = num1 * num2
    return num3

def menu():
    select = int(input("Seleccione una opción. \n------------------------\n0.- Salir\n1.- Sumar\n2.- Restar\n3.- Dividir\n4.- Multiplicar\n------------------------\n"))
    return select




select = -1


while (select != 0):

    num1 = int(input("Introduzca un número: "))
    num2 = int(input("Introduzca otro número: "))

    select = menu()    
    if(select == 1):
        print(sumaNumeros(num1,num2))
    elif(select == 2):
        print(restaNumeros(num1,num2))
    elif(select == 3):
        print(divideNumeros(num1,num2))
    elif(select == 4):
        print(multiNumeros(num1,num2))
    else:
        print("Fin del programa. ")