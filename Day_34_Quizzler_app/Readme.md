# 100 Days of Python
## Project 34: Quizzler App

This project is a Quizz app that will requets questions from a database of this website: [Open Trivia Database](https://opentdb.com/). To get the API from this page, you can enter this link [here](https://opentdb.com/api_config.php)

This API requieres four parameters:
* amount of questions
* category 
* difficulty
* and type (here will be boolean for True or False questions)

The first thing I did was to import the questions from the API with requests, and save them in a variable called question_data. This will be a list with diccionaries. Each dictionary will be a question, and what we need from the dictionaries is the "question" key and the "correct_answer" key. This will be in the data.py file. 

I followed the same structure as in the Day 17 project: quiz game. First, a Question class in the question_model.py file which This class just has two attributes. the Text and the Answer attributes.
The quiz_brain.py is the same. A class called QuizBrain that will manage the Question objects. The next_question method will return a string with the number of the question and the text of the question. This is for the GUI to show the text for the user. The check_answer method will compare the user answer's with the correct answer from the Question object. 

In another file I created all the objects for the interface. In the ui.py file I created the window, a Canvas with a white background, a button for the True answer, another button for the False answer. There are four methods in this Class. 

Get_next_question will check que BrainQuiz object to see if there are still Question objects. If there are, it will show the new question to the user, if not it will show a message saying the quiz is over. I also made two methods, one for the True button and one for the False button. 

Finally, one method that will turn the Canvas background to green if the user is correct, and will turned it red if the user is incorrect.

In the main.py file I made a FOR loop that will make each quiz question from the Open trivia database into a Question object. I had to used the HTML method unescape on these questions to turn all characters with HTML sequence into normal characters. [Here](https://docs.python.org/3/library/html.html) is the HTML library documentation. Then I just created the BrainQuiz object with the list of questions, and created the GUI for the user. When the user answered all the questions, I printed a message with the final score of the user.

I really like this project because here I implemented many things that I learn, like:
* Classes creation
* Objects and methods.
* GUI with Tkinter
* API's

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 34: App de Quizzes

Este proyecto es una app de Quizzes que solicitará preguntas de una base de datos de la siguiente página web: [Open Trivia Database](https://opentdb.com/). Para obtener la API de esta página, puedes ingresar [aquí](https://opentdb.com/api_config.php)

Esta API requiere cuatro parámetros:
* Cantidad de preguntas
* Categoría
* Dificultad
* y tipo (Aquí será booleando para preguntas de Verdadero o Falso)

This API requieres four parameters:
* amount of questions
* category 
* difficulty
* and type (here will be boolean for True or False queestions)

La primera cosa que hice fue importar las preguntas de la API con requests, y guardarlas en una variable llamada question_data. Esto será una lista con diccionarios. Cada diccionario será una pregunta, y lo que necesitamos de los diccionarios son las llaves "question" y "correct_answer". Esto estará en el archivo data.py

Use la misma estructura que en el proyecto del día 17: Juego de. Primero, en el archivo question_model.py está la clase Question que tiene dos atributos. Los atributos de Texto y Respuesta.
El archivo quiz_brain.py es el mismo. Una clase llamada QuizBrain que manejará los objectos Question. El método next_question retornará una cadena de caracteres con el número de la pregunta y el texto de la pregunta. Esto es para que la GUI le muestre el texto al usuario. El método check_answer comparará la respuesta del usuario con la respuesta correcta del objeto Question.

En otro archivo creé los objetos para la interfaz. En el archivo ui.py creé una ventana, un Canvas con un fondo blanco, un botón para la respuesta "Correcta", y otro botón para la respuesta "Falsa". Hay cuatro métodos en esta clase.

El método Get_next_question revisará el objecto BrainQuiz para ver si aún hay objectos Question. Si los hay, mostrará la siguiente pregunta al usuario, caso contrario mostrará un mensaje indicando que el Quiz terminó. También hice dos métodos, uno para el botón de "Verdadero" y otro para el botón de "Falso".

Finalmente, un método que cambiará el color de fondo del Canvas a ver si la respuesta del usuario es correcta, y lo cambiará a rojo si la respuesta del usuario es incorrecta.

En el archivo main.py hice un bucle FOR que convertirá cada pregunta del Quiz de la base de datos de Open Trivia en un objeto Question. Tuve que utililizar el método unescape de HTML para convertir todos los caracteres con secuencia HTML en caracteres normales. [Aquí](https://docs.python.org/3/library/html.html) está la documentación de la librería HTML. Luego creé un objeto BrainQuiz con la lista de preguntas, y creé la interfaz gráfica para el usuario. Cuando el usuario haya respondido todas las preguntas, imprimí un mensaje con el puntaje final para el usuario.

Este proyecto me gusta mucho porque aquí implementé muchas cosas que aprendí, tales como:
* Creación de Clases
* Objetos y métodos.
* Interfaz gráfica de usuarios con Tkinter
* APIs
