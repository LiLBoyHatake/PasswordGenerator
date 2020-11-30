#First import random
import random

#define chars
characters = 'abcdefghijklmnopqrstuvwyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

#Define
pig = input('Please input the number of password you want...')
pig = int(pig)
length = input('How long do you want the password to be?')
length = int(length)


for p in range(pig):
    password = ''
    for c in range(length):
        password += random.choice(characters)
    print(password)