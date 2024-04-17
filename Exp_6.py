#Aryan Naik 22AD1022

def get_integer_input (n):
    try:
        num = int(n)
        return num
    except ValueError:
        print("Error: Invalid Input, please input an integer value")

n = get_integer_input(input("Enter your Input: "))
print("Your Input is", n)