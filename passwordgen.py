#First import random
import random

#define chars
characters = 'abcdefghijklmnopqrstuvwyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'


number = input('Please input the number of password you want...')
number = int(number)
length = input('How long do you want the password to be?')
length = int(length)


for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(characters)
    print(password)