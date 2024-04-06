# This repository contains the weekly tasks for the Programming & Scripting module
# A total of 8 tasks had to be completed (all copied from the course website)
# Weekly Tasks 1:

For this week's tasks, 

Please post a simply introduction of yourself on teams, 
Install the required software on your machine,
Pull the sample code in my repository to your machine,
Create a GitHub account and repository for yourself (pands-mywork), and the weekly task (pands-weekly-tasks)
Commit and push a file to the weekly tasks repository called helloworld.py

This file should contain a python program that displays Hello World! when it is run.

# Weekly Tasks 02

When Banks are storing currency figures, they store them as integers (usually in cent).This is to avoid rounding errors. 

Write a program called bank.py 

The program should:

    Prompt the user and read in two money amounts (in cent)
    Add the two amounts
    Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

# Weekly Task 03

Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

# Weekly task 4

Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

Push the program in your pands-weekly-tasks GitHub repository (like you do for all the weekly tasks).

# Weekly Task 05

Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)

You will need to search the web to find how you work out what day it is.

# Weekly task 6

Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots. 

# Weekly task 7

Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.

The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.

Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.

# Weekly Task 8

Write a program called plottask.py that displays:

    a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
    and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

Some marks will be given for making the plot look nice (legend etc).