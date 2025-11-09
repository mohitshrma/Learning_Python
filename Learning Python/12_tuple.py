# 🧠 What Is a Tuple? --> uses parantheses() 
# - Immutable: Once created, you cannot change, add, or remove elements.
# - Ordered: Elements maintain their position and can be accessed via indexing.
# - Allows duplicates: You can have repeated values.
# - Generally, defined with parentheses: Example: my_tuple = (1, 2, 3)
# IMP:- Tuples are created using commas, not parantheses. Parantheses improve readability but are not required.
# Trailing commas in multi-element tuples are optional.

# Basic tuple
t1 = (10, 20, 30)

# Tuple without parentheses (comma is key)
t2 = 10, 20, 30

# Single-element tuple (note the comma)
t3 = (10,)  # NOT (10)
t3_ = (10)  # NOT a Tuple

# Nested tuple
t4 = (1, (2, 3), [4, 5])


# 🔄 Converting Sequences to Tuples
# ✅ From a List
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)


# ✅ From a String
my_string = "abc"
my_tuple = tuple(my_string)
print(my_tuple)  # Output: ('a', 'b', 'c')


# ✅ From a Range
my_range = range(4)
my_tuple = tuple(my_range)
print(my_tuple)  # Output: (0, 1, 2, 3)

# ✅ From a Set (unordered)
my_set = {10, 20, 30}
my_tuple = tuple(my_set)
print(my_tuple)  # Output: (10, 20, 30) — order may vary


# 🧠 Why Use tuple()?
# - To freeze a sequence so it can’t be modified.
# - To use it as a dictionary key or in a set (since tuples are hashable).
# - To ensure data integrity in functions or APIs.


# t = tuple(5) ❌ TypeError: 'int' object is not iterable.
t = tuple([5])

# Empty tuple
# 1. 1st way[using empty parantheses]
empty = ()
print(type(empty))

# 2. 2nd way[using constructor]
empty = tuple()
print(type(empty))


# ✅ Key differences from lists
# 1. Tuples are immutable
# 2. Tuples use parantheses and Lists use square brackets
# 3. Tuples are generally faster and smaller than lists [prefer tuples if there is read-only data]
t = (0,1,2)
#t[1] = 3 #cannot modify because of immutable nature

# ✅ Immutability
t = (1,2,3)
# t = 11 ❌ Raises TypeError
# t.append(4) ❌ Raises AttributeError
# t.remove(1) ❌ Raises AttributeError
# del t[1] ❌ Raises TypeError

# Immutability applies to the tuple container, not the objects inside it.
t = (1,[2,3]) #list can be modified if its inside tuple.
t[1].append(4)
print(t)

# Immutable tuples can be used as keys in dictionaries or stored in sets
original_tuple = (1,2,3)
original_tuple = original_tuple + (4,5)
print(original_tuple)


# ✅ Accessing tuple elements
fruits = ("apple","banana","cherry","date","elderberry")
print(fruits[0])
print(fruits[-2])
# Slicing - [start:stop:step]
print(fruits[1:4])
print(fruits[::-1])
nested_tuple = ((1,2),(3,4),(5,6))
print(nested_tuple[0][1]) #2


# Tuples can store mixed(heterogeneous) types
t = (42, "hello", [1,2,3], {'key': 'value'})
print(t[3])



# ✅ Unpacking tuples
# 🔓 What Is Tuple Unpacking?
# --> It means extracting values from a tuple and assigning them to variables directly.

person = ("Alex", 25, "New York")
name, age, city = person   # Python does this by matching the structure(number of items) on both sides of the assignment.
print(name)  # Alex
print(age)   # 25
print(city)  # New York

# a, b = 1,2,3 ❌ Raises TypeError

a, *b = 1,2,3
print(a) # 1
print(b) # [2,3]

a, *b, c = 1,2,3,5,6   # *--> unpacking operator
print(a) # 1
print(b) # [2,3,4,5]
print(c) # 6


# We can unpack in every sequence like list, string and so on.
a, b = [1,2]
print(a,b)

a,b = "He"
print(a,b)


# ✅ Iterating tuples
fruits = ('apple','banana','orange')
for fruit in fruits:
    print(fruit)

# enumerate() --> built-in enumerate() function in Python always returns an iterator of tuples
# syntax:- enumerate(iterable, start=0)

colors = ('red','green','blue')
for index,color in enumerate(colors):
    print(index,color)
print()

colors = ('red','green','blue')
for index,color in enumerate(colors, start = 4):
    print(index,color)


# Example:-
pairs = [(1,'a'),(2,'b'),(3,'c')]
for number, letter in pairs:
    print(number, letter)



# ✅ Concatenation and Repetition

tuple1 = (1,2,3)
tuple2 = (4,5)   # tuple2 = tuple([4,5])
result = tuple1 + tuple2
print(result) # (1, 2, 3, 4, 5)

tuple1 = ('a',)
result = tuple1 * 3
print(result) # ('a', 'a', 'a')

colors = ("red","green","blue")
print("green" not in colors)


tuple_a = (1,2,3)
tuple_b = (1,2,3)
tuple_c = (1,2,4)

print(tuple_a == tuple_b)
print(tuple_a == tuple_c)
print(tuple_a < tuple_c)


# ✅ Methods - count & index

t = (1, 2, 3, 2, 4)

# Count occurrences of 2
print(t.count(2))  # Output: 2

# Find index of first occurrence of 3
print(t.index(3))  # Output: 2


