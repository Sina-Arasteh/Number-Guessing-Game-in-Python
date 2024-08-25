import random
import math

upper_bound = int(input("Please enter the upper bound of your range: "))
lower_bound = int(input("Please enter the lower bound of your range: "))

random_number = random.randint(lower_bound, upper_bound)
max_num_guess = int(math.log2(upper_bound - lower_bound +1))

def number_guessing_game():
    print(f"You've got {max_num_guess} guesses to try")
    guess_number = int(input("Please enter your guess number: "))
    count_guess = 0
    if guess_number == random_number:
        return "Congratulations!\nTotal Number of Guesses = 1"
    else:
        while count_guess < (max_num_guess - 1):
            if guess_number == random_number:
                count_guess += 1
                return f"Congratulations!\nTotal Number of Guesses = {count_guess}"
            elif guess_number < random_number:
                print("Try Again! You guessed too small.")
                count_guess += 1
                print(f"You've still got {max_num_guess - count_guess} guess(es) to try")
                guess_number = int(input('guess again: '))
            else:
                print("Try Again! You guessed too high.")
                count_guess += 1
                print(f"You've still got {max_num_guess - count_guess} guess(es) to try")
                guess_number = int(input('guess again: '))
        return f"Better Luck Next Time!\nTotal Number of Guesses = {count_guess}"

print(number_guessing_game())