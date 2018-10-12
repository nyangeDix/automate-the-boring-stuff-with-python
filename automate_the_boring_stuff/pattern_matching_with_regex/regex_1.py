#import the module dude
import re

def kenyaPhone():
    kePhonenumber = re.compile(r'\d\d-\d\d-\d\d\d-\d\d\d')
    foundNumber = kePhonenumber.search('Hey here is my number: 07-17-590-340')
    print('Number found: ', foundNumber.group())

def kenyanPhone():
    kePhoneNumber = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d\d\d)')
    findNumber = kePhoneNumber.search('My number is 254-717-590340')
    print('Country Code: ' , findNumber.group(1))
    print('Rest of number: ' , findNumber.group(2))
    print(findNumber.group(0))
    print(findNumber.group())

kenyanPhone()