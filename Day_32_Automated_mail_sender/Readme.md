# 100 Days of Python
## Project 32: Automated mail sender

In this project I will be making a program that will send automated email under certain conditions.

I used the SMTP [(Simple Mail Transfer Protocol)](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol), which is an internet standard communication protocol used for mail transfer. 

Again I first practiced in another file. In the mail_connect folder I used the datatime module and the smtplib Library to send an email with a motivational phrase every monday. 

The project is in the birthday_wisher folder. This project will take data from a CSV file containing data from different birthdays. Here you can add information from more people you want to send a birthday email to. 

I used the pandas, datetime, random ans smtplib Libraries. In the letter_templates folder are three TXT files which will be randomly used to send different birthday messages.

I defined my email and my email password as variables. To use your own personal email just change these variables. With the datetime method now, the code will always have the actual date. Then, I read the csv file with the read_csv method. I used dictionary comprehension to check if there is any birthday date that is the same as today's date. Each date found this way will be stored in a dictionary. 

The final step is to loop through each item in the dictionary. If there are no items, I printed a message and the code ends. If there is data in the dictionary, with the random module I picked a template randomly and changed the placeholder [NAME] with the person's name. Finally, with the SMTP method, I sent the email.

There could be some issues when sending the email. You need to set the email protections to low, so the SMTP has no problem connecting to the email. 

I found this library really convenient when you need to send automated emails, or emails in determined dates.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 100 Días de Python
## Proyecto 32: Enviador automático de correos

En este proyecto estaré haciendo un programa que enviará correos de forma automática bajo ciertas condiciones.

Utilicé el SMTP []

I used the SMTP [(Protocolo para transferencia simple de correo)](https://es.wikipedia.org/wiki/Protocolo_para_transferencia_simple_de_correo), que es un protocolo estándar de comunicación por internet usado para la transferencia de correos.

Nuevamente, primero practiqué en otro archivo. En la carpeta mail_connect utilicé el módulo datetime y la librería smtplib para envíar un correo con una frase motivacional todos los días lunes.

El proyecto está en la carpeta birthday_wisher. este proyecto tomará información de un archivo CSV que contiene datos de distintos cumpleaños. Aquí puedes añadir información de más personas a las que quieras envíar un correo de cumpleaños.

Utilicé las librerías pandas, datetime, random y smtplib. En la carpeta letter_templates hay tres archivos TXT que usaré de forma aleatoria para enviar distintos mensajes de cumpleaños.

Definí mi correo y la contraseña del correo como variables. Para usar tu correo personal sólo debes cambiar estas variables. Con el método now de datetime, el código siempre tendrá la fecha actual. Luego, leí el archivo CSV con el método read_csv. Utilicé comprensión de diccionarios para verificar si había algún cumpleaños con la misma fecha del día de hoy. Cada fecha encontrada de esta manera será guardada en forma de diccionario.

El paso final es buscar en un bucle por cada objeto en el diccionario. Si no hay objetos, solo imprimí un mensaje y el código termina. Si existen datos en el diccionario, con el módulo random seleccioné una carta base y reemplacé la palabra marcador [NAME] con el nombre de la persona. Finalmente, con el método SMTP, envié el correo.

Puede haber algunos problemas cuando se envía el correo. Necesitas predeterminar las protecciones del correo en bajo, para permitir al protocolo SMTP conectarse al correo sin problemas. 

Encontré esta librería muy conveniente cuando necesitas mandar correos de forma automática, o en fechas determinadas.
