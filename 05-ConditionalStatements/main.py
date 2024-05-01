# Using if, elif, and else statements
x = 10
if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")


# Comparison operators
a = 5
b = 10
print("a == b:", a == b)
print("a != b:", a != b)
print("a < b:", a < b)
print("a > b:", a > b)
print("a <= b:", a <= b)
print("a >= b:", a >= b)


# Logical operators
x = 5
y = 10
z = 15
print("x < y and y < z:", x < y and y < z)
print("x < y or y > z:", x < y or y > z)
print("not(x < y):", not(x < y))


# Nested conditional statements
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
