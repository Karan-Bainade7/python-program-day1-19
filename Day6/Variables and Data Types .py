# Variables
# Variables are containers for storing data values.

# Creating Variables
# Python has no command for declaring a variable.

# A variable is created the moment you first assign a value to it.


a=10
b="karan bainade"
print(a);
print(b);
print(type(a));
print(type(b));


a=20
name="karanbaiande"
per=85.43
love_to_kirti=True
print(type(love_to_kirti));
print(type(per));
print(type(a));
print(type(name));

'''
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.'''

'''
Python Keywords
Python has a set of keywords that are reserved words that cannot be used as variable names, function names, or any other identifiers:
Keyword	Description


and	A logical operator
as	To create an alias
assert	For debugging
break	To break out of a loop
class	To define a class
continue	To continue to the next iteration of a loop
def	To define a function
del	To delete an object
elif	Used in conditional statements, same as else if
else	Used in conditional statements
except	Used with exceptions, what to do when an exception occurs
False	Boolean value, result of comparison operations
finally	Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for	To create a for loop
from	To import specific parts of a module
global	To declare a global variable
if	To make a conditional statement
import	To import a module
in	To check if a value is present in a list, tuple, etc.
is	To test if two variables are equal
lambda	To create an anonymous function
None	Represents a null value
nonlocal	To declare a non-local variable
not	A logical operator
or	A logical operator
pass	A null statement, a statement that will do nothing
raise	To raise an exception
return	To exit a function and return a value
True	Boolean value, result of comparison operations
try	To make a try...except statement
while	To create a while loop
with	Used to simplify exception handling
yield	To return a list of values from a generator'''

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

myname="karan"

my_name="karan"
_myname="karna"
MYNAME="KARAN"

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

x,y,z="karan","arjun","ram"
print(x);
print(y);
print(z);

x=y=z= "karan"
print(x);
print(y);


# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

# Example
# Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


girls=["komal","kirit","kalyani","renu","pooja","shravni","kajal","kangana","rahni"]
karan_girlfriends=girls
print(karan_girlfriends);


fruits =["apple","banana","cherry"]
x,y,z= fruits
print(x);
print(y);
print(z);


p="python is awsome language"
print(p);

#In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

k="pytohn"
p="is"
o="fantastic language"
print(k,p,o);


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = "John"
print(x + y)# we can not added interger and stirng to connect eash other

x = 5
y = "John"
print(x , y)



# Python Data Types
# Built-in Data Types
# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType




#In Python, the data type is set when you assign a value to a variable:


x = "Hello World"	#str
myname="karan punamsing bainade" #str
print(myname);

x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	

y=["karan","arjun","ram","sham","jaam"]


x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	

y={}
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType