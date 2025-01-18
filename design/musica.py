from tabulate import tabulate
from logic.musica import musicadd, musicos, music
from formula.PARA_TODO import openJSON




def buiscar_musica():
    musica = openJSON("musica")
    musicadd()
    print("¿Qué cancion deseas buscar?")
    cancion = input("cancion: ")
    for musica in musica:
        if musica["cancion"] == cancion:
            print(tabulate([musica], headers="keys", tablefmt="grid"))
            break
    else:
        print("No se encontró el pelicula")



def buste():
    musica = openJSON("musica")
    musicos()
    print("¿Qué cancion deseas busar?")
    artista = input("Artista: ")
    for musica in musica:
        if musica["cantante"] == artista:
            print(tabulate([musica], headers="keys", tablefmt="grid"))
            break
    else:
        print("No se encontró el pelicula")


def buisr_musicar():
    musica = openJSON("musica")
    music()
    print("¿Que cancion deseas buscar")
    genero = input("genero: ")
    for musica in musica:
        if musica["genero"] == genero:
            print(tabulate([genero],  headers="keys", tablefmt="grid" ))
            break
    else:
        print("No se encontró el pelicula")

