
from tabulate import tabulate
from logic.Libros import Libros
from formula.PARA_TODO import openJSON



def buscar_libros():
    
    libros = openJSON("libros")
    Libros()
    print("¿Qué libro deseas buscar?")
    titulo = input("Título: ")
    for libro in libros:
        if libro["titulo"] == titulo:
            print(tabulate([libro], headers="keys", tablefmt="grid"))
            break
    else:
        print("No se encontró el libro")
    



  