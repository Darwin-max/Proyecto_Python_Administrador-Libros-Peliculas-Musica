import json

def openJSON(datos):
    try: 
        with open(f"data/{datos}.json", "r", encoding="utf-8") as file :
            data = file.read()  # Leer el archivo JSON
            converted = json.loads(data)  # Convertir el contenido a lista de Python
            return converted
    except FileNotFoundError:
        print(f"El archivo {datos}.json no existe.")
        return []
    except json.JSONDecodeError:
        print("El archivo JSON tiene un formato inválido.")
        return []

def writeJSON(datos, diccionario):
    with open(f"data/{datos}.json", "w", encoding="utf-8") as file:
        json.dump(diccionario, file, indent=4)


