horas = int(input("Introduce el número de horas: "))
precio = int(input("Ahora el precio de la hora: "))
km = int(input("Y por último, los km: "))
salario = horas * precio

i = horas
if(i > 36):
    salario += 2
    i - 1

if(km < 100):
    print("Dieta local")
elif (100 < km < 500):
    print("Dieta nacional")
else:
    print("Dieta internacional")

print("Salario bruto: ",salario)

if(salario < 250):
    print("Salario final, sin retención: ", salario)
elif(250 < salario < 800):
    salario = salario * .8
    print("Salario final con retención del 20%: ", salario)
else:
    salario = salario * .6
    print("Salario final con retención del 40%: ", salario)