# for loop syntax and usage
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# while loop syntax and usage
num = 1
while num <= 5:
    print(num)
    num += 1


# Loop control statements (break, continue)
for i in range(1, 11):
    if i == 5:
        break
    print(i)

for j in range(1, 11):
    if j % 2 == 0:
        continue
    print(j)


# Looping through sequences
# List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Tuple
colors = ("red", "green", "blue")
for color in colors:
    print(color)

# String
message = "Hello"
for char in message:
    print(char)


# Nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
