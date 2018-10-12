spam = {'color':'red', 'size':'20'}

#access all items
for v in spam.items():
    print(v)

#access values
for c in spam.values():
    print(c)

#access keys in a dictionary
for d in spam.keys():
    print(d)

#adding list and key values
spam['brand'] = 'Nike'

for r, t in spam.items():
    print('Key: ' + r + ' value ' + str(t))

#Check if key of values exists in a dictionary
if 'color' in spam.keys():
    print("Key is available")
else:
    print ("Key not available")

#Get method
picnicItems = {'apples' : 5, 'cupcakes':4}
print("I am bringing " + str(picnicItems.get('cupcakes', 0)) + " of cupcakes")