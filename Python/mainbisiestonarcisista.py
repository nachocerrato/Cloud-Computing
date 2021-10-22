
from metodosbisiestonarcisista import menu, bisiesto, narcisista, fechaNacBisiestos

selec = menu()

if(selec == 1):
    numero = int(input("Introduzca un número: "))
    bisiesto(numero)
elif(selec == 2):
    numero = int(input("Introduzca un número: "))
    narcisista(numero)
elif(selec == 3):
    fechaTexto = str(input("Introduzca su fecha de nacimiento (00/00/0000 o 00-00-0000): "))
    fechaNacBisiestos(fechaTexto)