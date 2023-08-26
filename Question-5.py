# Write a python script to create a calculator class with 2 methods for adding and subtracting 2 values

class calculator:
    def add(self,x,y):
        return x+y
    
    def subtract(self,a,b):
        return a-b

person1 = calculator()

print(person1.add(5,6))

print(person1.subtract(123,54))