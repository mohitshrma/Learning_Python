# String is a sequence of characters enclosed within quotes

name = 'Alex'

# Letters, Numbers, Special Symbols, Whitespace characters and Unicode characters

print("\u0061")
print("\U0001F600")

language = 'Python'
#   P    y    t      h       o       n
#  [0]  [1]  [2]     [3]     [4]     [5]  <- Position / Indices

print(language[3])

print("1 + 2") # String so, can't be evaluated

print(1 + 2 * 3) # evaluation happens using BODMAS rule


name1 = 'Python'
name2 = "Python"
print(name1 ==  name2)

# When to use single quotes vs double quotes in String words/characters.
# 1. If your string has single quote within the word, use double quotes to enclose.
message = "Don't be late"
message = 'Don\'t be late' #using escape sequence
print(message)

# 2. If your string has double quotes within the word, use single quote to enclose.
dialogue = 'She said, "Java is not an OOP language."'
dialogue = "She said, \"Java is not an OOP language.\""
print(dialogue)

#Escape sequence \n for new line
poem = "Roses are red, \nViolets are blue, \nmy love increases forever, \njust for you"
print(poem)

#Multi-line String using triple quotes (single or double both)
poem1 = '''Roses are red,
Violets are blue,
so is my love,
deep for you'''
print(poem1)

#Question: Print this line (C:\Users\Vipul\Documents)
task = "C:\\Users\\Vipul\\Documents"
print(task)


### String Conactenation #######

a = 1
b = 2

print(a + b)

first_name = "Alex"
last_name = "Gregg"
print(first_name,last_name)

age = 26
message = "My age is " + str(age)
print(message)

#Question 2 : Concat string with int value
city = "New York"
temp = 75
weather_report = "The temperature in " + city + " is " + str(temp)+ " farenheit"
print(weather_report)

# Better way to do it using f String. It automatically converts any other type to String
weather_report = f"The tempearture in {city} is {temp} farenheit"
print(weather_report)

a = 5
b = 10
print(f"The sum of {a} and {b} is {a + b}")

name = "Patrick"
print(f"The first character of {name} is {name[0]}")

# This is a curly brace: {
print(f"This is a curly brace:{{")
print(f"This is a curly brace:}}")

a = 3
res = a * 3
print(res)

# Star pattern to print box
star = "*"
print((star * 5 + "\n") * 5) 

# Multiplying String value to zero gives empty string
a = "Java"
print(a * 0) #empty string
print(a)
print(a * -1) #empty string

# Question: print this 'PyPythonthon'
print("py" * 2 + "thon" * 2)



#len --> length function in python
a = "Pyhton"
length = len(a)
print(length)

print(len(""))
print(len("Hello\nWorld"))

msg = "Help!"
print(len(msg) == 5)

print("apple" == "apple")
print("apple" == "Apple")
print("apple" == "orange")
print("apple" != "orange")
print(1 < 2)
print(11 > 2)
print(15 <= 8)
print(23 >= 9)

# These operators compare lexicographically
print("a" < "b")
print("apple" < "banana")
print("apple" > "Apple")
print("apple" < "ape")

print(ord("a")) # 97
print(ord("A")) # 65
print("\u0061") # a



###### String Indexing and Slicing ###########

language  = "PYTHON"
# print(language[len(language)]) will give string index out of bounds error

print(language[len(language) - 1])


# String:     P   Y   T   H   O   N 
# Index:      0   1   2   3   4   5
# Neg Idx:    -6  -5  -4  -3  -2  -1

print(language[-3]) 

# string[start:end]
# start --> inclusive, end ---> exclusive

txt = "Python Programming"
slice = (txt[0:6]) 
slice3 = (txt[:6]) # we can remove starting index(auto from 0 index)
print(slice, slice3)    # output--> Python
 
# Question: Print programming only from above text using slicing
slice1 = (txt[7:18])
slice2 = (txt[7:]) # if we want till end, we can remove the last index as well.
print(slice1, slice2)

#Pro
print(txt[7:10]) #positive slicing
print(txt[-11:-8]) #negative slicing


# string[start:end:step]
print(txt[0:6:2]) # prints Pto from 'Python' skipping 1 character


# A negative step traverses the String into reverse direction
print(txt[::-2]) #start,end,-2 for 2 step

#Reverse a string
reverse = (txt[::-1])
print("reverse string is", reverse)


#### String methods ###

demo = "Python in Ai"
print(demo.upper()) # converts to upper case
print(demo.lower()) # converts to lower case
print(demo.title()) #converts to Title Case
print(demo.capitalize()) #converts first character of entire string to Capital

words = "   hello python programming   "
print(words.strip()) #removes spaces from whole string
print(words.lstrip()) #removes spaces from starting of the string
print(words.rstrip()) #removes spaces from ending of the string


#string.find(substring,start,end)
text = "Python is amazing, Python is fun"
idx = text.find("is") # helps to find the substring or character in a string
idx1 = text.find("is",18) 
print(idx)
print(idx1)

#string.count(substring,start,end)
print(text.count("P")) #count number of occurences of character/substring in a string
#string.index(substring,start,end)
# The .index() method is similar to .find() but raises a ValueErrorif substring is not found.

email = "AlexJoegmail.com"
print(email.find("@")) #help to filter/condition

# string.replace(old, new, count)
text = "Hello World"  
replaced = text.replace("World", "Python") 
print(replaced)

text = "banana banana banana"
print(text.replace("banana", "apple",2))

text1 = "Python"
text2 = "Python3"
print(text1.isalpha()) #returns true if all the characters are alphabet, no numeric character is there
print(text2.isalpha()) #returns false since all characters are not alphabet, there is one numeric character

print(text1.isalnum()) #returns true (alpha-numeric - either letter or number)
print(text2.isalnum()) #returns true (alpha-numeric - either letter or number)

text1 = "2322"
text2 = "2python"
print(text1.isdigit()) #returns true since given value is digit
print(text2.isdigit()) #returns false since given value is not digit


#islower(), isupper()
print(text1.islower())
print(text2.isupper())

txt = "  "
print(txt.isspace())


#startswith(), endswith()
text = "Python is amazing"
print(text.startswith("Python"))    #True
print(text.startswith("is"))      #False
print(text.endswith("amazing"))     #True
print(text.endswith("core"))        #False
print(text.endswith("is", 0, 9))

#split() --> splits down words and converts to list 
text = "apple,banana,orange,grape"
print(text.split(","))
sentence = "Python is fun to learn"
print(sentence.split(" "))

#join() --> concatenate any number of string along with separator
li = ['apple','banana','orange','grape']
newtext = ",".join(li)   # the string are joined using comma
print(newtext)

#.format() method
name  = "Alex"
age = 30
message = "Hello my name is {} and my age is {} ".format(name,age)
print(message) 

message = "Hello my name is {0} and my age is {1} - {0} ".format(name,age)
print(message)

message = "Hello my name is {p1} and my age is {p2}".format(p1=name, p2=40)  
print(message) 


# Old style formatting with % operator
# syntax -> "string with format specifier" % values

name = "Alice"
greeting = "Hello, %s!" % name
print(greeting)


# %s - String(or any object with a string representation)
# %d - Integer
# %f - Float
# %x - Hexadecimal
# %o - Octal
# %.2f - Float with precision (2 decimal places in this example)

#example:
age = 25
message = "I am %d years old." %age
print(message)

name = "Bob"
age = 30
message = "My name is %s and I am %d years old." %(name, age)
print(message)

pi = 3.14159265359
print("Pi rounded to 2 decimal places: %.2f" %pi)


#String Immutability 
s = "Hello"
print(id(s))
#s[0] = "M" wont work
print("M" + s[1:])
s = "M" + s[1:]
print(id(s)) 


#Raw Strings (Even if escape sequence is used, it will print it as it is)
rs = r"Hel\lo"
print(rs)

print(r"C:\Users\Name\Documents")

# odd \ --> escape closing quote
# even \ --> doesn't escape closing quote


#Practice Question 1: String Method Chaining
#strip, capitalize the first letter of each word, and replace "SKILLS" with "Expertise"
text = " python programming SKILLS "
print(text.strip().title().replace("Skills","Expertise"))

#Question 2: Advanced Slicing Challenge
# Print every second character using slicing
# Print the string in reverse order using slicing
# Extract and print just "Programming" using negative indices
s = "Python Programming Language"
second = s[::2]
print(second)

reverse = s[::-1]
print(reverse)

neg = s[-20:-9]
print(neg)

#Question 3: String concatenation and slicing
# Create a new string by extracting the first letter of each word and concatenating them
text = "python is easy to learn"
result = text[0] + text[7] + text[10] + text[15] + text[18]

#Question 4: String Palindrome Check
#pop, madam, radar
word = "madam"
reverse_word = word[::-1]
print(reverse_word == word)

#Question 5: Find count occurrences of 'i','s','p', and 'm' in given text.
text = "mississippi"
print(text.count("i"), text.count("s"),text.count("p"),text.count("m"))

count_i = text.count("i")
count_s = text.count("s")
count_p = text.count("p")
count_m = text.count("m")

print(f"i: {count_i}")
print(f"s: {count_s}")
print(f"p: {count_p}")
print(f"m: {count_m}")