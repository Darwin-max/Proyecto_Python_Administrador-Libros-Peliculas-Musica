
from design.menus import menuPrincipal
from logic.Libros import *
from design.general import *

#     Muestra el menú principal y permite seleccionar entre las opciones 
libro = []
pelicula = []
musica = []
categoria = []

if __name__ == '__main__':
   while True:
      print(menuPrincipal) 
      try:
         opcion = int(input("Ingrese el número de la opción: "))

         if opcion == 1:
            añadirElemento(libro, pelicula, musica)
         elif opcion == 2:
            conti()
         elif opcion == 3:
            noloencuentro()
         elif opcion == 4:
            editele()
         elif opcion == 5:
            eliminele()
         elif opcion == 6:
            verelecat(input("ingrese la categoria: "))
         elif opcion == 7:
            guardarcargar(libro, pelicula, musica)
         elif opcion == 8:
            print("¡Hasta luego!")
            break
         else:
            print("Por favor, selecciona una opción válida.")
      except ValueError:
         print("Por favor, selecciona una opción válida.")
      else:
         x = input("Presione enter para continuar")

