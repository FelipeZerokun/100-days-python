# 100 Days of Python
## Project 36: Stock Trading news app

On this project I made a program that checks the stocks value of certain company, compares the price with the previous day price, and if the price has gone up or down by 5% or more, the program will look for news of that company and send a message to the user's phone with all this information.

I used three APIs this time. [Twilio](https://www.twilio.com/), which we already know from previous projects, [Alphavantage](https://www.alphavantage.co/) which has stock APIS and the [NewsApi](https://newsapi.org), which has APIs for all kind of news.

The first thing I did was to get some stocks data from the Tesla company. What we need for this API is the key, the company stock name and the url. The using the request's method GET, I can get data from that company's stocks. 
Like other pages, Alphavantage has different APIs for different needs. [Here](https://www.alphavantage.co/documentation/) is the documentation for their APIs. I used Time series (Daily) because I want the closing prices of the stocks from yesterday and the day before yesterday.

After getting those values, I have to check if there is a positive or negative difference of the 5%. If this condition is met, I could simple send a message to the user with this information. However, I will search for news of the company and attach it to the message.

To get news from the NewsApi I just need the API key, the url and the company's name. Notice the company's name and their stock's name is not the same. Using these parameters and the requests GET method, I got a file with different news as a json file. I sliced the file to get only the first three articles. Then, I added them in a list as strings. 

Finally, I sent an SMS to the user for each article in my list with the Twilio API.

Here I used another two interesting APIs that you may find useful. If you are into stock's investment, the stocks API can be incredibly useful.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 100 D??as de Python
## Proyecto 36: app de noticias sobre acciones

En este proyecto hice un programa que revisa el precio de las acciones de cierta compa????a, los compara con el precio del d??a anterior, y si el precio ha subido o bajado en un 5% o m??s, el programa buscar?? noticias sobre esa compa????a y enviar?? un mensaje al usuario con toda esta informaci??n.

Utilic?? tres APIs esta vez. [Twilio](https://www.twilio.com/), la cu??l ya hemos usado en proyectos anteriores, [Alphavantage](https://www.alphavantage.co/) La cual tiene APIs para acciones, y [NewsApi](https://newsapi.org), la cu??l tiene APIs para todo tipo de noticias.

Lo primero que hice fue obtener datos sobre las acciones de la compa????a Tesla. Lo que necesito para esta API es la llave, el nombre de las acciones de la compa????a y la direcci??n url. Utilizando el m??todo GEt de la m??dulo requests, obtuve los datos de las acciones de la compa????a.
C??mo otras p??ginas, Alphavantage tiene distintos APIs para distintas necesidades. [Aqu??](https://www.alphavantage.co/documentation/) est?? la documentaci??n para sus APIs. Yo us?? Time Series (Daily) porque necesito los precios de cierre de las acciones del d??a de ayer, y del d??a antes de ayer.

Despu??s de obtener esos valores, tuve que revisar si la differencia positiva o negativa era del 5%. Si se cumpl??a esta condici??n, podr??a simplemente haber enviado un mensaje al usuario con esta informaci??n. Sin embargo, busqu?? informaci??n sobre la compa????a y la a??ad?? al mensaje

Para obtener noticias de la pagina NewsApi, s??lo se necesita la llave API, la direcci??n URL y el nombre de la compa????a. Vale la pena notar que el nombre de la compa????a y el nombre usado para sus acciones no es el mismo. Utilizando estos par??metros y el m??todo GET de requests, obtuve un archivo con diferentes noticias en un formato Json. Separ?? el archivo para tener s??lo los tres primeros art??culos. Luego, los a??ad?? a una lista como cadenas de caracteres.

Finalmente, env??e un SMS al usuario con cada art??culo en mi lista utilizando la API de Twilio.

Aqu?? utilic?? otros dos APIs interesantes que puedes encontrar ??tiles. Si est??s invirtiendo en la bolsa de acciones, la API de acciones te resultar?? incre??blemente ??til.
