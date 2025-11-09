# 🧠 What Is a Function?
# - A function lets you group code that performs a task so you can reuse it.
# - It helps avoid repetition and makes your code modular and readable.

#In Python, a function is a reusable block of code that performs a specific task when called. 
# You define it using the def keyword and call it by its name followed by parentheses.

# 🛠️ How to Define a Function
def greet():
    print("Hello, Max!")

# - def starts the function definition.
# - greet is the function name.
# - () can hold parameters (more on that below).
# - The indented block is the function body.

# 📞 How to Call a Function
greet()  # Output: Hello, Max!


# 📦 Functions with Parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alex")  # Output: Hello, Alex!


#Example:- Write a function that takes two numbers as parameters, return sum of their squares.
def sum_then_square(a, b):
    c = ((a+b)**2)
    return c

res = sum_then_square(1,2)
print(res)


#Question: Write a function that takes two numbers as parameters, divide them and make sure if denominator is zero, print accordingly.
def divide(a,b):
    if(b == 0):
        print("Cannot divide by zero")
    else:
      return  a / b

print(divide(3,3)) # a=3, b=3

print(divide(b = 4, a = 32)) #keyword arguments
print(divide(10, b = 5)) # must pass positional arguments before keyword arguments

# Example:Pass a list as parameter to a function and print sum of even numbers in that list
def sum_of_even(li):
    sum = 0
    for i in li:
        if i%2 == 0:
            sum += i
    return sum

total_sum = sum_of_even([1,3,2,4,5,6,10,8,9,12,13,15])
print(total_sum) 

# Note:- A function can return multiple values which is comma separated(meaning it is a tuple!)
def fun1():
    return "Hello",1,2,True

a = fun1()
print(a)
print(type(a))

# Unpacking a tuple from a function
def fun():
    return 1,2 #tuple

a,b = fun() #unpack
print(a,b)

# Use __doc__ to print documentation
print(print.__doc__)
print(abs.__doc__)
print(len.__doc__)

# If you want to have documentation of user-defined function, it can be done using ''' inside function.
#Example:-
def show_name(first_name,last_name):
    ''' It will return the first and last name of the user'''
    print(f"{first_name} {last_name}")

show_name("Alex","Grey")

print(show_name.__doc__) #shows description of the function




#✅ Args and Kwargs in python

# Question: Write a function that takes three numbers as parameters and returns it's sum
def sum_of_three_numbers(a,b,c):
    '''It returns the sum of given three numbers'''
    return a+b+c

print(sum_of_three_numbers(1,2,3))

# Args
# - *args lets you pass any number of positional arguments to a function.
# - Inside the function, args becomes a tuple.
#Example:-
def sum_of_nums(*nums):
    total = 0
    for i in nums:
        total += i
    return total

print(sum_of_nums(1,2,3,4))

# 2. Passing message as well
def sum_of_nums(msg,*nums):
    print(msg)
    total = 0
    for i in nums:
        total += i
    return total

print(sum_of_nums("This is a message",1,2,3)) #Remember to maintain positional argument always


#kwargs
# 🧠 What Are **kwargs?
# - **kwargs lets you pass any number of keyword arguments (name=value pairs).
# - Inside the function, kwargs becomes a dictionary.

#Example of kwargs(works in key-value pair)
def build_profile(**things):
    print("Building profile..")
    for i,j in things.items():
        print(f"{i}: {j}")

build_profile(name = "Max", age = 25, profession = "Software Developer", hobbies = ["Gaming","Football"])

# Example of combining args and kwargs
# First positional arguments, 2nd default paramaters, 3rd keyword arguments
def demo(*args, **kwargs):
    print("Positional:", args) #tuple based
    print("Keyword:", kwargs) #dictionary based

demo(1, 2, 3, name="Max", job="Developer")
# Output:
# Positional: (1, 2, 3)
# Keyword: {'name': 'Max', 'job': 'Developer'}

"""
📊 Python: *args vs **kwargs — Comparison Table

| Feature            | *args                                | **kwargs                                 |
|--------------------|---------------------------------------|-------------------------------------------|
| Type               | Tuple                                 | Dictionary                                 |
| Purpose            | Variable number of positional args    | Variable number of keyword args           |
| Syntax             | def func(*args):                      | def func(**kwargs):                       |
| Access             | args[0], args[1], ...                 | kwargs['key'], kwargs.get('key')          |
| Use Case           | Summing numbers, flexible inputs      | Config options, named parameters          |
| Order in function  | Comes before **kwargs                 | Comes after *args                         |
| Default value?     | No                                    | Yes, via kwargs.get('key', default)       |
| Java Equivalent    | Varargs (`...`)                       | No direct equivalent                      |

🔧 Example: Using *args
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3))  # Output: 6

🔧 Example: Using **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Max", age=25)
# Output:
# name: Max
# age: 25

🔧 Example: Combining *args and **kwargs
def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo(1, 2, name="Max", role="Dev")
# Output:
# Args: (1, 2)
# Kwargs: {'name': 'Max', 'role': 'Dev'}
"""
#Unpacking of args and kwargs
def add(x,y,z):
    return x + y + z

vals = [1,2,3]
print(add(*vals)) 

params = {"x":10, "y":20, "z":30}
print(add(**params))




#✅ Function Scope in python
# Function scope refers to the visibility and lifetime of variables defined inside a function — they are local to that function and inaccessible from outside.

a = 1 # global variable
def fun():
    a = 11 # local variable
    print(f"Value of a is {a}")
fun()
print(f"Value of a is {a}")


# 🧠 What Is Scope?
# - Scope defines where a variable can be accessed.
# - Python uses the LEGB rule to resolve variable names:
# - Local: Inside the current function
# - Enclosing: In enclosing functions (nested)
# - Global: At the module level
# - Built-in: Python’s built-in names like len, sum


# 🔍 Function Scope (Local)
# Variables defined inside a function are local to that function:
def greet():
    message = "Hello, Mohit!"
    print(message)

greet()
# print(message)  # ❌ Error: message is not defined outside the function



# 🧬 Enclosing Scope (Nested Functions)
def outer():
    x = "outer value"
    def inner():
        print(x)  # Accesses x from enclosing scope
    inner()

outer()  # Output: outer value



# 🌍 Global Scope
# Variables defined outside functions are global:
x = "global value"

def show():
    print(x)

show()  # Output: global value

# To modify a global variable inside a function, use global:
count = 0

def increment():
    global count
    count += 1



# 🔁 Built-in Scope
#Python has built-in functions like:
print(len("Max"))  # Uses built-in len()

"""
📘 Python Function Scope — LEGB Rule Summary

| Scope Level | Description                                | Example Access             | Notes                                |
|-------------|--------------------------------------------|----------------------------|--------------------------------------|
| Local (L)   | Variables defined inside the current func  | def foo(): x = 5          | Most specific scope                  |
| Enclosing (E)| Variables in outer (enclosing) functions  | def outer(): def inner(): | Used in nested functions             |
| Global (G)  | Variables defined at module level          | x = 10 outside any func    | Accessible inside functions (read)   |
| Built-in (B)| Python’s built-in names                    | len(), sum(), print()      | Least specific, always available     |

🔍 Example: Local vs Global
x = "global"

def show():
    x = "local"
    print(x)  # Output: local

show()
print(x)      # Output: global

🔍 Example: Enclosing Scope
def outer():
    msg = "enclosing"
    def inner():
        print(msg)
    inner()

outer()  # Output: enclosing

🔍 Example: Using global keyword
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1
"""

########################


"""
🔁 Python `nonlocal` Keyword — Quick Reference

📌 Purpose:
- Used inside nested functions to modify variables from the enclosing (outer) function scope.
- Does NOT affect global variables — only variables in the nearest enclosing function.

🔍 Syntax:
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
    inner()
    print(x)  # Output: 15

🧪 Without `nonlocal`:
def outer():
    x = 10
    def inner():
        x += 5  # ❌ UnboundLocalError: local variable 'x' referenced before assignment
    inner()

✅ With `nonlocal`:
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
    inner()
    print(x)  # Output: 15

📘 Scope Comparison:
| Keyword    | Affects Scope       | Use Case                          |
|------------|---------------------|-----------------------------------|
| local      | Current function    | Default variable assignment       |
| nonlocal   | Enclosing function  | Modify outer function variable    |
| global     | Module/global scope | Modify global variable            |

🧠 Use Case:
- Useful in closures, decorators, and stateful nested functions.
"""


# Type Conversion Functions
number_str = "42"
number_int = int(number_str)
print(type(number_int))

price = float("19.99")
age = 25
age_str = str(age)

print(bool(0))      # Output:True
print(bool(1))      # Output:False
print(bool(""))     # Output:False
print(bool("hi"))   # Output:True

numbers = (1,2,3,4)
numbers_list = list(numbers) # Output:[1,2,3,4]
number_set = set(numbers)   # Output:{1,2,3,4}


# ✅ Built-in mathematical functions in Python
"""
🔧 Python Built-in Mathematical Functions

✅ These work without importing any module:

print(min(3, 7, 2, 9))     # Minimum → 2
print(max(3, 7, 2, 9))     # Maximum → 9
print(abs(-10))            # Absolute value → 10
print(pow(2, 3))           # Power → 8 (same as 2 ** 3)
print(round(3.14159, 2))   # Round to 2 decimal places → 3.14
print(sum([1, 2, 3, 4]))   # Sum of list → 10

📘 Notes:
- `pow(x, y)` is equivalent to `x ** y`
- `abs(x)` works for int, float, and even complex numbers
- `min()` and `max()` can take multiple arguments or a list

🔍 Example with list:
numbers = [5, -3, 12, 0]
print(min(numbers))        # → -3
print(max(numbers))        # → 12
print(abs(numbers[1]))     # → 3
print(pow(numbers[0], 2))  # → 25
"""

# ✅ Built-in sequence functions in Python 
"""
📚 Python Built-in Sequence Functions — Quick Reference

✅ These functions work on sequences like lists, tuples, strings, ranges, etc.

🔢 len() — Length of sequence
items = [1, 2, 3, 4]
print(len(items))  # → 4

🔍 max() / min() — Largest / Smallest item
print(max(items))  # → 4
print(min(items))  # → 1

➕ sum() — Sum of numeric sequence
print(sum(items))  # → 10

🔁 sorted() — Returns a new sorted list
print(sorted(items))  # → [1, 2, 3, 4]

🔄 reversed() — Returns an iterator in reverse order
print(list(reversed(items)))  # → [4, 3, 2, 1]

🔍 any() — True if any item is truthy
flags = [False, True, False]
print(any(flags))  # → True

🔍 all() — True if all items are truthy
print(all(flags))  # → False

🔁 enumerate() — Index + value pairs
for i, val in enumerate(items):
    print(i, val)
# Output:
# 0 1
# 1 2
# 2 3
# 3 4

🔁 zip() — Combine multiple sequences
names = ["Max", "Asha"]
scores = [85, 90]
for name, score in zip(names, scores):
    print(name, score)
# Output:
# Max 85
# Asha 90
"""

# ✅ Working with map(), filter() and reduce()

# 1. map(function,iterable)

def square(x):
    return x ** 2
numbers = [1,2,3,4,5]
squared_numbers = map(square,numbers)
print(list(squared_numbers))


def add_numbers(x,y):
    return x + y
list1 = [1,2,3]
list2 = [4,5,6]
result = map(add_numbers,list1,list2)
print(list(result))


def convert_int(a):
    return int(a)
string_numbers = ["1","2","3","4"]
result = map(convert_int,string_numbers)
print(list(result))


"""
🔁 Python map() — Apply a Function to a Sequence

✅ Purpose:
Apply a function to every item in an iterable and return a transformed result.

🔧 Syntax:
map(function, iterable)

🔢 Example 1: Capitalize names
names = ["alex", "max", "sara"]
capitalized = list(map(str.capitalize, names))
print(capitalized)  # → ['Alex', 'Max', 'Sara']

🔢 Example 2: Add title using lambda
names = ["alex", "max"]
titled = list(map(lambda name: f"Mr. {name.capitalize()}", names))
print(titled)  # → ['Mr. Alex', 'Mr. Max']

🔢 Example 3: Combine names and scores
names = ["Alex", "Max"]
scores = [88, 92]

def format_result(name, score):
    return f"{name} scored {score}"

results = list(map(format_result, names, scores))
print(results)
# → ['Alex scored 88', 'Max scored 92']

📘 Notes:
- `map()` returns a lazy iterator — wrap with `list()` to view results.
- Great for transforming data in pipelines or backend logic.
"""

#✅ 2.filter(function, iterable)
# -> is used to extract elements from an iterable (like a list or tuple) that satisfy a given condition.

def is_even(x):
    return x % 2 == 0
numbers = [1,2,3,4,5,6,7,8]
even_numbers = filter(is_even,numbers)
print(list(even_numbers))

"""
🔍 Python filter() — Select Items Based on a Condition

✅ Purpose:
Filter elements from an iterable based on a function that returns True or False.

🔧 Syntax:
filter(function, iterable)

🔢 Example 1: Filter passing scores
scores = [45, 82, 67, 90, 38]

def is_pass(score):
    return score >= 60

passed = list(filter(is_pass, scores))
print(passed)  # → [82, 67, 90]

🔢 Example 2: Using lambda to filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # → [2, 4, 6]

🔢 Example 3: Filter names starting with 'A'
names = ["Alex", "Max", "Anna", "John"]

starts_with_a = list(filter(lambda name: name.startswith("A"), names))
print(starts_with_a)  # → ['Alex', 'Anna']

📘 Notes:
- `filter()` returns a lazy iterator — wrap with `list()` to view results.
- Ideal for data cleaning, validation, and conditional selection.
"""


#✅3. reduce()
# --> reduce() in Python applies a function cumulatively to the items of an iterable, reducing it to a single value. It’s part of the functools module.

# 🔧 Syntax:
# from functools import reduce
# reduce(function, iterable)

from functools import reduce
def add(x,y):
    return x + y
numbers = [1, 2, 3, 4, 5]
total = reduce(add,numbers)
print(total)


# 🔢 Example: Sum of numbers
from functools import reduce
numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)
print(total) #->10



# ✅ Lambda Functions

"""
⚡ Python Lambda Expressions — Key Characteristics

✅ Anonymous Function:
- Defined without a name using the `lambda` keyword.

✅ Single Expression Only:
- Contains only one expression (no statements or multiple lines).
- Automatically returns the result of that expression.

✅ Syntax:
lambda arguments: expression

✅ Used for Short, Throwaway Functions:
- Commonly used with `map()`, `filter()`, `reduce()`, and sorting.

✅ Can Take Multiple Arguments:
- But only one expression is allowed.

✅ No `return` Keyword Needed:
- The result of the expression is returned implicitly.

✅ Example:
square = lambda x: x * x
print(square(5))  # → 25

✅ Comparison with def:
- `lambda` is concise but less readable for complex logic.
- `def` is preferred for multi-line or reusable functions.

✅ Functional Programming Friendly:
- Often used in pipelines and inline transformations.
"""
# 1. Example using function using def() and lambda expression.
def add_two_numbers(x,y):
    return x + y

add_lambda = lambda x,y: x + y #equivalent lambda expression of above function
print(add_lambda(1,2))

# 2. Example:-
def square(x):
    return x ** 2

sq_lambda = lambda x:x**2
print(sq_lambda(3))

# 3. Example:- Function with no parameter in lambda expression

def greet():
    return "World"

demo_lambda = lambda : "World"
print(demo_lambda())


# 4. Example:- Function with parameter and default value converted to lambda expression

def power(x,y = 2):
    return x ** y

power_l = lambda x, y = 2: x ** y
print(power_l(11,3))


"""
🔁 Lambda Expressions in Higher-Order Functions

✅ What is a Higher-Order Function?
- A function that takes another function as an argument or returns one.

✅ Lambda Use Cases:
Perfect for short, inline functions passed to higher-order functions.

🔢 Example 1: map() — Transform each item
names = ["alex", "max", "sara"]
capitalized = list(map(lambda name: name.capitalize(), names))
print(capitalized)  # → ['Alex', 'Max', 'Sara']

🔢 Example 2: filter() — Select items based on condition
scores = [45, 82, 67, 90]
passed = list(filter(lambda score: score >= 60, scores))
print(passed)  # → [82, 67, 90]

🔢 Example 3: reduce() — Combine items cumulatively
from functools import reduce
numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # → 10

🔢 Example 4: sorted() — Custom sort logic
students = [("Alex", 85), ("Max", 92), ("Sara", 78)]
sorted_by_score = sorted(students, key=lambda student: student[1])
print(sorted_by_score)
# → [('Sara', 78), ('Alex', 85), ('Max', 92)]

📘 Tip:
Use lambdas when the function logic is simple and doesn’t need reuse.
"""

# Example:Use lambda expression to convert celsius to farenheit

celsius_temps = [0,20,30,40]
f_temps = map(lambda x: (x * 9/5) +32, celsius_temps)
print(list(f_temps))

#2. 
numbers = [1,2,3,4,5,6,7,8,9,10]
res = list(filter(lambda x : x % 2 == 0, numbers))
print(res)

# 3. Filter strings longer than 5 characters
words = ["apple","banana","cat","elephant","dog"]
res = list(filter(lambda s: len(s) > 5, words))
print(res)

#4.Calculate total compensation from given list using lambda function

employees = [
    {'name':'John', 'salary':50000, 'bonus':5000},
    {'name':'Jane', 'salary':60000, 'bonus':7000},
    {'name':'Bob', 'salary':45000, 'bonus':4000},
]

print(list(map(lambda x:x['salary'] + x['bonus'],employees)))

# ❌ This won't work - multiple statements
# bad_lambda = lambda x: print(x); return x * 2 

# ✅ Can use ternary operator
sign_lambda = lambda x:"positive" if x > 0 else ("negative" if x < 0 else "zero")
print(sign_lambda(5))
print(sign_lambda(-2))
print(sign_lambda(0))

# ❌ Lambda functions can't have docstrings
square_lambda = lambda x: x ** 2

# ❌ This doesn't work as expected
bad_lambda = lambda x:print(f"Processing {x}") # Returns None, not useful

# ❌ Hard to read complex lambda
f = lambda x: (lambda y: y**2)(x) if x % 2 == 0 else (lambda z: z + sum(map(lambda a: a * 2, range(z))))(x)

#✅ More readable as a regular function
def process_number(x):
    if x % 2 == 0:
        return x ** 2
    else:
        doubled_sum = sum(a * 2 for a in range(x))
        return x + doubled_sum



#✅ Functions as First-Class Objects

''' 
Being passed as arguments to other functions
Being returned as values from other functions
Being assigned to variables
Being stored in data structures(lists,dictionaries,etc)
Being created at runtime
'''

#✅ 1. Being passed as arguments to other functions
def shout(text):
    return text.upper()

def greet(func):
    return func("hello")

print(greet(shout))  # Output: HELLO


#🔁 2. Being returned as values from other functions
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
print(times3(5))  # Output: 15



#📦 3. Being assigned to variables
def say_hi():
    return "Hi!"

greeting = say_hi
print(greeting())  # Output: Hi!



#📚 4. Being stored in data structures (lists, dictionaries, etc.)
def add(x, y): return x + y
def subtract(x, y): return x - y

operations = {
    "sum": add,
    "diff": subtract
}

print(operations["sum"](10, 5))    # Output: 15
print(operations["diff"](10, 5))   # Output: 5



#⚙️ 5. Being created at runtime
def make_adder(n):
    return lambda x: x + n

add10 = make_adder(10)
print(add10(5))  # Output: 15



