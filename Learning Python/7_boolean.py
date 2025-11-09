# booleans --> True/False
a = True
b = False
print(type(a))

age = 18
is_adult = age >= 18
print(is_adult)

# boolean is a subclass of Integer
print(True == 1)
print(False == 0)

print(True + True) # 1+1 = 2


# truthy or falsy(truthy equivalent of True and falsy equivalent of False)

#Falsy values in Pyton:
print(bool(0))          #False
print(bool(0.0))        #False
print(bool(''))         #False (empty String)
print(bool([]))         #False (empty list)
print(bool({}))         #False (empty dictionary)
print(bool(None))       #False


# All other values are truthy:
print(bool(42))             #True
print(bool(-1))             #True
print(bool('hello'))        #True
print(bool([1,2]))          #True

#Every Boolean is an integer
print(isinstance(True,int))

#Integers are not boolean --> False
print(isinstance(1,bool))

a = 10
print(a.bit_length())

print(True.bit_length()) #1
print(False.bit_length()) #0


# Logical Operators


###### Logical Operators in Python ##########

# 1. 'and' operator
# Returns True only if BOTH conditions are True
x = 5
y = 10
print("and example:", x > 2 and y < 15)  # True because both conditions are True

# 2. 'or' operator
# Returns True if AT LEAST ONE condition is True
print("or example:", x < 2 or y < 15)    # True because y < 15 is True

# 3. 'not' operator
# Inverts the Boolean value (True becomes False, False becomes True)
is_valid = True
print("not example:", not is_valid)      # False because not True is False

# Combined example
# Using all three operators together
if x > 2 and not y > 15:
    print("Combined logic: x is greater than 2 and y is not greater than 15")


# has photo_id and age >= 18 --> Driving License
has_photoid = True
age = 17
print(has_photoid and age >= 18)

# has Driving license or photo id --> Club
has_dl = True
has_photoid = False
print(has_dl or has_photoid)


# have no injury --> play football
has_injury = True
print(not has_injury)

x = 5
y = 10
print(x > 0 and y > 0) #True and True
print(x > 7 and y > 0) #False and True

age = 25
income = 30000
print(age > 18 or income > 50000)   #True
print(age < 18 or income > 50000)   #False
print(age < 18 or not(income > 50000))  #True

#Short-circuit-evaluation (Short-circuit evaluation in Python means that logical expressions using 
#and or or stop evaluating as soon as the result is determined — saving time and avoiding 
# unnecessary computation.)

# Boolean Operator Precedence
# not > and > or
result = True or False and not True
        # 1st Step:- True or False and False
        # 2nd Step:- True or False
        # 3rd Step:-  True

age = 25
income = 30000
credit_score = 700
is_eligible = (age >= 18 and age <= 65) and (income > 25000 or credit_score > 650)
print(is_eligible)

working_age = 18 <= age <=65
print(working_age)

# != == <= >= < >

text = "Python3"
print(text.isalpha()) 
print(text.startswith("Py"))



