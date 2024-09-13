#RETO 13 - Parte 3
"""
Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
Imprima los nombres completos (nombre y apellidos) de las personas que están en en un rango de edades dado por el usuario.
"""
import json

def deportes(data):
    #Se ingresa el deporte
    deporte : str = input("Ingrese nombre del deporte: ")

    #Se eligen las personas que coincidan con el indicador
    for persona, informacion in data.items():
        if deporte in informacion["deportes"]:
            nombres = informacion["nombres"]
            apellidos = informacion["apellidos"]
            print(f"{nombres} {apellidos} practica {deporte}")
        else:
            continue
    return

def edad(data):
    #Se ingrsa el rango de edad
    edad : str = input("Ingrese el rango de edad (en digitos). Ejemplo 13,15: ")

    #Se obtiene el rango de edad como enteros
    rango = edad.split(",")
    edad_menor : int = int(rango[0])
    edad_mayor : int = int(rango[1])

    #Se eligen las personas que coincidan con el indicador
    for persona, informacion in data.items():
        if edad_menor <= informacion["edad"] <= edad_mayor:
            nombres = informacion["nombres"]
            apellidos = informacion["apellidos"]
            edades = informacion["edad"]
            print(f"{nombres} {apellidos} tiene {edades} años.")
        else:
            continue
    return

if __name__ == "__main__":
    #Ruta al archivo JSON
    archivo = 'C:/Users/Angyp/OneDrive/Documentos/Universidad/Programación de Computadores/RETO 13/archivo.json'
    #Cargar archivo
    readFile = open(archivo, "r")
    data = json.load(readFile)
    readFile.close()

    deportes(data)
    edad(data)

# ! /\|=\/