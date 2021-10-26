ciudades = ["Sevilla","Córdoba","Madrid","Alicante","Santiago"]

contenido = "@".join(ciudades)
print(contenido)

cities = contenido.split(sep="@")

for ciudad in cities:
    print(ciudad)
print("Fin de programa")