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

# 100 D??as de Python
## Proyecto 15: M??quina para preparar caf??.

Este proyecto es una aplicaci??n de la vida real de una m??quina que prepara caf?? dependiendo de lo que el usuario pida y los ingredientes en la m??quina.

Hay un archivo PDF detallando los requerimientos que la m??quina debe tener.

Hay muchas cosas que se deben tener en cuenta como ingredientes, dinero, caf?? en el men??, entre otras.

En este caso, los datos van a estar guardados en diccionarios dentro de un diccionario. Esta es una gran forma de guardar elementos ??nicos que tienen caracter??sticas comunes y son parte de la misma categor??a. En el archivo menu.py hay dos diccionarios. Uno para los distintos caf??s, y otro para los recursos. Dentro del diccionario de caf??s, hay tres diccionarios, con tres tipos distintos caf??s, y cada uno con sus respectivos ingredientes. El diccionario de recursos tiene cada ingrediente necesario para hacer caf??s y las cantidades.
Aqu?? se puede observar m??s claramente por qu?? los diccionarios son tan buenos para manejo de datos.

Lo que hice primero fue crear el modo operacional para la m??quina. Para esto, cree un buble que va a contener tres IFs condicionales, cada uno para un modo de operaci??n de la m??quina. Uno para la funci??n de preparar caf??s, uno para la funci??n de reportes y uno para apagar la m??quina. Si ninguna de estas condiciones se satisface, la m??quina entender?? que el usuario se equivoc?? al ingresar su pedido, y volver?? a pedirlo.

Luego, me enfoqu?? en obtener los ingredientes para cada tipo de caf??. Si no hay suficientes ingredientes en la m??quina, se mostrar?? un mensaje para el usuario.
Despu??s de eso, a??ad?? un condicional para el ingreso de dinero del usuario. Cada caf?? tiene un costo, y el usuario debe ingresar distinto tipo de monedas. Tambi??n cree una funci??n que sumar?? el total de las monedas insertadas por el usuario. Si el usuario no insert?? suficientes monedas, se mostrar?? un mensaje.
Si hay suficientes ingredientes y el dinero insertado por el usuario es suficiente, entonces la m??quina preparar?? el caf??. Voy a restar los ingredientes usados para el caf?? de lo ingredientes totales, y a??adir?? el dinero del caf?? al dinero total en la m??quina.

Este es un buen proyecto para ver c??mo se puede programa una m??quina en la vida real. Tambi??n, es otro ejemplo en qu?? tan ??tiles pueden ser los diccionarios para el almacenamiento y manejo de datos.
