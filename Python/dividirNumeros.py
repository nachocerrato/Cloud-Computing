def dividirNumeros():
    try:
        numero1 = int(input("Introduzca un número: "))
        numero2 = int(input("Introduzca otro número: "))
    except:
        print("Error general en algún lugar. ")
    finally:
        print("Siempre me ejecuto. ")
        