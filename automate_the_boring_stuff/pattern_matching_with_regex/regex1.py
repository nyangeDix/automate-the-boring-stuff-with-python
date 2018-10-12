#Create a function to find the kenyan phone number
import re

def get_kenya(number):
    #phoneNumber = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
    #Every d in the compiler function represents a digit
    if True:
        phoneNumber = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
        get_confirmation = phoneNumber.search(number)
        print('Phone number found: ' + get_confirmation.group())

get_kenya('My number is 0717-590-340')