#Aryan Naik 22AD1022
def seperate_odd_eve(elements):
    odd_list = []
    even_list = []
    for num in elements:
        if num%2==0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return odd_list, even_list

def calculate_average_sum(student_tuple):
    roll_no, name, marks = student_tuple
    total_marks = 0
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    return total_marks, average_marks

def check_python_presence(string):
    if "python" in string.lower():
        return True
    else:
        return False
    
def sort_by_name(student_tuples):
    return sorted(student_tuples, key=lambda x: x[1])

if __name__ == "__main__":
    # 1. Take the number of elements
    num_elements = int(input("Enter the number of elements: "))

    # 2. Take the elements of each list one by one
    elements = []
    for i in range(num_elements):
        elements.append(int(input(f"Enter element {i+1}: ")))

    # 3-5. Separate odd and even elements
    odd_numbers, even_numbers = seperate_odd_eve(elements)
    print("Odd elements: ", odd_numbers)
    print("Even elements: ", even_numbers)
    merged_list = sorted(odd_numbers + even_numbers)
    print("Merged and sorted list: ", merged_list)

    # 6. Accept elements in the form of tuple
    roll_no = int(input("Enter student roll number: "))
    name = input("Enter student name: ")
    marks_str = input("Enter student marks separated by space: ")
    marks = list(map(int, marks_str.split()))

    # 7. Calculate average and sum of marks
    total_marks, average_marks = calculate_average_sum((roll_no, name, marks))
    print("Total marks: ", total_marks)
    print("Average marks: ", average_marks)

    # 8. Check if "python" is present in the string
    string_to_check = input("Enter a string to check if 'python' is present: ")
    if check_python_presence(string_to_check):
        print("'python' is present in the string")
    else:
        print("'python' is not present in the string")

    # 9. Sort the tuple by name
    student_tuples = [(22, 'Aryan', 97), (20, 'Bob', 85), (25, 'Charlie', 90)]
    sort_students_tuples = sort_by_name(student_tuples)
    print("Sorted student tuples: ", sort_students_tuples)

    # 10. Create a dictionary and print it
    my_dict = {"brand": "Ford",
               "model": "Mustang",
               "year": 1964}
    print("Dictionary: ", my_dict)
