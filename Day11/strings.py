# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".

# You can display a string literal with the print() function:

print("karan is python developer");
print('karan is software develoepr');
a=("who are you?")
print(a, "i am software developer");


karan='''helllo \n my name is karan bainade. \n i am form maharashtra.'''
print(karan);
# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
tell_me_about_your_self='''my name is karan bainade. 
i am from mh india. 
i have completed UG from hi-tech institute of technology.'''
print(tell_me_about_your_self);

print("""karan is
      software develoepr in it company in banguluru.""");

#index concept start with 0 string index like array index wise.but not array.
profession="engineering"
print(profession[2]);
print(profession[9]);
print(profession[5]);
print(profession[3:7]);

print(profession[2:5]);


a = "Hello, World!"
print(a[1]);

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

# Example
# Loop through the letters in the word "banana":

for m in "karan":
  print(m);
for engg in "cse_branch":
  print(engg);

for x in "banana":
  print(x)


for k in "karan bainade":
  print(k);

for karan in "love to kirti":
  print(karan);# the output show  in horizantal form

#String Length
# To get the length of a string, use the len() function.

# Example
# The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

name="karan punamsing bainade"
print(len(name));




# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

# Example
# Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("karan" in txt);

relative_name="arjun,mmama,mammi,,kaki,papa,mummy,bhau,vahini,kaka,baba,aaji"
print("baba"in relative_name);

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.");
