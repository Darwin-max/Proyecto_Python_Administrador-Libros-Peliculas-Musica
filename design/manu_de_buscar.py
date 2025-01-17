from tabulate import tabulate
from logic.Libros import añadirEle, ver_libros, Libros
from logic.musica import añadireleMusica, ver_musica
from logic.pelicula import añadirElpeli, ver_peliculas
from design.libros import buscar_libros
from design.menus import *
from design.peliculas import buiscar_pelicula


def menu():
    """
    Muestra los tres tipos de datos que pueden pedir     """
    while True:
        print("""
        *************************************************************************************
                                    Bienvenido al menú principal
                    libros          |   peliculas   |       musica       |   Salir
                        1           |       2       |         3          |     0
        *************************************************************************************
        """)
        return  int(input())