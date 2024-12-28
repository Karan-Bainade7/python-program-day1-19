'''List Methods
list.sort()
This method sorts the list in ascending order. The original list is updated

Example 1:
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)
Output:
['blue', 'green', 'indigo', 'voilet']\
[1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]
 
What if you want to print the list in descending order?
We must give reverse=True as a parameter in the sort method.

Example:
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)
Output:
['voilet', 'indigo', 'green', 'blue']
[9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1, 1]
The reverse parameter is set to False by default.

Note: Do not mistake the reverse parameter with the reverse method.

reverse()
This method reverses the order of the list.

Example:
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)
Output:
['green', 'blue', 'indigo', 'voilet']
[7, 9, 8, 2, 1, 2, 1, 6, 3, 5, 2, 4]
index()
This method returns the index of the first occurrence of the list item.

Example:
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))
Output:

1
3
count()
Returns the count of the number of items with the given value.

Example:
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
Output:
2
3
copy()
Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

Example:
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)
Output:
['voilet', 'green', 'indigo', 'blue']
['voilet', 'green', 'indigo', 'blue']
append():
This method appends items to the end of the existing list.

Example:
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)
Output:
['voilet', 'indigo', 'blue', 'green']
insert():
This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

Example:
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)
Output:
['voilet', 'green', 'indigo', 'blue']
extend():
This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

Example 1:
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)
Output:
['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
Concatenating two lists:
You can simply concatenate two lists to join two lists.

Example:
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
Output:
['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']'''



l=[20,1,7,3,2,5,7,12,7,18]
l.sort()
l.append(19)
l.reverse()
print(l.index(7))
print(l.count(7))
print(l)
# print(numbers.sort())


#Here’s a list example with several methods commonly used in Python to manipulate lists. We'll use the list:

'''
list_values = [2, 4, 5, 6, 9, 8, 1, 5, 2, 9, 8]
List Methods and Examples:
append() - Adds an item to the end of the list.

python
Copy code
list_values.append(7)
print(list_values)  # Output: [2, 4, 5, 6, 9, 8, 1, 5, 2, 9, 8, 7]
insert() - Inserts an item at a specific index.

python
Copy code
list_values.insert(3, 10)  # Insert 10 at index 3
print(list_values)  # Output: [2, 4, 5, 10, 6, 9, 8, 1, 5, 2, 9, 8]
remove() - Removes the first occurrence of a value.

python
Copy code
list_values.remove(5)  # Removes the first 5
print(list_values)  # Output: [2, 4, 10, 6, 9, 8, 1, 5, 2, 9, 8]
pop() - Removes and returns the item at a specific index (default: last item).

python
Copy code
popped_value = list_values.pop(2)  # Removes the value at index 2
print(popped_value)  # Output: 10
print(list_values)  # Output: [2, 4, 6, 9, 8, 1, 5, 2, 9, 8]
count() - Counts the occurrences of a specific value.

python
Copy code
count_of_9 = list_values.count(9)
print(count_of_9)  # Output: 2
index() - Returns the index of the first occurrence of a value.

python
Copy code
index_of_8 = list_values.index(8)
print(index_of_8)  # Output: 4
sort() - Sorts the list in ascending order.

python
Copy code
list_values.sort()
print(list_values)  # Output: [1, 2, 2, 4, 5, 6, 8, 8, 9, 9]
reverse() - Reverses the order of the list.

python
Copy code
list_values.reverse()
print(list_values)  # Output: [9, 9, 8, 8, 6, 5, 4, 2, 2, 1]
copy() - Creates a shallow copy of the list.

python
Copy code
copied_list = list_values.copy()
print(copied_list)  # Output: [9, 9, 8, 8, 6, 5, 4, 2, 2, 1]
clear() - Removes all elements from the list.

python
Copy code
list_values.clear()
print(list_values)  # Output: []
Full Example:
python
Copy code
list_values = [2, 4, 5, 6, 9, 8, 1, 5, 2, 9, 8]
print("Original list:", list_values)

# Append
list_values.append(7)
print("After append:", list_values)

# Insert
list_values.insert(3, 10)
print("After insert:", list_values)

# Remove
list_values.remove(5)
print("After remove:", list_values)

# Pop
popped = list_values.pop()
print("After pop:", list_values, "| Popped value:", popped)

# Count
print("Count of 9:", list_values.count(9))

# Sort
list_values.sort()
print("After sort:", list_values)

# Reverse
list_values.reverse()
print("After reverse:", list_values)

# Copy
copied = list_values.copy()
print("Copied list:", copied)

# Clear
list_values.clear()
print("After clear:", list_values)'''