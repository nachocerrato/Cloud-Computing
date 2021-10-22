num1 = int(input("Por favor, introduce un número: "))
num2 = int(input("Por favor, introduce un segundo número: "))
num3 = int(input("Por favor, introduce un tercer número (el último): "))
suma = num1 + num2 + num3

if(num1 > num2 and num1 > num3):
    print("El mayor es: ", num1)
    if(num2 > num3):
        print("El menor es: ", num3," y el intermedio: ",num2)
    else:
        print("El menor es: ", num2," y el intermedio: ",num3)
elif(num2 > num1 and num2 > num3):
    print("El mayor es: ", num2)
    if(num1 > num3):
        print("El menor es: ", num3," y el intermedio: ",num1)
    else:
        print("El menor es: ", num1," y el intermedio: ",num3)
else:
    print("El mayor es: ", num3)
    if(num1 > num2):
        print("El menor es: ", num2," y el intermedio: ",num1)
    else:
        print("El menor es: ",num1," y el intermedio: ",num2)    
print("La suma de los 3 es: ", suma)