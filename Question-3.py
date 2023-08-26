# Write a python script to update 2nd question, change email and age to __email and __age 

class profile:
    def __init__(self,name,__age,__email):
        self.__age = __age
        self.__name = name 
        self.__email = __email

    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age

    def set_email(self,email):
        self.__email = email
        
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

if __name__ == "__main__":
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    email = input("Enter E-mail: ")

    person1 = profile(name,age,email)
    print("Name:",person1.get_name())
    print("Age:",person1.get_age())
    print("E-mail:",person1.get_email())

    new_name = input("Enter new name: ")
    person1.set_name(new_name)

    new_age = int(input("Enter age: "))
    person1.set_age(new_age)

    new_email = input("Enter email: ")
    person1.set_email(new_email)

    print()
    print("Updated Profile")
    print("Name:",person1.get_name())
    print("Age:",person1.get_age())
    print("Email:",person1.get_email())