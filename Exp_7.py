#Aryan Naik 22AD1022
file_name = 'exp_7.txt'

print("Input the data in the file")
f = open(file_name, 'w')
f.write(input("Input: "))
f.close()

print("")
print("Reading the data from the file")
f = open(file_name, 'r')
print(f.read())
f.close()

print("")
print("Appending and Reading the file")
f = open(file_name, 'a+')
f.write(input("Input to Append: "))
f.seek(0)
print("Reading the data from the file just appended")
print(f.read())
f.close()

print("")
print("Counting")
f = open(file_name, "r")
if f.readable():
    lines = f.readlines()
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)    
    print("Number of lines:", num_lines)
    print("Number of words:", num_words)
    print("Number of characters:", num_chars)
else: 
    print("File is not readable or does not exist")