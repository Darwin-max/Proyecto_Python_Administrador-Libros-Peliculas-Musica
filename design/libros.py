
from tabulate import tabulate
from logic.Libros import Libros , Libr, nose
from formula.PARA_TODO import openJSON



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
            print(tabulate( [   Libros], headers="keys", tablefmt="grid"))
            break
    else:
        print("No se encontró el libro")