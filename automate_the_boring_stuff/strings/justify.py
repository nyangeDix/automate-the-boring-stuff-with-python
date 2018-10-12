name = "Dickson"
new_name = name.rjust(10)
print(new_name)

message = "Dickson codes in python, i am a coffee junkie to"
new_message = message.rjust(30)
print(new_message)

spam = "Hello World"
new_spam = spam.rjust(20, '*')
print(new_spam)
new_spam2 = spam.ljust(20, '-')
print(new_spam2)
new_spam3 = spam.center(20)
print(new_spam3)
new_spam4 = spam.center(20, '=')
print(new_spam4)