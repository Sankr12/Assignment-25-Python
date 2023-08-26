# Write a python script to create a Profile class with 3 attributes (name,email.age)

class profile:
    def __init__(self,name,age,email):
        self.age = age
        self.name = name 
        self.email = email

if __name__== "__main__":
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")
    
    person1 = profile(name,age,email)

    print()
    print("Profile Created")
    print("Name:",person1.name)
    print("Age:",person1.age)
    print("E-mail:",person1.email)