#Adds a default dictionary item to an already existing dictionary
#This only applies when the key and value are not available in the dictionary
food  = {'fruits':'apples',
         'vegetables':'kales',
         'cereals':'maize',
         'drinks':'vodka'
}

"""
if 'drugs' not in food:
    food['drugs'] = 'weed'
"""
#this can also be done as shown below

food.setdefault('drugs', 'weed')

print(food)