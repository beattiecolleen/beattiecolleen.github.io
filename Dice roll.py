#Dice roll
import random

min_limit = 1
max_limit = 6

roll_again = 'yes'

while roll_again == 'yes' or roll_again == 'y':
    print('Dices rolling ... ')
    print('The values are: ')
    #Variable for the first dice
    print(random.randint(min_limit, max_limit))
    print()
    #Variable of the second dice
    print(random.randint(min_limit, max_limit))
    print()
    
    roll_again = input('Roll the dices again? (y/n)')