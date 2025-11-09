# A dictionary in Python is a built-in data structure that stores key-value pairs.
#It ’s like a mini database where each key maps to a value — super useful for organizing and accessing data efficiently.

# 🧠 Key Features of Python Dictionaries
# - Unordered (until Python 3.6+ where insertion order is preserved)
# - Mutable — you can add, update, or delete entries
# - Keys must be unique and immutable (like strings, numbers, tuples)
# - Values can be any type


#Example of dictionary:-

#1.✅ Creating a dictionary
# syntax:- 
    # dictionary_name = {key1:value1, key2:value2, key3:value3}

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

#Empty dictionary
d = {}

#Example:
fruits = {
    "apple":"red",
    "banana":"yellow",
    "grapes":"green"
}

# By using dict() function
c = dict(apple = "red", banana = "yellow", grape = "green")
print(c)

d = dict([('apple','red'),('banana','yellow'),('grape','green')])
print(d)

# using tuple as key in dictionary
# Example:-
my_dict_tuple_key = {
    (34.0522, -118.2437): "Los Angeles",
    (40.7128, -74.0060): "New York"
    }

#mixed dictionary:-
mixed = {
    1:"one",
    "two":2,
    (3,4):"tuple as key"
}


#2. ✅ Accessing dictionary elements
# Using square brackets []
# Using get() method

person = {'name': 'Alice', 'age':25}
print(person['name']) #prints Alice
print(person.get('age')) 
print(person.get('city', 'NA')) # finds city otherwise print NA


# Question: Create a dictionary, take input and access key using get() method
students = {'Alex':88, 'Max':87, 'Rex':86} 
key = 'peter' #input().title()
# print(students.get(key,"Not Found"))
if key in students:
    print(students[key])
else:
    print("Not Found")


print(student["name"]) #prints Alice



#✅ Modifying Dictionaries in python
person = {"name":"Alice", "age":25}
person['age'] = 26
person['city'] = 'New York'
print(person)
del person['city']
print(person)
print(person.pop('name')) #error if not found else use fallback
print(person)
person.clear()
print(person)

person = {"name":"Alice", "age":25}
person.popitem() #Removes and returns the last inserted key-value pair from the dictionary.
print(person)
print(person.pop('something','NA'))


'''
╔════════════╦══════════════════════════════════════════════════════════════╗
║  Method    ║ Description                                                  ║
╠════════════╬══════════════════════════════════════════════════════════════╣
║ del        ║ Deletes a specific key-value pair using its key.            ║
║            ║ Syntax: del dict[key]                                       ║
║            ║ Raises KeyError if key not found.                           ║
╠════════════╬══════════════════════════════════════════════════════════════╣
║ pop()      ║ Removes and returns the value of the specified key.         ║
║            ║ Syntax: dict.pop(key[, default])                            ║
║            ║ Raises KeyError if key not found and no default is given.  ║
╠════════════╬══════════════════════════════════════════════════════════════╣
║ popitem()  ║ Removes and returns the last inserted key-value pair.       ║
║            ║ Syntax: dict.popitem()                                      ║
║            ║ Raises KeyError if dictionary is empty.                     ║
╠════════════╬══════════════════════════════════════════════════════════════╣
║ clear()    ║ Removes all items from the dictionary.                      ║
║            ║ Syntax: dict.clear()                                        ║
╚════════════╩══════════════════════════════════════════════════════════════╝
'''


#Update method in dictionary
# -->  is used to merge another dictionary or iterable of key-value pairs into the current dictionary.

#Syntax:-
# dict1.update(dict2)
# dict1: The dictionary to be updated.
# dict2: The dictionary (or key-value iterable) providing updates.

profile = {'name':'Alice','age':25}
updates = {'age':26, 'city':'New York'}
profile.update(updates)
print(profile)


profile = {'name':'Alice'}
profile.update([('age',12),['city','New York']])
print(profile)

profile.update(country='Something') 
print(profile)


#✅ Dictionary Operations
student = {"name":"Jack", "age":22, "grade":"B"}
print("name" in student) #checks key not values
print("name" not in student)
print(len(student))
for i in student:
    print(i, student[i])


#Question:
data = {"a":1, "b":2}
print(1 in data) #provide false because it checks only key not value

#Example on how to access values in a nested dictionary
data = {
    "id":101,
    "info":{
        "name":"Bob",
        "city":"NY"
    }
}
print(data['info']['city'])
print(len(data))



# ✅ Dictionary Methods - keys(), values(), items()
# 1. keys()
student = {"name":"Alice", "age":21, "grade":"A"}
keys = student.keys() #similar to set
#Returns a view object containing all the keys of the dictionary.
student["city"] = "NY"
print(keys) #dict_keys(['name', 'age', 'grade', 'city']) --> Live reflection of Dictionary Changes

#2. values()
print(student.values()) #dict_values(['Alice', 21, 'A', 'NY'])


'''
╔════════════════════════════╦════════════════════════════════════════════════════════════════════╗
║        Feature             ║ dict_keys / dict_values view              vs. list(dict.keys())     ║
╠════════════════════════════╬════════════════════════════════════════════════════════════════════╣
║ Type                       ║ dict_keys / dict_values (view object)     vs. list (standard list)  ║
╠════════════════════════════╬════════════════════════════════════════════════════════════════════╣
║ Mutability                ║ Immutable view (reflects live changes)     vs. Mutable copy          ║
╠════════════════════════════╬════════════════════════════════════════════════════════════════════╣
║ Reflects dict changes     ║ Yes — updates if dict changes              vs. No — static snapshot  ║
╠════════════════════════════╬════════════════════════════════════════════════════════════════════╣
║ Supports indexing         ║ No                                         vs. Yes                   ║
╠════════════════════════════╬════════════════════════════════════════════════════════════════════╣
║ Supports iteration        ║ Yes                                        vs. Yes                   ║
╠════════════════════════════╬════════════════════════════════════════════════════════════════════╣
║ Memory efficient          ║ More efficient (no copy made)              vs. Less efficient        ║
╠════════════════════════════╬════════════════════════════════════════════════════════════════════╣
║ Use case                  ║ Best for checking membership or iterating  vs. Best for indexing     ║
╚════════════════════════════╩════════════════════════════════════════════════════════════════════╝
'''

# 3. items()
items = student.items()
print(items) #dict_items([('name', 'Alice'), ('age', 21), ('grade', 'A'), ('city', 'NY')])



# ✅ Iterating through Dictionaries
person = {"name":"Alice","age":30,"city":"New York"}
for i in person:
    print(i)
for key in person.keys():
    print(key)
for value in person.values():
    print(value)
for key,value in person.items():
    print(f"{key}:{value}")

#Question: In a dictionary, if a value is even, delete it.

#Incorrect way: Modifying While Iterating
# data = {"a":1, "b":2, "c":3}
# for k in data:
#     if data[k] % 2 == 0:
#         del data[k]
# print(data)

# Correct way: Iterate over a copy of keys
# for k in list(data.keys()):
#     if data[k] % 2 == 1:
#         del data[k]


# ✅Complex Data Structures

students = {
    "101": {"name":"Alice", "age":20, "grade":"A"},
    "102": {"name": "Bob", "age":22, "grade":"B"},
    "103": {"name": "Charlie", "age":21, "grade":"A-"},
}
print(students["101"]['name'])

for roll_no,details in students.items():
    for k,v in details.items():
        print(k,v)


profile = {
    "username":"jdoe",
    "details": {
        "name":"John Doe",
        "email":"john@example.com",
        "age":30
    }
}


# ✅ Merging in Dictionary (python 3.9+)

a = {'a':1}
b = {'b':2, 'a':11}

a = a | b # or a|= b
print(a)

print(a.get('c','NA'))

#setdefault() --> retrieve the value of a key if it exists(and sets the value as well)
print(a.setdefault('c',123)) 
print(a)



#✅ Dictionary comprehension

# Syntax:-
# {key_expression: value_expression for item in iterable if condition}

res = {}
for i in range(1,11):
    if i % 2 == 0:
        res[i] = i ** 2
    else:
        res[i] = i ** 3
print(res)

# Rewriting above part using dictionary comprehension [sqaure for even, cube for odd]
res = {i:i**2 if i % 2 == 0 else i ** 3 for i in range(1,11)}
print(res)

#Question:Use dictionary comprehension to print sqaure for even numbers from 1 to 10.
even = {i:i**2 for i in range(1,11) if i % 2 == 0}
print(even)


#Example: List of tuple, needs to be converted to a dictionary
students = [("Max",82),("Alex",90), ("Charles",78)]
res = {i:j for i,j in students}
print(res)

#Question: Swap keys to values and vice-versa using dictionary comprehension
original = {'a':1, 'b':2, 'c':3}
res = {j:i for i,j in original.items()}
print(res)

# Question: Create a multiplication table from 1 to 5 using nested dictionary comprehension.

# Using traditional approach
res = {}
for i in range(1,6):
    inner_dict = {}
    for j in range(1,11):
        inner_dict[j] = i * j
    res[i] = inner_dict

for i in res:
    print(f"{i}: {res[i]}")


# Using dictionary comprehension
res = { i:{j:i*j for j in range(1,11)} for i in range(1,6)}
for i in res:
    print(f"{i}: {res[i]}")



#✅ Shallow and deep copy

student = {
    "name":"Rahul",
    "marks":[90,85,88]
}
# another_student = student
# student["marks"].append(99)
# print(student)
# print(another_student)


# shallow copy
another_student = student.copy() 
student["marks"].append(99)
print(id(student))
print(id(another_student))


#deep copy
import copy
student = {
    "name":"Rahul",
    "marks":[90,85,88]
}
another_student = copy.deepcopy(student)
another_student["marks"].append(99)
print(student["marks"])
print(another_student["marks"])

###### Use case of Dictionary ############

# - ✅ Store structured data (e.g., user profiles, settings)
# - 📊 Count occurrences (e.g., word frequency, vote tally)
# - 🔑 Map keys to values (e.g., student grades, product prices)
# - 🧭 Replace switch/case logic
# - 🧬 Represent nested data (e.g., JSON-like structures)
# - 🧠 Cache results (e.g., memoization in recursion)
# - ⚙️ Store configuration or environment settings
# - 📅 Group related data (e.g., logs by date, tasks by category)
# - 🔍 Fast lookup for values by key
# - 📦 Pass flexible parameters to functions (e.g., **kwargs)



######## INTERNAL WORKING OF DICTIONARY ############

# Hash Table --> special type of array

# 🧠 Internal Working of Python Dictionary

# 1. Hashing the Key
# - When you insert a key-value pair, Python computes the hash value of the key using the built-in hash() function.
# - This hash value determines where the key-value pair will be stored in memory.

# 2. Bucket Allocation
# - The dictionary maintains an array of buckets.
# - Each bucket can hold one entry: a combination of the key’s hash, a pointer to the key object, and a pointer to the value object.

# 3. Index Calculation
# - The hash value is converted into an index using modulo operation with the current size of the bucket array.
# This index tells Python where to place the key-value pair.

# 4. Collision Handling
# • If two keys hash to the same index (a collision), Python uses open addressing with probing to find the next available slot.
# • This ensures that all entries are stored without overwriting.

# 5. Resizing
# • Dictionaries start with a small number of buckets (typically 8).
# • When the load factor (number of entries vs. bucket size) exceeds a threshold, the dictionary resizes—doubling the number of buckets to maintain performance.

# 6. Lookup
# • To retrieve a value, Python hashes the key again, calculates the index, and checks the bucket.
# • If the key is not found at the expected index, it probes nearby buckets until it finds the key or confirms it’s missing.

# 7. Deletion
# - When a key is deleted, Python marks the bucket as dummy (not empty but not active).
# - This helps maintain probing integrity during future lookups.


# Note:- Probing is a technique used in hash tables to resolve collisions by searching for the next available
        #  slot when two keys hash to the same index.


student = {
    "name":"Rex",
    "age":30,
    "grade":"C"
}

# index = hash("name") % size_of_hash_table
index = hash("name") % 8
print(index)

index = hash("age") % 8
print(index)

index = hash("grade") % 8
print(index)

# if we use get() method, same procedure will repeat, calculate hash() function, find index and locate element.
student.get("name")
index = hash("name") % 8

# If collision occurs, python has internal mechanism that solves it.



# 📌 Key Properties of hash() function
# - Only works with immutable objects: Mutable types like lists or dictionaries will raise a TypeError.
# - Hash values are not guaranteed to be consistent across sessions: Python randomizes hash values between runs for security.
# - Used internally by Python: For example, dictionary keys are hashed to determine their storage location.


# ✅ When to Use Dictionary vs Set in Python
# - If you need unique keys with associated values, use a dict.
# - If you need unique keys only, use a set.
