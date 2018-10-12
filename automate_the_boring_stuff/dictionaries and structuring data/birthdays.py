birthdays = {'Dickson':'9 Sept', 'Nyange':'10 October', 'Ngoji':'12 December'}

while True:
    print("Please enter your friend's name:")
    name = input()

    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("Sorry person's information not available")
        print("What's their birthday?")
        bday = input()
        birthdays[name] = bday
        print("User information successfully added")
