#Create a program that will accept a list value and 
#Print out the list items as sentence, the last value of the list should be followed by (and)
def practisePro(listVal):
    for val in listVal:
        print ("I have the following fruits" + val)

fruits = ['mango', 'orange', 'watermelon', 'guavas']
practisePro(fruits)