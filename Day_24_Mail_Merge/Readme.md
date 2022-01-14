# 100 Days of Python
## Project 24: Mail merge.

We did a bit of file editing in the Snake game project, where we wrote on a txt file every time the user got a new highscore.
Now, in this proyect we will have a closer look on how to open, modify, replace and more on external files.

I uploaded two folders again, one with some practice with the methods, and the second with the actual mail merge project.

In the text_practice folder in only one main.py file. Here you can see how I practice a bit with the "with" and "as" keywords for writing and editing some txt files.

Now for the project, the main objective is to created files like mails, where we take a list of names and replace the word placeholder "[name]" with each name. This is helpful when you need to send the same letter to different persons. There are several folders in the project so we could practice with folder paths as well.

To begin, we just need a txt file with the names of all the people we want to send the letters. In the project, this list is inside the folder Names, inside of the folder Input. In this folder is also the folder Letters, which cointain the base letter file. Notice that in the base letter text is the placerholder "[name]".

I will save all the letters in a folder called ReadyToSend, inside of the Output folder.

The project is quite simple. In the main.py file I firstly open the name list with the "with" and "as" keywords. I do it this way to save some code lines, because only using the "open" method, I should close the file later. The with and as keywords close the file as soon as the code in the indented lines is over.
After is open the file, I use the method readlines to get all the names inside the txt file in a list.

Now I used another "with" and "as" to open the base letter. I save the text in the file in a variable called starting_letter. Now, with a FOR loop I will replace the PLACEHOLDER in the starting letter with the actual name in the name list, and save that text as a new variable. Now I will use the open method to open the text where the letter will be stored. If the file with that name does not exist, the method will create a new file with that name. I use the method write to insert the text into the file I just created.
Since I am in a FOR loop, this will be done for all the names in the list.

Now all the new letters will be in the destination folder, each one with a name in the list.

This was a pretty interesting project that shows how Python can be used to do repetitive tasks. We learnt how to open files, how to read what's inside of those files, and how we can edit or replace data from the files. So far, we have only used txt files, but in the next project we will try with other files as well.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 100 Días de Python
## Proyecto 24: Fusión para correos.

En el proyecto del juego de Snake realizamos un poco de edición de un archivo, dónde escribíamos en un archivo txt cada vez que el usuario obtenía un nuevo puntaje máximo.
Ahora, en este proyecto vamos a ver más de cerca cómo abrir, modificar, reemplazar y más en archivos externos.

Subí dos carpetas nuevamente, una con un archivo de práctica, y la otra con el proyecto de fusión para correos.

En la carpeta de text_practice hay sólo un archivo main.py. Aquí se puede observar cómo practiqué un poquito con las palabras clave "with" y "as" para escritura y edición de archivos txt.

Ahora para el proyecto, el objetivo principal es crear archivos como correos, dónde se tomará una lista de nombres que reemplazarán la palabra marcador "[name]" con cada uno de los nombres. Esto es muy útil cuando se necesita envíar la misma carta a diferentes personas. Hay múltiples carpetas en este proyecto para así practicar con rutas de carpetas.

Para comenzar, sólo necesitamos un archivo txt con los nombres de todas las personas a la que queremos envíar las cartas. En este proyecto, la lista está dentro de una carpeta llamada Names, dentro de la carpeta llamada Input. En esta carpeta también estará el archivo de la carta base en la carpeta llamada Letters. Dentro del texto de esta carta base estará la palabra marcador "[name]".

Guardaré todas las cartas en una carpeta llamada ReadyToSend, dentro de la carpeta Output.

Este proyecto es bastante sencillo. Dentro del archivo main.py abriré la lista con los nombres usando "with" y "as". Lo hago de esta forma para ahorrar unas líneas de código, ya que si utilizo el método open, debería cerrar el archivo cuando termine de usarlo. Con las palabras clave "with" y "as" una vez que se termine el código en las líneas indentadas, el archivo se cerrará automáticamente.
Después de abrir el archivo, guardé los nombres como lista en una variable usando el método readlines.

Ahora utilizando otro "with" y "as" abrí la carta base. Guardé el texto en una variable llamada starting_letter. Ahora, con un bucle FOR voy a reemplazar la palabra marcador en la carta base con los nombres en la lista, y guardaré ese texto en una nueva variable. Ahora usaré el método open para abrir el archivo dónde que utilizaré para la carta. Si el archivo con el nombre especificado no existe, este método creará un archivo con ese nombre. Utilizé el método write para insertar el text dentro del archivo recién creado.
Ya que estoy en un bucle FOR, este proceso se repitirá con todos los nombres en la lista.

Ahora todas las nuevas cartas estarán en la carpeta de destino, cada una con un nombre de la lista.

Este fue un proyecto muy interesante que nos muestra cómo puede ser utilizado Python para realizar tareas repetitivas. Aprendimos cómo abrir archivos, cómo leer lo que está dentro de estos archivos y cómo editar o reemplazar información en esos archivos. Hasta ahora, sólo hemos utilizado archivos txt, pero en el siguiente proyecto probaremos con otros archivos también.
