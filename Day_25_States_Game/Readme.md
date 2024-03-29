# 100 Days of Python
## Project 25: States game

Here I learnt how to use CSV files!
CSV (Comma-separated value) is a delimited text file that separates values using commas. This is a pretty common way to store and share tabular data, o a single relationship database.
Here I will be using one of the most common and useful libraries in python for Data manipulation. Used in data science and data analytics. Its the Pandas library.

I made a small project before the main one, and I uploaded because it was really interesting for me. So, I will explain the small project first, before the States game project.

The Great Squirrel Census project was a really interesting project from [The squirrel Census](https://www.thesquirrelcensus.com/), where numerous volunteers went to the Central Park to count up all the squirrels in the park. This lead to an amazing squirell database here: [NYC Open data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw).
In this database, you can see many characteristics like, age, fur color, location, behaviour, and much more. So, using this database I practiced how to manage a CSV file using Python. This project's objective is to count up how many squirrels from each color are in this database. The fur colors are Gray, cinnamon and black.

Before anything, you must install the pandas library in your IDE, and then import it to the project.
using the read_csv method from Pandas I imported the Squirrel CSV file into a variable. This variable will be a Pandas object known as a dataframe. It is similar to a list. With the conditional ["Primary Fur Color"] == "Color" I can get all the column that match the "color". So, I just did the comparisson with the three colors, and used the len method to count how many were on each one. 
Finally, to learn how to transform this data into a CSV file, I used the DataFrame and the to_csv methods with the data I got.

Now, the States Game project
Basically, it is a game where you have remember all the states in a map of the United States of America.
To make this game dinamic, I used the Screen method from the Turtle module. Using the addshape method I can use a image as a background for the screen. 
I created the NameTheState class that will create an invisible Turtle object that will have a text with the name of each state. The map will begin empty, and every time the user enters the name of a State, the text with the name will appear in the map. The only method in this class is write_state_name, which will move the turtle object to certain coords in the map and show a text with the State's name.

To know exactly where each state is in terms of X and Y coords, I created a function in the main.py file called get_mouse_click_coor that will return the coordinates of the mouse when I click somewhere in the map. This way I can get all the States coords in the map. I created a CSV file that will have all the states with their own coords separated by comma. After getting the coords of all 50 states, I commented out the function. 

Again, I will be using Pandas for the CSV file management.
I will use a While loop for the duration of the game. I will ask the user the enter the name of a State with input. Then, I will import all the states from the CSV file using Pandas method read_csv. Then I will compare the user's answer with each state on the list. If the User's answer is an actual State and it is not in the map yet, then I will call the write_state_name method. 

If the user gets all 50 states, the game ends. The user may also exit the game by writing the word Exit. By doing this, the program will check all the states the user didn't get and save them in a different CSV file for the user to know which States he missed. 
Finally, the program will print how many states did the user get.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 25: Juego de los Estados.

¡Aquí aprendí como usar los archivos CSV!
CSV (Valores separados por coma por sus siglas en inglés) es un archivo de texto delimitado que separa valores utilizando comas. Ésta es una forma común de guardar y compartir información tabulada, o base de datos con una relación simple.

Aquí usaré una de las librerías más comunes y útiles en python para la manipulación de Datos. Es utilizada para Data science y analítica de datos. Es la librería Pandas

Realicé un pequeño proyecto antes del principal, y lo subí porque me parece bastante interesante. Así que, explicaré el proyecto pequeño primero, antes de empezar con el proyecto de juego de los Estados.

El proyecto de Gran Censo de Ardillas (Great Squirrel Census) es un proyecto interesante de [The squirrel Census](https://www.thesquirrelcensus.com/), dónde numerosos voluntarias fueron al parque Central Park y contaron todas las ardillas en el parque. De esto salió una sorprendente base de datos aquí: [NYC Open data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw).
En esta base de datos, se pueden ver características cómo edad, color del pelaje, ubicación, comportamiento, entre otras. Así que, utilizando esta base de datos practiqué cómo manipular un archivo CSV utilizando Python. El objetivo de este proyecto es contar cuántas ardillas de cada color de pelaje hay en la base de datos. Los colores de pelaje son Gris, Canela y negro.

Antes de nada, se debe instalar la librería Pandas en tu IDE, y luego importarla al proyecto.
Usando el método read_csv de Pandas, importé el archivo CSV de las ardillas a una variable. Esta variable tendrá un objeto conocido como dataframe. Es muy similar a una lista. Con el condicional ["Primary Fur Color"] == "Color" se puede obtener todas las columnas que coincidas con el "color". Hice la comparación con los tres colores, y usando el método len contabilizé cuántas columnas había de cada color.
Finalmente, para aprender cómo transformar esta información en un archivo CSV, utilicé los métodos DataFrame y to_csv.

Ahora, el proyecto del juego de Estados.
Básicamente es un juego dónde debes recordas todos los Estados en un mapa de los Estados Unidos de América.
Para hacer este juego dinámico, utilicé el método Screen del módulo Turtle. Utilizando el método addshape puedo usar una imagen como dóndo para la ventana.
Creé la clase NameTheState que creará objetos Turtle invisibles que tendrá un texto con el nombre de cada Estado. El mapa iniciará vacío, y cada vez que el usuario ingrese el nombre de un estado, el texto con el nombre aparecerá en el mapa. El único método en esta clase es write_state_name, que moverá el objeto Turtle a determinadas coordenadas en el mapa y mostrará el texto con el nombre del Estado.

Para saber dónde exactamente estará el Estado en términos de coordenadas de X y Y, creé una función en el archivo main.py llamada get_mouse_click_coo que regresará las coordenadas del ratón cuando haga click en cualquier lugar del mapa. De esta forma puede tener las coordenadas de todos los Estados del mapa. Creé un archivo CSV que tendrá todos los Estados con sus respectivas coordenadas. Después de obtener las coordenadas de los 50 Estados, comenté esta función.

Nuevamente estaré usando Pandas para el manejo de los archivos CSV.
Usaré un bucle While durante todo el juego. The programa le pedirá al usuario que ingrese el nombre de un Estado con input. Luego, importaré todos los estados del archivo CSV utilizado el método de Pandas read_csv. Luego compararé la respuesta del usuario con cada estado en la ista. Si la respuesta del usuario es un Estado real y no está en el mapa aún, se llamará el método write_state_name.

Si el usuario consigue los 50 Estados, el juego termina. El usuario también puede salir del juego escribiendo la palabra Exit. Al hacer esto, el programa revisará todos los Estados que el usuario con consiguió escribir y los guardará en otro archivo CSV para que el usuario sepa cuáles Estados no recordó.
Finalmente, el programa imprimirá cuántos Estados consiguió recordar el usuario.
