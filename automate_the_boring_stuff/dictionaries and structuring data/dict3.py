dickson = {
    'color':'light skinned',
    'weight':'70kgs',
    'hobby':'computer programming',
    'sports':'badminton',
    'girlfriend':'single'
}

#Accessing Dickson's values
print("This tell a lot about Dickson")
for n in dickson.values():
    print(n)

#Now let's access the keys use
for v in dickson.keys():
    print("This are the keys used in dickson: ", v)

#Access everithing
for all_things in dickson.items():
    print(all_things)

#print a single value
print ("Hahaha! Guys Dickson is ",dickson['girlfriend'])

#print dickson's sports
print ("Hey! Dickson likes playing", dickson['sports'])