# 100 Days of Python
## Project 18: Turtle Drawing project.

The objective of this project is to recreate the drawing from the image using the Turtle module.
In the beginning are some commented out lines of code, which I used to understand a bit the methods in the Turtle module.

First of all, I created the canvas for the project using the Screen class. Then I focused on the logic for the turtle to paint a pattern pretty similar to the one in the picture.
I made a function called hor_drawing that will paint dots from left to right in an horizontal line separated equally. After this, I made a loop that will move the turtle up certain distance and reset the turtle position to the left, so it can paint again. This repeats until all the canvas is fully painted with dots.

The dots will have random colors, but not just any random colors. To simulated the drawing from the picture as close as possible, I used a module called Colorgram. In the Cologram module there is a method that can extract colors from the image. With colorgram.extract I can get an object with RGB colors as attributes. Making these attributes as tuples, I can have a list of all the random colors from the image. I popped up the first two elements from the list, because they are most likely the backgroud colors from the image, which I don't really need. 
I also made a function that will created random RBG color tuples, but using this function will created too many random color dots, and although it was somewhat similar, I wanted an image really close to the original.

This project is really good for getting used to the turtle module, which will be used in the following project. It is a really good module for creating visual objects using in games, or tools, or other things. I found this module really fascinating and enjoyed a lot using it in my projects.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
