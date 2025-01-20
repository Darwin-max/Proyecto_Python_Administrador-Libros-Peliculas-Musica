from tabulate import tabulate
from logic.Libros import añadirEle, ver_libros
from logic.musica import añadireleMusica, ver_musica
from logic.pelicula import añadirElpeli, ver_peliculas
from design.libros import buscar_libros, busca_auti, buscar_gene
from design.menus import *
from design.peliculas import buiscar_pelicula, buisr_pelicula, uisr_peliculas
from design.manu_de_buscar import menu
from design.musica import buiscar_musica, buste,  buisr_musicar

def añadirElemento():    
    while True:
        print(añadir_emtos)
        try:
            opcion = int(input("Ingrese el número de la opción: "))
            match opcion:
                case 1:
                    añadirEle()
                    
                case 2:
                    añadirElpeli()
                    
                case 3:
                    añadireleMusica()
                    
                case 4:
                    break
                case _:
                    print("Por favor, selecciona una opción válida.")
        except ValueError:
            print("Por favor, selecciona una opción válida.")


            
def conti():
    while  True:
        print(verTodosElementos)
        try:
                opcion = int(input("Ingrese el número de la opción: "))
    
                if opcion == 1:
                    ver_libros()
                elif opcion == 2:
                    ver_peliculas()
                elif opcion == 3:
                    ver_musica()
                elif opcion == 4:
                    break
                else:
                    print("Por favor, selecciona una opción válida.")
        
        except ValueError:
                print("Por favor, selecciona una opción válida.")


        
def noloencuentro():
    
    while True:
        print(buscatElemento)
        try:
            opcion = int(input("Ingrese el número de la opción: "))
            match opcion:
                    case  1:
                        while True:
                            meno = menu()
                            match meno:
                                case 1:
                                    buscar_libros()
                                case 2:
                                    buiscar_pelicula()
                                case 3:
                                    buiscar_musica()
                                case 0:
                                    break
                                case _:
                                    print("opcion no valida")
                    case 2:
                        while True:
                            meno = menu()
                            match meno:
                                case 1 :
                                    busca_auti()
                                case 2 :
                                    buisr_pelicula()
                                case 3 :
                                    buste()
                                case 0 :
                                    break
                                case _:
                                    print("opcion no valida")
                    case 3:
                        while True:
                            meno = menu()
                            match meno:
                                case 1:
                                    buscar_gene()
                                case 2:

                                    uisr_peliculas ()
                                case 3:
                                    buisr_musicar()
                                case 0 :
                                    break
                                case _:
                                    print("obcion no valida")
                    case 4:
                        break
        except ValueError:
            print("Por favor, selecciona una opción válida.")



            

# def editele ():
#     while True:
#         print(editarElemento)
#         try:
#             opcion = int(input("Ingrese el número de la opción: "))
#             if opcion == 1:
#                 pass
#             elif opcion == 2:
#                 pass
#             elif opcion == 3:
#                 pass
#             elif opcion == 4:
#                 pass
#             elif opcion == 5:
#                 break
#             else:
#                 print("Por favor, selecciona una opción válida.")
#         except ValueError:
#             print("Por favor, selecciona una opción válida.")          

# def eliminele():
#     while True:
#         print(eliminarElemento)
#         try:
#             opcion = int(input("Ingrese el número de la opción: "))
#             if opcion == 1:
#                 pass
#             elif opcion == 2:
#                 pass
#             elif opcion == 3:
#                 break
#             else:
#                 print("Por favor, selecciona una opción válida.")
#         except ValueError:
#             print("Por favor, selecciona una opción válida.")  

# def verelecat():
#     while True:
#         print(verelementosPorcategoria)
#         try:
#             opcion = int(input("Ingrese el número de la opción: "))
#             if opcion == 1:
#                 pass
#             elif opcion == 2:
#                 pass
#             elif opcion == 3:
#                 pass
#             elif opcion == 4:
#                 break
#             else:
#                 print("Por favor, selecciona una opción válida.")
#         except ValueError:
#             print("Por favor, selecciona una opción válida.")

# def guardarcargar():
#     while True:
#         print(guardarCargar)
#         try:
#             opcion = int(input("Ingrese el número de la opción: "))
#             if opcion == 1:
#                 pass
#             elif opcion == 2:
#                 pass
#             elif opcion == 3:
#                 break
#             else:
#                 print("Por favor, selecciona una opción válida.")
#         except ValueError:
#             print("Por favor, selecciona una opción válida.")


