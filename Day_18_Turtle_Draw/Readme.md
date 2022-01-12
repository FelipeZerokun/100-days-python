# 100 Days of Python
## Project 18: Turtle Drawing project.

The objective of this project is to recreate the drawing from the image using the Turtle module.
In the beginning are some commented out lines of code, which I used to understand a bit the methods in the Turtle module.

First of all, I created the canvas for the project using the Screen class. Then I focused on the logic for the turtle to paint a pattern pretty similar to the one in the picture.
I made a function called hor_drawing that will paint dots from left to right in an horizontal line separated equally. After this, I made a loop that will move the turtle up certain distance and reset the turtle position to the left, so it can paint again. This repeats until all the canvas is fully painted with dots.

The dots will have random colors, but not just any random colors. To simulated the drawing from the picture as close as possible, I used a module called Colorgram. In the Cologram module there is a method that can extract colors from the image. With colorgram.extract I can get an object with RGB colors as attributes. Making these attributes as tuples, I can have a list of all the colors from the image. I popped up the first two elements from the list, because they are most likely the backgroud colors from the image, which I don't really need. 
I also made a function that will created random RBG color tuples, but using this function will created too many random color dots, and although it was somewhat similar, I wanted an image really close to the original.

This project is really good for getting used to the turtle module, which will be used in the following projects. It is a really good module to create visual objects using them in games, or tools, or other things. I found this module really fascinating and enjoyed a lot using it in my projects.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 100 Días de Python
## Proyecto 18: Proyecto de dibujo con Turtle

El objetivo de este proyecto es recrear el dibujo de la imagen usando el módulo Turtle.
Al inicio hay algunas líneas de código comentadas, las cuales usé para entender un poco los métodos del módulo Turtle.

Primero que nada, cree un canvas para el proyecto con la clase Screen. Luego me enfoqué en la lógica para que la "tortuga" pintara un patrón muy similar al que está en la imagen.
Hice una función llamada hor_drawing que pintará puntos de izquierda a derecha en una línea horizontal separados equitativamente. Después de esto, hice un bucle que moverá la tortuga hacia arriba cierta distancia y reiniciará la posición de la tortuga hacia la izquierda, para que pueda pintar nuevamente. Esto se repite hasta que todo el canvas esté pintado con puntos.

Los puntos van a tener un color aleatorio, pero no cualquier color. Para asemejar la pintura en la imagen tanto como se pueda, utilicé un módulo llamado Colorgram. En el módulo Colorgram hay un método que puede extraer los colores de una imagen. Con colorgram.extract puedo obtener un objeto con solos colores RGB como atributos. Convirtiendo estos atributos en vectores, puedo hacer una lista con todos los colores de la imagen. Saqué los primeros dos elementos de la lista ya que lo más probable es que sea colores de fondo de la imagen, que no necesito.
También hice una función que crea colores en formato RGB aleatorios, pero usando esta función creaba puntos de colores demasiado aleatorios, y a pesar de que era un poco simmuilar, yo quería que la imagen se pareciera mucho más a la original.

Este project es muy útil para aconstumbrarse al módulo Turtle, que será usado en los siguientes proyectos. Es un muy buen módulo para crear objetos visuales usándolos en juegos, o herramientas, u otras cosas. Encontré este módulo fascinante y disfruté mucho usarlo en mis proyectos.
