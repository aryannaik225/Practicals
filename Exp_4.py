class Calculate:
    def __init__ (self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def calculate(self):
        print("Area of rectangle ==> ",self.length*self.breadth)

l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
obj = Calculate(l,b)
obj.calculate()