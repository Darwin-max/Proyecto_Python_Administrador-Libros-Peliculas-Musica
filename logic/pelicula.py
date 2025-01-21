
from tabulate import tabulate
from formula.PARA_TODO import *

def validar_numero(mensaje):
        while True:
                try:
                        valor = int(input(mensaje))
                        return valor
                except ValueError:
                        print("Por favor, ingrese un número válido.")


def añadirElpeli(ll):
        while True:
                opc = input("ingrese s para añadir un nuevo libro y 0 para terminar: ")
                if opc == '0' :
                        break 
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
                nuevo_id = max([peliculas.get("id", 0) for peliculas in peliculas], default=0) + 1 # Generar un ID único para el nuevo libro                nuevo_libro["id"] = nuevo_id    # Añadir el ID al nuevo libro
                id = nuevo_id
                titulo = input("Título: ").strip()
                director = input("Director: ").strip()
                genero = input("Género: ").strip()
                año = input("Año de publicación: ").strip() # Año de la película
                descripcion = input("Descripción: ").strip()
                valoracion = int(input("Valoracion: "))

                while valoracion < 1 or valoracion > 10:
                        print("Valoración no válida. Debe estar entre 1 y 10.")
                        valoracion = int(input("Valoracion: "))
                # Crear un diccionario con los datos de la película
                nueva_pelicula = {
                        "id": id,
                        "titulo": titulo,
                        "director": director,
                        "genero": genero,
                        "anio_publicacion": año,
                        "descripcion": descripcion,
                        "valoracion": valoracion
                }
                ll.append(nueva_pelicula)
                return nueva_pelicula
                # Retornar el libro añadido
                


def ver_peliculas(): # Buscar una película en la lista de películas
        peliculas =  openJSON("peliculas")
        print(tabulate(peliculas, headers="keys", tablefmt="grid") ) # Mostrar la lista de películas





def peliculas_():
        peliculas = openJSON("pelicula")
        sarey = []
        for dicccionario in peliculas:
                dicccionario.pop("categoria")
                dicccionario.pop("id")
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
                dicccionario.pop("categoria")
                dicccionario.pop("id")
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
                dicccionario.pop("categoria")
                dicccionario.pop("id")
                dicccionario.pop("director")
                dicccionario.pop("año")
                dicccionario.pop("titulo")
                dicccionario.pop("valoracion")
                dicccionario.pop("descripcion")
                cansado.append(dicccionario)
        print(tabulate(    cansado, headers="keys", tablefmt="grid"))
                
def cantio():
        libros = openJSON("libros")
        tatiana = []
        for diccionario in libros:
                diccionario.pop("valoracion")
                diccionario.pop("titulo")
                diccionario.pop("id")
                diccionario.pop("descripcion")  
                diccionario.pop("anio_publicacion")
                diccionario.pop("genero")
                diccionario.pop("autor")
        tatiana.append(diccionario)
        print(tabulate(tatiana, headers="keys", tablefmt="grid"))
