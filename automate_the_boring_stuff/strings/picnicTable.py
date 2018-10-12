"""
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
"""

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
for k, v in picnicItems.items():
    print(k.ljust(12, '.') + str(v).rjust(5))

print('-------------------------')

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
for k, v in picnicItems.items():
    print(k.ljust(20, '.') + str(v).rjust(6))
    