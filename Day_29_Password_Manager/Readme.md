# 100 Days of Python
## Project 29: Password manager

This is a small APP project that let's the user manage all of his/hers passwords. In a previous project I made a random password generator, and I will implement the same code here.

The GUI will have three spaces for the user to enter the website, the email for that website and the password. The user will also have a button to randomly generate a password if needed.

I will be using the TKinter module. Also I imported some methods from the random module for the password generator.

I defined two functions. In the generate_password function I used almost the same code as the day 05 project. This code will return a random password with 5 to 7 letters, 2 to 5 numbers and 2 to 5 symbols.

The other function is save. This function will take all the information in the textboxes and wil save it in a file called data.txt. I used the open and write methods with the keywords "with" and "as" for this. If any of the textboxes is empty, the function will return a prompt window warning the user not to leave any textbox empty. If all the textboxes are filled, a prompt window will appear asking the user for confirmation. After this, the textboxes will be emptied.

Using a Tk object, I created a window and used a small log. Then, I created three labels, website, email and password. Also, I will make one textbox entry for each one of these. Finally, I created two buttons. One for the random password generator function, and one for the save function.

This project can be used as an actual APP for your passwords, but it is really simple and saving your passwords in a TXT file may not be the best idea. In the next project I will be making an improved password manager.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 29: Administrador de contraseñas.

Este proyecto es una pequeña APP que le permite al usuario gestionar sus contraseñas. En un proyecto anterior hice un generador aleatorio de contraseñas, y estaré implementando el mismo código aquí.

La interfaz de usuario tendrá tres espacios para que el usuario ingrese la página web, el correo para esa página y la contraseña. El usuario también tendrá un botón que generará una contraseña de forma aleatoria si lo necesita.

Estaré usando el módulo TKinter. También importé algunos métodos del módulo random para el generador de contraseñas.

Definí dos funciones. En la función generate_password usé casi el mismo código que en el proyecto del día 05. Este código retornará una contraseña aleatoria con 5-7 letras, 2-5 números y 2-5 símbolos.

La otra función es save. Esta función tomará toda la información en los cuadros de texto y la guardará en un archivo llamado data.txt. Usé los métodos open y write junto con las palabras clave "with" y "as" para esto. Si cualquiera de los cuadros de texto está vacío, la función retornará una ventana de advertencia pidiendo al usuario no dejar ningún cuadro de texto vacío. Si todos los cuadros de texto tienen información, aparecerá una ventana pidiendo al usuario que confirme. Después de esto, todos los cuadros de texto quedará vacíos.

Utilizando un objeto Tk, creé una ventana y usé una pequeña imagen. Luego, creé tres etiquetas para la página web, el correo y la contraseña. También hice un cuadro de texto para cada uno. Finalmente creé dos botones. Uno para la función generadora de contraseñas, y el otro para la función de guardado.

Este proyecto puede ser utilizado cómo una APP real para guardar contraseñas, pero es bastante simple y guardar tus contraseñas en un archivo TXT puede no ser la mejor idea. En el siguiente proyecto haré una versión mejorada del administrador de contraseñas.
