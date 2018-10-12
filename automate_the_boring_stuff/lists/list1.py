import copy

def get_list_length():
    list_items = ['Dickson', 'Sanderson', 'Flora', 'Scaver']
    return len(list_items)#len returns the number of words in the list

def get_new_list():
    list_values = [['cat', 'bat'], [10, 20, 30, 40, 50]]
    return list_values

def list_animals():
    list_values = ['cat', 'bat', 'rat', 'elephant']
    return list_values

print(get_list_length())

spam_list = get_new_list()
print(spam_list[0][1])#
print(spam_list[1][4])
spam_animals = list_animals()
print(spam_animals[-4])

#Getting sublists with slices
print(spam_animals[0:-1])
print(spam_animals[0:3])
print(spam_animals[:2])
print(spam_animals[1:])
print(spam_animals[:])
print("The length for spam animals list is: ",len(spam_animals))

#Chaning a list value 
spam_animals[-1] = 'dove'
print(spam_animals[:])

#list concatenation and list replication
spam_list = [1, 2, 3, 4]
new_spam = spam_list + ['Dickson', 'Sanderson', 'Flora', 'Scaver']
print(new_spam)

#Removing values from a list
del spam_animals[-1]
print(spam_animals[:])

#Loops in lists
numbers = [i for i in range(0,5)]
print(numbers)

#Using lists in for
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

print ("Enter name of a supply")
supply = input()

if supply not in supplies:
    print ("Supply is not available in list")
else:
    print("Supply available")

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

#Methods
spam_greetings = ['hello', 'hi', 'howdy', 'heyas']
print(spam_greetings.index('hi'))
print(spam_greetings.index('heyas'))

#Adding values to a list
#----------using append
spam_greetings.append('Hey')
spam_greetings.append('Yoh!')

#using insert
spam_greetings.insert(1, 'Yah Bro!')
spam_greetings.insert(0, 'Salaam Aleikum')

print(spam_greetings[:])

#Removing values from a list
spam_greetings.remove('hello')
print(spam_greetings)

#sorting the values in a list
spam_greetings.sort(reverse=True)
print(spam_greetings)

spam_greetings.sort(key = str.lower)
print(spam_greetings)

spam_letters = ['A', 'B', 'C', 'D']
spam_cheese = copy.copy(spam_letters)
spam_cheese[2] = 100
print(spam_cheese)