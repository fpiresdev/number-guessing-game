import random

# Constants
VERY_CLOSE_THRESHOLD = 5
CLOSE_THRESHOLD = 15
BANNER = [
    "***********************",
    "*                     *",
    "*       WELCOME       *",
    "*     TO THE GAME     *",
    "*                     *",
    "***********************"
]

# Function to handle replay prompt


def replay_prompt():
    while True:

        play_again = input("PLAY AGAIN? (Y/N): ").strip().lower()

        if play_again == 'y':
            print("RESTARTING THE GAME...")
            return True
        elif play_again == 'n':
            print("THANK YOU FOR PLAYING! GOODBYE! :)")
            return False
        else:
            print("INVALID INPUT! PLEASE ENTER 'Y' OR 'N'.")


def get_feedback(distance, guess_int, random_number):
    """Generate feedback message based on distance from target."""
    if distance == 0:
        return "CONGRATULATIONS! YOU GUESSED IT RIGHT!"
    
    direction = "HIGHER" if guess_int < random_number else "LOWER"
    
    if distance <= VERY_CLOSE_THRESHOLD:
        return f"VERY CLOSE! TRY {direction}."
    elif distance <= CLOSE_THRESHOLD:
        return f"CLOSE! TRY {direction}."
    else:
        return f"FAR! TRY {direction}."


# Function to start the number guessing game


def start_game():
    print("---GAME STARTED, GUESS THE NUMBER FROM 1 TO 100!---")
    print()
    random_number = random.randint(1, 100)

    while True:
        guess = input("ENTER YOUR GUESS: ")

        if not guess.isdigit():
            print("INVALID INPUT! PLEASE ENTER A NUMBER.")
            continue
        
        guess_int = int(guess)
        
        if guess_int < 1 or guess_int > 100:
            print("OUT OF RANGE! PLEASE GUESS A NUMBER BETWEEN 1 AND 100.")
            continue

        distance = abs(guess_int - random_number)
        feedback = get_feedback(distance, guess_int, random_number)
        print(feedback)
        
        if distance == 0:
            return


# Display welcome message
for line in BANNER:
    print(line)

# Password protection loop
while True:
    password = input("ENTER PASSWORD TO START: ").strip().lower()

    if password == "letmein":
        print("ACCESS GRANTED")
        print("Starting the game...")
        while True:
            start_game()
            if not replay_prompt():
                break

        break
    else:
        print("ACCESS DENIED")
        print("TRY AGAIN")
