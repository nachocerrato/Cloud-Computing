import os

global ciudades
ciudades  = []

def mostrarCiudades():
    for c in ciudades:
        print(c)
    
#cargar ciudades desde fichero
def leerFile():
    if(os.path.isfile("ciudades.txt")):
        fichero = open("ciudades.txt","r")
        contenido = fichero.read()
        fichero.close()

        global ciudades
        ciudades = contenido.split(sep="$")
        print("Datos cargados correctamente")
    else:
        fichero = open("ciudades.txt","w+")
        contenido = fichero.read()
        fichero.close()

        ciudades = contenido.split(sep="$")
        print("Datos cargados correctamente")

#guardar ciudades en fichero
def guardarFile():
    respuesta = "$".join(ciudades)
    fichero = open("ciudades.txt","w+")
    fichero.write(respuesta)
    fichero.flush()
    fichero.close()
    print("Datos almacenados")

#insertar ciudades en lista
def insertaCiudad():
    ciudad = str(input("Introduzca una ciudad: "))
    ciudades.append(ciudad)

def mostrarMenu():
    selec = int(input("Menú inicial\n---------------\n0.- Salir\n1.- Leer ciudades\n2.- Guardar ciudades\n3.- Nueva ciudad\n4.- Mostrar ciudades\n---------------\n"))
    return selec
selec = -1

print("Ejemplo con Files y listas\n---------------\n")

while(selec != 0):
    selec = mostrarMenu()
    if(selec == 1):
        leerFile()
    elif(selec == 2):
        guardarFile()
    elif(selec == 3):
        insertaCiudad()
    elif(selec == 4):
        mostrarCiudades()
    elif(selec == 0):
        print("Hasta luego")
    else:
        print("Opción incorrecta")
print("Fin de programa")