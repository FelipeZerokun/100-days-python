# 100 Days of Python
## Project 16: Coffee Maker Machine with Classes

From here on, we will be doing the projects with OOP mentality.
This is the same project as day 16, but now I'll be creating classes with attributes and methods that serve the same purposes.

In the OOP practice folder, I practiced a bit with object creation, and how to use different methods.
I practiced with two popular turtle and pretty table. I will be using turtle module more in the next projects.

In the OOP Coffee machine, I created two new files. The coffee_maker.py and the money_machine.py.

The coffee_maker.py contains all the attributes and methods necessary for the coffee making function. The attributes are the ingredientes for the coffees. 
The methods are the following:
* Report: Returns the quantity of the total ingredients in the coffee machine.
* is_resource_sufficient: compares the total ingredients in the coffee machine with the ingredients needed to prepare a particular coffee. Returns True is there are enough ingredients for that coffee.
* make_coffee: If there are enough ingredients, this method subtracts the ingredients needed for the coffee from the total ingredients in the Machine.

The money_machine.py contains all the attributes and methods neccesary for the coins counting and money storage.
The methods are the following:
* report: Returns how much money is in the machine.
* process_coins: asks the user to insert the coins, and then adds each one for the total of money_received.
* make_payment: compares the money_received with the total cost of a coffee, if it is enough returns True, but if it is not prints a message and returns False.

The menu.py contains all the coffees with their respective ingredients needed to prepare each one. The menu class has the following methods:
* get_items: Prints all the items in the menu.
* find_drink: Search for a specific drink in the menu. If it does not find it, returns None.

With the classes and objects, it is much easier to organize different tasks withint a project. If I need to modify something, or add another method, I simply go to the class files and change whatever I need.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 D??as de Python
## Proyecto 16: M??quina de hacer caf?? con Clases

De aqu?? en adelante, voy a hacer los proyectos con metalidad de OOP (programaci??n orientada a objetos).
??ste es el mismo proyecto que el d??a 16, pero ahora voy a estar creando clases con atributos y m??todos que servir??n para el mismo prop??sito.

En la carpeta OOP practice, estaba practicando un poco con la creaci??n de objetos, y c??mo usar distintos m??todos.
Practiqu?? con dos m??dulos muy populares, turtle y prettytable. Estar?? usando el m??dulo turtle en futuros proyectos.

En la carpeta de OOP Coffee Machine, a??ad?? dos nuevos archivos. coffee_maker.py and the money_machine.py.

El archivo coffee_maker.py contiene todos los atributos y m??todos necesarios para la funci??n de preparar caf??. Los atributos son los ingredientes para los caf??s.
Los m??todos son los siguientes:
* Report: regresa la cantidad total de ingredientes en la m??quina de caf??.
* is_resource_sufficient: compara el total de ingredientes en la m??quina de caf?? con los ingredientes necesarios para preparar un caf?? en particular. Retorna True si hay suficientes ingredientes para dicho caf??.
* make_coffee: Si hay suficientes ingredientes, este m??todo restar?? los ingredientes necesarios para el caf?? de los ingredientes totales en la m??quina

El archivo money_machine.py contiene todos los atributos y m??todos necesarios para el conteo de monedas y almacenamiento de dinero.
Los m??todos son los siguientes:
* report: Retorna cu??nto dinero hay en la m??quina.
* process_coins: Pide al usuario insertar las monedas, las suma y a??ade el total a money_received.
* make_payment: compara el dinero en money_received con el costo total del caf??, si es suficiente retorna True, pero si no lo es muestra un mensaje y retorna False.

El archivo  menu.py contiene todos los caf??s con los respectivos ingredientes necesarios para preparar cada uno. Le case men?? tiene los siguientes m??todos:
* get_items: Imprime todos los objetos dentro del men??.
* find_drink: Busca una bebida espec??fica dentro del men??. Si no la encuentra, retorna None.

Con las clases y los objetos, es mucho m??s f??cil organizar distintas tareas dentro de un proyecto. Si necesito modificar algo, o a??adir alg??n otro m??todo, simplemente voy a los archivos con la clase y cambio lo que necesite.
