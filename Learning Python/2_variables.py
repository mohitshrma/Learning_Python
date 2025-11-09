#Creating variables in python
# name, variable, location, data type

x = 1    #integer
name = "Ankit"  #String
price = 999.99  #float
is_adult = True #Boolean

# In Python, type() is a built-in function used to check the data type of a variable or value
print(type(x))
print(type(name))
print(type(price))
print(type(is_adult))

# Example demonstrating that python is dynamically typed
x = name    # easily can store string value into number type automatically
print(x)    # x prints 'Ankit' 

# Assigning values to multiple variables in same line and use of separator
a = 1
b = 2
c = 3
print(a,b,c, sep = ",")

d,e,f = 4, 5, 6.6
print(d,e,f, sep = ",")

print(d + e)


### Variable naming conventions and rules ###

# 1. letters, digits and underscores are allowed
var1_ex = 3.5

# 2. must start with letter or _
x = 2
_y = 3

# 3. cannot start with number
# 11_rex = 5 

# 4. case sensitive
name = "Vipul"
Name = "Akshit"

# 5. Spacing is not allowed while naming variable
# name ram = "Hello"

# 6. Can't use python keywords - if, else, print, while, for, def, class, etc.

print(name)
print(Name)

# Snake case is generally used in python along with underscore.

usernameofinstagram = "Badboyz"
user_name_of_instagram = "BadBoyz" # preferred way