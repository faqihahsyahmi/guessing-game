import art
import random

def play_game():
    print(art.logo)
    #user choose game level - easy or hard
    lives = 5
    level = input("Choose a difficulty. Type 'easy' or 'hard' ").lower()
    if level == "easy":
        lives = 10

    chosen_number = random.randint(1,100)
    #player_input = int(input("Make a guess: "))
    is_game_over = False

    #print(chosen_number)

    while not is_game_over:
        #compare user input with chosen number
        if lives != 0:
            player_input = int(input("Make a guess: "))
            
            if player_input == chosen_number:
                print(f"Wow, you guess right! The answer is {chosen_number}")
                is_game_over = True
            elif player_input > chosen_number:
                lives -= 1
                print("Too high")
                print(f"You have {lives} left!")
            elif player_input < chosen_number:
                lives -= 1
                print("Too low")
                print(f"You have {lives} left!")
        else:
            is_game_over = True
            print("You ran out of lives!")


while input("Play Guessing Game? 'y' or 'n': ").lower() == "y":
    print("\n"*20)
    play_game()
