import json
import tempfile
from tabulate import tabulate
from formula.PARA_TODO import openJSON




def añadireleMusica():
        musica = openJSON("musica") # Cargar los datos de la lista de música
        input("\nPresione Enter para continuar...")
        """
        Añade una nueva canción a la lista de música y retorna la canción añadida.
        """
        # Mostrar la lista actual de música
        print("\nLista actual de música:")
        if musica:
                print(tabulate(musica, headers="keys", tablefmt="grid"))
        else:
                print("La lista está vacía.")

        # Solicitar los datos de la nueva canción
        cancion = input("Canción: ").strip()
        artista = input("Artista: ").strip()
        genero = input("Género: ").strip()
        año = input("Año: ").strip()

        # Crear un diccionario con los datos de la canción
        nueva_cancion = {
        "Canción": cancion,
        "Artista": artista,
        "Género": genero,
        "Año": año
        }

        # Añadir la nueva canción a la lista de música
        musica.append(nueva_cancion)
        return nueva_cancion  # Retornar la canción añadida

# Llamar a la función para añadir una canción
cancionNueva = añadireleMusica()

# Mostrar la nueva canción añadida en formato tabular
print("\nNueva canción añadida:")
print(tabulate([cancionNueva], headers="keys", tablefmt="grid"))

# Guardar los datos de la nueva canción en un archivo JSON temporal
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as archivo_temp:
        json.dump(cancionNueva, archivo_temp, indent=4)
        print(f"\nArchivo JSON temporal creado en: {archivo_temp.name}")

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

