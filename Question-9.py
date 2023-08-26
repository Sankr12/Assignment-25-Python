# Write a python script to create an application like Truecaller where names 
# and numbers are stored. Truecaller class will have 2 methods (1st to fetch 
# the name of a number and 2nd to add a new entry).

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


phone1 = Truecaller()
if __name__ == "__main__":
    
    name = input("\nEnter you name: ")
    number = int(input("\nEnter your number: "))

    phone1.add_info("Sandeep", 8860033614)
    phone1.add_info("Sanjay", 9625524691)
    phone1.add_info("Shashi", 9717085118)
    phone1.add_info("Mummy", 9958089022)
    phone1.add_info("Papa", 9717123521)
    phone1.add_info("Manish Puri Goswami", 7982688959)
    phone1.add_info("Ayush Rai", 8447035979)

    phone1.add_info(name,number)

    number_input = int(input("\nEnter number to search name: "))

    print(phone1.fetch_info(number_input))
    