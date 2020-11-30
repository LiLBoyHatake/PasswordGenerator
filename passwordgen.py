#First import random
import random
import os
import os.path
import string
import time

#define chars
characters = 'abcdefghijklmnopqrstuvwyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

print('Please make sure that you have a Passwords.txt file located on your desktop.')

#Define
length = input('How long do you want the password to be?')
length = int(length)


password = ''

passwordApp = input('Title for file... ')

for c in range(length):
    password += random.choice(characters)
    print(password)

print('Making a file for your password')

passFile = open(os.path.expanduser(os.path.join('~/Desktop/Passwords.txt')), 'a')
passFile.write(passwordApp + '\n' + password + '\n')

time.sleep(1.5)
print('File Saved')

print('Thanks for using LiLBoyHatakes code! Thanks to Gravy for giving me some code fix ideas!')