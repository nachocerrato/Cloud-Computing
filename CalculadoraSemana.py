dia = int(input("Introduce el día que naciste: "))
mes = int(input("Ahora el número de mes: "))
ano = int(input("Y por último, el año: "))

semana = {0: "Sábado", 1: "Domingo", 2: "Lunes", 3: "Martes", 4: "Miércoles", 5: "Jueves", 6: "Viernes"}


uno = round(((mes + 1) * 3) / 5)
dos = round(ano / 4)
tres = round(ano / 100)
cuatro = round(ano / 400)
cinco = round(dia + (mes * 2) + ano + uno + dos - tres + cuatro + 2)
seis = round(cinco / 7)
siete = round(cinco - (seis * 7))

print(semana[siete])