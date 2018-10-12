#Get method checks if a key exists in a dictionary
food  = {'fruits':'apples',
         'vegetables':'kales',
         'cereals':'maize',
         'drinks':'vodka'
}

print("Jane likes eating", food.get('fruits', 'Mangoes'), "to gain more Vitamins C")
print("William a thief likes to smoke", food.get('drugs', 'weed'), "atleast everyday")