
# Some strings
a = "hello world"
b = "hello world 2"
c = " "
d = "4546"

""" String Formating Operations """

a.capitalize()          # Makes the first letter of first word to Upper Case
"hello".capitalize()    # This a valid statement too, can use the same format for all

a.upper()               # Convert all the alphabets in the string to upper case

a.lower()               # Convert all the alphabets in the string to lower case

a.title()               # Convert all the first letters of the words present in a given string to upper case

a.casefold()            # Convert the string to lower case

""" String Conditional Operators """

a.istitle()             # Check whether a given string is in title format i.e, first letter of every word is in upper case

a.isupper()             # Check whether every alphabet is upper case

a.islower()             # Check whether every alphabet is lower case

a.isspace()             # Check whether a given string comatains only bkank spaces

a.isalnum()             # Checks whether a given string conatains only alphabets or numbers

a.isalpha()             # Check if all the characters in a string are alphabets or not

a.isdigit()             # Check if all the characters in a string are numbers or not

a.count("e")            # Count the number of occurances of a given character or a substring
a.count("lo")           # Valid statement

a.endswith("d")         # Checks whether a given string ends with the specified character or sub-string

a.find("h")             # Search for a given character or a sub-string and returns its index, returns -1 if not found

a.index("h")            # Search for a given character or a sub-string and returns its index, throws an error if not found

"".join([a,b,c])        # Joins the string passed together
",".join([a,b,c])       # Joins the strings passed and inserts a comma between them
" ".join([a,b,c])       # Joins the strings passed and inserts a blank space between them 

a + b + c               # Joins the strings in the specified order

