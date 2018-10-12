#! python 3
#! pw.py - an insecure password locker
PASSWORDS = {
    'email' : 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'blog' : 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'luggage' : '12345'
}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage : python pw [account] - copy account password')
    sys.exit()

account = sys.argv[1] #First command line argv in the account name

if account in PASSWORDS:
