<img src="https://studenthub.atu.ie/assets/ATU_Logo.fa93bf0a.svg" alt="ATU Logo" width="300" height="100">

# This repository contains the weekly tasks for the Programming & Scripting module
***
## A total of 8 tasks had to be completed [(all copied from the course website)](https://vlegalwaymayo.atu.ie/course/view.php?id=8088)
***

## Weekly task 01:

For this week's tasks, 

Please post a simply introduction of yourself on teams, 
Install the required software on your machine,
Pull the sample code in my repository to your machine,
Create a GitHub account and repository for yourself (pands-mywork), and the weekly task (pands-weekly-tasks)
Commit and push a file to the weekly tasks repository called helloworld.py

This file should contain a python program that displays Hello World! when it is run.

Summary:
Based on the lecture and course material this task was very easy.


## Weekly task 02

When Banks are storing currency figures, they store them as integers (usually in cent).This is to avoid rounding errors. 

Write a program called bank.py 

The program should:

    Prompt the user and read in two money amounts (in cent)
    Add the two amounts
    Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

Summary:
Like weekly task01 I coud easily figure it out based what had been covered in class so far and on th course material.


## Weekly task 03

Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

Summary:
Weekly task03 was becoming significantly more challenging than the previous two tasks and required a bit fo research. Sources I used: \
 https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string \
 https://www.geeksforgeeks.org/python-string-length-len/ \
 https://www.codeease.net/programming/python/python-function-to-mask-part-of-string \
 https://stackoverflow.com/questions/52408105/masking-part-of-a-string


## Weekly task 04

Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

Push the program in your pands-weekly-tasks GitHub repository (like you do for all the weekly tasks).

Summary:
For weekly task04 I 'recycled' some lines of code from the sample code and lecture material of week04. Furthermore, I used the following references: \
 https://docs.python.org/3/tutorial/controlflow.html \
 https://stackoverflow.com/questions/2244270/get-a-try-statement-to-loop-around-until-correct-value-obtained \
 https://stackoverflow.com/questions/21837208/check-if-a-number-is-odd-or-even-in-python

I also have to admit that Dr Atul Kumar Ojha who lectures at University of Galway in NLP/ML helped me with the fine tuning of this code.


## Weekly task 05

Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)

You will need to search the web to find how you work out what day it is.

Summary:
As proposed by the lecturer I went straight to websearch to complete this task, found the sources listed below and helped myself with sample code from week04 if/else statement. \
 https://www.geeksforgeeks.org/python-datetime-weekday-method-with-example/ \
 https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date

## Weekly task 06

Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots. 

Summary:
Like for weekly task04, Dr Atul Kumar Ojha who lectures at University of Galway in NLP/ML assisted me in completing this task. Useful was also lecture material from topic04 flow-loops alongside the following references: \
 https://docs.python.org/3/library/functions.html \
 https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm \
 https://www.w3schools.com/python/gloss_python_indentation.asp?ref=blog.duy.dev \
 https://realpython.com/python-while-loop/


## Weekly task 07

Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.

The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.

Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.

Summary:
For this task course material from topic07 was very helpful but I also used different sources from the internet which are listed below. I decided to get a Spanish text from the internet for this task because Spanish has more variants of the letter E/e than English and I wanted to explore this a bit as part of the task. As prerequiste I saved the file A21.txt in the pands-weekly-tass folder. My conclusion is that python would indeed include any possible variant of the letter E/e, é etc. in the count with the code I used. Very interesting was the fact that due to special characters in the original text, I had to transform that the source text to Unicode-UTF8 first before being able to run a code on it. References: \
 https://stackoverflow.com/questions/69319005/count-a-string-in-a-text-file-with-python \
 https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character \
 https://www.w3schools.com/python/ref_string_count.asp 

## Weekly task 08

Write a program called plottask.py that displays:

    a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
    and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

Some marks will be given for making the plot look nice (legend etc).

Summary:
For this task I availed of the lecture material from week08 as well as from Ian's class -linspace()- and the following resources from the internet: \
 https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html \
 https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/ \
 https://www.geeksforgeeks.org/plot-mathematical-expressions-in-python-using-matplotlib/ \
 https://stackoverflow.com/questions/8209568/how-do-i-draw-a-grid-onto-a-plot-in-python 
