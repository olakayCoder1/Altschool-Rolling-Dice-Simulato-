


'''
This is one of the interesting python projects and will generate a
random number each dice the program runs, and the users can
use the dice repeatedly for as long as they want. When the user
rolls the dice, the program will generate a random number between
1 and 6 (as on a standard dice . The number will then be displayed
to the user. It will also ask users if they would like to roll the dice
again. The program should also include a function that can
randomly grab a number within 1 to 6 and print it.

'''
import random


def roll_dice():
    die_one = random.choice(range(1,7))
    die_two = random.choice(range(1,7))
    return [ die_one , die_two]


def start():
    try:
        user_ask = input('Do you want to roll dice ( Yes or No ) : ')
    except ValueError:
        print('Invalid input response')
        return
    if user_ask.lower() == 'yes':
        dice_output = roll_dice()
        print(dice_output)
        start()
    if user_ask.lower() == 'no':
        return
    print('Thanks for checking ')
    return

if __name__ == "__main__" :
    start()

