from datetime import datetime

def age():  
    birthday = input("\nWelcome, please enter your birthday (MM/DD/YYYY): ")
    birthdate = datetime.strptime(birthday, "%m/%d/%Y")
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < \
    (birthdate.month, birthdate.day))
    print("\nYour age is " + str(age) + " years old.\n")

age()
