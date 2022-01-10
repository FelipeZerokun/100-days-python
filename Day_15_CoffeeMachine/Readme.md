# 100 Days of Python
## Project 15:Coffee Maker Machine

This project is a real life application of a machine that will prepare coffee depending on what the user asks and the ingredients in the machine.

There is a PDF detailing the requirements that the machine must have.

There are many things your could must keep track off like ingredients, money, coffees in the menu, and other things. 
In this case, the data will be store as dictionaries within a dictionary. This is a great way to store unique elements that have common characteristics and are part of the same category. In the menu.py we have two dictionaries. One for coffees and one for resources. In the coffees dictionaries we have three dictionaries, three different types of coffees, each containing their respective ingredients. The resources dictionary has each ingredient necessary for making coffees and the quantity.
Here it can be seen more clearly why dictionaries are so good for data management.

What I did first is creating the operational mode for the machine. For this, I created a while loop that will contain three conditional IFs, for each operating mode of the machine. One for the coffee function, one for the report function and one to turn off the machine. If none of these conditions are meet, the machine will understand the user entered an invalid input and will ask again.

Then, I focused on getting the ingredients for each kind of coffee. If there were not enough ingredients in the machine, a message will be displayed for the user.
After that, I added a conditional for the money input from the user. Each coffee has a cost, and the user has to enter different kind of coins. I also created a function that will add the total of the coins inserted from the user. If the user did not inserted enough coins a message will be shown.
If there are enough ingredients and the money inserted by the user is enough, then the machine will prepare the Coffee. I will remove the ingredients user for the coffee from the total ingredientes in the machine, and I will add the money from the coffee will be added to the total money in the machine.

This is a good project to see how you can program a real life machine. Also, another look into how userful dictionaries can be for data storage and management.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 15: Máquina para preparar café.

Este proyecto es una aplicación de la vida real de una máquina que prepara café dependiendo de lo que el usuario pida y los ingredientes en la máquina.

Hay un archivo PDF detallando los requerimientos que la máquina debe tener.

Hay muchas cosas que se deben tener en cuenta como ingredientes, dinero, café en el menú, entre otras.

En este caso, los datos van a estar guardados en diccionarios dentro de un diccionario. Esta es una gran forma de guardar elementos únicos que tienen características comunes y son parte de la misma categoría. En el archivo menu.py hay dos diccionarios. Uno para los distintos cafés, y otro para los recursos. Dentro del diccionario de cafés, hay tres diccionarios, con tres tipos distintos cafés, y cada uno con sus respectivos ingredientes. El diccionario de recursos tiene cada ingrediente necesario para hacer cafés y las cantidades.
Aquí se puede observar más claramente por qué los diccionarios son tan buenos para manejo de datos.

Lo que hice primero fue crear el modo operacional para la máquina. Para esto, cree un buble que va a contener tres IFs condicionales, cada uno para un modo de operación de la máquina. Uno para la función de preparar cafés, uno para la función de reportes y uno para apagar la máquina. Si ninguna de estas condiciones se satisface, la máquina entenderá que el usuario se equivocó al ingresar su pedido, y volverá a pedirlo.

Luego, me enfoqué en obtener los ingredientes para cada tipo de café. Si no hay suficientes ingredientes en la máquina, se mostrará un mensaje para el usuario.
Después de eso, añadí un condicional para el ingreso de dinero del usuario. Cada café tiene un costo, y el usuario debe ingresar distinto tipo de monedas. También cree una función que sumará el total de las monedas insertadas por el usuario. Si el usuario no insertó suficientes monedas, se mostrará un mensaje.
Si hay suficientes ingredientes y el dinero insertado por el usuario es suficiente, entonces la máquina preparará el café. Voy a restar los ingredientes usados para el café de lo ingredientes totales, y añadiré el dinero del café al dinero total en la máquina.

Este es un buen proyecto para ver cómo se puede programa una máquina en la vida real. También, es otro ejemplo en qué tan útiles pueden ser los diccionarios para el almacenamiento y manejo de datos.
