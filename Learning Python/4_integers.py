# Integers can be positive, negative or zero
a = 10
b = -22
c = 0
print(a,b,c)
print(type(a))
# Python integers have unlimited precision
salary = 10_00_000
print(salary)
binary_num = 0b101010  #0b--> prefix for binary number
print(type(binary_num))
print(binary_num)
print(bin(10))

hex_num = 0x2AF #0x--> prefix for hexadecimal number
# 2*256 + 10*16 + 15*1
# 512 + 160 + 15
# 687
print(hex_num)


######### Arithmetic Operators ###########
a = 10
b = 3
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Regular Division: {a / b}") # 3.3.333333333333335
print(f"Integer Division: {a // b}") # 3
print(f"Power: {a ** b}")
print(f"Modulus: {a % b}")
print(f"Negation of: {a} = {-a}")
print(f"Absolute value of {b} - {a} = {abs(b - a)}") # if we dont care about negative or positive but only in magnitude

result = 2 + 3 * 4

result = 10 - 2 ** 3 // 2 + 7
print(result)

### Bitwise Operator ####
x = 10  # 1010 in binary
y = 6   # 0110 in binary
        # 0010 (AND)
        # 1110 (OR)
        # 1100 (XOR)
        
# Bitwise AND & (Both should be compulsorily 1, output 1, if different, output is 0, prefers 0)
bitwise_and = x & y
print(f"{x} & {y} = {bitwise_and}")

# Bitwise OR | (if both are 0, output 0, if different digit output is 1, prefers 1)
bitwise_or = x | y 
print(f"{x} | {y} = {bitwise_or}")
print(0b1110)

# Bitwise XOR ^ (if both digits are different, output is 1, otherwise same digit is 0)
bitwise_xor = x ^ y
print(f"{x} ^ {y} = {bitwise_xor}")
print(0b1100)

# Bitwise NOT ~ (Flips the binary digits[if 0 make it 1, if 1 make it 0])
bitwise_not = ~x
print(f"Binary of {x} is {bin(x)}") #00001010 --> 1111 0101
# 1111 0101 -> 00001010 (flip)
# 00001010 + 00000001 = 00001011 (add 1)
print(f"~{x} = {bitwise_not}")
print(0b00001011)

#Left_Shift [Shifts the bits of a number to the left by a specified number of positions.]
left_shift = x << 1  #left shift by 1 (1010 --> 10100)
left_shift_n = x << 2 #left shift by 2 (1010 --> 101000)
print(f"{x} << 1 = {left_shift}")
print(f"{x} << 2 = {left_shift_n}")

#Right_Shift [Shifts the bits of a number to the right by a specified number of positions. 
                # Each right shift divides the number by 2^n, discarding the remainder.]
right_shift = x >> 1  #right shift by 1 (1010 --> 0101)
right_shift_n = x >> 2 #right shift by 2 (1010 --> 0010)
print(f"{x} >> 1 = {right_shift}")
print(f"{x} >> 2 = {right_shift_n}")

#Questions:
#floor division --> returns largest integer less than or equal to the exact division
print(10 // 3)          #3
print(10.0 // 3)        #3.0
print(-10 // 3)         #-4 since it is less than -3.333
print(10 // -3)         #-4 since it is less than -3.333


#Assignment Operators
x = 1
a,b = 1,2
c = d = 3

# x = int(input())
# y = int(input())

#swap using old method using temporary value
temp = x
x = y
y = temp

#Swap using python; new method
x,y = y,x

print(x,y)
print(type(x),type(y))


z = 3
z += 2
z -= 2
z *= 2
z /= 2
z **= 5
print(z)

msg = "Hello"
msg = msg + " World" * 2
print(msg) # prints Hello World World



