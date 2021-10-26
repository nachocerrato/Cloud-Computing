import coche

print("Coche")
selec = -1

while(selec != 0):
    coche.Coche.getEstado(coche.Coche)

    selec = coche.Coche.menuCoche()

    if(selec == 1):
        coche.Coche.arrancar(coche.Coche)
    elif(selec == 2):
        coche.Coche.acelerar(coche.Coche)
    elif(selec == 3):
        coche.Coche.frenar(coche.Coche)
    elif(selec == 4):
        coche.Coche.detener(coche.Coche)
    else:
        print("Coche aparcado")

