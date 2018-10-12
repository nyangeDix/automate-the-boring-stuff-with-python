import re
phone_number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
search_number = phone_number.findall('Home number: 254-452-5620 Work: 254-562-4854')
for number in search_number:
    print (number)