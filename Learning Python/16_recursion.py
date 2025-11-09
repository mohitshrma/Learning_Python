# Recursion is a programming technique where a function calls itself to solve a problem by breaking it into smaller,
# simpler subproblems.

# 🧠 Key Concepts of Recursion in Python
# - Recursive Function: A function that calls itself within its definition.
# - Base Case: The condition that stops the recursion (prevents infinite loops).
# - Recursive Case: The part where the function calls itself with modified input

def sum_of_n(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total
ans = sum_of_n(5)
print(ans)

# Using recursion for same task above.
def sum_rec(n):
    if n == 1:
        return 1
    return n + sum_rec(n-1)

print(sum_rec(5))


# Question: Find factorial using recursion

#Using iterative approach
def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    return ans
print(fact(5))


# Using recursive approach
def fact_rec(n):
    if n == 1:
        return 1
    return n * fact_rec(n - 1)
print(fact_rec(5))


# Fibonacci series using recursion

def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n-1) + fib(n-2)

print(fib(9))



def countdown(n):
    if n == 0:
        return 
    countdown(n-1)
    print(n)

print(countdown(5))

# ✅ Use Recursion When:
# - The problem has a natural recursive structure (e.g., tree traversal, factorial, Fibonacci).
# - You need to explore multiple paths (e.g., backtracking, maze solving, permutations).
# - The solution is elegant and concise with recursion (e.g., quicksort, merge sort).
# - You're working with divide-and-conquer algorithms.
# - You’re solving problems with limited depth (under ~1000 calls).
# - You want to express mathematical recurrence relations directly.

# 🚫 Avoid Recursion When:
# - The recursion depth may exceed Python’s limit (default ~1000 calls).
# - An iterative solution is more efficient and readable.
# - You’re dealing with large datasets or deep loops (e.g., dynamic programming).
# - You need high performance (recursion adds overhead in Python).
# - The recursive logic is hard to debug or trace.
# - You’re not using memoization for overlapping subproblems (e.g., naive Fibonacci).


