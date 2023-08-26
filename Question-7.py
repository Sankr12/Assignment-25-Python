# Write a python script to create phone class with 2 methods to print the features (calling and sms)

class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def call(self, number):
        print(f"Calling {number}...")
    
    def send_sms(self, number, message):
        print(f"Sending SMS to {number}: {message}")

# Creating an instance of the Phone class
my_phone = Phone("Samsung", "Galaxy S21")

# Example usage
phone_number = "123-456-7890"
sms_message = "Hello, how are you?"

my_phone.call(phone_number)
my_phone.send_sms(phone_number, sms_message)
