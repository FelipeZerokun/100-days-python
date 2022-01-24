# 100 Days of Python
## Project 35: Weather Alert APP

This is a small project that you could find very useful.

Using an API from [OpenWeatherMaps.org](https://openweathermap.org/) and an API from [Twilio](https://www.twilio.com/) I made an app that will check the climate for the next 12 hours of certain location. The app will send a SMS to the user cellphone if it will rain in the next 12 hours.

There are several APIs in the OpenWeatherMaps website, but I will be using the [Current Weather API](https://openweathermap.org/current). The parameters for this API are the following:
* lat, lon: Geographical coordinates
* appid: You API key. Unique for each user.
* mode: the response format. Could be xml, html or json. Default format is json.
* units: standard, metric or imperial units.
* lang: for output language.
Again, I used the [LatLong.net](https://www.latlong.net/) website to get my coordinates.

For the Twilio API, you need to create an account and get a free trial number. [Here](https://www.twilio.com/docs/sms/quickstart/python) are some example of how to user the Twilio Client method to send SMS.

With the response method, I got a json file from the Weather API. Then, I grabbed the hourly data from that file. Then, I sliced the data for the first 12 hours. 
With a FOR loop, I checked every hourly data to see if there was rain in any of them. There are several codes for the weather, [here](https://openweathermap.org/weather-conditions) you can check them. For this case, basically anythin under the code 700 means rain or snow. So, if the code for any of those 12 hours is below 700, a variable called will_rain will become True.

Finally, if the will_rain variable is True, following the example from the Twilio page, I sent an SMS to my cellphone saying that I should bring an umbrella.

It is really interesting to be able to connect with other APPS and pages to get information, and for me it was even more interesting to be able to send myself SMS. I really found this really useful, specially when cellphones are such a useful tool for people.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 35: APP de alerta del clima

Este es un pequeño proyecto que encontrarás muy útil

Utilizando una API de [OpenWeatherMaps.org](https://openweathermap.org/) y una API de [Twilio](https://www.twilio.com/), hice una app que revisará el clima de las siguientes 12 horas de cierta ubicación. La app enviará un SMS al celular del usuario indicando si va a llover en las próximas 12 horas.

Hay varios APIs en la página web de OpenWeatherMaps, peor estaremos utilizando [Current Weather API](https://openweathermap.org/current). Los parámetros necesarios para esta API son los siguientes:
* lat, lon: Coordenadas geográficas
* appid: Tu llave API. Única para cada usuario.
* mode: El formato de la respuesta. Puede ser xml, html o json. El formato por defecto es json.
* units: Unidades estándar, métricas o imperiales.
* lang: para el lenguaje de salida.
Nuevamente, utilicé la página web [LatLong.net](https://www.latlong.net/) para obtener mis coordenadas.

Para la API de Twilio, necesitas crear una cuenta y obtener un número de prueba. [Aquí](https://www.twilio.com/docs/sms/quickstart/python) hay algunos ejemplo de cómo utilizar el método Client para enviar SMS.

Con el método response, obtuve un archivo json de la API de Weather. Luego, tomé los datos por hora de ese archivo. Luego, corté los datos para las primeras 12 horas.
Con un bucle FOR, revisé los datos de cada hora para ver si había lluvia en alguno de ellos. Hay varios códigos para el clima, [aquí](https://openweathermap.org/weather-conditions) puedes revisarlos todos. En este caso, básicamente cualquier código por debajo de 700 indica lluvia o nieve. Así que, si el código de cualquiera de esas 12 horas está por debajo de 700, una variable llamada will_rain será True.

Finalmente, si la variable will_rain es True, siguiendo el ejemplo de la página de Twilio, envié un SMS a mi celular diciendo que debería llevar un paraguas.

Es muy interesante poder conectarse con otras apps y páginas para obtener información, y para mi fue aún más interesante poder enviarme un SMS a mi mismo. Realmente encontré esto muy útil, especialmente cuando los celulares son herramientas tan útiles para las personas.
