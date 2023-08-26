# Write a python script to create a smartphone class by inheriting 
# Calculator 2.0 and phone class. 

class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, a, b):
        return a - b

class Calculator2(Calculator):
    def multiplication(self, x, y):
        return x * y
    
    def division(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"

class Phone(Calculator2):
    def call(self, number):
        print(f"Calling {number}...")
    
    def send_sms(self, number, message):
        print(f"Sending SMS to {number}: {message}")

class SmartPhone(Phone):
    def browse_internet(self, URL):
        print(f"Browsing... {URL}")

if __name__ == "__main__":
    phone1 = SmartPhone()
    print("\nPower On!\n")
    
    while True:
        choice = input("Enter what you want to use [call/sms/calculator/internet] or off: ").lower()
        
        if choice == "call":
            number = input("Enter number: ")
            phone1.call(number)
            print()

        elif choice == "internet":
            url = input("Enter URL: ")
            phone1.browse_internet(url)
            print()

        elif choice == "sms":
            number = input("Enter number: ")
            message = input("Enter message: ")
            phone1.send_sms(number, message)
            print()

        elif choice == "calculator":
            value1 = float(input("Enter first number: "))
            calchoice = input("Enter the Operation [add/sub/multi/div]: ").lower()
            
            if calchoice in ["add", "sub", "multi", "div"]:
                value2 = float(input("Enter second number: "))
                
                if calchoice == "add":
                    print(f"{value1} + {value2} =", phone1.add(value1, value2))
                elif calchoice == "sub":
                    print(f"{value1} - {value2} =", phone1.subtract(value1, value2))
                elif calchoice == "multi":
                    print(f"{value1} * {value2} =", phone1.multiplication(value1, value2))
                else:
                    print(f"{value1} / {value2} =", phone1.division(value1, value2))
                print()
            else:
                print("Invalid operation. Please choose add/sub/multi/div.")
                print()
        
        elif choice == "off":
            print("\nPower Off!\n")
            break
        
        else:
            print("Invalid choice. Please choose from call/sms/calculator/internet/off.")
            print()
