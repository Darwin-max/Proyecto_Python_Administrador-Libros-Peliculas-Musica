from tabulate import tabulate
from logic.Libros import Libros , Libr, nose
from formula.PARA_TODO import *


def buscar_libros():
    libros = openJSON("libros")  # Carga la lista de libros desde el archivo JSON
    Libros()  # Llama a una función para mostrar información (si la tienes definida)

    # Verifica si hay libros cargados
    if not libros:
        print("No hay libros disponibles para buscar.")
        return

    # Solicita el título al usuario
    print("¿Qué libro deseas buscar?")
    titulo = input("Título: ").strip()  # Elimina espacios al inicio y final

    # Busca libros que coincidan con el título
    libros_buscarti = [
        libro for libro in libros if libro.get("titulo", "").lower() == titulo.lower()
    ]

    # Imprime el resultado de la búsqueda
    if libros_buscarti:
        print(f"Libros encontrados con el título '{titulo}':")
        print(tabulate(libros_buscarti, headers="keys", tablefmt="grid"))
    else:
        print(f"No se encontraron libros con el título '{titulo}'.")



def busca_auti():
    Libros = openJSON("libros")
    Libr()
    print("¿Qué libro deseas buscar?")
    autor = input("Autor: ")
    for  Libros in Libros :
        if Libros ["autor"] == autor:
            print(tabulate( [   Libros], headers="keys", tablefmt="grid"))
            break
    else:
        print("No se encontró el libro")
    

def buscar_gene():
    Libros = openJSON("libros") 
    nose()
    print("¿Que libro deseas")
    genero = input("genero: ")
    for  Libros in Libros :
        if Libros ["genero"] == genero:
            print(tabulate(    Libros, headers="keys", tablefmt="grid"))
            break
    else:
        print("No se encontró el libro")

def edit_titulo ():
    libros = openJSON("libros")
    print (tabulate(libros, headers="keys", tablefmt="grid"))
    if not libros:
        print("No hay libros disponibles para editar.")
        return

    print("¿Qué libro deseas editar?")
    titulo = input("Título: ").strip()

    for libro in libros:
        if libro.get("titulo", "").lower() == titulo.lower():
            print("Libro encontrado:")
            print(tabulate(libros, headers="keys", tablefmt="grid"))
            nuevo_titulo = input("Nuevo título: ").strip()
            libro["titulo"] = nuevo_titulo
            print("Título actualizado.")
            writeJSON("libros", libros)
            break
        else:
            print(f"No se encontro un libro con el título '{titulo}'.") 



def edit_autor ():
    libros = openJSON("libros")
    print (tabulate(libros, headers="keys", tablefmt="grid"))
    if not libros:
        print("No hay libros disponibles para editar.")
        return

    print("¿Qué libro deseas editar?")
    autor = input("Autor: ").strip()

    for libro in libros:
        if libro.get("autor", "").lower() == autor.lower():
            print("Libro encontrado:")
            print(tabulate(libros, headers="keys", tablefmt="grid"))
            nuevo_autor = input("Nuevo autor: ").strip()
            libro["autor"] = nuevo_autor
            print("autor actualizado.")
            writeJSON("libros", libros)
            break
        else:
            print(f"No se encontro un libro con ese autor '{autor}'.") 


def edit_generoLibro ():
    libros = openJSON("libros")
    print (tabulate(libros, headers="keys", tablefmt="grid"))
    if not libros:
        print("No hay libros disponibles para editar.")
        return

    print("¿Qué libro deseas editar?")
    Genero = input("Genero: ").strip()

    for libro in libros:
        if libro.get("genero", "").lower() == Genero.lower():
            print("Libro encontrado:")
            print(tabulate(libros, headers="keys", tablefmt="grid"))
            nuevo_autor = input("Nuevo genero: ").strip()
            libro["genero"] = nuevo_autor
            print("genero actualizado.")
            writeJSON("libros", libros)
            break
        else:
            print(f"No se encontro un libro con ese genero '{Genero}'.") 
        #esto es para que no se modifique el json original de una ves si no que lo gusrde en un json temporal


def edit_valoraLibro ():
    libros = openJSON("libros")
    print (tabulate(libros, headers="keys", tablefmt="grid"))
    if not libros:
        print("No hay libros disponibles para editar.")
        return

    print("¿Qué libro deseas editar?")
    valo = input("Valoracion: ").strip()

    for libro in libros:
        if libro.get("valoracion", "").lower() == valo.lower():
            print("Libro encontrado:")
            print(tabulate(libros, headers="keys", tablefmt="grid"))
            nuevo_valor = input("Nueva valoracion: ").strip()
            libro["valoracion"] = nuevo_valor
            print("valoracion actualizado.")
            writeJSON("libros", libros)
            break
        else:
            print(f"No se encontro un libro con esa valoracion '{valo}'.") 
        #esto es para que no se modifique el json original de una ves si no que lo gusrde en un json temporal
