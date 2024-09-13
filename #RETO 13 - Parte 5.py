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