import json
from tabulate import tabulate
from formula.PARA_TODO import openJSON

musica = openJSON("musica") # Cargar los datos de la lista de música
def añadireleMusica():  # Añadir elementos a la lista de música
        print(tabulate(musica, headers="keys", tablefmt="grid"))  # Mostrar la lista de música
        cansion = input("Canción: ")    # Solicitar los datos de la canción
        artista = input("Artista: ")            
        genero = input("Género: ")
        año = input("Año: ")
        dada = {"Canción": cansion, "Artista": artista, "Género": genero, "Año": año}  # Crear un diccionario con los datos de la canción y el resto de elementos
        musica.append(dada)    # Añadir el diccionario a la lista de música  

        
