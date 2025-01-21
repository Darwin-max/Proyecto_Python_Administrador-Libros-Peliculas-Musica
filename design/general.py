
from logic.Libros import añadirEle, ver_libros
from logic.musica import añadireleMusica, ver_musica
from logic.pelicula import añadirElpeli, ver_peliculas
from design.libros import buscar_libros, busca_auti, buscar_gene, edit_titulo, edit_autor, edit_generoLibro, edit_valoraLibro, eli_titulo, eli_id, verEle_categoriaLibr
from design.menus import *
from design.peliculas import buiscar_pelicula, buisr_pelicula, uisr_peliculas, editer_titulo, edit_autorpeli, edit_peli, elim_titulo, elim_Idpelicul, buiscar_categoriaPeli
from design.manu_de_buscar import menu
from design.musica import buiscar_musica, buste,  buisr_musicar, modificar_titulo, edit_autorMusi, edit_genroMusi, edit_genroMusi, edit_valorMusi, eliminar_titulo, eliminar_idMusi, buiscar_catemusica
from formula.PARA_TODO import *


def añadirElemento(libro, peliculas, musica):    
    while True:
        print(añadir_emtos)
        try:
            opcion = int(input("Ingrese el número de la opción: "))
            match opcion:
                case 1:
                    añadirEle(libro)
                    
                case 2:
                    añadirElpeli(peliculas)
                    
                case 3:
                    añadireleMusica(musica)
                    
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

def eliminele():
    while True:
        print(editarElemento)
        try:
            opcion = int(input("Ingrese el número de la opción: "))
            match opcion:
                case 1 :
                    meno = menu()
                    match meno:
                        case 1:
                            eli_titulo()
                        case 2:
                            elim_titulo()
                        case 3:
                            eliminar_titulo()
                        case 0:
                            break
                        case _:
                            print("opcion no valida")
                case 2:
                    meno = menu()
                    match meno:
                        case 1:
                            eli_id()
                        case 2:
                            elim_Idpelicul()
                        case 3:
                            eliminar_idMusi()
                        case 0:
                            break
                        case _:
                            print("opcion no valida")
                case 3:
                    break
            print("Por favor, seleccione una obcion valida")
        except ValueError:
            print("Por favor, seleccionar una opcion valida")

def verelecat( libro, pelicula, musica):
    while True:
        print(verelementosPorcategoria)
        try:
            opcion = int(input("Ingrese el número de la opción: "))
            if opcion == 1:
                verEle_categoriaLibr(libro)
            elif opcion == 2:
                buiscar_categoriaPeli(pelicula)
            elif opcion == 3:
                buiscar_catemusica(musica)
            elif opcion == 4:
                break
            else:
                print("Por favor, selecciona una opción válida.")
        except ValueError:
            print("Por favor, selecciona una opción válida.")


def loadColection(libro, pelicula, musica):
    
    booksSave = openJSON("libros")
    musicSave = openJSON("Musica")
    moviesSave = openJSON("peliculas")
    pressEnter()
    return  booksSave, musicSave, moviesSave



def saveColection(libro, pelicula, musica):
    book = openJSON("libros")
    music = openJSON("Musica")
    movie = openJSON("peliculas")
    book.extend(libro)
    music.extend(musica)
    movie.extend(pelicula)
    writeJSON("libros", book)
    writeJSON("Musica", music)
    writeJSON("peliculas", movie)
    print('hecho')
    input('Press Enter...')

def guardarcargar(libro, pelicula, musica):
    while True:
        print(guardarCargarDesign)
        try:
            opcion = int(input("Ingrese el número de la opción: "))
            if opcion == 1:
                saveColection(libro, pelicula, musica)
            elif opcion == 2:
                loadColection(libro, pelicula, musica)
            elif opcion == 3:
                break
            else:
                print("Por favor, selecciona una opción válida.")
        except ValueError:
            print("Por favor, selecciona una opción válida.")


def pressEnter ():
    print("Exito")
    input('Presiona Enter para continuar...')