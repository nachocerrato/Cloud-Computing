print("Lista de nombres\n---------------\n")

selec = -1
nombres = []
eliminable = False


def start():
    nuevo = ""
    while ((nuevo.upper() != "OK")):
            nuevo = str(input("Nombre: "))
            if((nuevo.upper() != "OK")):
                nombres.append(nuevo)
    menu()

def menu():
    longitud = len(nombres)
    for i in range(longitud):
        print("Pos: "+ str(i)+ " - Nombre: "+ nombres[i])
    print("---------------")    
    selec = int(input("Menú inicial\n---------------\n0.- Salir\n1.- Nuevo nombre\n2.- Eliminar nombre (posición)\n3.- Comenzar de nuevo\n---------------\n"))

    if(selec == 1):
        nuevoNombre()
    elif(selec == 2):
        eliminaNombre()
    elif(selec == 3):
        comienza()
    else:
        exit()

def nuevoNombre():
    nuevo = str(input("Indica el nuevo nombre: "))
    nombres.append(nuevo)
    menu()

def eliminaNombre():
    eliminable = False
    eliminado = str(input("\nIndica el nombre a eliminar: "))
    longitud = len(nombres)
    for i in range(longitud):
        if(nombres[i] == str(eliminado)):
            posicion = i
            eliminable = True
    nombres.pop(posicion)
    if(eliminable == False):
        print("No existe ese nombre en la lista. ")
    menu()

def comienza():
    nombres.clean()
    print("Lista borrada, comience de nuevo a agregar nombres. ")
    start()

start()

