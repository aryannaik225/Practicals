# Define a string

str1 = "   hello"
str2 = "world     "
string = str1 + " " + str2 
print(str1)
print(str2)

#1. Concat
print("1. Concat")
print(string)


# 2. Strip whitespace
print("\n2. Strip whitespace:")
string = string.strip()
print(string)  # Output: hello world

# 3. Title case
print("\n3. Title case:")
print(string.title())  # Output: Hello World
 

# 4. Uppercase
print("\n4. Uppercase:")
print(string.upper())  # Output: HELLO WORLD

# 5. Lowercase
print("\n5. Lowercase:")
print(string.lower())  # Output: hello world

# 6. Length of the string
print("\n6. Length of the string:")
print(len(string))  # Output: 15
