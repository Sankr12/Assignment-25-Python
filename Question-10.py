# Write a python script to add a new method in smartphone class which accepts 
# Truecaller object as a parameter and call the fetch method of truecaller

class Truecaller:
    def __init__(self):
        self.contacts = {}

    def add_info(self,name,number):
        self.contacts[number] = name
        
    def fetch_info(self,number):
        if number in self.contacts:
            return self.contacts[number]
        else:
            return "Contact Not Found"

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

class Phone(Calculator2,Truecaller):
    def call(self, number):
        print(f"Calling {number}...")
    
    def send_sms(self, number, message):
        print(f"Sending SMS to {number}: {message}")

class SmartPhone(Phone,Truecaller):
    def browse_internet(self, URL):
        print(f"Browsing... {URL}")

if __name__ == "__main__":
    phone1 = SmartPhone()
    print("\nPower On!\n")
        
    while True:
        choice = input("Enter what you want to use [call/sms/calculator/contacts/internet] or off: ").lower()
        
        if choice == "call":
            number = input("Enter number: ")
            phone1.call(number)
            print()

        elif choice == "contacts":
            phone1.add_info("Sandeep", 8860033614)
            phone1.add_info("Sanjay", 9625524691)
            phone1.add_info("Shashi", 9717085118)
            phone1.add_info("Mummy", 9958089022)
            phone1.add_info("Papa", 9717123521)
            phone1.add_info("Manish Puri Goswami", 7982688959)
            phone1.add_info("Ayush Rai", 8447035979)

            number_input = int(input("\nEnter number to search name: "))
            print(phone1.fetch_info(number_input))            

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
