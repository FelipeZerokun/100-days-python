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

# 100 D??as de Python
## Proyecto 25: Juego de los Estados.

??Aqu?? aprend?? como usar los archivos CSV!
CSV (Valores separados por coma por sus siglas en ingl??s) es un archivo de texto delimitado que separa valores utilizando comas. ??sta es una forma com??n de guardar y compartir informaci??n tabulada, o base de datos con una relaci??n simple.

Aqu?? usar?? una de las librer??as m??s comunes y ??tiles en python para la manipulaci??n de Datos. Es utilizada para Data science y anal??tica de datos. Es la librer??a Pandas

Realic?? un peque??o proyecto antes del principal, y lo sub?? porque me parece bastante interesante. As?? que, explicar?? el proyecto peque??o primero, antes de empezar con el proyecto de juego de los Estados.

El proyecto de Gran Censo de Ardillas (Great Squirrel Census) es un proyecto interesante de [The squirrel Census](https://www.thesquirrelcensus.com/), d??nde numerosos voluntarias fueron al parque Central Park y contaron todas las ardillas en el parque. De esto sali?? una sorprendente base de datos aqu??: [NYC Open data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw).
En esta base de datos, se pueden ver caracter??sticas c??mo edad, color del pelaje, ubicaci??n, comportamiento, entre otras. As?? que, utilizando esta base de datos practiqu?? c??mo manipular un archivo CSV utilizando Python. El objetivo de este proyecto es contar cu??ntas ardillas de cada color de pelaje hay en la base de datos. Los colores de pelaje son Gris, Canela y negro.

Antes de nada, se debe instalar la librer??a Pandas en tu IDE, y luego importarla al proyecto.
Usando el m??todo read_csv de Pandas, import?? el archivo CSV de las ardillas a una variable. Esta variable tendr?? un objeto conocido como dataframe. Es muy similar a una lista. Con el condicional ["Primary Fur Color"] == "Color" se puede obtener todas las columnas que coincidas con el "color". Hice la comparaci??n con los tres colores, y usando el m??todo len contabiliz?? cu??ntas columnas hab??a de cada color.
Finalmente, para aprender c??mo transformar esta informaci??n en un archivo CSV, utilic?? los m??todos DataFrame y to_csv.

Ahora, el proyecto del juego de Estados.
B??sicamente es un juego d??nde debes recordas todos los Estados en un mapa de los Estados Unidos de Am??rica.
Para hacer este juego din??mico, utilic?? el m??todo Screen del m??dulo Turtle. Utilizando el m??todo addshape puedo usar una imagen como d??ndo para la ventana.
Cre?? la clase NameTheState que crear?? objetos Turtle invisibles que tendr?? un texto con el nombre de cada Estado. El mapa iniciar?? vac??o, y cada vez que el usuario ingrese el nombre de un estado, el texto con el nombre aparecer?? en el mapa. El ??nico m??todo en esta clase es write_state_name, que mover?? el objeto Turtle a determinadas coordenadas en el mapa y mostrar?? el texto con el nombre del Estado.

Para saber d??nde exactamente estar?? el Estado en t??rminos de coordenadas de X y Y, cre?? una funci??n en el archivo main.py llamada get_mouse_click_coo que regresar?? las coordenadas del rat??n cuando haga click en cualquier lugar del mapa. De esta forma puede tener las coordenadas de todos los Estados del mapa. Cre?? un archivo CSV que tendr?? todos los Estados con sus respectivas coordenadas. Despu??s de obtener las coordenadas de los 50 Estados, coment?? esta funci??n.

Nuevamente estar?? usando Pandas para el manejo de los archivos CSV.
Usar?? un bucle While durante todo el juego. The programa le pedir?? al usuario que ingrese el nombre de un Estado con input. Luego, importar?? todos los estados del archivo CSV utilizado el m??todo de Pandas read_csv. Luego comparar?? la respuesta del usuario con cada estado en la ista. Si la respuesta del usuario es un Estado real y no est?? en el mapa a??n, se llamar?? el m??todo write_state_name.

Si el usuario consigue los 50 Estados, el juego termina. El usuario tambi??n puede salir del juego escribiendo la palabra Exit. Al hacer esto, el programa revisar?? todos los Estados que el usuario con consigui?? escribir y los guardar?? en otro archivo CSV para que el usuario sepa cu??les Estados no record??.
Finalmente, el programa imprimir?? cu??ntos Estados consigui?? recordar el usuario.
