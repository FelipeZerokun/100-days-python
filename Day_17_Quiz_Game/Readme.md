# 100 Days of Python
## Project 17: Quiz Game

Again, here are two folders. One for practice and one for the actual project.

In the practice folder is a file where I practiced creating a class with a constructor, and some attributes. I also made a small method to change some of this attribues.
This was a good small practice to understand how classes are made, and how objects are created and have their own attributes.

Now for the project, it is a Quiz game. There are a set of questions of true or false in the file data.py. The data is structure as a list with dictionaries. Each question has a text with the actual question and a text with the answer, True or False.
I made a class in the question_model.py file that will make questions and answers into an object.
I could have used the questions and answer as dictionaries, but for the sake of practising objects creation, I made each question an object.

For the question making structure, I made a class called QuizBrain. When this class is initialized, it will take a list with the questions as objects. 
The class has a method called still_has_question_ that will check the number of questions in the list and the questions answered by the user. If the user already answered all the questions, this method returns False.
The next_question method will print the question for the user, and expects and answer from the user. After the user answers, the method will check if the user answer is correct and add a point to the user's score, or is incorrect.
Every time the user answers a question, question number attribute will increment by one.

The main.py file will just have a loop where it will make the questions objects, so everytime I run the file, if I add more questions to the list, all of them will be made objects.
After this, I create the object for the quiz structure, and use the next_question method until there are no more questions.
When the user has answered all the questions, a message will be shown with the number of correct answers from the user.

This project starts to show the advantajes of using classes in different files, instead of using functions. The code is much more organized, if you need to change or add something you just go to the class file, and it is much more easier for other people to read and understand your code.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 D??as de Python
## Proyecto 17: Juego de preguntas.

Nuevamente, aqu?? tengo dos carpetas. Una de pr??ctica y una para el proyecto en s??.

En la carpeta de pr??ctica hay un archivo en donde practiqu?? c??mo crear una clase con un constructor, y algunos atributos. Tambi??n hice un peque??o m??todo para cambiar algunos de sus atributos.

Ahora para el proyecto, es un juego de preguntas. Hay un n??mero de preguntas de verdadero o falso en el archivo data.py. Los datos est??n estructurados como una lista de diccionarios. Cada pregunta tiene un text con la pregunta actual y un texto con la respuesta, True o False.

Hice una clase en el archivo question_model.py que transformar?? las preguntas y respuestas en un objeto.
Pude haber utilizado las preguntas y respuestas como diccionarios, pero por el valor de aprendizaje de creaci??n de objetos, hice a cada pregunta un objeto.

Para la estructura de elaboraci??n de preguntas, hice una clase llamada QuizBrain. Cuando se inicializa esta clase, necesitar?? una lista con las preguntas como objetos.
La clase tiene un m??todo llamado still_has_question que revisar?? el n??mero de preguntas en la lista y las preguntas que el usuario vaya contestando. Si el usuario ya respondi?? todas las preguntas, este m??todo retornar?? Falso.
El m??todo next_question va a imprimir la pregunta para el usuario, y esperar?? una respuesta. Despu??s de que el usuario responda, el m??todo revisar?? si la respuesta del usuario es la correcta y a??adir?? un punto de ser el caso, o si es incorrecta.
Cada vez que el usuario responde una pregunta, el atributo de n??mero de pregunta incrementar?? en uno.

El archivo main.py solo tendr?? un bucle d??nde convertir?? las preguntas en objetos, as?? que cada vez que corra el archivo, si he a??adido m??s preguntas a la lista, todas ellas se convertir??n en objetos.
Despues de esto, un objeto con la estructura para las preguntas ser?? creado, y se usar?? el m??todo next_question hasta que no haya m??s preguntas.
Cuando el usuario haya respondido todas las preguntas, un mensaje se mostrar?? indic??ndole al usuario cu??ntas respuestas correctas obtuvo.

Este proyecto empieza a mostrar las ventajas de usar clases en archivos diferentes, en vez de usar funciones. El c??digo es mucho m??s organizado, si necesitas cambiar o a??adir algo simplemente vas al archivo de la clase, y es mucho m??s f??cil para otras personas leer y entender tu c??digo
