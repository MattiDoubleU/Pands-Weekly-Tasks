# Python accounts
# Author: Matthias Wiedemann

# Created variable for account number using input (as it is a prompt) & string function as account numbers are stored as strings
# Use negative indexes to start the slice from the end of the string (as we want to display last 4 digits of acc number)
# Display first 6 digits as 'X', I simply created another variable masked_account number = letter X multiplied by 6 since we are maskind the first 6 digits
# Added \t for good measure

accountnumber = str(input("\tPlease enter 10 digit account number: "))
masked_accountnumber = 'X' * 6 + accountnumber[-4:] # display last 4 digits of account number
print(f"\tAccount number is {masked_accountnumber}")

# Extra: The solution could be to use 'len()' function which is used to determine the length of a sequence or collection.
# It returns the number of characters in a string for example.

accountnumber = str(input("Please enter account number: "))
list_size = len(accountnumber) # defining variable list size with 'len()' function to allow unlimited length of input string.
masked_accountnumber = 'X' * list_size + accountnumber[-4:]
print(f"Account number is {masked_accountnumber}")

# I couldn't figure out how to make Xs represent the masked numbers minus the visible digits.
# Update: I copied the below code from https://stackoverflow.com/questions/52408105/masking-part-of-a-string. Looks like it does exactly that.

masked_accountnumber = len(accountnumber[:-4])*"#"+accountnumber[-4:]
print(f"Account number is {masked_accountnumber})