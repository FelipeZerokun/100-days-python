# 100 Days of Python
## Project 1４: Higher-Lower Game.

Another project game. Here, the user must guess which celebrity has more followers on Instagram. The user can keep guessing correctly, accumulating win streaks. If the user fails, the game ends and the win streak goes back to 0.
The celebrities data in on a different file called game_data.py. The data may be a bit outdated from actual numbers, but works the same. This project shows how really useful can dictionaries be as data structures. 
If you check the game_data.py file, you will see that all the dictionaries have the same "keys" names, but different values. This is really useful when you need to call different dictionaries from a list using the same keywords.

For this project, I define a function that takes three arguments that will compare the data from the file with what the user entered. It will return which celebrity has more followers and if the user's guess was correct.

The first thing I did, is to randomly take two celebrities from the data's list, and I named then option_A and option_B. Here the game begins, the options are showed to the user, and if the user guesses correctly, the option_B will replace option_A and the program will randomly pick a new celebrity from the data file as a new option_B, and so on. If the program were to choose the same celebrity that is already in the option_A, it would again randonly choose another celebrity until it is different from the option_A. This is done by comparing the key values "name" from each diccionary.

This project is really good to practice how to manage the data inside of dictionaries. Here I realized how I can use dictionaries inside of a list to organize similir kind of data, and how I can manage this data with ease.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 1４: Juego de Mayor o menor.

Otro juego como proyecto. Aquí, el usuario debe adivinar cuál celebridad tiene más seguidores en Instagram. El usuario puede continuar adivinando correctamente, acumulando rachas de victoria. Si el usuario falla, el juego termina y las rachas de victoria vuelven a 0.
Los datos de las celebridades están en un archivo distinto llamado game_data.py. Los datos pueden estar un poco desactualizados de los números actuales, pero funciona de igual manera. Este proyecto muestra qué tan útil pueden ser los diccionarios como estructuras de datos.
Si se revisa el archivo game_data.py, se puede observar que todos los diccionarios tienen nombres "keys" iguales, pero valores distintos en cada uno. Esto es realmente útil cuando necesitas traer datos de diccionarions dentro de una lista usando la misma palabra clave.

Para este proyecto, yo definí una función que toma tres arguments y que va a comparar los datos de los archivos con lo que el usuario ingresó. Luego va a retornar cuál de las celebridades tiene más seguires y si el intento de adivinar del usuario estuvo correcto.

La primera cosa que hice, fue tomar dos celebridades aleatoreamente de la lista de datos, y los llamé option_A y option_B. Aquí el juego empieza, y se muestran las opciones al usuario. Si el usuario adivina correctamente, la option_B reemplazará la option_A, y el programa escogerá randómicamente una nueva celebridad de los archivos de datos como nueva option_B, y así sucesivamente. Si el programa llegara a escoger la misma celebridad que ya está en la variable option_A, el programa escogerá nuevamente a otra celebridad hasta que sea una distinta a la option_A. Esto se logra al comprar los valores llave "name" de cada diccionario.

Este proyecto es realmente bueno para practicar el manejo de datos dentro de los diccionarios. Aquí puede entender cómo usar diccionarios dentro de listas para organizar información semenjante, y cómo manejar estos datos con facilidad.
