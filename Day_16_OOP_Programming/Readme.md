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

# 100 Días de Python
## Proyecto 16: Máquina de hacer café con Clases

De aquí en adelante, voy a hacer los proyectos con metalidad de OOP (programación orientada a objetos).
Éste es el mismo proyecto que el día 16, pero ahora voy a estar creando clases con atributos y métodos que servirán para el mismo propósito.

En la carpeta OOP practice, estaba practicando un poco con la creación de objetos, y cómo usar distintos métodos.
Practiqué con dos módulos muy populares, turtle y prettytable. Estaré usando el módulo turtle en futuros proyectos.

En la carpeta de OOP Coffee Machine, añadí dos nuevos archivos. coffee_maker.py and the money_machine.py.

El archivo coffee_maker.py contiene todos los atributos y métodos necesarios para la función de preparar café. Los atributos son los ingredientes para los cafés.
Los métodos son los siguientes:
* Report: regresa la cantidad total de ingredientes en la máquina de café.
* is_resource_sufficient: compara el total de ingredientes en la máquina de café con los ingredientes necesarios para preparar un café en particular. Retorna True si hay suficientes ingredientes para dicho café.
* make_coffee: Si hay suficientes ingredientes, este método restará los ingredientes necesarios para el café de los ingredientes totales en la máquina

El archivo money_machine.py contiene todos los atributos y métodos necesarios para el conteo de monedas y almacenamiento de dinero.
Los métodos son los siguientes:
* report: Retorna cuánto dinero hay en la máquina.
* process_coins: Pide al usuario insertar las monedas, las suma y añade el total a money_received.
* make_payment: compara el dinero en money_received con el costo total del café, si es suficiente retorna True, pero si no lo es muestra un mensaje y retorna False.

El archivo  menu.py contiene todos los cafés con los respectivos ingredientes necesarios para preparar cada uno. Le case menú tiene los siguientes métodos:
* get_items: Imprime todos los objetos dentro del menú.
* find_drink: Busca una bebida específica dentro del menú. Si no la encuentra, retorna None.

Con las clases y los objetos, es mucho más fácil organizar distintas tareas dentro de un proyecto. Si necesito modificar algo, o añadir algún otro método, simplemente voy a los archivos con la clase y cambio lo que necesite.
