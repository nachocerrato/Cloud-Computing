from typing import TextIO
import datetime


def menu():
    selec = int(input("Menú inicial\n------------\n0.- Salir\n1.- Bisiesto\n2.- Narcisista\n3.- Introduce tu fecha de nacimiento\n------------\n"))
    return selec

def bisiesto(numero):
    annobisiesto = 0
    if(numero%4 == 0):
        if(numero%100 != 0 or (numero%100 == 0 and numero%400 == 0)):
            annobisiesto = numero
    return annobisiesto

def narcisista(numero):
    suma = 0
    longitud = len(str(numero))
    parseado = str(numero)
    for i in range(longitud):
        digito = parseado[i]
        digitoint = int(digito)
        suma = suma + (digitoint ** longitud)
    if (suma == int(numero)):
        print("Es un número narcisista. ")
    else:
        print("No es un número narcisista. ")

def getAnnoFecha(textoFecha):
    if(textoFecha.find("/") != -1):
        textoFecha = textoFecha.replace("/","@")
    else:
        textoFecha = textoFecha.replace("-","@")
    ultimarroba = textoFecha.rfind("@")
    anno = textoFecha[ultimarroba + 1:]
    return int(anno)

def fechaNacBisiestos(textoFecha):
    fecha = getAnnoFecha(textoFecha)
    fechahoy = datetime.date.today()
    annoactual = fechahoy.year
    for i in range(fecha, annoactual + 1):
        if(bisiesto(i) != 0):
            print(bisiesto(i))