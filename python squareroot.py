# python squareroot.py
# Compute the square root of a positive floating-point number using Newton's method: Xn+1 ​= 0.5 ​(Xn​+N/Xn​​).
# With help of stackoverflow.com. and my housemate who lectures NLP/ML at University of Galway.
# Author: Matthias Wiedemann
# Indentation is crucial as it serves as a means of defining the structure and hierarchy of code blocks. 

def sqrt(number):                       # Creating function 'sqrt' as per task instruction and based on Newton's method.       
    
    if number < 0:                      # If defined condition (positive number) not met raise exception:
        raise ValueError("Please enter a positive number")  # ValueError is an exception class that applies when type (floating number) is correct but with an inappropriate value (negative in this case).

    X = number / 2                      # Defining variable 'X' which is initial guess for the square root, input number divided by 2.

    while True:                         # If condition is met (true) loop (while) until desired outcome (approximation of the square root of the input number) using Newton's method until convergence:
        
        N = 0.5 * (X + (number / X))    # Defining variable 'N' which is next guess.
        
        if abs(N - X) < 0.00001:        # Check if the difference between consecutive guesses is very small using function 'abs'(Return the absolute value of argument) and '<0.00001' to indicate the
                                        # the difference between X & N is smaller than 0.0001, when this condition is met, iteration can stop (approximation converged).
            return N                    # Exit function and return final result of the square root approximation to the caller of the function.
        
        X = N                           # When first bloc of code is executed the result in 'N' is assigned to 'a' to reiterate operation until condition defined in line 18 is met.

# Continuously prompt the user to enter a number until a valid input is provided (positive floating number). This is achieved by creating a 2nd loop (while):
while True:
    string = input("Please enter a positive floating point number: ")   # Creating variable 'string' and assinging to any input for potential errors caused by invalid input.
    try:                                                                # 'try' statement is used for exception handling. It allows to define a block of code in which exceptions may occur, and then specify how to handle those exceptions.
        number = float(string)                                          # Defining variable 'number' which is a float, if not prompt user as per function 'except' below.
        if number <= 0:                                                 # If negative as per line 30 (this line).
            print("Please enter a positive number.")
        else:                                                           # If correct, condition (positive floating number) is met iteratation of approximation starts as defined above.
           
            approximation = sqrt(number)                                                # Variable 'approximation' is the final result of function 'sqrt'
            print(f"The square root of {number} is approximately: {approximation:.2f}") # Printing two floating points (rounded) only: '.2f'.
            break                                                                       # Exit the loop if a valid input is provided
    except ValueError:                                                                  # If input is not a number as per line 28.
        print("Invalid input. Please enter a valid positive floating point number.")
