import json
import tabulate
def designDiscs():
    print("""
    ===========================================
        Buscar un Elemento
    ===========================================
    ¿Cómo deseas buscar?
    1. Buscar por Título
    2. Buscar por Autor/Director/Artista
    3. Buscar por Género
    4. Regresar al Menú Principal
    ===========================================
Selecciona una opción (1-4):
    """)

def tableDiscs():
        with open("data/discs.json", "r") as file:
            discs = json.load(file)
            print(tabulate(discs, headers="keys", tablefmt="grid"))


