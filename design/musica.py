
from tabulate import tabulate
from logic.musica import designDiscs
def musica():
    """
    Muestra el menú de música y permite seleccionar entre las opciones de pedidos, productos y edición de pedidos.
    """
    while True:
        print("""
        ===========================================
        Ver Todos los Elementos
        ===========================================
        ¿Qué categoría deseas ver?
        1. Ver Todos los Libros
        2. Ver Todas las Películas
        3. Ver Toda la Música
        4. Regresar al Menú Principal
        ===========================================
Selecciona una opción (1-4):
        """)
        try:
            principal = input("Ingrese el número de la opción: ")
            match principal:
                case "3":
                    while True:
                        option = designDiscs()
                        match option:
                            case 1:
                                tableDiscs()
                            case 2:
                                tableSongs()
                            case 3:
                                tableMusic()
                            case 0:
                                break
                            case _:
                                print("Opción no válida en Música.")
        except ValueError:
            print("")



  