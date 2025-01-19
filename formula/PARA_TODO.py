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

    
# def writeJSON(datos, diccionario):
# #--- GUARDAR EL DICCIONARIO A JSON ---
# #1. Serializar el diccionario a formato JSON
#     objetoJson= json.dumps(diccionario)

# #Guardar en un archivo JSON la variable "objetoJson"
#     with open (f"data/{datos}.json", "w") as archivoSalida:
#         archivoSalida.write(objetoJson)

def writeJSON(datos, diccionario):
    with open(f"data/{datos}.json", "w", encoding="utf-8") as file:
        json.dump(diccionario, file, indent=4)