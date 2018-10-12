spam = "    Hello Dickson    "
spam_1 = spam.strip()
print(spam_1)
spam_2 = spam.lstrip()
print(spam_2)
spam_3 = spam.rstrip()
print(spam_3)

new_spam = 'SpamSpamSpamBaconSpamEggsSpam'
new_spam2 = new_spam.strip('ampS')
print(new_spam2)