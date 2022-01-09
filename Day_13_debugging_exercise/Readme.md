# 100 Days of Python
## Project 13: Debugging Exercise

This is not a project itself, but rather a debuggin practice.

In this project are three flies, each has a small code that has one problem. The goal of this project is to review each code and find the bug preventing it from working like intended.

In the first file, debug_01.py, the code should take a integer number as input and return a text saying if the number is even or odd.
The problem with the code is that it tries to compare two values with the assignation sign ("=" is for assignation, "==" is for comparison). This is a SyntaxError.
So, instead of this -> if number % 2 = 0:, you should write this -> if number % 2 == 0:

If you run this file with a debugger, it will show a message like this: "SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?"
Also, in Pycharm and other IDEs, even before you run the code the IDE will mark the mistake with a red underline.

For the second file, debug_02.py, the code will take a year from the user, and return in text if it is a leap year or not.
Here you will not see the error before running like in the exercise number one, because there is no actual error in the code. But if you try to run the code the following message will be shown: "TypeError: not all arguments converted during string formatting". The TypeError means that we are trying to associate two different types of variables. In this case, strings with integers. Remember that the "input" method give us a variable in the form of string. So, if we want to use it as a integer, float or any kinf of number we must convert it first. year = int(input("Which year do you want to check?")) the int method here should do the trick.

For the third file, debug_03.py, the code is for the FizzBuzz game. The code will show the numbers from 1 to 100, and every multiple of 3 should be replaced with the word "Fizz", every multiple of 5 should be replace with the word "Buzz". If the number is both multiple of 3 and 5, it should be replaced with the word "FizzBuzz".
If you try and run the code as it is, there should be no problem at all. However, what is shown is not what you would expect from the code. The first thing you may notice is that the conditional for FizzBuzz says IF the number is multiple of 3 OR 5. That should not be the case, instead it should be AND. The other thing here you can notice is that there are 3 individual conditional IFs, however they should all be linked. So, using ELIF insteaf of the second and third IFs should solve everything.

This last example is a really good practice of following the code line by line to see if what you are expecting really happens in the code. Since there are no errors here, it can be misleading, but reviewing the code line by line is a great way to find what is lacking in the code.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 13: Ejercicio de depuración.

Éste no es un proyecto en sí, sino una práctica de depuración.

En este proyecto hay tres archivos, cada uno tiene un pequeño código con un problema. El objetivo de este proyecto es revisar cada código y encontrar el error que evita que el código funcione como debería.

En el primer archivo, debug_01.py, el código debería tomar un número entero y retornar un texto diciendo si el número es par o es impar.
El problema en el código es que intenta comparar dos valores con un signo de asignación ("=" es para asignación, "==" es para comparasión). Este es un error de sintaxis (SyntaxError).
Así que, en lugar de esto -> if number % 2 = 0:, debería estar esto -> if number % 2 == 0:.

Si corres este archivo con un depurador, va a mostrar un mensaje como: "Error de sintaxis: no se puede asignar a la expresión aquí. ¿Tal vez quiso decir '==' en lugar de '='?"
También, en Pycharm y otros IDEs, incluso antes de corre el código el IDE va a marcar el error subrayado con una línea roja.

Para el segundo archivo, debug_02.py, el código va a tomar un año ingresado por el usuario, y retornará un texto diciendo si es año bisiesto o no lo es.
Aquí, a diferencia del primer ejercicio, no se verá el error hasta correr el código con el depurador, porque no hay un error en sí en el código. Pero si intentas correr el código un mensaje como el siguiente aparecerá: "Error de tipo: no todos los argumentos se convirtieron durante el formateo de cadena de caracteres". El error de tipo significa que estamos intentando asociar dos variables con distintos tipos. En este caso, cadena de caracteres con números enteros. Recuerden que el método "input" nos retorna una variable del tipo "string" o cadena de caracteres. Así que si queremos usar esa variable como un número entero, flotando o cualquier otro número, primero debemos convertirla.
year = int(input("Which year do you want to check?")). El método int debería hacer el truco en este caso.

Para el tercer archivo, debug_03.py, el código es para el juego FizzBuzz. El código va a mostrar los números del 1 al 100, y cada número múltiplo de 3 debería ser reemplazado con la palabra "Fizz" y cada número múltiplo de 5 debería ser reemplazado con la palabra "Buzz". Si el número es tanto múltiplo de 3 como de 5, el número debería ser reemplazado con la palabra "FizzBuzz".
Si se intenta correr el código tal como está, no debería haber ningún problema. Sin embargo, lo que nos muestra no es lo que esperamos del programa. La primera cosa que se puede observar en el código es que el condicionar para "FizzBuzz" toma en cuenta si el número es múltiplo de 3 "O" múltiplo de 5. Ese no debería ser el caso, en cambio debería ser "Y". La otra cosa que uno se puede dar cuenta es que hay 3 IFs condicionales individuales, sin embargo debería estar todos vinculados. Así que, utilizando ELIF en lugar del segundo y tercer IF debería solucionar todo.

Este último ejemplo es una práctica realmente buena para seguir el código linea por linea y ver si realmente está sucediendo lo que uno esperaría que sucediera. Debido a que no hay errores aquí, puede resultar algo confuso, pero revisar el código linea por linea es una gran forma de encontrar qué es lo que le está faltando al código.
