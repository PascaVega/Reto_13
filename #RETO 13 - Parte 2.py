#RETO 13 - Parte 2
"""
Desarrollar una función que reciba dos diccionarios como parámetros y los mezcle, es decir, 
que se construya un nuevo diccionario con las llaves de los dos diccionarios.
Si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.
"""

import pprint

def mezclar_diccionarios(diccionario_1 : dict, diccionario_2 : dict) -> dict:
    nuevo_diccionario : dict = diccionario_1

    #Se obtienen las llaves de los diccionarios
    llaves_1 = diccionario_1.keys()
    llaves_2 = diccionario_2.keys()
    
    for llave in llaves_2:
        if llave not in llaves_1:
            valor = diccionario_2.get(llave)
            elemento : dict = {llave:valor}
            nuevo_diccionario.update(elemento)

    return nuevo_diccionario

if __name__ == "__main__":
    #Se define el diccionario
    diccionario_1 = {
    "amor": 10,
    "sol": "luz",
    "mar": 23,
    "cielo": "azul",
    "fuego": 45,
    "montaña": "alta",
    "río": 9,
    "árbol": "grande",
    "ciudad": 54,
    "flor": "hermosa",
    "viento": 33,
    "lluvia": "suave"
}
    diccionario_2 = {
    "amor": "fruta",
    "perro": "animal",
    "cielo": "espacio",
    "rojo": "color",
    "río": "líquido",
    "sol": "estrella",
    "auto": "vehículo",
    "espejo": "objeto",
    "silla": "mueble",
    "árbol": "planta",
    "luna": "satélite",
    "puerta": "entrada"
}

    #Se crea el nuevo diccionario
    nuevo_diccionario : dict = {}

    #Se llama a la función
    nuevo_diccionario = mezclar_diccionarios(diccionario_1, diccionario_2)

    #Se imprime el nuevo diccionario
    pprint.pprint(nuevo_diccionario)

# ! /\|=\/