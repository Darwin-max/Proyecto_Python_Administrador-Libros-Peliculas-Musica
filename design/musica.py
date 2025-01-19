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
    musica = openJSON("musica")  # Asegúrate de que "musica.json" exista y tenga el formato adecuado.
    music() # importa para mostrar una tabla donde muestre todas las musica por genero 
    if not musica:
        return
    
    print("¿Qué musica deseas buscar por género?")
    genero = input("Género: ").strip()
    
    # Filtrar todas las películas que coincidan con el género indicado
    musica_encontradas = [
        musica for musica in musica if musica.get("genero", "").lower() == genero.lower()
    ]
    
    if musica_encontradas:
        print(f"Películas del género '{genero}':")
        print(tabulate(musica_encontradas, headers="keys", tablefmt="grid"))
    else:
        print(f"No se encontraron películas del género '{genero}'.")

