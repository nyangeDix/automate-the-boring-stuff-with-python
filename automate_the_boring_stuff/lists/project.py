import random

messages = ['It is certain',
            'It is decided;y so',
            'Yes definately',
            'Reply hazy try again',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful'
    ]

print(messages[random.randint(0, len(messages) -1)])