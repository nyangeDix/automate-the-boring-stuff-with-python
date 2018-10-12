#The character "|" is called the pipe key
import re
findName = re.compile(r'Dickson | Nyange')
mo = findName.search('Dickson is Nyange')
print(mo.group())
#note the difference between the two set of codes
findName2 = re.compile(r'Nyange | Dickson')
mo2 = findName2.search('Nyange is Dickson')
print(mo2.group())
#The pipe key can also be used to match several patterns
findBat = re.compile(r'Bat(man|mobile|plate|plane|copter)')
mo3 = findBat.search('Yesterday i saw a Batcopter on the hills')
print(mo3.group())
print(mo3.group(1))
#optional matching with question mark
findBat2 = re.compile(r'Bat(wo)?man') #the part (wo)? is optional
mo4 = findBat2.search('I saw Batman')
print(mo4.group())
#Second set of code to test optional
mo5 = findBat2.search('I am a Batwoman')
print(mo5.group())

findNumber = re.compile(r'(\d\d\d)?\d\d\d-\d\d\d\d')
moNumber = findNumber.search('My number is 120-4542')
print(moNumber.group())

#Matching zero or more with the start
find_name = re.compile(r'Bat(wo)*man')
search_name = find_name.search('I am a Batman')
print(search_name.group())

search_name2 = find_name.search('Flora is a Batwoman')
print(search_name2.group())

search_name3 = find_name.search('Wakio is a Batwowowowowowoman')
print(search_name3.group())

#matching one or more with the the plus
findPlus = re.compile(r'Bat(wo)+man')
search_more = findPlus.search('I am a Batwoman')
print(search_more.group())

search_more2 = findPlus.search('I killed a Batman')
if search_more2 == None:
    print ("The pattern didn't find a match")

search_more3 = findPlus.search('I am Batwowowowoman')
print(search_more3.group())

#matching with curly braces
find_new_regex = re.compile(r'(Ho){4}')
more_search = find_new_regex.search('HoHoHoHo')
print(more_search.group())

#Greedy and none greedy matching
find_laugh = re.compile(r'(ha){3,5}?')
search_laugh = find_laugh.search('He laughed so hahahaha')
print(search_laugh.group())

search_laugh2 = find_laugh.search('She laughed so nicely, hahahaha')
print(search_laugh2.group())
