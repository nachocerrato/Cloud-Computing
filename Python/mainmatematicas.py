import metodosexternosmates

select = -1


while (select != 0):

    num1 = int(input("Introduzca un número: "))
    num2 = int(input("Introduzca otro número: "))

    select = metodosexternosmates.menu()    
    if(select == 1):
        print(metodosexternosmates.sumaNumeros(num1,num2))
    elif(select == 2):
        print(metodosexternosmates.restaNumeros(num1,num2))
    elif(select == 3):
        print(metodosexternosmates.divideNumeros(num1,num2))
    elif(select == 4):
        print(metodosexternosmates.multiNumeros(num1,num2))
    else:
        print("Fin del programa. ")