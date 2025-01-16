import json



def openJSON(datos):
    with open(f"data/{datos}.json", "r", encoding="utf-8") as file :
        data = file.read()  # Leer el archivo JSON
        converted = json.loads(data)  # Convertir el contenido a lista de Python
        return converted
    
def writeJSON(datos, diccionario):
                                                        #--- GUARDAR EL DICCIONARIO A JSON ---
                                                                #1. Serializar el diccionario a formato JSON
    objetoJson= json.dumps(diccionario)

#Guardar en un archivo JSON la variable "objetoJson"
    with open("./archivos/ejemplo.json","w") as archivoSalida:
        archivoSalida.write(objetoJson)








