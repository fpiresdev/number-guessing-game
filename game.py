import random

line01 = "***********************"
line02 = "*                     *"
line03 = "*       WELCOME       *"
line04 = "*     TO THE GAME     *"

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


# Function to start the number guessing game


def start_game():
    print("---GAME STARTED, GUESS THE NUMBER FROM 1 TO 100!---")
    print('')
    random_number = random.randint(1, 100)

    while True:
        guess = input("ENTER YOUR GUESS: ")

        if not guess.isdigit():
            print("INVALID INPUT! PLEASE ENTER A NUMBER.")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("OUT OF RANGE! PLEASE GUESS A NUMBER BETWEEN 1 AND 100.")
            continue

        distance = abs(guess - random_number)
        if distance == 0:
            print("CONGRATULATIONS! YOU GUESSED IT RIGHT!")
            return
        elif distance <= 5:
            if guess < random_number:
                print("VERY CLOSE! TRY HIGHER.")
            else:
                print("VERY CLOSE! TRY LOWER.")
        elif distance <= 15:
            if guess < random_number:
                print("CLOSE! TRY HIGHER.")
            else:
                print("CLOSE! TRY LOWER.")
        else:
            if guess < random_number:
                print("FAR! TRY HIGHER.")
            else:
                print("FAR! TRY LOWER.")


# Display welcome message (probably the least efficient way to do this, but it works for now)
print(line01)
print(line02)
print(line03)
print(line04)
print(line02)
print(line01)

# Password protection
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
