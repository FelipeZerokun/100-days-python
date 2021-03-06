# 100 Days of Python
## Project 37: Habit Tracking APP

Here I made a small habit tracker that shows how many days in a row the user has done some activity, and how much activity per day. Here is an example of how:
![Pixela example](./pixela_image.png "Habit Tracking example")
For this I will be using the [Pixela](https://pixe.la/) website. Pixela has a Github you can check and support here: [Pixela's Github](https://github.com/a-know/Pixela)

I used other methods from HTTP requests. With these methods I can send, update and delete data from another program or website.

Following the "How do I use Pixela?" section, the first step is to create a username. Here you just need a username and a token which you can make yourself. The other parameters are agreeTermsOfService and notMinor, both must be Yes. In the response text should say "Success". You can see you user profile using this url with your username: http://pixe.la/@"username"

The second step is to create a graph definition. The endpoint for the graphs is the same as for the user creation but with /USERNAME/GRAPHS.
The parameters for the graph are:
* id: The graph ID
* name: The graph title
* unit: A text indicating the units. For this case units will be Km.
* type: The type of data in the graph
* color: The color of the squares. Here are used some japanese names for the colors.

Also, you need a Headers dictionary with your username Token, so the graph is created in YOUR Pixela's profile page. After running the code, you should see the response message with Sucess text. Now, you can browse https://pixe.la/v1/users/a-know/graphs/test-graph to see your graph and look for it in your Pixela's profile, like this:

![Graph example](./running_graph.png "Running Graph")

Now, for the graph to show some data we need to send some information. In another dictionary I put today's date and through an input how many kilometers I ran. Again, using the post method with a new URL, I sent a request. If the return message was Success, then the graph was updated with the new data. You can reload your graph in your profile to see the changes. You can use different dates to fill up the graph, and see how it works.

After this, I played a bit with the put method. This method is to update data that is already in the website. For example, if I wanted to change the units from my graph from Km to calories. Or if I wanted to change the amount of Kms on a day, etc.

The last thing to try was the Delete method. This method is used to erase any data that is already in the website.

In this project I practice with not only getting data from APIs but sending, updating and deleting data. With this I can understand a bit better how powerful APIs really are.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 D??as de Python
## Proyecto 37: APP de seguimiento de h??bitos

Aqu?? hice una peque??a app para seguimiento de h??bitos que muestra cu??ntos d??as seguidos el usuario ha hecho alguna actividad, y cu??nta actividad por d??a. Aqu?? hay un ejemplo de c??mo se ve la app:
![Ejemplo de Pixela](./pixela_image.png "App de seguimiento de h??bitos")
Para esto estar?? usando la p??gina web y API de [Pixela](https://pixe.la/). Pixela tiene una p??gina Github que puedes revisar y apoyar aqu??: [Github de Pixela](https://github.com/a-know/Pixela)

Utilic?? otros m??todos del m??dulo HTTP requests. Con estos m??todos puedo enviar, actualizar y borrar informaci??n de otro programa o p??gina web.

Siguiendo la secci??n de "How do I use Pixela?", el primer paso es crear un usuario. Aqu?? solo necesitas el nombre de usuario y un Token que puedes hacer t?? mismo. Los otros par??metros son agreeTermsOfService y notMinor, los cuales deben ser "yes". En el texto de response deber??a decir "Success". Ahora puedes observar tu perfil utilizando esta direcci??n web con tu nombre de usuario: http://pixe.la/@"username"

El segundo paso es crear un gr??fico definido. La direcci??n web para los gr??ficas es la misma que para la creaci??n de usuario pero con "/USERNAME/GRAPHS."
Los par??metros para el gr??fico son:
* id: La identificaci??n del gr??fico
* name: El t??tlulo del gr??fico
* unit: Un texto indicando las unidades. En esto caso ser??n Km
* type: El tipo de datos en el gr??fico
* color: El color de los cuadros. Aqu?? se utilizan algunas palabras en japon??s para los colores.

Tambi??n, se necesita un diccionario de Cabecear with tu Token de usuario, para que el gr??fico sea creado en un p??gina de Pixela. Despu??s de correr el c??digo, deber??as ver un mensaje de respuesta con el texto de "Success". Ahora puedes visitar https://pixe.la/v1/users/a-know/graphs/test-graph para ver tu gr??fico, y puedes verlo en tu perfil de Pixela as??:

![Ejemplo de gr??fico](./running_graph.png "Gr??fico de Correr")

Ahora, para que el gr??fico muestre alg??n tipo de datos, debemos enviar informaci??n. En otro diccionario pus?? la fecha de how, y a trav??s de un input, cu??ntos kilometros. Nuevamente, utilizando el m??todo post con un nuevo URL, env??a el request.Si el mensaje retornado fue Success, entonces el gr??fico fue actualizando con los nuevos datos. Puedes recargar tu gr??fico en tu perfil y ver los cambios. Puedes utilizar diferentes fechas para llenar el gr??fico con datos, y ver c??mo funciona.

Despu??s de esto, jugu?? un poco con el m??todo PUT. Este m??todo se utiliza para actualizar informaci??n que ya est?? en el sitio. Por ejemplo, si quisiera cambiar las unidades de mi gr??fico de Km a calorias. O si quisiera cambiar la cantidad de kilometros en un d??a, etc.

Lo ??ltimo que hice fue probar el m??todo Delete. Este m??todo es usado para borrar cualquier informaci??n que ya est?? en la p??gina web.

En este proyecto practiqu?? no s??lo con recibir datos de APIs, sino enviando, actualizando y borrando datos. Con esto puedo entender un poco m??s el potencial real de las APIs.
