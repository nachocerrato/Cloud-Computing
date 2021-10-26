import persona 

print("Ejemplo clases Persona")
person = persona.Persona()

person.nombre = "Alumno"
person.apellido = "Azure"
person.fechaNac = 1984

print(person.getNombreCompleto())
print("Edad: " + str(person.getEdad()))
print("País por defecto: " + person.pais)