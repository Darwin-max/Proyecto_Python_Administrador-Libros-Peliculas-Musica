from tabulate import tabulate
from logic.pelicula import  peliculas_ , pelicas_, masTarde
from formula.PARA_TODO import openJSON






def buiscar_pelicula():
    peliculas = openJSON("peliculas")  # Carga la lista de libros desde el archivo JSON
    peliculas_() # Llama a una función para mostrar información (si la tienes definida)    
    print("¿Qué pelicula deseas buscar?")# Solicita el título al usuario
    titulo = input("Título: ")  # Elimina espacios al inicio y final

    for peliculas in peliculas:
        if peliculas["titulo"] == titulo:
            print(tabulate([peliculas], headers="keys", tablefmt="grid"))
            break
    else:
        print("No se encontró el pelicula")



def buisr_pelicula():
    peliculas = openJSON("peliculas")
    pelicas_()
    print("¿Qué pelicula deseas buscar?")
    director = input("Director: ").strip()
    peliculas_encontradas = [
        pelicula for pelicula in peliculas if pelicula.get("director") == director
    ]
    
    if peliculas_encontradas:
        print(f"Películas dirigidas por {director}:")
        print(tabulate(peliculas_encontradas, headers="keys", tablefmt="grid"))
    else:
        print(f"No se encontraron películas dirigidas por {director}.")
    

def uisr_peliculas():
    peliculas = openJSON("peliculas")  # Asegúrate de que "peliculas.json" exista y tenga el formato adecuado.
    masTarde() # importa para mostrar una tabla donde muestre todas las peliculas por genero 
    if not peliculas:
        return
    
    print("¿Qué películas deseas buscar por género?")
    genero = input("Género: ").strip()
    
    # Filtrar todas las películas que coincidan con el género indicado
    peliculas_encontradas = [
        pelicula for pelicula in peliculas if pelicula.get("genero", "").lower() == genero.lower()
    ]
    
    if peliculas_encontradas:
        print(f"Películas del género '{genero}':")
        print(tabulate(peliculas_encontradas, headers="keys", tablefmt="grid"))
    else:
        print(f"No se encontraron películas del género '{genero}'.")

