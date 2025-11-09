# 🔁 while loop: repeats as long as the condition is True
count = 0
while count < 5:
    print("Count:", count)
    count += 1

#example:-
x = 1
while (x <= 500):
    print("Hello World!", x)
    x += 1

# break keyword :used to exit a loop immediately, skipping any remaining iterations. It works in both for and while loops.
#example:-
x = 1
while (x <= 500):
    print("Hello World!", x)
    x += 1
    if x == 4:
        break

#Example:- To print from 10 to 1
x = 10
while(x >= 1):
    print("Value is :", x)
    x -= 1



# 🔁 for loop: used to iterate over a sequence (like a list, tuple, string, or range) and execute a block of code for each item in that sequence.

''' syntax:-
for variable in sequence:
    #code block(loop body)
'''
#example: To iterate and print each element in a list using for loop
fruits = ['apple','orange','banana']
for fruit in fruits:
    print(fruit)

#example:-
name = "Morrison"
for letter in name:
    print(letter.upper())



# range() --> The  function in Python generates a sequence of numbers, commonly used for looping a specific 
                #   number of times.

    # Syntax    --> range(stop)
    #           --> range(start,stop)
    #           --> range(start,stop,step) [start(default 0), end(exclusive), step(difference and default is 1)]
    #           It does not create a list in memory (unless explicitly converted)
#example:- Using for and range() function to print from 0 to 4
for i in range(5):
    print("Hello World!", i)

print(range(10)) #--> prints a range object; not a list

# Example:- To convert a range into a list
print(list(range(5))) # --> [0,1,2,3,4]

# Using range in list
fruits = ["apple","banana","orange","grapes"]
for i in range(len(fruits)):
    print(fruits[i])

#reverse above list using range() function
fruits = ["apple","banana","orange","grapes"]
for i in range(len(fruits)-1, -1, -1):
    print(fruits[i])


### enumerate() function in python ########
# The enumerate() function in Python is used to loop over an iterable and get both the index and the value of 
# each item — super handy when you need position info while iterating.

for index, fruit in enumerate(fruits):
    print(fruits[index])

#Example:-
names = ['Ashton', 'Aisha', 'Liam']

for index, name in enumerate(names):
    print(f"{index}: {name}")


# break keyword in python #### --> Exit the loop immediately regardless of the loop condition.
for number in range(10):
    if number == 5:
        break
    print(number)


# continue keyword in python #### --> skips the loop for current iteration and move to the next one.
for number in range(10):
    if number == 5:
        continue
    print(number)

# pass keyword in python #### --> is a placeholder that does nothing — it's used when a statement is required 
                                # syntactically but you don’t want any code to run yet.

for number in range(10):
    if number == 5:
        pass
    print(number)


# Question: If number is even, print even otherwise odd
for number in range(1,21):
    if number % 2 == 0:
        print(f"{number}:Even number")
    else:
        print(f"{number}:Odd number")

# Question: Take a number from user input and check if the number is prime or not.
x = 7 # int(input("Please enter a number. "))
count = 0
for i in range(1, x + 1):
    if x % i == 0:
        count += 1
if count == 2:
        print(f"{x}: It is a prime number")
else:
    print(f"{x}: It is not a prime number")


# for and while loops both can have an optional else
# The else block executes after the loop finishes normally
# but not if the loop is terminated with a break statement.

'''
for item in sequence:
    # loop body
    if some_condition:
        break
else:
    # Runs only if the loop was not broken        
    
'''
#Example showcasing use of else in for loop
nums = [1,3,5,7,9]
for x in nums:
    if x % 2 == 0:
        print("Even number found", x)
        break
else:
    print("No even numbers found")    


##### Nested Loop ##########

#Example 1:-
for i in range(1,5):
    stars = ""
    for j in range(i):
        stars += "*"
    print(stars)

print()

for i in range(1,4):   #outer for --> rows
    s = ""
    for j in range(i): #inner for --> columns
        s += "*"
    print(s)

