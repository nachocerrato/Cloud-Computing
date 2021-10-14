num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))


if(num1 > num2):
    print("El segundo número debe ser mayor.")
else:
    while num1 < num2:
        if(num1%2 != 0):
            print(num1)
        num1 += 1