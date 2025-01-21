
from tabulate import tabulate
from formula.PARA_TODO import openJSON


def validar_numero(mensaje):
        while True:
                try:
                        valor = int(input(mensaje))
                        return valor
                except ValueError:
                        print("Por favor, ingrese un número válido.")

def añadireleMusica(ll):
        while True:
                opc = input("ingrese s para añadir un nuevo libro y 0 para terminar: ")
                if opc == '0' :                                 #este es if se esta utilizando por que quedava retornando de manera infita  agrgar un producto
                        break     
                musica = openJSON("musica") # Cargar los datos de la lista de música
                input("Presione Enter para continuar...")
                
                #Añade una nueva canción a la lista de música y retorna la canción añadida.
                # Mostrar la lista actual de música
                if musica:
                        print("Lista actual de música:")
                        print(tabulate(musica, headers="keys", tablefmt="grid"))
                else:
                        print("La lista está vacía.")

                # Solicitar los datos de la nueva canción
                nuevo_id = max([musica.get("id", 0) for musica in musica], default=0) + 1 # Generar un ID único para el nuevo libro                nuevo_libro["id"] = nuevo_id    # Añadir el ID al nuevo libro
                id = nuevo_id
                cancion = input("Canción: ").strip()
                artista = input("Artista: ").strip()
                genero = input("Género: ").strip()
                año = input("Año: ").strip()
                valoracion = input("valoracion: ").strip()

                while valoracion < 1 or valoracion > 10:
                        print("Valoración no válida. Debe estar entre 1 y 10.")
                        valoracion = int(input("Valoracion: "))
                # Crear un diccionario con los datos de la canción
                nueva_cancion = {
                "id": id,
                "Canción": cancion,
                "Artista": artista,
                "Género": genero,
                "Año": año,
                "valoracion": valoracion
                }
                ll.append(nueva_cancion)
                return nueva_cancion  # Retornar la canción añadida

# este es el segundo punto del proyecto que es buscar una cancion en la lista de musica 
# acordarse de que todavia me falta tabular bien las tablas de musica

def ver_musica():  # Buscar una canción en la lista de música
        musica = openJSON("musica") # Cargar los datos de la lista de música
        print(tabulate(musica, headers="keys", tablefmt="grid"))  # Mostrar la lista de música
        




def musicadd():
        musica = openJSON("musica")
        Nahomi = []
        for dicccionario in musica:
                dicccionario.pop("categoria")
                dicccionario.pop("id")
                dicccionario.pop("genero")
                dicccionario.pop("cantante")
                dicccionario.pop("disco")
                
                
                Nahomi.append(dicccionario)
        print(tabulate(Nahomi, headers="keys", tablefmt="grid"))
                


def musicos():
        musicass = openJSON ("musica")
        francy = []
        for dicccionario in musicass:
                dicccionario.pop("categoria")
                dicccionario.pop("id")
                dicccionario.pop("genero")
                dicccionario.pop("cancion")
                dicccionario.pop("disco")
                francy.append(dicccionario)
        print(tabulate(francy, headers="keys", tablefmt="grid"))
                
                
def music():
        musicas = openJSON("musica")
        kenji = []
        for dicccionario in musicas:
                dicccionario.pop("categoria")
                dicccionario.pop("id")
                dicccionario.pop("cantante")
                dicccionario.pop("cancion")
                dicccionario.pop("disco")
                kenji.append(dicccionario)
        print(tabulate(kenji, headers="keys", tablefmt="grid"))

def misiqu():
        libros = openJSON("libros")
        tatiana = []
        for diccionario in libros:
                diccionario.pop("titulo")
                diccionario.pop("id")
                diccionario.pop("descripcion")  
                diccionario.pop("anio_publicacion")
                diccionario.pop("genero")
                diccionario.pop("autor")
        tatiana.append(diccionario)
        print(tabulate(tatiana, headers="keys", tablefmt="grid"))

