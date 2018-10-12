import random

#functions with parameters
def hello(name):
    print("Hello" + name + " welcome back again")

#function with return
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly 20'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful' 

#global and local variables
eggs = 190

def spam():
    eggs = 90
    bacon()
    print(eggs)

def bacon():
    ham =101
    eggs = 0

#Calling functions below
hello("Dickson")

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

spam()
print(eggs)