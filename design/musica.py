
from tabulate import tabulate
from logic.musica import musicadd, musicos, music, misiqu
from formula.PARA_TODO import *





def buiscar_musica():
    musica = openJSON("musica")
    musicadd()
    print("¿Qué cancion deseas buscar?")
    cancion = input("cancion: ")
    for musica in musica:
        if musica["cancion"] == cancion:
            print(tabulate([musica], headers="keys", tablefmt="grid"))
            break
    else:
        print("No se encontró el pelicula")



def buste():
    musica = openJSON("musica")
    musicos()
    print("¿Qué cancion deseas busar?")
    artista = input("Artista: ")
    for musica in musica:
        if musica["cantante"] == artista:
            print(tabulate([musica], headers="keys", tablefmt="grid"))
            break
    else:
        print("No se encontró el pelicula")


def buisr_musicar():
    musica = openJSON("musica")  # Asegúrate de que "musica.json" exista y tenga el formato adecuado.
    music() # importa para mostrar una tabla donde muestre todas las musica por genero 
    if not musica:
        return
    
    print("¿Qué musica deseas buscar por género?")
    genero = input("Género: ").strip()
    
    # Filtrar todas las películas que coincidan con el género indicado
    musica_encontradas = [
        musica for musica in musica if musica.get("genero", "").lower() == genero.lower()  
    ]
    
    if musica_encontradas:
        print(f"Películas del género '{genero}':")
        print(tabulate(musica_encontradas, headers="keys", tablefmt="grid"))
    else:
        print(f"No se encontraron películas del género '{genero}'.")

def modificar_titulo():
        musicas = openJSON("musica")
        print (tabulate(musicas, headers="keys", tablefmt="grid"))
        if not musicas:
            print("No hay canciones disponibles para editar.")
            return

        print("¿Qué cancion deseas editar?")
        titulo = input("Título: ").strip()

        for musica in musicas:
            if musica.get("titulo", "").lower() == titulo.lower():
                print("cancion encontrado:")
                print(tabulate(musica, headers="keys", tablefmt="grid"))
                nuevo_titulo = input("Nuevo título: ").strip()
                musica["titulo"] = nuevo_titulo
                print("Título actualizado.")
                writeJSON("musica", musicas)
                break
            else:
                print(f"No se encontro un libro con el título '{titulo}'.") 
                #guardar el json en un archivo temporal para pode guardarlo en el 7 punto de guardar guardar guardar
    


def edit_autorMusi ():
    musicas = openJSON("musica")
    print (tabulate(musica, headers="keys", tablefmt="grid"))
    if not musica:
        print("No hay cansiones disponibles para editar.")
        return

    print("¿Qué cansion deseas editar?")
    artista = input("Autor: ").strip()

    for musica in musicas:
        if musica.get("artista", "").lower() == artista.lower():
            print("Cancion encontrada:")
            print(tabulate(musicas, headers="keys", tablefmt="grid"))
            nuevo_artista = input("Nuevo artista: ").strip()
            musica["artista"] = nuevo_artista
            print("Artsita actualizado.")
            writeJSON("musica", musicas )
            break
        else:
            print(f"No se encontro un cansion con ese artista'{artista}'.") 
        #esto es para que no se modifique el json original de una ves si no que lo gusrde en un json temporal




def edit_genroMusi ():
    musicas = openJSON("musica")
    print (tabulate(musica, headers="keys", tablefmt="grid"))
    if not musica:
        print("No hay cansiones disponibles para editar.")
        return

    print("¿Qué cansion deseas editar?")
    genero = input("Genero: ").strip()

    for musica in musicas:
        if musica.get("genero", "").lower() == genero.lower():
            print("Cancion encontrada:")
            print(tabulate(musicas, headers="keys", tablefmt="grid"))
            nuevo_genro = input("Nuevo genero: ").strip()
            musica["genero"] = nuevo_genro
            print("Genero actualizado.")
            writeJSON("musica", musica)
            break
        else:
            print(f"No se encontro un cansion con ese genero'{genero}'.") 
        #esto es para que no se modifique el json original de una ves si no que lo gusrde en un json temporal



def edit_valorMusi ():
    musicas = openJSON("musica")
    print (tabulate(musica, headers="keys", tablefmt="grid"))
    if not musica:
        print("No hay cansiones disponibles para editar.")
        return

    print("¿Qué cansion deseas editar?")
    valo = input("Valoracion: ").strip()

    for musica in musicas:
        if musica.get("valoracion", "").lower() == valo.lower():
            print("Cancion encontrada:")
            print(tabulate(musicas, headers="keys", tablefmt="grid"))
            nuevo_genro = input("Nuevo valoracion: ").strip()
            musica["valoracion"] = nuevo_genro
            print("Valoracion actualizado.")
            writeJSON("musica", musicas)
            break
        else:
            print(f"No se encontro un cansion con esa valoracion'{valo}'.") 
        #esto es para que no se modifique el json original de una ves si no que lo gusrde en un json temporal



def eliminar_titulo():
        musicas = openJSON("musica")
        print (tabulate(musicas, headers="keys", tablefmt="grid"))
        if not musicas:
            print("No hay canciones disponibles para editar.")
            return

        print("¿Qué cancion deseas editar?")
        titulo = input("Título: ").strip()

        for musica in musicas:
            if musica.get("titulo", "") == titulo:
                print("Canción encontrada:")
                musicas.remove(musica)  # Aquí sí puedes usar `.remove()` porque `musicas` es una lista
                print(tabulate(musicas, headers="keys", tablefmt="grid"))
                writeJSON("musica", musicas)
                break
        else:
            print(f"No se encontró una canción con el titulo '{titulo}'.")


def eliminar_idMusi():
        musicas = openJSON("musica")
        print (tabulate(musicas, headers="keys", tablefmt="grid"))
        if not musicas:
            print("No hay canciones disponibles para eliminar.")
            return

        print("¿Qué cancion deseas editar?")
        id = input("ID: ").strip()

        for musica in musicas:
            if musica.get("id", "") == id:
                print("Canción encontrada:")
                musicas.remove(musica)  # Aquí sí puedes usar `.remove()` porque `musicas` es una lista
                print(tabulate(musicas, headers="keys", tablefmt="grid"))
                writeJSON("musica", musicas)
                break
        else:
            print(f"No se encontró una canción con el id '{id}'.")


def buiscar_catemusica(kk):
    musica = openJSON("musica")

    musica = openJSON("libros")  # Carga la lista de libros desde el archivo JSON
    misiqu()  # Llama a una función para mostrar información (si la tienes definida)
    # Verifica si hay libros cargados
    if not musica:
        print("No hay libros disponibles para buscar.")
        return
    
    print("¿Qué libro deseas buscar?")  # Solicita el título al usuario
    titulo = input("categoria: ").strip()  # Elimina espacios al inicio y final
    # Busca libros que coincidan con el título
    musica_buscarti = [
        musicas for musicas in musica if musica.get("categoria", "").lower() == titulo.lower()
    ]
    # Imprime el resultado de la búsqueda
    if musica_buscarti:
        print(f"Libros encontrados con el título '{titulo}':")
        print(tabulate(musica_buscarti, headers="keys", tablefmt="grid"))
    else:
        print(f"No se encontraron libros con el título '{titulo}'.")


    kk.append(musica_buscarti)