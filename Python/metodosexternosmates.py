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
