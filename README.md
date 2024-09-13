# Reto 13
| Nombre                 | Identificación | Grupo | Trabajo          |
|------------------------|----------------|-------|------------------|
| Angélica Pascagaza Vega| 1031652163     |   5   | Trabajo individual |

## Solución del reto
<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 8 - Parte 1</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">En esta ocasión, se baso en un diccionario en donde todos los valores son enteros.</td>
  </tr>
</table>

**Parte 1**
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 8 - Parte 2</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Desarrollar una función que reciba dos diccionarios como parámetros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Para este ejercicio, se creó un nuevo diccionario basado en el primero, para luego comparar las llaves del seguno e irlas agrgando a medida que se verifica que no estén ya en el nuevo diccionario.</td>
  </tr>
</table>

**Parte 2**
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 8 - Parte 3</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Cree un programa que lea de un archivo con dicho JSON e:
      <li>Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.</li>
      <li>Imprima los nombres completos (nombre y apellidos) de las personas que est�en en un rango de edades dado por el usuario.</li></td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">En esta ocasión, se creó un archivo <i>JSON</i> a parte, luego se leyó el archivo en el programa de <i>Python</i> y se extrajeron los valores correspondientes.</td>
  </tr>
</table>

**JSON**
```json
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "Diaz Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["Futbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
```

**Parte 3**
```python
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
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 8 - Parte 4</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Imprimir las fechas de alerta, el tipo de alerta y las variables asociadas.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Para este punto, se convirtieron las fechas a un lenguaje legible y luego se recorrió el <i>JSON</i> para analizar los tipos de alertas.</tr>
</table>

**Parte 4**
```python
#RETO 13 - Parte 4
"""
El programa deberá imprimir las fechas de alerta, el tipo de alerta y las variables asociadas.
"""

import json
from datetime import datetime

#Convertir UTC a fecha legible
def utc_to_date(utc_timestamp) -> str:
    return datetime.utcfromtimestamp(utc_timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

#Revisar alertas
def revisar_alertas(data):

    #Lista de los tipos dde alertas a buscar
    alertas = ["alertPrecip", "alertAlertas", "alertVelViento", "alertTmpMax", "alertTmpMin"]
    for alerta in alertas:
        for i in range(len(data['dt'])):
            alerta_value = data[alerta][str(i)]

            #Revisar si hay un alerta
            if alerta_value == "X":
                fecha = utc_to_date(data['date'][str(i)])

                #Alerta de precipitaciones
                if alerta == "alertPrecip":
                    descripcion = data['weather'][str(i)][0]['description'] if data['weather'][str(i)] else "No disponible"
                    print(f"Fecha: {fecha}, Alerta: {alerta}, Descripción: {descripcion}")

                #Alerta de la velocidad del viento
                elif alerta == "alertVelViento":
                    vel_viento = data['velViento'][str(i)]
                    print(f"Fecha: {fecha}, Alerta: {alerta}, Velocidad del viento: {vel_viento} m/s")
                
                #Alerta de temperatura máxima
                elif alerta == "alertTmpMax":
                    tmp_max = data['tmpMax'][str(i)]
                    print(f"Fecha: {fecha}, Alerta: {alerta}, Temperatura máxima: {tmp_max}°C")

                #Alerta de temperatura mínima
                elif alerta == "alertTmpMin":
                    tmp_min = data['tmpMin'][str(i)]
                    print(f"Fecha: {fecha}, Alerta: {alerta}, Temperatura mínima: {tmp_min}°C")
                
                #En caso de no ser ninguno de los campos presentados
                else:
                    continue

if __name__ == "__main__":
    #Cargar archivo JSON
    jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
    data = json.loads(jsonString)
    revisar_alertas(data)

# ! /\|=\/
```

<table cellspacing="1" bgcolor="" align="center">
  <tr bgcolor="#252582">
    <th><b>Reto 8 - Parte 5</b></th>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">A través de un programa conectese a al menos 3 API's , obtenga el JSON, imprimalo y extraiga los pares de llave : valor.</td>
  </tr>
  <tr bgcolor="#e4e4ed">
    <td style="color:#141414" align="center">Para el quinto punto del reto, se emplearon tres diferentes API's, en donde dos cuentan con variables para navegar.</td>
  </tr>
</table>

**Parte 5** 
```python
#RETO 13 - Parte 5
import requests

def bitcoin():
    #URL de la API
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    #Se realiza la solicitud GET a la API
    response = requests.get(url)

    if response.status_code == 200:

        #Se convierte la respuesta JSON a un diccionario de Python
        data = response.json()

        bpi = data['bpi']
    
        #Se imprimen los datos obtenidos
        print("Precio actual del Bitcoin:")
        for currency, info in bpi.items():
            code = info['code']
            rate = info['rate']
            description = info['description']
            print(f"{description} ({code}): {rate}")
    else:
        print(f"Error: {response.status_code}")
        return
    
def predicción_nombre():
    # URL de la API con el nombre que deseas analizar
    url = "https://api.nationalize.io"

    nombre : str = input("Ingrese el nombre a buscar: ").lower()
    variable = {'name': nombre}

    #Se realiza la solicitud GET a la API
    response = requests.get(url, params=variable)

    if response.status_code == 200:
        #Se convierten la respuesta JSON a un diccionario de Python
        data = response.json()
    
        #Se imprimen los datos obtenidos
        print("Predicciones de nacionalidad:")
        for prediccion in data['country']:
            codigo_pais = prediccion['country_id']
            probabilidad = prediccion['probability']
            print(f"País: {codigo_pais}, Probabilidad: {probabilidad:.2f}")
    else:
        print(f"Error: {response.status_code}")


    return
def universidades_por_nacion():
    url = "http://universities.hipolabs.com/search"

    #Se ingresa el nombre de la nación
    nacion : str = input("Ingrese el nombre de la nación: ").lower()
    variable = {'country': nacion}

    #Realizar la solicitud GET a la API
    response = requests.get(url, params=variable)

    if response.status_code == 200:

        #Se convierte la respuesta JSON a un diccionario de Python
        data = response.json()
    
        #Se imprimen los datos obtenidos
        for universidad in data:
            nombre = universidad.get('name', 'No name')
            pagina_web = universidad.get('web_pages', 'No web_pages')
            print(f"Nombre: {nombre}, Url de la página web: {pagina_web}")
        else:
            print(f"Error: {response.status_code}")
    return



if __name__ == "__main__":
    print("Valor del bitcoin en tiempo real en USD, GBR y EUR")
    bitcoin()
    print()
    print("Predicción de la nacionalidad de un a persona basado en su nombre.")
    predicción_nombre()
    print()
    print("Lista de universidades que hay en una nación.")
    universidades_por_nacion()
    
# ! /\|=\/
```

