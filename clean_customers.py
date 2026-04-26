# Functions for cleaning  `customers.txt`

def format_email(email):
    return email.lower()

def format_name(name):
    return name.title()

def format_phone(number):
    return number.replace(" ", "").replace("-", "").replace("+", "")

if __name__ == '__main__':
    email = "KUMAR@gmail.com"
    name = "Vincent RAJ"
    number = "+91- 23923933"
    print(format_email(email))
    print(format_name(name))
    print(format_phone(number))