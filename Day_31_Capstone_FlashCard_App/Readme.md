# 100 Days of Python
## Project 31: Flashcard App

The third Capstone project in the course.

This is a flashcard app for learning japanese vocabulary!
I am a Japanese culture enthusiast, and I have been learning japanese for a couple years now, so for my flashcard app I decided to make it for learning Japanese Kanji characters.
For the Kanjis database, I grabbed some json databases from [David Gouveia](https://github.com/davidluzgouveia) github's proyect [Kanji data](https://github.com/davidluzgouveia/kanji-data). He has some good proyects, go and check them!

Using flashcards is a good technique for vocabulary learning. In this app, a flashcard with a random Kanji will be shown to the user, then the user will have three seconds to recognize the kanji before the flashcard turns and shows the Kanji's meaning. If the user knows the Kanji meaning, he/she should click the check button, otherwise he/she should click the X button. The app will remember which Kanjis the user didn't know and save them in a CSV file. 

This project is divided into four parts to make it more understandable. 

# First step
The first thing I did was to import the database in a file called kanji_database.py. Here I took all the data inside the "kanji-kyouiku.json" file using the json library. This is imported as a dictionary object, and I save it in a variable called kanji_dataset.

Then, using Try/Except I will try to open the kanjis_to_learn.csv file. If the file does not exist, in the Except part I will create a list with the Kanjis from the kanji_dataset. If the CSV file exists, I will take the Kanji from it and stores them in a list. I called this list user_list. This way, I can keep track of the kanjis that the user does not know.

# Second step
Now, for the second step I created the GUI used for the app. I used Tkinter module for this. First, I set some variables I used in the GUI. I picked a random Kanji from the user_list, and using it as a key I looked for some definitions in the Kanji dictionary. Then, I created a window as a Tk object. Also, I loaded the images used in the project.

After the window, I created the canvas for the words in japanese and english. Since the first thing the user will see is the japanese Kanji, I used the create_text method with the Kanji_word and the on'yomi and kun'yomi readings. The last things I needed for the UI are the buttons. I created two buttons, one for the "right" option and one for the "wrong" option. For now, these buttons won't have a command. Here an image showing how is the window so far.

![FlashCard example](./flashcard_example.png "Flashcard APP example")

# Third step
After the GUI, I needed a function that after three seconds "flips" the flashcard and shows the user the meaning of the Kanji in english.
I defined a function called flip_card that will simple change the objects in the canvas to their english version. In the case of the on'yomi and kun'yomi readins, I will use a blank space so nothing appears in the canvas. Also, I needed to add a after method where I created the window object, so my function is executed 3000 ms after the code began.
When the flashcard is flipped, the canvas will look like this

![FlashCard example](./flashcard_example2.png "Flashcard APP example")

# Fourth step

The last thing I did was to create the functions for each button. The function for the wrong button is the easiest, because I just need to "flip" the flashcard back and add a new random Kanji. I defined a new function called new_word, which will do exactly that. Take a new random word from the user_list and change all the objects in the canvas back to japanese. Now, everytime the user click the "wrong" button, the flashcard will flip and show a new kanji.
For the "right" button I define another function called known_word. This function will take the Kanji out of the user_list, and save the list in the csv file, so this kanji does not appear again for the user. After this, the function will call the new_word function to make a new kanji appear in the canvas. 

I had to add a IF condition in the known_word function that checks the lenght in the user_list. If there are no items in the list, the window will close.
If the user want to start again, just <ins>delete the kanjis_to_learn.csv file</ins> in the data folder.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 D??as de Python
## Proyecto 31: App de tarjetas did??cticas.

El tercer gran proyecto en el curso.

????sta es una aplicaci??n de tarjetas din??micas para aprender vocabulario japon??s!
Soy un entusiaste de la cultura japonesa, y he estado aprendiendo japon??s desde hace un par de a??os, as?? que para mi app de tarjetas din??micas decid?? hacerla para aprender los caracteres Kanji japoneses.
Para la base de datos de Kanji, tom?? algunas base de datos json del proyecto github de [David Gouveia](https://github.com/davidluzgouveia) llamado [Kanji data](https://github.com/davidluzgouveia/kanji-data). Tiene buenos proyectos, ??vayan a verlos!

Utilizar tarjetas din??micas de una buena t??cnica para el aprendizaje de vocabulario. En esta app, se mostrar?? al usuario una tarjeta con un kanji aleatorio, luego el usuario tendr?? tres segundos para reconocer el Kanji antes de que la tarjeta giro y muestre el significado del Kanji. Si el usuario sabe el significado del Kanji debe presionar el bot??n con el visto, caso contrario deber??a presionar el bot??n con la X. La app recordar?? cu??les Kanji el usuario no reconoce y los guardar?? en un archivo CSV.

Este proyecto est?? dividido en cuatro partes para hacerlo m??s entendible.

# Primer paso
La primera cosa que hice fue importar el archivo de la base de datos llamado kanji_database.py. Lo que hice fue tomar todos los datos dentro del archivo "kanji-kyouiku.json" usando la librer??a Json. Ser?? importado como un objecto diccionario, y lo guardar?? en una variable llamada kanji_dataset.

Luego, usando Try/Except intent?? abrir el archivo kanjis_to_learn.csv. Si el archivo no existe, en la parte de Except crear?? una lista con los Kanji de kanji_dataset. Si existe el archivo CSV, lo import?? y met?? los Kanjis en una lista. Esta lista la llam?? user_list. De esta forma puedo hacer seguimiento de los kanji que el usuario no conoce.

# Segundo paso
Para el segundo paso lo que hice fue crear la GUI que usar?? para la app. Utilic?? el m??dulo Tkinter para esto. Primero, establec?? algunos par??metros que us?? para la GUI. Escog?? un Kanji aleatorio de la lista user_list, y lo us?? como llave para buscar algunas definiciones en el diccionario con Kanjis. Luego, cre?? una ventana c??mo objeto Tk. Tambi??n cargu?? algunas im??genes que usar?? en el proyecto.

Despu??s de la ventana, cre?? un Canvas para las palabras tanto en japon??s como en ingl??s. Ya que lo primero que ver?? el usuario es el Kanji japon??s, us?? el m??todo create_text con el kanji en kanji_word y las pronunciaciones on'yomi y kun'yomi. Lo ??ltimo que necesitaba para la GUI eran los botones. Cre?? dos botones, uno para la opci??n "correcta" y uno para la opci??n "equivocada". Por ahora, estos botones no tienen un comando. Aqu?? est?? una imagen mostrando como queda la ventana hasta ahora.

![FlashCard example](./flashcard_example.png "Ejemplo de la tarjeta din??mica")

# Tercer paso
Despu??s del GUI, necesitaba una funci??n que despu??s de tres segundos "girara" la tarjeta para mostrarle al usuario el significado del Kanji en ingl??s.
Defin?? una funci??n llamada flip_card que cambia los objetos en el canvas por su versi??n en ingl??s. En el caso de las pronunciaciones on'yomi y kun'yomi, us?? espacios en blanco para que no aparezca nada en el canvas. Tambi??n tuve que a??adir un m??todo after d??nde cre?? el objeto para la ventaja, de forma que mi funci??n se ejecute 3000 ms despu??s de que inicie el c??digo.
Cu??ndo la tarjeta se gire, el canvas se ver?? as??

![FlashCard example](./flashcard_example2.png "Ejemplo de la tarjeta din??mica")

# Cuarto paso
Lo ??ltimo que hice fue crear las funciones para cada bot??n. La funci??n para el bot??n de incorrecto es la m??s f??cil, ya que s??lo necesito que "voltee" la tarjeta de regreso y que ponga un nuevo Kanji. Defin?? una funci??n llamada new_word, que hace exactamente eso. Tomar un nuevo Kanji de forma aleatoria de la lista user_lust y cambiar todos los objetos en el canvas de vuelta al japon??s. Ahora, cada vez que el usuario haga click en el bot??n "incorrecto", la tarjeta din??mica girar?? y mostrar?? un nuevo Kanji.

Para el bot??n de "correcto" defin?? otra funci??n llamada known_word. Esta funci??n sacar?? el Kanji de la lista user_list, y guardar?? la lusta como un archivo csv, de esta forma el Kanji no aparecer?? de nuevo para el usuario. Despu??s de esto, la funci??n llamar?? a la otra funci??n new_word para que aparezca un nuevo kanji en el Canvas.

Tuve que a??adir una condici??n IF a la funci??n known_word que verifica la longitud de la lista user_list. Si no hay objectos en la lista, la ventana se cerrar??.
Si el usuario desea comenzar desde cero, solo debe borrar el archivo <ins>delete the kanjis_to_learn.csv </ins> en la carpeta Data
