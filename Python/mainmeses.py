import mes

meses = []

for i in range(12):
    meses.append(mes.Mes.crearMes())

for i in range(12):
    print(meses[i].nombre + ", temp max: " + str(meses[i].maxtemp) 
                          + ", temp min: " + str(meses[i].mintemp)
                          + ", temp avg: " + str(meses[i].avgtemp))