# 100 Days of Python
## Project 30: Improved password manager

In the previous project I made a simple password manager that would save different passwords from different websites in a TXT file. However, but to see the passwords the user should open the file and look for it manually. In this improved password manager, the user can search for an specific website and the program will return the password.

In the try_catch_exceptions folder I just practiced a bit with the most common errors, and using Try to get this errors and printing messages or running a different code. I find this pretty useful, specially when I need the user to enter specific inputs. Since I can't really control what the user inputs in my program, I can use code to prevent errors from this inputs and instead give messages or do something else.

In the other folder is the project. Almost all the project is the same as the original password manager, but I made a new function called search, which will get the data in the website textbox and seach the file. Here I will use Try and search for the user input, but if it is not in the file, I will prompt a message telling the user that no data was found.

Now, the other different thing here is that I am using a json file. Json ([JavaScript Object Notation](https://en.wikipedia.org/wiki/JSON)) is another format that can be used to manipulate and share data. Json is a pretty common data format. To open a json file in the program I needed to import the Json library. In the next project I will be using Json format data and practice a bit more with it.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 30: Administrador de contraseñas mejorado.

En el proyecto anterior hice un administrador de contraseñas muy simple que guarda diferentes contraseñas de distintas páginas web en un archivo TXT, pero para ver las contraseñas el usuario tenía que abrir el archivo y buscarlas manualmente. En este administrador de contraseñas mejorado, el usuario puede buscar una página web en específico y el programa le dará la contraseña.

En la carpeta de try_catch_exceptions practiqué un poco los errores más comunes, y usando Try para atrapar estos errores e imprimir mensajes o correr un código distinto. Encontré esto muy útil, especialmente cuando necesito que el usuario ingrese algo específico. Debido a que no puedo controlar lo que el usuario va a ingresar, puedo usar mi código para prevenir errores de estas entradas y retornar un mensaje o hacer algo más.

En la otra carpeta está el proyecto. Casi todo el proyecto es lo mismo que el anterior administrador de contraseñas, pero hice una nueva función llamada search, la cuál buscará la información dentro del cuadro de texto y buscará en el archivo. Aquí usaré un Try para buscar lo que ingresó el usuario, pero si no está en el archivo, aparecerá un mensaje indicándole al usuario que no se encontró nada.

Ahora, la otra cosa distinta aquí es que estoy usando un archivo json. Json ([JavaScript Object Notation](https://es.wikipedia.org/wiki/JSON) es otro formato que es utilizado para manipular y compartir datos. Json es un formato de data muy común. Para abrir un archivo Json en el programa necesité importar la librería Json. En el siguiente proyecto estaré utilizando más data con formato Json y practicaré un poco más.
