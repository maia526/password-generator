import random

print('Welcome to your password genrator!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%&*(),.:;1234567890'

number = input("How many passwords would you like? ")
number = int(number)

length = input('How long should the passwords be? ')
length = int(length)

print('\nHere are your passwords:')

for pwd in range(number): #pwd short for password
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
