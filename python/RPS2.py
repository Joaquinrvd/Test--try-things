import random 
answers = ["rock", "paper", "scissors"]
def pick_answer():
    return random.choice(answers)
    


def RPS():
    print("welcome to Rock Paper Scissors!")
    player1 = input("Player 1, Please enter your name: ")
    p1_choice = input(f"{player1}, chose between Rock, Paper, & Scissors ").lower()
    while not is_valid_move(p1_choice):
        print("Invalid choice. Please try again.")
        p1_choice = input(f"{player1}, choose between Rock, Paper, & Scissors: ").lower()
    cpu = pick_answer()



# I got the code to work but i used chatgbt to compress this part down
    if p1_choice == cpu:
        print(f"Both chose {cpu}. It's a tie!")
    elif (p1_choice == "rock" and cpu == "scissors") or \
         (p1_choice == "paper" and cpu == "rock") or \
         (p1_choice == "scissors" and cpu == "paper"):
        print(f"{p1_choice.capitalize()} beats {cpu}, {player1} wins!")
    elif (cpu == "rock" and p1_choice == "scissors") or \
         (cpu == "paper" and p1_choice == "rock") or \
         (cpu == "scissors" and p1_choice == "paper"):
        print(f"{cpu.capitalize()} beats {p1_choice}, computer wins!")
    else:
        print("Invalid choice. Please select rock, paper, or scissors.")


answers = ["rock", "paper", "scissors"]

def pick_answer():
    return random.choice(answers)

def is_valid_move(player_move):
    return player_move in answers
RPS()

