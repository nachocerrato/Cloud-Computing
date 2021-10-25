print("Ejemplo ficheros")

fichero = open("nombre.txt","w+")
print("Introduzca su nombre: ")
nombre = input()

fichero.write("Su nombre es..." + nombre)
fichero.close()


archivo = open("nombre.txt","a")
print("Introduzca otro nombre")
nombre = input()
archivo.write("\n" + nombre)
archivo.close()
print("Fin de programa")