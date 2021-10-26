import random



class Mes:
    contador = 1
    nombre = ""
    maxtemp = 47
    mintemp = -2
    avgtemp = (maxtemp + mintemp) / 2

    def crearMes():
        mes = Mes()
        mes.nombre = "Mes " + str(Mes.contador)
        Mes.contador += 1
        mes.maxtemp = random.randint(25,47)
        mes.mintemp = random.randint(-2,8)
        mes.avgtemp = (mes.maxtemp + mes.mintemp) / 2
        return mes