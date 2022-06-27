#password generator
import random

print('Password Generator')
print('-------------------')
print()

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?,.;:*&%$§1234567890'

amount_passwords = input('How many passwords do you want to generate? ')
amount_passwords = int(amount_passwords)

length_passwords = input('How many characters do you want your password(s) to have? ')
length_passwords = int(length_passwords)

print('Here are your passwords: ')

for i in range(amount_passwords):
    passwords = ''
    for j in range(length_passwords):
        passwords += random.choice(characters)
    print(passwords)