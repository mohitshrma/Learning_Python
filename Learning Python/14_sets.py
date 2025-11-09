# ✅ What is a Set?
# unordered, unindexed, mutable, unique, heterogeneous

# ✅ Key characteristics of Python Sets

# Python Set Characteristics
# - Unordered: No guaranteed order of elements
# - Unique elements: Automatically removes duplicates
# - Mutable container: You can add or remove items, should have mutable items
# - Immutable items: Elements must be hashable (e.g., int, str, tuple)
# - Fast membership testing: Much faster than lists
# - No indexing or slicing: Unlike lists or tuples


#✅ Creating a Set
# A. Set Literals {} 
# B. set() constructor

#Examples:-
numbers = {1,2,3,4,5}
names = {"Max","Alex","Charlie"}
mixed = {1,"hello",3.14, True}
print(numbers)

# Empty set - IMPORTANT: you cannot use {} for empty set
# e = {} # This creates an empty dictionary, not a set!
e = set() # Rather use set constructor to create empty set

# Duplicates are automatically ignored
s = {1,3,4,5,23,2,1,3,4,5}
print(s)

#s = {1, "Hello", True, (1,2,4), [1,3,5]} #throws error--> unhashable type [list,number,boolean not supported]
#print(s)


# The set() function creates a set from an iterable (like a list, tuple, or string).
list_data = [1,2,3,4,5,1,2,3]
set_from_list = set(list_data)
print(set_from_list)

text = "hello"
set_from_string = set(text)
print(set_from_string)

tuple_data = (1,2,4,5,2)
set_from_tuple = set(tuple_data)
print(set_from_tuple)

empty_set = set()
print(type(empty_set))
print(len(empty_set))

s = set(range(1,6))
print(s)

# ✅ Set Operations
my_set = {1,2,3}
print("Original:", my_set)

# using add() to add 1 element only
my_set.add(4)
print("After adding 4:", my_set)
my_set.add(2)
print("After adding 2 again:", my_set)

# Using update() to add multiple elements
my_set.update([5,6,7])
print("After update with list:", my_set)
my_set.update("abc")
print("After update with string:", my_set)
my_set.update([8,9],{10,11},"xy")
print("After multiple updates:", my_set)

'''
remove(element): Removes element, raises Keyerror if not found
discard(element): Removes element, does nothing if not found
pop(): Removes and returns an arbitrary element
clear(): Removes all element
'''

my_set = {1,2,3,4,5}
my_set.remove(3)
print("After removing 3:", my_set)
# my_set.remove(33) --> raises keyerror
my_set.discard(33)
print(my_set.pop()) #random value is removed
print(my_set)

# Membership testing
fruits = {"apple","banana","orange","grape"}
print("apple" in fruits)


# ✅ Mathematical Set Operations

# 1. Union --> use | (pipe operator)
set_a = {1,2,3,4}
set_b = {3,4,5,6}
union_result1 = set_a | set_b
print("Union using | :",union_result1)

# By using union() method
union_result2 = set_a.union(set_b)
print("Union using union():", union_result2)

# Multiple union
set_c = {7,8,9}
union_multiple = set_a | set_b | set_c
print("Multiple union of three sets using |", union_multiple)

#Union with other iterables (only union() method)
union_with_list = set_a.union([10,11,12])
print("Union with list:", union_with_list)

#Example:-
user1_interests = {"movies","books","music"}
user2_interests = {"music","sports","travel"}
user3_interests = {"games","coding","cooking"}

all_interests = user1_interests | user2_interests | user3_interests
print("Union interest combined :", all_interests)


# 2. Intersection --> use &(and) operator
set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}
intersection_result = set_a & set_b
print("Intersection using &: ", intersection_result)

#By using intersection() method
intersection_result2 = set_a.intersection(set_b)
print("Intersection using intersection():",intersection_result2)

set_c = {3,4,5,9,10}
intersection_multiple = set_a & set_b & set_c 
print("Intersection of three sets:", intersection_multiple)

set_d = {10,11,12}
empty_intersection = set_a & set_d
print("Empty intersection:", empty_intersection)

#Example:-
developer1_skills = {"python","java","sql","git"}
developer2_skills = {"python","javascript","sql","docker"}
developer3_skills = {"python","sql","mongodb","react"}

common_skill = developer1_skills & developer2_skills & developer3_skills
print("Common skill: ", common_skill)

# 3.Difference --> use -(minus) sign
set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}
difference_result = set_a - set_b
print("Difference of two sets using - : ", difference_result)

difference_result2 = set_a.difference(set_b)
print("Difference of two sets using difference(): ", difference_result2)

set_c = {2,3,9,10}
difference_multiple = set_a - set_b - set_c
print("Difference of multiple sets using -:", difference_multiple)

# 4. Symmetric difference --> ^ symbol
set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}
sym_difference_result = set_a ^ set_b
print("Symmetric Difference of two sets using ^ : ", sym_difference_result)

sym_difference_result2 = set_a.symmetric_difference(set_b)
print("Difference of two sets using symmetric_difference(): ", sym_difference_result2)


# 5.issubset() method
set_a = {1,2,3}
set_b = {1,2,3,4,5}
set_c = {1,2}
print("A is subset of B:", set_a.issubset(set_b))
print("B is subset of A:", set_b.issubset(set_a))
print("C is subset of A:", set_c.issubset(set_a))

# 6.issuperset() method
print("A is superset of A:", set_b.issuperset(set_a))
print("B is superset of B:", set_a.issuperset(set_b))
print("C is superset of C:", set_a.issuperset(set_c))

# <= operator
# --> This operator checks if the left set is a subset of (or equal to) the right set.
print("A <= B:", set_a <= set_b)
print("A <= A:", set_a <= set_a)
print("C <= A:", set_c <= set_a)
print("A < A:", set_a < set_a)
print("C < A:", set_c < set_a)

 
set_a = {1,2,3}
set_b = {4,5,6}
set_c = {3,4,5}
print("A and B are disjoint:", set_a.isdisjoint(set_b))
print("A and C are disjoint:", set_a.isdisjoint(set_c))
print("B and C are disjoint:", set_b.isdisjoint(set_c))

#same as isdisjoint()
print(len(set_a & set_b) == 0)
#Empty set is disjoint with any set

# ✅ Copying sets
original_set = {1,2,3}
new_set = original_set
new_set.add(4)
print(original_set)

new_set = original_set.copy()
new_set.add(5)
print(original_set)

# 🧬 Why Deep Copy Has No Real Use in Sets
# ✅ Sets in Python contain only immutable, hashable elements — like int, str, or tuple.
# - These elements cannot be changed, so there's no nested structure to recursively copy.
# - A shallow copy is enough because there's nothing deeper to copy.


# ✅ Iterating over sets with loops

set_a = {1,2,3}
for i in set_a:
    print(i)
print()

numbers = {1,2,3,4,5}
for i in numbers:
    if i%2 == 0:
        print(i)

# ✅ Frozen Sets --> Frozensets are immutable versions of sets

regular_set = {1,2,3,4,5}
frozen_set = frozenset(regular_set)

print("Regular set:", regular_set)
print("Frozen set:", frozen_set)

# Sample frozen sets
frozen_set = frozenset([1, 2, 3])
other_set = frozenset([3, 4, 5])

# Length
print("Length of frozen set:", len(frozen_set))

# Membership
print("Is 2 in frozen set?", 2 in frozen_set)

# Union
print("Union:", frozen_set | other_set)

# Intersection
print("Intersection:", frozen_set & other_set)


#frozen_set.add(5)
#frozen_set.remove(1)

mutable_set = {1,2,3}
immutable_set = frozenset([1,2,3])

print("Sets are equal:", mutable_set == immutable_set)
print("Sets are equal:", mutable_set is immutable_set)


# Comparison of set vs frozenset in Python

# | Feature               | set                          | frozenset                     |
# |-----------------------|-------------------------------|-------------------------------|
# | Mutability            | Mutable (can be changed)      | Immutable (cannot be changed)|
# | Hashable              | ❌ Not hashable               | ✅ Hashable                   |
# | Can be a dictionary key | ❌ No                         | ✅ Yes                        |
# | Supports add/remove   | ✅ Yes                        | ❌ No                         |
# | Use in sets           | ❌ Cannot be nested in sets   | ✅ Can be nested in sets      |
# | Syntax                | set([1, 2, 3]) or {1, 2, 3}   | frozenset([1, 2, 3])          |
# | Use case              | Dynamic collections           | Fixed, hashable collections   |