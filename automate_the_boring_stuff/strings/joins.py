#String Joins
description = ' '.join(['Dickson','is','a','coffee','junkie'])
print(description)

#String Split
message = "Programming requires passion and persitance"
new_message = message.split()
print(new_message)

spam = '''Dear Dickson,

Hello my code mate, it's been a while and i was wondering when 
are we to make our second python program? Let's meet on 20th, October
and discuss on how we are going to make our new program.

Regards,
Sanderson Mwakamba
'''

new_spam = spam.split('\n')
print(new_spam)