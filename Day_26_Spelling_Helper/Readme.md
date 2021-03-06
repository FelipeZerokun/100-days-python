# 100 Days of Python
## Project 26: Spelling helper

This project is a tool for spelling. The user enters a Name, and using the [nato phonetic alphabet](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet), the program will spell that name letter by letter.

In this project I will practising a bit dictionary and list comprehension. 
This is really useful for when we need to use specific data in a list or a dictionary. For example, in the previous project we needed only the squirrels with specific fur color. With a condictional, we only took the columns that met that condition.

Dictonary comprehension: new_dict = {new_key:new_value for item in list}

List comprehension: new_list = [new_item for item in list if test]

Using read_csv from Pandas library, I imported a csv file with the nato alphabet as a DataFrame. Then I used dictionary comprehension to convert the data in this DataFrame to a list, where the keys will be the letters in the alphabet and the values will be the phonetic equivalent to each letter. 

So far, when an error ocurred during the code execution, we let the debugger catch it but this would stop the program. Sometimes, this error is not our fault. For example, in the calculator project we ask the user to enter a number, but the user can make a mistake and enter a letter. If I try to convert a letter to a integer number, there will be an error and the program will end. We can avoid this by using [Exception Handling](https://en.wikipedia.org/wiki/Exception_handling). With the keyword Try we can try lines of codes that may incur into an error, and print a message instead of completely stopping the code.

We will start using Exception handling to avoid ending the code abruptly, and give the user another chance to enter the correct information. In this case, the user must enter only alphabetic characters. If the user enters a number, with Try I will catch that error, and print a message for the user. Inside of a While loop, I will keep looping until the user enters a valid input.

I could use a for loop to check letter by letter the name the user entered as input, but with list comprehension I can do the same in a simple line of code.
If there were no errors in the execution of this code, the program will print the nato phonetic alphabet equivalent to the name the user entered.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 D??as de Python
## Proyecto 26: Ayudante para deletreo.

Este proyecto es una herramienta para deletrear. El usuario ingresa un nombre, y utilizando el [alfabeto radiof??nico](https://es.wikipedia.org/wiki/Alfabeto_radiof%C3%B3nico), el programa deletrear?? ese nombre letra por letra.

En este proyecto practicar?? un poco con la comprensi??n de dictionarios y la comprensi??n de listas.
Esto es realmente ??til cuando necesitamos utilizar datos espec??ficos en una lista o dictionario. Por ejemple, en el proyecto anterior s??lo necesit??bamos las ardillas con un color de pelaje espec??fico. Con un condicional, tomamos s??lo las columnas que cumpl??an dicha condici??n.


Comprensi??n de diccionarios: new_dict = {new_key:new_value for item in list}

Comprensi??n de listas: new_list = [new_item for item in list if test]

Utilizando el m??todo read_csv de la libreria Pandas, import?? un archivo csv con el alfabeto radiof??nico como un DataFrame. Luego utilic?? la comprensi??n de Diccionarios para convertir los datos en esta lista, d??nde las "key" ser??n las letras y los "values" ser?? el equivalente fon??tico de cada letra.

Hasta ahora, cuando ocurr??a un error durante la ejecucci??n del c??digo, dej??bamos que el debugger lo atrapara pero esto hac??a que el programa se detuviera. A veces, este error no era nuestra culpa. Por ejemplo, en el proyecto de la calculadora, le pedimos al usuario ingresar un n??mero, pero el usuario puede ingresar una letra por error. Si intento convertir una letra en un n??mero entero, ocurrir?? un error y el programa terminar??. Podemos evitar esto usando el [Manejo de Excepciones](https://es.wikipedia.org/wiki/Manejo_de_excepciones). Utilizando la palabra clave Try, podemos intentar correr l??neas de c??digo que pueden incurrir en un error, e imprimir un mensaje en lugar de que el programa se detenga por completo.

Empezaremos a utilizar el Manejo de excepciones para evitar terminar la ejecucci??n del c??digo de forma abrupta, y darle al usuario otra oportunidad de ingresar la informaci??n correcta. En este caso, el usuario debe ingresar ??nicamente caracteres alfab??ticos. Si el usuario ingresa un n??mero, Try atrapar?? el error e imprimir?? un mensaje para el usuario. Dentro de un bucle While, seguir?? repitiendo hasta que el usuario ingrese un valor correcto.

Podr??a utilizar un bucle FOR para revisar letra por letra lo que el usuario ingres??, pero utilizar?? compresi??n de Listas para hacer lo mismo en una simple l??nea de c??digo.
Si no hubieron errores en la ejecucci??n del c??digo, el programa imprimir?? el equivalente en el alfabeto radiofon??tico de lo que el usuario ingres??.
