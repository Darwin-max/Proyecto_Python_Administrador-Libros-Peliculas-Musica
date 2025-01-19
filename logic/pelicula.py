import json
import tempfile
from tabulate import tabulate
from formula.PARA_TODO import *





def añadirElpeli():
        peliculas = openJSON("peliculas") # Cargar los datos de la lista de películas
        input("Presione Enter para continuar...")

        # Añade una nueva película a la lista de películas y retorna la película añadida.
        # Mostrar la lista actual de películas
        print("Lista actual de películas:")
        if peliculas:
                print(tabulate(peliculas, headers="keys", tablefmt="grid"))
        else:
                print("La lista está vacía.")

        # Solicitar los datos de la nueva película
        titulo = input("Título: ").strip()
        director = input("Director: ").strip()
        genero = input("Género: ").strip()
        año = input("Año de publicación: ").strip() # Año de la película
        descripcion = input("Descripción: ").strip()

        # Crear un diccionario con los datos de la película
        nueva_pelicula = {
                "titulo": titulo,
                "director": director,
                "genero": genero,
                "anio_publicacion": año,
                "descripcion": descripcion
        }

        # Añadir la nueva película a la lista de películas
        peliculas.append(nueva_pelicula)
        return nueva_pelicula  # Retornar la película añadida

        # Llamar a la función para añadir una película
peliculaNueva = añadirElpeli()

        # Mostrar la nueva película añadida en formato tabular
print("\nNueva película añadida:")
print(tabulate([peliculaNueva], headers="keys", tablefmt="grid"))

        # Guardar los datos de la nueva película en un archivo JSON temporal
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as archivo_temp:
        json.dump(peliculaNueva, archivo_temp, indent=4)
        print(f"\nArchivo JSON temporal creado en: {archivo_temp.name}")


def ver_peliculas(): # Buscar una película en la lista de películas

        print(tabulate(peliculas, headers="keys", tablefmt="grid") ) # Mostrar la lista de películas





def peliculas_():
        peliculas = openJSON("pelicula")
        sarey = []
        for dicccionario in peliculas:
                dicccionario.pop("genero")
                dicccionario.pop("año")
                dicccionario.pop("director")
                dicccionario.pop("valoracion")
                dicccionario.pop("descripcion")
                sarey.append(dicccionario)
        print(tabulate(sarey, headers="keys", tablefmt="grid"))
                


def pelicas_():
        pelicula = openJSON("peliculas")
        amor =  []
        for dicccionario in pelicula:
                dicccionario.pop("genero")
                dicccionario.pop("año")
                dicccionario.pop("titulo")
                dicccionario.pop("valoracion")
                dicccionario.pop("descripcion")
                amor.append(dicccionario)
        print(tabulate(    amor, headers="keys", tablefmt="grid"))
                
def masTarde (): # para mostrar las peliculas por genero
        
        pelicula = openJSON("peliculas")
        cansado = []
        for dicccionario in pelicula:
                dicccionario.pop("director")
                dicccionario.pop("año")
                dicccionario.pop("titulo")
                dicccionario.pop("valoracion")
                dicccionario.pop("descripcion")
                cansado.append(dicccionario)
        print(tabulate(    cansado, headers="keys", tablefmt="grid"))
                