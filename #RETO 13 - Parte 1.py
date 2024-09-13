#RETO 13 - Parte 1
#Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.

def imprimir_valores_ascendentes(diccionario : dict):
    
    #Se obtienen los valores del diccionario
    valores = diccionario.values()
    
    #Se ordenan los valores
    valores_ordenados = sorted(valores)
    
    #Se imprimen los valores ordenados
    for valor in valores_ordenados:
        print(valor)

    return

if __name__ == "__main__":
    #Se define el diccionario
    diccionario : dict = {"a": 1, "b": 9, "c": 35, "d": 7, "e": 2, "f": 32, "g": 8, "h": 128}

    #Se llama a la función
    imprimir_valores_ascendentes(diccionario)

# ! /\|=\/