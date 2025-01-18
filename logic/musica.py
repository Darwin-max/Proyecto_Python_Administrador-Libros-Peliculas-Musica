import json
from tabulate import tabulate
from formula.PARA_TODO import openJSON

musica = openJSON("musica") # Cargar los datos de la lista de música
def añadireleMusica():  # Añadir elementos a la lista de música
        print(tabulate(musica, headers="keys", tablefmt="grid"))  # Mostrar la lista de música
        cansion = input("canción: ")    # Solicitar los datos de la canción
        artista = input("cantante: ")            
        genero = input("genero: ")
        año =  input("disco: ")
        musiced= {"Canción": cansion, "Artista": artista, "Género": genero, "Año": año}  # Crear un diccionario con los datos de la canción y el resto de elementos
        musica.append(musiced)  # Añadir los datos a la lista de música




# este es el segundo punto del proyecto que es buscar una cancion en la lista de musica 
# acordarse de que todavia me falta tabular bien las tablas de musica

def ver_musica():  # Buscar una canción en la lista de música
        print(tabulate(musica, headers="keys", tablefmt="grid"))  # Mostrar la lista de música
        




def musicadd():
        musica = openJSON("musica")
        Nahomi = []
        for dicccionario in musica:
                dicccionario.pop("genero")
                dicccionario.pop("cantante")
                dicccionario.pop("disco")
                
                
                Nahomi.append(dicccionario)
        print(tabulate(Nahomi, headers="keys", tablefmt="grid"))
                


def musicos():
        musicass = openJSON ("musica")
        francy = []
        for dicccionario in musicass:
                dicccionario.pop("genero")
                dicccionario.pop("cancion")
                dicccionario.pop("disco")
                francy.append(dicccionario)
        print(tabulate(francy, headers="keys", tablefmt="grid"))
                
                
def music():
        musicas = openJSON("musica")
        kenji = []
        for dicccionario in musicas:
                dicccionario.pop("cantante")
                dicccionario.pop("cancion")
                dicccionario.pop("disco")
                kenji.append(dicccionario)
        print(tabulate(kenji, headers="keys", tablefmt="grid"))

