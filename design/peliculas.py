from tabulate import tabulate
from logic.pelicula import  peliculas_ , pelicas_, masTarde, cantio
from formula.PARA_TODO import *

def buiscar_pelicula():
    peliculas = openJSON("peliculas")  # Carga la lista de libros desde el archivo JSON
    peliculas_() # Llama a una función para mostrar información (si la tienes definida)    
    print("¿Qué pelicula deseas buscar?")# Solicita el título al usuario
    titulo = input("Título: ")  # Elimina espacios al inicio y final

    for peliculas in peliculas:
        if peliculas["titulo"] == titulo:
            print(tabulate([peliculas], headers="keys", tablefmt="grid"))
            writeJSON("pelicula", peliculas)
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
    ]           # Filtra las películas de la lista `peliculas` que coincidan con el género especificado (ignorando mayúsculas y minúsculas).
                # La condición verifica si el valor asociado a la clave "genero" en cada película coincide con el género buscado.
                # Si una película no tiene la clave "genero", se usa una cadena vacía como valor predeterminado.

    if peliculas_encontradas:
        print(f"Películas del género '{genero}':")
        print(tabulate(peliculas_encontradas, headers="keys", tablefmt="grid"))
    else:
        print(f"No se encontraron películas del género '{genero}'.")


def editer_titulo():
    peliculas = openJSON("peliculas")
    print(tabulate(peliculas, headers="keys" , tablefmt= "grid"))
    if not peliculas:
        print("no hay peliculas disponibles para editar")
        return
    print("¿Que libro deceas modificar?")
    titulo = input("¿Que libro deceas editar")

    for pelicula in peliculas:
        if pelicula.get("titulo", "").lower() == titulo.lower():
            print("Pelicula encontrada:")
            print(tabulate(peliculas, headers="keys", tablefmt="grid"))
            nuevo_titulo = input("Nuevo título: ").strip()
            peliculas["titulo"] = nuevo_titulo
            print("Titulo actualizado.")
            writeJSON("pelicula", peliculas)
            break
        else:
            print(f"No se encontro un libro con el titulo'{peliculas}'")
    

def edit_autorpeli ():
    peliculas = openJSON("peliculas")
    print (tabulate(peliculas, headers="keys", tablefmt="grid"))
    if not peliculas:
        print("No hay peliculas disponibles para editar.")
        return

    print("¿Qué libro deseas editar?")
    Director = input("Director: ").strip()

    for pelicula in peliculas:
        if pelicula.get("director", "").lower() == Director.lower():
            print("Pelicula encontrada:")
            print(tabulate(peliculas, headers="keys", tablefmt="grid"))
            nuevo_director = input("Nuevo director: ").strip()
            peliculas["director"] = nuevo_director
            print("director actualizado.")
            writeJSON("pelicula", peliculas)
            break
        else:
            print(f"No se encontro un pelicula con el ese autor '{Director}'.") 


def edit_peli ():
    peliculas = openJSON("peliculas")
    print (tabulate(peliculas, headers="keys", tablefmt="grid"))
    if not peliculas:
        print("No hay peliculas disponibles para editar.")
        return

    print("¿Qué libro deseas editar?")
    Genero = input("Genero: ").strip()

    for pelicula in peliculas:
        if pelicula.get("genero", "").lower() == Genero.lower():
            print("Pelicula encontrada:")
            print(tabulate(peliculas, headers="keys", tablefmt="grid"))
            nuevo_director = input("Nuevo genero: ").strip()
            peliculas["genero"] = nuevo_director
            print("director actualizado.")
            writeJSON("pelicula", peliculas)
            break
        else:
            print(f"No se encontro un pelicula con el ese genero '{Genero}'.") 
        #esto es para que no se modifique el json original de una ves si no que lo gusrde en un json temporal


def edit_valopeli ():
    peliculas = openJSON("peliculas")
    print (tabulate(peliculas, headers="keys", tablefmt="grid"))
    if not peliculas:
        print("No hay peliculas disponibles para editar.")
        return

    print("¿Qué libro deseas editar?")
    valo = input("Valoracion: ").strip()

    for pelicula in peliculas:
        if pelicula.get("valoracion", "").lower() == valo.lower():
            print("Pelicula encontrada:")
            print(tabulate(peliculas, headers="keys", tablefmt="grid"))
            nuevo_valo = input("Nueva valoracion: ").strip()
            peliculas["valoracion"] = nuevo_valo
            print("Valoracion actualizado.")
            writeJSON("pelicula", peliculas)
            break
        else:
            print(f"No se encontro un pelicula con el ese valoracion '{valo}'.") 

def elim_titulo():
    peliculas = openJSON("peliculas")
    print(tabulate(peliculas, headers="keys" , tablefmt= "grid"))
    if not peliculas:
        print("no hay peliculas disponibles para editar")
        return
    print("¿Que libro deceas modificar?")
    titulo = input("¿Que libro deceas editar")

    for pelicula in peliculas:
        if pelicula.get("titulo", "").remove() == titulo.remove():
            print("Pelicula encontrada:")
            print(tabulate(peliculas, headers="keys", tablefmt="grid"))
            writeJSON("pelicula", peliculas)
            break
        else:
            print(f"No se encontro un libro con el titulo'{peliculas}'")

def elim_Idpelicul():
    peliculas = openJSON("peliculas")
    print(tabulate(peliculas, headers="keys" , tablefmt= "grid"))
    if not peliculas:
        print("no hay peliculas disponibles para editar")
        return
    print("¿Que libro deceas modificar?")
    ID = input("ID: ").strip()

    for pelicula in peliculas:
        if pelicula.get("id", "").remove() == ID.remove():
            print("Pelicula encontrada:")
            print(tabulate(peliculas, headers="keys", tablefmt="grid"))
            writeJSON("pelicula", peliculas)
            break
        else:
            print(f"No se encontro un libro con el titulo'{peliculas}'")

def buiscar_categoriaPeli(kk):
    peliculas = openJSON("peliculas")  # Carga la lista de libros desde el archivo JSON
    cantio() # Llama a una función para mostrar información (si la tienes definida)    
    print("¿Qué pelicula deseas buscar?")# Solicita el título al usuario
    catego = input("Categoria: ")  # Elimina espacios al inicio y final


    for peliculas in peliculas:
        if peliculas["categoria"] == catego:
            print(tabulate(peliculas, headers="keys", tablefmt="grid"))
            writeJSON("pelicula", peliculas)
            break
    else:
        print("No se encontró el pelicula")

    



    cantio()  # Llama a una función para mostrar información (si la tienes definida)
    # Verifica si hay libros cargados
    if not peliculas:
        print("No hay libros disponibles para buscar.")
        return
    
    print("¿Qué libro deseas buscar?")  # Solicita el título al usuario
    titulo = input("categoria: ").strip()  # Elimina espacios al inicio y final
    # Busca libros que coincidan con el título
    peli_buscarti = [
        pelicula for pelicula in peliculas if peliculas.get("categoria", "").lower() == titulo.lower()
    ]
    # Imprime el resultado de la búsqueda
    if peli_buscarti:
        print(f"Libros encontrados con el título '{titulo}':")
        print(tabulate(peli_buscarti, headers="keys", tablefmt="grid"))
    else:
        print(f"No se encontraron libros con el título '{titulo}'.")


    kk.append(peli_buscarti)