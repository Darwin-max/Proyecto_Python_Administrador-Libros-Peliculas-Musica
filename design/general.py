
from logic.Libros import añadirEle, ver_libros
from logic.musica import añadireleMusica, ver_musica
from logic.pelicula import añadirElpeli, ver_peliculas
from design.libros import buscar_libros, busca_auti, buscar_gene, edit_titulo, edit_autor, edit_generoLibro, edit_valoraLibro
from design.menus import *
from design.peliculas import buiscar_pelicula, buisr_pelicula, uisr_peliculas, editer_titulo, edit_autorpeli, edit_peli
from design.manu_de_buscar import menu
from design.musica import buiscar_musica, buste,  buisr_musicar, modificar_titulo, edit_autorMusi, edit_genroMusi, edit_genroMusi, edit_valorMusi
from formula.PARA_TODO import *


def añadirElemento(libro):    
    while True:
        print(añadir_emtos)
        try:
            opcion = int(input("Ingrese el número de la opción: "))
            match opcion:
                case 1:
                    añadirEle(libro)
                    
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



            

def editele ():
    while True:
        print(editarElemento)
        try:
            opcion = int(input("Ingrese el número de la opción: "))
            match opcion:
                case 1 :
                    meno = menu()
                    match meno:
                        case 1:
                            edit_titulo()
                        case 2:
                            editer_titulo()
                        case 3:
                            modificar_titulo()
                        case 0:
                            break
                        case _:
                            print("opcion no valida")
                case 2:
                    meno = menu()
                    match meno:
                        case 1:
                            edit_autor()
                        case 2:
                            edit_autorpeli()
                        case 3:
                            edit_autorMusi()
                        case 0:
                            break
                        case _:
                            print("opcion no valida")

                case 3:
                    meno = menu()
                    match meno:
                        case 1:
                            edit_generoLibro()
                        case 2:
                            edit_peli()
                        case 3:
                            edit_genroMusi()
                        case 0:
                            break
                        case _:
                            print("opcion no valida")
                case 4:
                    meno = menu()
                    match meno:
                        case 1:
                            edit_valoraLibro()
                        case 2:
                            edit_genroMusi()
                        case 3:
                            edit_valorMusi()
                        case 0:
                            break
                        case _:
                            print("opcion no valida")
                case 5:
                    break
            print("Por favor, seleccione una obcion valida")
        except ValueError:
            print("Por favor, seleccionar una opcion valida")

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


def saveColection(libro, pelicula, musica):
    book = openJSON("libros")
    music = openJSON("Musica")
    movie = openJSON("peliculas")
    book.extend(libro)
    music.extend(musica)
    movie.extend(pelicula)
    print('hecho')
    input('Press Enter...')

def guardarcargar(libro, pelicula, musica):
    while True:
        print(guardarCargar)
        try:
            opcion = int(input("Ingrese el número de la opción: "))
            if opcion == 1:
                saveColection(libro, pelicula, musica)
            elif opcion == 2:
                pass
            elif opcion == 3:
                break
            else:
                print("Por favor, selecciona una opción válida.")
        except ValueError:
            print("Por favor, selecciona una opción válida.")


