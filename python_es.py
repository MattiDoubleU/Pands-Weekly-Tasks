# Python_es.py
# Author: Matthias Wiedemann
# This program reads in a text file and outputs the number of e's it contains.
# Stackoverflow.com guided me through the task: https://stackoverflow.com/questions/69319005/count-a-string-in-a-text-file-with-python.
# 1. I stored the text file in the same folder as the program. I took a text from an online portal and stored it as .txt via notepad++: A21.txt.
# 2. I wanted to have a look at text first before carrying out the count of letter 'E/e'.

# As per Topic07-files.ipynb files should be opened with the ``with open( filename, mode) as f: `` command

FILENAME = "A21.txt"
with open(FILENAME) as f:
    f=open("A21.txt","r", errors="ignore") # Initially I got an error (UnicodeDecodeError:) so asked a question in stackoverflow.com https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character.
    str =  f.read()
    print (str)

# Turned out that since there are Spanish characters in the text I would have to use this solution (encoding='utf-8'). Same source:

FILENAME = "A21.txt"
with open(FILENAME) as f:
    f=open("A21.txt","r",encoding='utf-8') 
    str =  f.read()
    print (str)


    
FILENAME = "A21.txt"
e = 0                                                 # To count the letter 'e' we would have to assign integer 0 to e.
with open("A21.txt", "r", encoding='utf-8') as f:
    for line in f:                                    # and initiate loop over the file.
        e += line.count("e")                          # Count() method returns the number of times as specified value appears in a string: https://www.w3schools.com/python/ref_string_count.asp
                                                      # 0e+1e=1e+1e=2e and so until loop finished.
print(f"There are {e} es in this text")


# I was worried this code would count lower case e's only or omit é so I modified the code:

FILENAME = "A21.txt"
é = 0                                                 
with open("A21.txt", "r", encoding='utf-8') as f:
    for line in f:                                    
        é += line.count("e")                          
                                                      
print(f"There are {é} E/es in this text")

# The result is the same. Python is clever : E or e,é, any variant of e = 0 without need for being told. :)
