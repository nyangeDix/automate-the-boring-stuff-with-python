import re

def getName(name_list):
    get_name = re.compile(r'\d+\s\w+')
    search_name = get_name.findall(name_list)
    return search_name

def searchLetters(my_string):
    get_string = re.compile(r'[aeiouAEIOU]')
    find_string = get_string.findall(my_string)
    return find_string

name_strings = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'
my_list = getName(name_strings)
print(my_list)

my_article = 'Robocop eats baby food. BABY FOOD.'
my_article_list = searchLetters(my_article)
print(my_article_list)