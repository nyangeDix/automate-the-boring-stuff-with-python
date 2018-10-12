def getWord(word):
    if word.islower():
        return word.upper()
    else:
        return 'not found'

def get_alpha(word):
    if word.isalpha():
        print("Word entered only consists of alphabetical letters")
    
def get_alnum(word):
    if word.isalnum():
        print("Word consists of alphabets and numbers")

def get_dec(word):
    if word.isdecimal():
        print("Word consists only of numbers")
    
def get_title(word):
    #Checks if word is uppercase
    if word.istitle():
        print("Word is of uppercase letters")

def get_start(word):
    if word.startswith('Dickson'):
        print("Yes string starts with Dickson")
    
def get_end(word):
    if word.endswith('Python'):
        print("Yes the word ends with the word python")

get_title('Dickson')