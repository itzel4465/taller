peliculas = {"anabel" : "rapido y furioso",
            "karli" : "la noche del demonio",
            "joaquin" : "cars"
            }

print (peliculas["anabel"])

for nombre, peli in peliculas:
    print("Nombre alumno %s" % nombre)
    print("Nombre pelicula %s" % peli)

num = 24 * 10
nombre = "chucho"
utiles = ["mochila", "libreta", "lapiz"]
frutas = ["manzana", "pera", "uva"]
dia_clases  = {"nombre":nombre, "utiles":utiles,
                "frutas":frutas, "num":num}
print(dia_clases["frutas"])