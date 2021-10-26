class Persona:
    nombre = ""
    apellido = ""
    fechaNac = 0
    pais = ""
    def __str__(self):
        return self.nombre + " " + self.apellido
        + ", País: " + self.pais + ", Edad: " + str(self.getEdad)

    def __init__(self):
        self.pais = "Francia"

    def getNombreCompleto(self):
        return self.nombre + " " + self.apellido
    
    def getEdad(self):
        return 2021 - self.fechaNac

    def getDescripcion(self, midescripcion):
        return self.getNombreCompleto() + ", " + midescripcion
