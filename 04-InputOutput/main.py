# Using input() function
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello,", name, "! You are", age, "years old.")


# Formatting output using print() function
name = "Alice"
age = 30
print("Hello, " + name + "! You are", age, "years old.")

# Using string interpolation
print(f"Hello, {name}! You are {age} years old.")

# Using formatting parameters
print("Hello, {}! You are {} years old.".format(name, age))


# Basic string formatting techniques
name = "Bob"
age = 25

# %-formatting
print("Hello, %s! You are %d years old." % (name, age))

# str.format()
print("Hello, {}! You are {} years old.".format(name, age))

# f-strings (formatted string literals)
print(f"Hello, {name}! You are {age} years old.")


# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:", content)

# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, World!")
    print("Data written to file successfully.")


