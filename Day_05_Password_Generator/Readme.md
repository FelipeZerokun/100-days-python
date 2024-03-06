# 100 Days of Python
## Project 5: Random Password Generator.

This is a really useful project where the users can generate random passwords with the number of letters, numbers and symbols of their choice.
There were two difficulties on this project in the course. 
- Easy:The position of the characters would not be randomized (first will be letters, then numbers and then symbols) 
- Hard: Everything in the password would be randomized.

First of all, I created three lists, containing all the letters, all the numbers and all the symbols. From this list is where the program will randomly pick characters for the password.

For both easy and hard cases, what I first did was to ask the user how many letters, numbers and symbols would be in the password. With the FOR statement, I choose random characters from each list according to the number entered by the user. Concatenating each character in one variable. For the easy case, this would be it. Just return the password to the user.
For the hard case, one final step is required. From the variable with all the random characters, I took each character randomly into a new variable, and then print it out to the user.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 5: Generador de contraseñas aleatorias.

Éste es un proyecto muy útil donde los usuarios pueden generar contraseñas de forma aleatoria con la cantidad de números, letras y símbolos de su elección.
Hay dos dificultades para este proyecto en el curso. Fácil, donde la posición de los caracteres no es aleatoria (primero son las letras, luego números y luego símbolos) y el modo difícil donde todo en la contrañsera será aleatorio.

Primero que nada, cree tres listas conteniendo todas las letras, todos los números y todos los símbolos. El programa escogerá los caracteres aleatorios de estas listas para la contraseña.

Para las dos dificultades, lo primero que hice es preguntarle al usuario cuántas letras, números y símbolos quiere en la contraseña. Con un FOR, el programa escogerá aleatoriamente de cada lista la cantidad necesaria de caracteres de acuerdo con lo ingresado por el usuario. Concatenando cada caracter en una sóla variable. Para la dificultad fácil, esto sería todo. Solo falta regresar la variable al usuario.
Para el caso difícil, hay un paso adicional. De la variable con los caracteres aleatorios, el programa escoge uno aleatoriamente y lo pasa a una variable nueva, y luego la imprime para el usuario.
