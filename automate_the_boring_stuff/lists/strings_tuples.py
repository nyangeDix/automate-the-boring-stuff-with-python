my_name = 'Dickson'
#print(name[0])#Prints the first letter in a list
for letter in my_name:
    print("*****" + letter + "*****")

#Tuple data type
eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])

#Concerting list to a tuple
list_names = ['Dickson', 'Sanderson', 'Flora', 'Scaver']
print(tuple(list_names))
