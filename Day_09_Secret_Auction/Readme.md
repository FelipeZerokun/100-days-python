# 100 Days of Python
## Project 9: Secret Auction

This project will let different users enter a value, and in the end the user that entered the biggest value wins. Just like an auction!
I used dictonaries for the users and their bids. It is a great way to keep two different values together. For example, the user_01 bid $50, I want these two values to always be correlated. I defined a function that asks for the name and bids from different users, gets them in a dictionary and then adds the dictionary to a list where all the users with their own bids will be kept.
The program will keep asking for new names and bids until a user confirms no new entries. After this, using a for loop I checked every bid in the list, and returned the name of the user with the higher bid.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 9: Subasta secreta

Este proyecto le permite a diferentes usuarios ingresar un valor, y al final el usuario que haya ingresado el mayor valor gana. !Igual que una subasta!
Utilicé diccionarios para los usuarios y sus apuestas. Es una gran forma de mantener dos valores distintos juntos. Por ejemplo, el usuario user_01 apostó $50, yo quiero que estos dos valores estén siempre correlacionados. Definí una función que pide el nombre y la cantidad que va a apostar a cada usuario, y los añade en un diccionario. Luego añade ese diccionario a una lista dónde todos los usuarios y sus apuestas correspondientes van a estar guardados.
El programa seguirá pidiendo por nuevos usuarios y sus apuestas hasta que un usuario confirme que no hay nuevos ingresos. Después de esto, usando un bucle FOR comparo los valores de las apuestas y regreso el nombre del usuario con la mayor apuesta.
