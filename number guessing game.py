import random
import math

upper_bound = int(input("Please enter the upper bound of your range: "))
lower_bound = int(input("Please enter the lower bound of your range: "))

random_number = random.randint(lower_bound, upper_bound)
max_num_guess = int(math.log2(upper_bound - lower_bound +1))

def number_guessing_game():
    print(f"You've got {max_num_guess} guesses to try")
    guess_number = int(input("Please enter your guess number: "))
    count_guess = 1
    if guess_number == random_number:
        return "Congratulations!\nTotal Number of Guesses = 1" 
    while count_guess < max_num_guess:
        if guess_number == random_number:
            return f"Congratulations!\nTotal Number of Guesses = {count_guess}"
        elif guess_number < random_number:
            print(f"Try Again! You guessed too small.\nYou've still got {max_num_guess - count_guess} guess(es) to try")
            guess_number = int(input('guess again: '))
            count_guess += 1
        else:
            print(f"Try Again! You guessed too high.\nYou've still got {max_num_guess - count_guess} guess(es) to try")
            guess_number = int(input('guess again: '))
            count_guess += 1
    if guess_number == random_number:
        return f"Congratulations!\nTotal Number of Guesses = {count_guess}"
    return f"Better Luck Next Time!\nTotal Number of Guesses = {count_guess}\nThe random number was: {random_number}"

print(number_guessing_game())