allGuests = {'Dickson': ['Jack Daniels', 'Sminnorf'],
              'Liverson': ['Kenya Cane', 'Kibao'],
              'Wakio' : ['Legend', 'Simba Imara']}

def getDrinks(guests):
    for n in guests.items():
        for name in n:
            print(name)

getDrinks(allGuests)

newGuests = {'Alice' : {'apples' : 5, 'pretzels' : 12},
            'Bob' : {'ham sandwiches' : 3, 'apples' : 2},
            'Carol' : {'cups' : 3, 'apple pies' : 1}
}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print("Number of things being brought")
print (' - apples' + str(totalBrought(allGuests, 'apples')))