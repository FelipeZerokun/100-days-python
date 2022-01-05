# 100 Days of Python
## Project 8: Ceaser cipher

A Ceaser Cipher is a cipher method that takes each word from a phrase and shifts them with another letter placed a number of spaces down the alphabet.
This project lets the user encrypth or decrypt a phrase given by the same user. 

There should be two modes for the cipher. Encode and Decode modes. The encode mode will be used to cipher a clear message by shifting the letters to the right position in the alphabet. The Decode mode should take a encrypted message and turn it normal by shifting the letters to the left position in the alphabet.

For this, the first thing the code must have is a list with all the letters of the alphabet in perfect order. English alphabet has 26 letters.

The first thing the program will do is ask the user if he wants to enconde or decode a message. Then it will prompt the user to enter the message. Finally, it will ask the user how many spaces to shift the message. One of the problems here is if the user enters a number bigger than 26, because it will exceed the size of the alphabet list and will end up in an error. Using the modulo operator (%) I can get the remainder of a division. In this case, if I get the remainder of the number of shifts divided by 26, I will always get a number between 0 and 25.
With all the information, I can loop between every letter in the message shifting their position to the left or right some number of times according to what the user wants. In the case I go beyond the letter "z" I will loop back to "a" and viceversa.

This project is a good example where even when the code logic seems perfect, problems would still appear. I had to try many, many times with different messages and compare the result I expected with the one I got. So I could undestand what my code lacked.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 8: cifrado César.

El cifrado César es un método de cifrado que toma cada letra de una frase y la desplaza un determinado número de espacios en el alfabeto.
Este proyecto le permite al usuario codificar o decodificar una frase dada por el mismo usuario.

Debe haber dos modos para el cifrado. Codificar o decodificar. El modo de codificación será usado para codificar un mensaje claro al desplazar las letras hacia la derecha en el alfabeto. El modo de decodificar deberá tomar un mensaje encriptado y regresarlo a la normalidad desplazando las letras hacia la izquierda en el alfabeto.

Para esto, lo primero que el código debe tener es una lista con todas als letras del alfabeto en perfecto orden. El programa está hecho para traducir mensajes en inglés, así que uso el alfabeto inglés con 26 letras.

La primera cosa que el programa hace es preguntarle al usuario si quiere codificar o decodificar un mensaje. Luego le pedirá el mensaje. Finalmente, le preguntará al usuario cuántos espacios en blanco quiere que se desplacen las letras. Uno de los problemas aquí es cuando el usuarui ingresa un número mayor a 26, ya que excederá el tamaño de la lista con el alfabeto y esto llevará a un error. Utilizando el operador módulo (%) puedo obtener el residuo de una divisióin. En este caso, si obtengo el resudio del número de desplazamientos dividido para 26, siempre tendré un número entre 0 y 25. 

Con toda la información, hice un bucle dónde desplazo cada letra dentro del mensaje hacia la derecha o izquierda el número de veces indicado por el usuario. En caso de que me desplazó más allá de la letra "z", regreso a la letra "a" y viceversa.

Este proyecto es un buen ejemplo dónde incluso cuándo la lógica parece perfecta, ciertos problemas pueden aparecer. Me tocó intentar muchas, muchas veces con distintos mensajes y comparar el resultado que yo esperaba con el resultado que realmente obtuve. Para así entender qué le faltaba a mi código
