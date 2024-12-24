# Slicing
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.

# ExampleGet your own Python Server
# Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5]);

love="kirti and karan love each other.";
print(love[0:21]);

# Slice From the Start
# By leaving out the start index, the range will start at the first character:
b = "Hello, World!"
print(b[:5])



# Slice To the End
# By leaving out the end index, the range will go to the end:

# Example
# Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])


# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example
# Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])


# String Methods
# Python has a set of built-in methods that you can use on strings.

#immutable string hm use change nhi kr sakte bhai 

# Note: All string methods return new values. They do not change the original string.

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

nm="karan bainade"
mm="@"
print(nm.count("karan"));
print(nm.upper());
print(nm.capitalize());
print(nm.strip());
print(nm.join(mm));


b = "HelloWorld"
print(len(b));
print(b[-6:-2])
#4:8-->>owor

karan_item="kirti_fulpagar"
print(len(karan_item));
print(karan_item[-6:-3]);
#total lengh is 14 so 14-6 & 14-3-->>8:11
#8:11-->lpa


b = "Hello, World!"
print(b[:2])
b = "Hello, World!"
print(b[2:])


a = "Hello, World!"
print(a.upper());
print(a.lower());
print(a.strip());#Remove Whitespace
print(a.replace("llo","nkoc"));


# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.

a = "Hello"
b = "World"
c = a + b
print(c);


# Example
# To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b #IN TWO WORLS HAVE SPACE BETWEEN THEM TO USED IT.
print(c);

# age = 36
# txt = "My name is Karan Bainade, I am  older  "+ age +"years"
# print(txt); #output-->>TypeError: must be str, not int





# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
# Example
age=23
txt= f"my name is karan bainade  and i am older {age} years."
print(txt);


#Placeholders and Modifiers  *IMP*
#A placeholder can contain variables, operations, functions, and modifiers to format the value.
love=2022
my=f"i love to kirit since {love} year."
print(my);

x=50
print(f'The price is {x:.2f} dollars')  #output-->>>>50.00




# Escape Character
# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

txt = "We are the so-called \"india\" from the maharashtra."
print(txt);

#join method

# Syntax
# string.join(iterable)
myTuple = ("karan", "arjun", "amsas_puri")

x = "Welcome ".join(myTuple)
y=" Your Happy Day, "
x=y.join(myTuple)
print(x)


#find() method
# Where in the text is the word "welcome"?:

txt = "Hello, welcome to my world."

x = txt.find("welcome")
# print(len(txt));

print(txt)



# Syntax
# string.translate(table)

# Python String translate() Method

# ExampleGet your own Python Server
# Replace any "S" characters with a "P" character:

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  90}

txt = "Hello Sam!"

print(txt.translate(mydict))