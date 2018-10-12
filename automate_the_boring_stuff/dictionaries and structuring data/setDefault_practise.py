#Program to calculate how many times a letter appears in the sentense
#Pretty printing
import pprint

message = "It was a cold afternoon on September 9, 1996. So i decided to drink tea"
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

message2 = "Dickson likes programming in python"

count2 = {} 

for n in message2:
    count2.setdefault(n, 0)
    count2[n] = count2[n] + 1
    
pprint.pprint(count2)