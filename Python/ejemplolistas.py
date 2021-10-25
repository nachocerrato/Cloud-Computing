nombres = ['Fati','Nacho','Ana','Otto','Diego','Sandra']


def mostrarNombres():
    longitud = len(nombres)
    for i in range(longitud):
        name = nombres[i]
        print("Posicion: " + str(i) + " - Nombre: " + nombres[i])

print("Ejemplo de listas")

nombres.append("El nuevo")
nombres.insert(3,"El del medio")

mostrarNombres()