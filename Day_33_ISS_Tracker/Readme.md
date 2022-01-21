# 100 Days of Python
## Project 33: ISS Tracker

This project will track the ISS [(International Space Station)](https://www.nasa.gov/mission_pages/station/main/index.html) via their API. If the Space Station is close to our position, and it is dark, the program will send an email telling you to watch up in the sky to see the Space Station.

An API [(Application Programming Interface)](https://en.wikipedia.org/wiki/API) is an interface that allows two applications to communicate with each other. This means that any application could receive or send data through this connection.

There are several web pages or companies that offer connectivity to their APIs, free or paid, and they send you different kind of data. In this case, I will be requesting data to the ISS asking for their coordinates. 

To do this, the requests library is needed. Also, the URL from the website we want to get the data is necessary. Here is the [API](http://api.open-notify.org/iss-now.json) for the ISS position.
I made an infinite loop that will check the ISS position every minute. 

Now, to check at what time is the sunrise and sunset of where I am, I used another API from a page called [sunrise-sunset](https://www.sunrise-and-sunset.com/en). Here you can see the estimated sunrise and sunset times of different cities. To use this site APIs I need to provide the latitude and longitude of the city I want to check. In [latlong.net](https://www.latlong.net/) website I can check the coordinates of any place in the world. I saved the coordinates in a dictionary called parameters, which I used for the Sunrise Sunset API.

Now with both conditions, I just need to compare ISS coordinates with my coordinates, and if the time is past sunset and before sunrise, the app will send an email using the SMTP method.

This project is a really good introduction to APIs, which can be a powerful tool to get data from other sites.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 33: Seguidor de la EEI

Este proyecto seguirá la trayectoria de la EEI [(Estación Espacial Internacional)](https://es.wikipedia.org/wiki/Estaci%C3%B3n_Espacial_Internacional) a través de su API. Si la estación espacial está cerca de nuestra posición, y es de noche, el programa enviará un correo diciendo que mires al cielo para ver la estación espacial.

Una API [(Interfaz de programación para aplicaciones)](https://es.wikipedia.org/wiki/Interfaz_de_programaci%C3%B3n_de_aplicaciones) es una interfez que permite a dos aplicaciones comunicarse entre ellas. Esto significa que cualquier aplicación puede recibir o enviar datos a través de esta conexión.

Hay varias páginas web o compañías que ofrecen conectividad a sus APIs, gratis o pagada, y pueden enviarte diferente tipo de data. En este caso, estaré solicitando datos a la EEI para conocer sus coordenadas.

Para lograr esto, la librería requests es necesaria. También, es necesaria la dirreción del sitio web de dónde se quiere obtener la información. Aquí está el [API](http://api.open-notify.org/iss-now.json) para la ubicación de la EEI.
Hice un bucle infinito que revisará la posición de la Estación espacial cada minuto.

Ahora, para revisar cuándo es la salida y la puesta del sol en dónde esto, utilicé otra API de una pagina llamada [sunrise-sunset](https://www.sunrise-and-sunset.com/en). Aquí se pueden ver las horas estimadas de salida del sol y puesta del sol de distintas ciudades. Para utilizar este API se necesita proveer la longitud y latitud de la ciudad que quiero revisar. En la página web [latlong.net](https://www.latlong.net/) se puede revisar las coordenadas de cualquier lugar en el mundo. Guardé estas coordinadas en un diccionario llamado parameters, el cuál utilicé para el API de Sunset Sunrise.

Ahora con las dos condiciones, sólo comparé las coordenadas de la EEI con mis coordenadas, y si la hora es después de la puesta del sol y antes de la salida del sol, la app enviará un correo utilizando el método SMTP.

Este proyecto es una buena introducción a las APIs, las que pueden ser herramientas muy útiles para obtener información de otros sitios.
