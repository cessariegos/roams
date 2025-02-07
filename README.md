# API de Generación de Texto.

## Descripción
La función de esta API es generar texto a partir de un prompt utilizando un modelo de inteligencia artificial preentrenado de Hugging Face.

## Instrucciones para instalar las dependencias
El primer requisito sería tener instalado Python.
El segundo requisito sería instalar las librerias necesarias mediante el siguiente comando:

    pip install flask transformers torch

## Instrucciones para ejecutar la API
Ejecutar el programa mediante el siguiente comando:

    python main.py

Mediante la pagina Postman o por consola, enviar un prompt a 'http://127.0.0.1:5000/texto' junto con los siguientes parámetros para generar un texto:

    {
	"prompt": "(string no vacío)",
    "max_length": (número entero mayor que 0 y menor o igual que 1000),
    "temperature": (número decimal entre 0.2 y 1.2),
    "top_p": (número decimal entre 0.4 y 0.9)
    }

Para ver el historial de textos generados dirigirse a 'http://127.0.0.1:5000/solicitudes'

## Ejemplo de solicitudes
Ejemplo 1:
Enviar mediante Postman el siguiente código a 'http://127.0.0.1:5000/texto'
{
	"prompt": "¿Cómo puedo ir desde Francia hasta China?",
    "max_length": 200,
    "temperature": 0.9,
    "top_p": 0.8
}

Resultado obtenido:
{
    "Texto:": "¿Cómo puedo ir desde Francia hasta China? Con un coche de alquiler puedes ir desde Francia a China. Las opciones de viaje más comunes son:\nLas opciones de viaje más populares son \"Viajar a Francia\" y \"Vuelos a Francia\". Las aerolíneas más populares son Lufthansa, Air France, Air China y United Airlines.\nEn el itinerario de la ruta París - China puedes encontrar los mejores precios de vuelos a China. En la parte superior hay una buena cantidad de ofertas de vuelos a China.\nPuedes encontrar más información sobre el libro con el ISBN 8493087073 en algunos de los sitios indicados abajo. A través de la página de búsqueda de fuentes puedes encontrar también información sobre otros ISBN. Para modificar el contenido de esta página usa este enlace.\nEl mapa topográfico de Ravensbronn y sus alrededores"
}

Ejemplo 2:
Enviar el siguiente prompt:
{
	"prompt": "¿Para que sirve un tornillo?",
    "max_length": 150,
    "temperature": 1,
    "top_p": 0.7
}

Resultado obtenido:
{
    "Texto:": "¿Para que sirve un tornillo? - Wikipedia, la enciclopedia libre El tornillo es un elemento metálico, generalmente de acero, que se usa para unir un elemento metálico al metal o a un objeto sólido.\nEl tornillo es un elemento metálico, generalmente de acero, que se usa para unir un elemento metálico al metal o a un objeto sólido.\nLa soldadura se realiza con la punta de los dedos, a diferencia de la soldadura por arco, la soldadura es un método de trabajo manual.\nLa soldadura es una técnica de soldar a alta temperatura y baja presión, que se realiza mediante el uso de un clavo, una punta de"
}

Para ver el historial de textos generados, en http://127.0.0.1:5000/solicitudes se muestra:
{
  "Solicitudes": [
    {
      "id": 2,
      "prompt": "¿Para que sirve un tornillo?",
      "response": "¿Para que sirve un tornillo? - Wikipedia, la enciclopedia libre El tornillo es un elemento metálico, generalmente de acero, que se usa para unir un elemento metálico al metal o a un objeto sólido.\nEl tornillo es un elemento metálico, generalmente de acero, que se usa para unir un elemento metálico al metal o a un objeto sólido.\nLa soldadura se realiza con la punta de los dedos, a diferencia de la soldadura por arco, la soldadura es un método de trabajo manual.\nLa soldadura es una técnica de soldar a alta temperatura y baja presión, que se realiza mediante el uso de un clavo, una punta de"
    },
    {
      "id": 1,
      "prompt": "¿Cómo puedo ir desde Francia hasta China?",
      "response": "¿Cómo puedo ir desde Francia hasta China? Con un coche de alquiler puedes ir desde Francia a China. Las opciones de viaje más comunes son:\nLas opciones de viaje más populares son \"Viajar a Francia\" y \"Vuelos a Francia\". Las aerolíneas más populares son Lufthansa, Air France, Air China y United Airlines.\nEn el itinerario de la ruta París - China puedes encontrar los mejores precios de vuelos a China. En la parte superior hay una buena cantidad de ofertas de vuelos a China.\nPuedes encontrar más información sobre el libro con el ISBN 8493087073 en algunos de los sitios indicados abajo. A través de la página de búsqueda de fuentes puedes encontrar también información sobre otros ISBN. Para modificar el contenido de esta página usa este enlace.\nEl mapa topográfico de Ravensbronn y sus alrededores"
    }
  ]
}