import random
import math

lower_bound = int(input("Please enter the starting endpoint of your range: "))
upper_bound = int(input("Please enter the ending endpoint of your range: "))

random_number = random.randint(lower_bound, upper_bound)
minimum_num_guess = math.log2(upper_bound - lower_bound +1)
def number_guessing_game():
    guess_number = int(input("Please enter your guess number: "))
    count_guess = 1
    while guess_number != random_number:
        if guess_number < random_number:
            print("Try Again! You guessed too small.")
            count_guess += 1
            guess_number = int(input('guess again: '))
        else:
            print("Try Again! You guessed too high.")
            count_guess += 1
            guess_number = int(input('guess again: '))
    if count_guess <= minimum_num_guess:
        return f"Congratulations!\nTotal Number of Guesses = {count_guess}"
    else:
        return f"Better Luck Next Time!\nTotal Number of Guesses = {count_guess}"