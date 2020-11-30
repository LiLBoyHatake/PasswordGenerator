#First import random
import random

#define chars
characters = 'abcdefghijklmnopqrstuvwyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'



#Define
length = input('How long do you want the password to be?')
length = int(length)

for c in range(length):
    password += random.choice(characters)
    print(password)

with open('file.txt', 'a') as myFile:
    myFile.write(password)