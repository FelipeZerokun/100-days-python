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

# 100 Días de Python
## Proyecto 26: Ayudante para deletreo.

Este proyecto es una herramienta para deletrear. El usuario ingresa un nombre, y utilizando el [alfabeto radiofónico](https://es.wikipedia.org/wiki/Alfabeto_radiof%C3%B3nico), el programa deletreará ese nombre letra por letra.

En este proyecto practicaré un poco con la comprensión de dictionarios y la comprensión de listas.
Esto es realmente útil cuando necesitamos utilizar datos específicos en una lista o dictionario. Por ejemple, en el proyecto anterior sólo necesitábamos las ardillas con un color de pelaje específico. Con un condicional, tomamos sólo las columnas que cumplían dicha condición.


Comprensión de diccionarios: new_dict = {new_key:new_value for item in list}

Comprensión de listas: new_list = [new_item for item in list if test]

Utilizando el método read_csv de la libreria Pandas, importé un archivo csv con el alfabeto radiofónico como un DataFrame. Luego utilicé la comprensión de Diccionarios para convertir los datos en esta lista, dónde las "key" serán las letras y los "values" será el equivalente fonético de cada letra.

Hasta ahora, cuando ocurría un error durante la ejecucción del código, dejábamos que el debugger lo atrapara pero esto hacía que el programa se detuviera. A veces, este error no era nuestra culpa. Por ejemplo, en el proyecto de la calculadora, le pedimos al usuario ingresar un número, pero el usuario puede ingresar una letra por error. Si intento convertir una letra en un número entero, ocurrirá un error y el programa terminará. Podemos evitar esto usando el [Manejo de Excepciones](https://es.wikipedia.org/wiki/Manejo_de_excepciones). Utilizando la palabra clave Try, podemos intentar correr líneas de código que pueden incurrir en un error, e imprimir un mensaje en lugar de que el programa se detenga por completo.

Empezaremos a utilizar el Manejo de excepciones para evitar terminar la ejecucción del código de forma abrupta, y darle al usuario otra oportunidad de ingresar la información correcta. En este caso, el usuario debe ingresar únicamente caracteres alfabéticos. Si el usuario ingresa un número, Try atrapará el error e imprimirá un mensaje para el usuario. Dentro de un bucle While, seguirá repitiendo hasta que el usuario ingrese un valor correcto.

Podría utilizar un bucle FOR para revisar letra por letra lo que el usuario ingresó, pero utilizaré compresión de Listas para hacer lo mismo en una simple línea de código.
Si no hubieron errores en la ejecucción del código, el programa imprimirá el equivalente en el alfabeto radiofonético de lo que el usuario ingresó.
