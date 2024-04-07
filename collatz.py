# collatz.py
# Author: Matthias Wiedemann

# For control flow keywords 'while, if, elif, else' are used and for exception handling 'try, except'.
# Be mindful of indentation: Python relies on indentation to define scope in the code.
# https://stackoverflow.com/ has helped me greatly with my weekly tasks.
# https://stackoverflow.com/questions/2244270/get-a-try-statement-to-loop-around-until-correct-value-obtained

while True: # Loop statement: True is a boolean value that always evaluates to true, so the loop will continue indefinitely unless a break statement is encountered or an exception is raised.
    try:    
        number = int(input("Please enter a positive integer: "))
        if number <= 0:
            print(f"{number} is not a positive integer.")
        else:
            while number != 1:                  # != is a comparison operator used to determine whether two values are not equal to each other.
                print(number, end=" ")          # In Python 3.x, end=' ' is used to place a space after the displayed string instead of a newline. 
                if number % 2 == 0:             # checks if a number is even. https://stackoverflow.com/questions/21837208/check-if-a-number-is-odd-or-even-in-python.
                    number = number // 2        # If even, divide by 2.
                else:
                    number = (number * 3) + 1   # If odd, multiply by 3 and add 1.
            print(1)                            # Print the final value which is always 1 (defined in line 7: number !=1)
            break                               # Exit the loop if input is valid.
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")


# Same thing again but without end=" ". The results will print each value in a new line.


while True: 
    try:    
        number = int(input("Please enter a positive integer: "))
        if number <= 0:
            print(f"{number} is not a positive integer.")
        else:
            while number != 1:                 
                print(number)         
                if number % 2 == 0:
                    number = number // 2        
                else:
                    number = (number * 3) + 1  
            print(1)                           
            break                             
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")