"""
    # /*
#  * Llamar a una API es una de las tareas más comunes en programación.
#  *
#  * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#  * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
#  *
#  * Aquí tienes un listado de posibles APIs: 
#  * https://github.com/public-apis/public-apis
#  */
"""

import requests  # Importamos la biblioteca 'requests' para hacer la llamada a la API

# Definimos la URL de la API que vamos a llamar
url = 'https://api.chucknorris.io/jokes/random'

# Realizamos la llamada HTTP utilizando el método 'get' de 'requests'
response = requests.get(url)

# Verificamos el código de estado de la respuesta para asegurarnos de que la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()  # Convertimos la respuesta en formato JSON a un diccionario de Python
    joke = data['value']  # Extraemos el chiste del diccionario
    print('Chiste de Chuck Norris:', joke)  # Mostramos el chiste en la terminal
else:
    print('Error al realizar la solicitud:', response.status_code)  # Mostramos un mensaje de error si la solicitud falla
