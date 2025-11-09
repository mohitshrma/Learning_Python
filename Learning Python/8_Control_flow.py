name = "Alice"
print(f"Hello, {name}")
print("Welcome to Python Programming")


# 1. making decisions
# 2. Repeating actions
# 3. jumping to different parts of the program

# Examples with single -if, if-else, nested-if and if-elif

age = 19    #int(input())
if age >= 18:
    print("You are an adult.")
    print("I said you are an adult")
print("Outside if block")

temp = 1 #int(input("Enter Temperature: "))
is_raining = True # bool(input("Leave empty if not raining else type anything"))
if temp < 10 and is_raining:
    print("Please wear your jacket")
else:
    print("No need for a jacket")

name = "" #empty string,list, dictionary are evaluated as False
if name:
    print(name)


temp = 5
is_snowing = True
if temp < 10:
    print("It's freezing!")
    print("Wear a heavy coat.")
    if is_snowing:
        print("And don't forget your boots!")
print("Have a nice day!")


money = 500
is_popcorn_available = True
if money >= 400:
    print("Went to watch the movie")
    if(is_popcorn_available):
        print("Let's eat popcorn")


# Pass is a keyword in python used with blocks, class & loops(conditions) when a statement is required
    # but no action needed. Does nothing.!!
#Example:-
def my_function():
    pass  # Function does nothing (yet)

#Example 2:-
score = 50
if score < 60:
    pass
print("You need to study more.")


# if-else examples
if score >= 40:
    print("Passed")
else:
    print("Failed")
    print("Need to work hard.!")


age = 15
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")

# Question: Use to check if person is over 18 and password is valid or not [Valid password has atleast 8 letters on it]
age = 17
if age >= 18:
    password = input("Enter your password: ")
    if(len(password) < 8):
        print("Invalid password!! You need to have password with 8 or more characters long")
    else:
        print("Valid password. Password set successfully!")
else:
    print("Age must be equal or greater than 18.")


# Question: Input a number and check if the number is odd or even.
number = 32  #int(input("Enter your number "))
if(number % 2 == 0):
    print("Number is even.")
else:
    print("Number is odd.")


score =  76
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")


# Question: Given a number, check if it is positive single digit(1-9), zero or negative(<=0), positive(greater than 9)
x = 10 #int(input("Please input a number"))
if(x <= 0):
    print("Zero or negative value detected!")
elif(x>0 and x<=9):
    print("Positive single digit detected!")
else:
    print("Positive value detected!")


#Question: Print according to given scenario

has_fever = True
has_cough = True
has_rash = False

if has_fever:
    print("Take fever medication.")
if has_cough:
    print("Take cough syrup.")
if has_rash:
    print("Apply anti-itch cream.")


# Question: Print tax according to salary and age
age = 17
income = 50000
if(age >= 18):
    if(income < 30000):
        print("Low income tax.")
    elif(income >=30000 and income <=70000):
        print("Medium income tax.")
    else:
        print("High income-tax")
else:
    print("Age too low. Icome-Tax does't apply on the individual.")


#Question: Combining conditions 
    # a -> 6,7,9 -> lucky
    # else -> unlucky

a = 7
if (a == 6 or a == 7 or a == 9):
    print("lucky")
else:
    print("Unlucky")

# Using list:-[Better approach] using in operator
li = [6,7,9]
a = 6
if a in li:
    print("Lucky")
else:
    print("Unlucky")

######## Ternary Operator in Python ########

''' value_if_true if condition else value_if_false '''

#Example 1
age = 20
status = "adult" if age >=18 else "minor"
print(status)

#Example 2
a, b = 5, 10
max_val = a if a > b else b
print(max_val)  # Output: 10


#Example 3
number = 17
divisor = 7
result = print(number/divisor) if divisor != 0 else print("cannot be divided.")

#Example 4
operation = input("sub or add ?")
a,b = 5,3
result = a + b if operation == "add" else a - b if operation == "sub" else "Unknown"
print(result)


####### SUMMARY #############
# ✅ if: Executes block if condition is True
x = 10
if x > 5:
    print("x is greater than 5")

# ✅ else: Executes block if condition is False
if x < 5:
    print("x is less than 5")
else:
    print("x is not less than 5")

# ✅ if-else: Two-way decision
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")

# ✅ if-elif-else: Multi-way decision
score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")

# ✅ nested if: if inside another if
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Non-positive number")