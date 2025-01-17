import json
from tabulate import tabulate
from formula.PARA_TODO import openJSON

musica = openJSON("musica") # Cargar los datos de la lista de música
def añadireleMusica():  # Añadir elementos a la lista de música
        print(tabulate(musica, headers="keys", tablefmt="grid"))  # Mostrar la lista de música
        cansion = input("Canción: ")    # Solicitar los datos de la canción
        artista = input("Artista: ")            
        genero = input("Género: ")
        año = int( input("Año: "))
        musiced= {"Canción": cansion, "Artista": artista, "Género": genero, "Año": año}  # Crear un diccionario con los datos de la canción y el resto de elementos
        musica.append(musiced)  # Añadir los datos a la lista de música




# este es el segundo punto del proyecto que es buscar una cancion en la lista de musica 
# acordarse de que todavia me falta tabular bien las tablas de musica

def ver_musica():  # Buscar una canción en la lista de música
        print(tabulate(musica, headers="keys", tablefmt="grid"))  # Mostrar la lista de música
        