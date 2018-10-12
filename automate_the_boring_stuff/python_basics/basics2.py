def fullName(first, second):
    fullname = first + " " + second
    return fullname.upper()

def fullName_mdname(first, second, middle = ''):
    fullName = first + ' ' + middle + ' ' + second
    return fullName.upper()

def get_string_num(stringName):
    return len(stringName)

firstname = input("Please enter your first name")
secondname = input("Please enter your second name")
middlename = input("Please enter your middle name - not a must though")

myNames = fullName(firstname, secondname)
print("My full names are: " + myNames)

myNames2 = fullName_mdname(firstname, secondname, middlename)
print("All my names: " + myNames2)