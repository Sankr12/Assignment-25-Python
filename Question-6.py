# Write a python script to create a calculator 2.0 class with 2 methods for 
# multiplication and Divsion of 2 values and inherit it from the calculator class.


class calculator:
    def add(self,x,y):
        return x+y
    
    def subtract(self,a,b):
        return a-b

class calculator2(calculator):
    def multiplication(self,x,y):
        return x*y
    
    def Divsion(self,x,y):
        return x/y

cal = calculator2()

value1 = 2323
value2 = 23

sum_result = cal.add(value1,value2)
subtration_result = cal.subtract(value1,value2)
multiplcation_result = cal.multiplication(value1,value2)
division_result = cal.Divsion(value1,value2)

print(f"Addition: {sum_result}")
print(f"Subtraction: {subtration_result}")
print(f"Multiplication: {multiplcation_result}")
print(f"Division: {division_result}")