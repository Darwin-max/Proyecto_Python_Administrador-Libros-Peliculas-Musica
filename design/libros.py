
from tabulate import tabulate
from logic.Libros import Libros , Libr
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
    
