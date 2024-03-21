import random
import time

def Start():
    name = input("Enter your name?:")
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def choose(max_guesses):
    random_number = random.randint(1, 200)
    guesses_taken = 0

    while guesses_taken < max_guesses:
        try:
            guess = int(input("Guess: "))

            if 1 <= guess <= 200:
                guesses_taken += 1
                if guess < random_number:
                    print("The guess of the number is too low.")
                elif guess > random_number:
                    print("The guess of the number is too high.")
                else:
                    print("Good job,!You guessed my number in {} guesses!".format(guesses_taken))
                    return
            else:
                print("Silly Goose! Please enter a number between 1 and 200.")

        except ValueError:
            print("I don't think that's a number. Sorry.")

    print("Nope. The number I was thinking of was {}.".format(random_number))

play_again = "yes"
while play_again.lower() in ["yes", "y"]:
    Start()
    choose(6)
    play_again = input("Do you want to play again? (yes/no):")