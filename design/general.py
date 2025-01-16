from tabulate import tabulate
from logic.musica import tableDiscs
from logic.Libros import añadirEle

from design.menus import verTodosElementos
# , buscatElemento, editarElemento, eliminarElemento, verelementosPorcategoria, guardarCargar
# from logic.peliculas import peliculas, buscar_peliculas



def añadirElemento():    
    while True:
        print(verTodosElementos)
        try:
            opcion = int(input("Ingrese el número de la opción: "))
            if opcion == 1:
                añadirEle()
            # elif opcion == 2:
            #     peliculas()
            elif opcion == 3:
                musica()
            elif opcion == 4:
                break
            else:
                print("Por favor, selecciona una opción válida.")
        except ValueError:
            print("Por favor, selecciona una opción válida.")

            
# def conti():
#     while  True:
#         print(verTodosElementos)
#         try:
#                 opcion = int(input("Ingrese el número de la opción: "))
    
#                 if opcion == 1:
#                     libros()
#                 # elif opcion == 2:
#                 #     peliculas()
#                 elif opcion == 3:
#                     musica()
#                 elif opcion == 4:
#                     break
#                 else:
#                     print("Por favor, selecciona una opción válida.")
        
#         except ValueError:
#                 print("Por favor, selecciona una opción válida.")


        
# def noloencuentro():
#     while True:
#         print(buscatElemento)
#         try:
#             opcion = int(input("Ingrese el número de la opción: "))
#             if opcion == 1:
#                 buscar_Libros()
#             # elif opcion == 2:
#             #     buscar_peliculas()
#             elif opcion == 3:
#                 tableDiscs()
#             elif opcion == 4:
#                 break
#             else:
#                 print("Por favor, selecciona una opción válida.")
#         except ValueError:
#             print("Por favor, selecciona una opción válida.")

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


