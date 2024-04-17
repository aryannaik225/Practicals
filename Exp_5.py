class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def display_info(self):
        print("ID:", self.id)
        print("Name:", self.name)

class Student(Person):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.ai_marks = None
        self.python_marks = None
        self.flat_marks = None
        self.sport_marks = None

    def display_info(self):
        super().display_info()
        if self.ai_marks is not None:
            print("AI Marks:", self.ai_marks)
        if self.python_marks is not None:
            print("Python Marks:", self.python_marks)
        if self.flat_marks is not None:
            print("FLAT Marks:", self.flat_marks)
        if self.sport_marks is not None:
            print("Sport Marks:", self.sport_marks)
    
    def set_marks(self, ai_marks, python_marks, flat_marks):
        self.ai_marks = ai_marks
        self.python_marks = python_marks
        self.flat_marks = flat_marks
    
    def set_sport_marks(self, marks):
        self.sport_marks = marks
    
    def calculate_result(self):
        total_marks = self.calculate_total_marks()
        if self.sport_marks is not None:
            total_marks += self.sport_marks
        
        percentage = (total_marks / 300) * 100
        print("Total Marks:", total_marks)
        print("Percentage:", percentage)
        print("Result:", "Pass" if percentage >= 40 else "Fail")
    
    def calculate_total_marks(self):
        if self.ai_marks is None or self.python_marks is None or self.flat_marks is None:
            raise ValueError("Marks in AI, Python, and FLAT subjects are required")
        return self.ai_marks + self.python_marks + self.flat_marks

class StudentWithSports(Student):
    def __init__(self, id, name, ai_marks, python_marks, flat_marks, sport_marks):
        super().__init__(id, name)
        self.ai_marks = ai_marks
        self.python_marks = python_marks
        self.flat_marks = flat_marks
        self.sport_marks = sport_marks

class StudentWithoutSports(Student):
    pass

if __name__ == "__main__":
    id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    ai_marks = float(input("Enter AI marks: "))
    python_marks = float(input("Enter Python marks: "))
    flat_marks = float(input("Enter FLAT marks: "))
    sport_option = input("Does the student have sports marks? (yes/no): ").lower()

    if sport_option == "yes":
        sport_marks = float(input("Enter sports marks: "))
        student = StudentWithSports(id, name, ai_marks, python_marks, flat_marks, sport_marks)
    else:
        student = StudentWithoutSports(id, name)
    
    student.display_info()
    student.calculate_result()
