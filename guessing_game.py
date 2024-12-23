import random

def guessing_game():
    # Step 2: Define the game rules and logic
    number_to_guess = random.randint(1, 100)
    attempts = 6
    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess the number.")

    while attempts > 0:
        # Get the player's guess
        guess = int(input("Enter your guess: "))
        
        # Step 3: Use conditional statements to manage game flow
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print("Congratulations! You guessed the correct number.")
            break
        
        attempts -= 1
        print(f"You have {attempts} attempts left.")
        
        if attempts == 0:
            print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}.")

# Step 4: Test and debug the game for correctness
guessing_game()
