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

# 100 D??as de Python
## Proyecto 34: App de Quizzes

Este proyecto es una app de Quizzes que solicitar?? preguntas de una base de datos de la siguiente p??gina web: [Open Trivia Database](https://opentdb.com/). Para obtener la API de esta p??gina, puedes ingresar [aqu??](https://opentdb.com/api_config.php)

Esta API requiere cuatro par??metros:
* Cantidad de preguntas
* Categor??a
* Dificultad
* y tipo (Aqu?? ser?? booleando para preguntas de Verdadero o Falso)

This API requieres four parameters:
* amount of questions
* category 
* difficulty
* and type (here will be boolean for True or False queestions)

La primera cosa que hice fue importar las preguntas de la API con requests, y guardarlas en una variable llamada question_data. Esto ser?? una lista con diccionarios. Cada diccionario ser?? una pregunta, y lo que necesitamos de los diccionarios son las llaves "question" y "correct_answer". Esto estar?? en el archivo data.py

Use la misma estructura que en el proyecto del d??a 17: Juego de. Primero, en el archivo question_model.py est?? la clase Question que tiene dos atributos. Los atributos de Texto y Respuesta.
El archivo quiz_brain.py es el mismo. Una clase llamada QuizBrain que manejar?? los objectos Question. El m??todo next_question retornar?? una cadena de caracteres con el n??mero de la pregunta y el texto de la pregunta. Esto es para que la GUI le muestre el texto al usuario. El m??todo check_answer comparar?? la respuesta del usuario con la respuesta correcta del objeto Question.

En otro archivo cre?? los objetos para la interfaz. En el archivo ui.py cre?? una ventana, un Canvas con un fondo blanco, un bot??n para la respuesta "Correcta", y otro bot??n para la respuesta "Falsa". Hay cuatro m??todos en esta clase.

El m??todo Get_next_question revisar?? el objecto BrainQuiz para ver si a??n hay objectos Question. Si los hay, mostrar?? la siguiente pregunta al usuario, caso contrario mostrar?? un mensaje indicando que el Quiz termin??. Tambi??n hice dos m??todos, uno para el bot??n de "Verdadero" y otro para el bot??n de "Falso".

Finalmente, un m??todo que cambiar?? el color de fondo del Canvas a ver si la respuesta del usuario es correcta, y lo cambiar?? a rojo si la respuesta del usuario es incorrecta.

En el archivo main.py hice un bucle FOR que convertir?? cada pregunta del Quiz de la base de datos de Open Trivia en un objeto Question. Tuve que utililizar el m??todo unescape de HTML para convertir todos los caracteres con secuencia HTML en caracteres normales. [Aqu??](https://docs.python.org/3/library/html.html) est?? la documentaci??n de la librer??a HTML. Luego cre?? un objeto BrainQuiz con la lista de preguntas, y cre?? la interfaz gr??fica para el usuario. Cuando el usuario haya respondido todas las preguntas, imprim?? un mensaje con el puntaje final para el usuario.

Este proyecto me gusta mucho porque aqu?? implement?? muchas cosas que aprend??, tales como:
* Creaci??n de Clases
* Objetos y m??todos.
* Interfaz gr??fica de usuarios con Tkinter
* APIs
