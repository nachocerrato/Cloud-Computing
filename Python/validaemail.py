print("---Validación de correo electrónico---")

correo = str(input("Por favor, indícanos tu correo electrónico: "))
arroba = 0
punto = 0
cuentarroba = 0
cuentapunto = 0

for i in range(len(correo)):
    if(correo[i] == "@"):
        arroba = i
        cuentarroba =+ 1
    if(correo[i] == "."):
        if(punto == 0):
            punto = i
            cuentapunto =+ 1
        else:
            cuentapunto =+ 1

diferencia = punto - arroba

if(cuentarroba > 0):
    if(cuentapunto > 0):
        if(correo.startswith(".") or correo.endswith(".") or correo.startswith("@") or correo.endswith("@")):
            print("El correo no debe empezar ni acabar con puntos o arrobas. ")
        elif(arroba > punto):
            print("Debe haber un error, has escrito el punto antes que la arroba. ")
        else:
            if(diferencia == 1):
                print("El correo no debería tener escrito un punto tras la arroba. ")
            elif(diferencia >= 2 and diferencia <= 5):
                print("Has escrito correctamente el correo electrónico. ")
            else:
                print("El dominio debe tener entre 2 y 4 caracteres. ")
    else:
        print("El correo debe tener al menos un punto. ")
else:
    print("El correo debe tener al menos una arroba. ")

