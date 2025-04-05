import random

def get_user_choice():
    choice = input("Choose Rock, Paper or Scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice!")
        choice = input("Choose Rock, Paper or Scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def decide_winner(user, computer):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}\n")
    
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = decide_winner(user_choice, computer_choice)
    print(result)

play()
