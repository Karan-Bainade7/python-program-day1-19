# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc


name="karan bainade"

for i in name:
    print(i);

my_fav_girls=['kirti','komal','punam','kajal','renu']
for my in my_fav_girls:
    print(my);
    for k in range(2):
        print(k+1);



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)



# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# Example
# Using the range() function:

for x in range(6):
  print(x)




# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.*imp*

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

# Example
# Using the start parameter:

for x in range(2, 6):
  print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

# Example
# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)


# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

# Example
# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")