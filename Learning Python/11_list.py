# In Python, a list is an ordered, mutable collection that can hold elements of any type.
# use square bracket --> []

# 🔹 Key Features of list:
# - ✅ Ordered: Elements maintain insertion order.
# - ✅ Mutable: You can add, remove, or change items.
# - ✅ Indexed: Access elements by position.
# - ✅ Heterogeneous: Can contain mixed types (e.g., integers, strings, other lists).
# - ✅ Iterable: Can be looped over using loops or comprehensions

my_list = [1,2,3,4,5]

# Empty list
empty = []

# List of strings
colors = ["red","green","boolean"]

# List of Booleans
flags = [True, False, True]

# List of mixed types
mixed_list = [1,"hello",3.14,False]

# List inside a list(nested)
nested = [[1,2],[3,4],[5,6]]

# Create a list in python built-in constructor --> list()
# example 1: empty list using list() constructor
li = list() 

# example 2: create a list of items using constructor but must be iterable(like string,set,tuple,list)
li = list("Hello")
print(li)

#using set to create list
s = {10,20,30}
lst = list(s)
print(lst)

# using range() function to create list
print(list(range(10)))

# can copy original list to another list
original_list = [4,3,88,999]
copied_list = list(original_list)
print(copied_list)


# Indexing in list
fruits = ['apple','banana','cherry']
print(fruits[2])


#slicing in list --> [start:stop:step]
numbers = [10,20,30,40,50]
print(numbers[1::])
print(numbers[1:22]) # does not give error, rather provides flexibility even in out of range scenario
print(numbers[len(numbers)-1])
print(numbers[::-1]) #reverse a list using slicing

# Question: use negative indexing to find last three numbers
print(numbers[-3:])


#### Modifying list ######

fruits = ['apple','banana','cherry']
#fruits[1] = 'blueberry'
#fruits[1:3] = ["blueberry","kiwi"] can even slice using indexes 
print(fruits)

# adding in a list using append() method at the end
fruits.append('mango')
print(fruits) #['apple', 'blueberry', 'cherry', 'mango']

#inserting in a list in given position using insert() method
fruits.insert(3, "banana")
print(fruits) #['apple', 'blueberry', 'cherry', 'banana', 'mango']

# To extend one list to another list using extend() method
fruits_2 = ["grapes","kiwi"]
fruits.extend(fruits_2)
print(fruits) #['apple', 'blueberry', 'cherry', 'banana', 'mango', 'grapes', 'kiwi']

# To remove item from list using remove() method --> takes value as an argument
fruits.remove("kiwi")
print(fruits) # ['apple', 'blueberry', 'cherry', 'banana', 'mango', 'grapes']

# To remove item from list using pop() method --> takes index as an argument (by default takes -1)
fruits.pop(-2) 
print(fruits) #['apple', 'blueberry', 'banana', 'mango', 'grapes']

del fruits[1:3] #is used to delete elements from a list by index — or even delete the entire list. It’s not a method of the list object, but a built-in statement.
print(fruits) #['apple','mango','kiwi']

fruits.clear()
print(fruits) # []



########## Shallow copy vs Deep copy in Python ##########

# 1. Shallow copy --> Creates a new object, but references the same inner objects (one level deep)
# 2. Deep copy --> Creates a new object and recursively copies all nested objects

# 🔍 When to Use
# - Shallow Copy: Fine for flat structures or when you want shared references.
# - Deep Copy: Safer for nested structures where changes to one shouldn't affect the other.



a = [1,2,3]
b = a
b.append(4) 
print(a)  #[1, 2, 3, 4]


a = [1,2,3]
b = a[:] #creates a shallow copy of a flat list
b.append(4) 
print(a)    #[1,2,3] 
print(b)    #[1,2,3,4] 


#nested-list(two-dimension list)
a = [[1,2],[3,4]]
b = a[:]
b[0][0] = 99
print(id(a[0]), id(b[0])) #same id(object reference)
print(b) 
print(a)
 

import copy
b = copy.deepcopy(a)
print(id(a[0]), id(b[0])) # different id(object reference)

# 🧰 Tools
# - copy.copy(obj) → Shallow copy
# - copy.deepcopy(obj) → Deep copy


# 🧪 Example in Python
#  import copy

# original = [[1, 2], [3, 4]]

# shallow = copy.copy(original)
# deep = copy.deepcopy(original)

# original[0][0] = 99

# print("Original:", original)   # [[99, 2], [3, 4]]
# print("Shallow:", shallow)     # [[99, 2], [3, 4]] ← inner list changed
# print("Deep:", deep)           # [[1, 2], [3, 4]] ← fully independent




##### Operations in List ######

# Concatenation of a list
a = [1,2,3]
b = [4,5]
result = a + b
result1 = a + b + [6]
print(result, result1)

#multiplication of list
a = [0,1]
print(a * 3)    # [0, 1, 0, 1, 0, 1]

a = [0] * 5
print(a) #[0, 0, 0, 0, 0]

# Check if any string is available in the list using 'in' operator(True or False)
fruits = ['apple','orange','cherry']
print('banana' in fruits)
print('apple' not in fruits) 

print("he" in "hello")


#Example:
nested = [[0] * 3] * 3
print(nested) #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]



print(len([1,2,3,[4,5]])) # --> 4
numbers = [10,5,8,3]
print(min(numbers)) # min() --> find minimum element of the list
print(max(numbers)) # max() --> find maximum element of the list
print(sum(numbers)) # sum() --> calculates sum of all elements of the list
names = ["Alice","Bob","Charlie"]
print(min(names)) # compares alphabet-wise(lexicographically)
print(max(names))
print(ord("l"), ord("L")) # provides ASCII value of both 


# More list methods

# 1. Reversing & Sorting

# reverse() --> list method, modifies original list, works only on lists, returns none
# reversed() --> built-in function, original remain unchanged, works with any iterable(list,string,tuple), returns reversed iterator

nums = [1,2,3,4]
nums.reverse()
print(nums)


print(list(reversed(nums)))


words = ['banana','apple','cherry']
words.sort() # works on same list
print(words)
words.sort(key = len, reverse = True)
print(words)

words = ['banana','apple','cherry']
sorted_words = sorted(words, key = len, reverse = True) #sorted() returns a new list
print(sorted_words)

#custom_sorting
#Example 1:- Sorting according to absolute value
nums = [-10,5,-3,2,-1]
nums.sort(key=abs) #key based on absolute value
print(nums)  #[-1, 2, -3, 5, -10]

#Example 2:- Sorting based on alphabetical(Lower type)
names = ["Alice","ALice","Charlie"]
print(sorted(names, key=str.lower,reverse=True))

#Example 3:- count() method to count number of occurrences of elements in a list
fruits = ['apple','banana','banana','cherry','apple']
print(fruits.count('apple')) 
print(fruits[1:3].count('banana'))

#Example 4:- index() method of list
print(fruits.index('cherry'))
print(fruits.index('apple',1,5))


############ Iterating a list #############
# Using for loop
for fruit in fruits:
    print(fruit)
print()

# Using index
for i in range(len(fruits)):
    print(fruits[i])

# Example:- To count number of apple in given list
c = 0
for fruit in fruits:
    if(fruit == 'apple'):
        c+=1
print(c)

# Example:- To find out the index of element 'orange' in given list
f_index = 0
for i in range(len(fruits)):
    if fruits[i] == 'orange':
        f_index = i
        break
print(f_index)

# Example:- To loop over an list, reversed it and add it to the empty list
reversed_list = []
for fruit in reversed(fruits):
    reversed_list.append(fruit)
print(reversed_list)
    
# Example:- Find the minimum number from the given list 
nums = [4,5,60,72,1,3,9]
min_num = nums[0]
for i in nums:
    if min_num > i:
        min_num = i
print(min_num)



####### Nested List #########

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][0]

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
print()

# Example: Iterate by Index
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()


# Note: using _ in for loop to indicate you are not using any variable while iterating(useful in python community)

good = []
li = [0,0,0]
for _ in range(3):
    good.append(li[:])
good[0][0] = 1
print(good)


#### == vs is #######
    # == --> value comparison
    # is --> reference comparison

a = [1,2,3]
b = [1,2,3]
 
print(a == b) #True
print(a is b) #False

b = a
print(a is b) #True


########### List Comprehension ###########

#By using loop
li = [1,2,3,4,5,6,7]
res = []
for i in li:
    res.append(i ** 2)

#By using list comprehension

# Syntax:-
# [expression for item in iterable if condition]

# another way to do it:- res = [expression for item in iterable]
# Example:- Find square of numbers of list
res = [i**2 for i in li]

#Example:- To find square of first ten natural numbers
res = [i**2 for i in range(1,11)]
print(res)

# Example:- Print even numbers from 1 to 10.
even_res = [i**2 for i in range(1,11) if i%2==0]
print(even_res)

# Using ternary opearator for above using if-else
res = [i**2 if i%2==0 else i for i in range(1,11)]
print(res)

#Question:Make combination of two different list
drinks = ['coffee','tea']
desserts=['cake','coffee','ice cream']

res = []
for i in drinks:
    for j in desserts:
        res.append((i,j))
print(res)

#Another way using list comprehension
res = [(i,j) for i in drinks for j in desserts]
print(res)


# Question:- Given a sentence, extract those words whose length is greater than 5 and convert those words into uppercase.

text = "Python list comprehension is powerful and concise"
words = text.split()
res = [word.upper() for word in words if len(word) > 5]
print(res)

    