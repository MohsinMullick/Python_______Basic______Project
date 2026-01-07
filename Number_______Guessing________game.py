# Number Guessing Game
import random#jsut for random numbers like randint()

print("Welcome to number guessing Game!!!!")
print("I am thinking of a number between 1 to 100: ")

secret_number = random.randint(1, 100)#this line important because user guess
attempts = 0 #just user how time to try

while True:# infinite loop until user guess number correct and then break
    guess = int(input("Enter your guess: "))
    attempts += 1  #count user how times 0 to increase

    if guess < secret_number:#check guess number how to far correct numbers
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")  # check guess number how to far correct numbers
    else:
        print(f"\nCongratulations! You guessed it in {attempts} attempts!")
        play_again = input("\nDo you want to play again (yes or no): ")
        if play_again.lower() == "yes":
            secret_number = random.randint(1, 100)
            attempts = 0
            print("\nNew game started! Guess again.")
        else:
            print("\nThank you for playing. Good Bye!")
            break