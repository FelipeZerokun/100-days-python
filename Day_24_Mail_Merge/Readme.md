# 100 Days of Python
## Project 24: Mail merge.

We did a bit of file editing in the Snake game project, where we wrote on a txt file every time the user got a new highscore.
Now, in this proyect we will have a closer look on how to open, modify, replace and more on external files.

I uploaded two folders again, one with some practice with the methods, and the second with the actual mail merge project.

In the text_practice folder in only one main.py file. Here you can see how I practice a bit with the "with" and "as" keywords for writing and editing some txt files.

Now for the project, the main objective is to created files like mails, where we take a list of names and replace the word placeholder "[name]" with each name. This is helpful when you need to send the same letter to different persons. There are several folders in the project so we could practice folder pathings as well.

To begin, we just need a txt file with the names of all the people we want to send the letters. In the project, this list is inside the folder Names, inside of the folder Input. In this folder is also the folder Letters, which cointain the base letter file. Notice that in the base letter text is the placerholder "[name]".

I will save all the letters in a folder called ReadyToSend, inside of the Output folder.

The project is quite simple. In the main.py file I firstly open the name list with the "with" and "as" keywords. I do it this way to save some code lines, because only using the "open" method, I should close the file later. The with and as keywords close the file as soon as the code in the indented lines is over.
After is open the file, I use the method readlines to get all the names inside the txt file in a list.

Now I used another "with" and "as" to open the base letter. I save the text in the file in a variable called starting_letter. Now, with a FOR loop I will replace the PLACEHOLDER in the starting letter with the actual name in the name list, and save that text as a new variable. Now I will use the open method to open the text where the letter will be stored. If the file with that name does not exist, the method will create a new file with that name. I use the method write to insert the text into the file I just created.
Since I am in a FOR loop, this will be done for all the names in the list.

Now all the new letters will be in the destination folder, each one with a name in the list.

This was a pretty interesting project that shows how Python can be used to do repetitive tasks. We learnt how to open files, how to read what's inside of those files, and how we can edit or replace data from the files. So far, we have only used txt files, but in the next project we will try with other files as well.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


