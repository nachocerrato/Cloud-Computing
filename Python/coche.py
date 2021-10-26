class Coche:
    marca = ""
    modelo = ""
    velocidad = 0
    estado = "detenido"

    def arrancar(self):
        self.velocidad = 1
        self.estado = "en marcha"

    def acelerar(self):
        if(self.estado == "detenido"):
            print("El coche primero debe arrancarse. ")
        else:
            self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1
    
    def detener(self):
        self.velocidad = 0
        self.estado = "detenido"
    
    def getEstado(self):
        if(self.estado == "detenido"):
            print("El coche está " + self.estado)
        else:
            print("El coche está " + self.estado + " y a " + str(self.velocidad) + " km/h.")
    
    def menuCoche():
        return int(input("Menú inicial\n---------------\n0.- Salir\n1.- Arrancar\n2.- Acelerar\n3.- Frenar\n4.- Detener\n---------------\n"))