def voting():
    try:
        age = input("Please enter age: ")
        age = int(age)
    except TypeError:
        print("Please enter the correct type")
    else:
        if int(age) >= 18:
            print("You are allowed to vote")
        elif int(age) <= 18:
            print("You are too young to vote")

def p_names():
    print("My name is")
    for i in range(5):
        print("Jimmy five times", str(i))

def get_total():
    total = 0
    for num in range(101):
        total = total + num
    print(total)

def get_name_while():
    i = 0
    while i < 5:
        print("Hey Jesus loves you brother and sister")
        i += 1

voting()