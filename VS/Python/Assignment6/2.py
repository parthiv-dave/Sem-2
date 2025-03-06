import random

class Rock_paper_scissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ["rock", "paper", "scissors"]
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "draw"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.user_wins += 1
            return "user"
        else:
            self.computer_wins += 1
            return "computer"
    
    def check_winner(self):
        if self.user_wins > self.rounds // 2:
            return "User wins the game!"
        elif self.computer_wins > self.rounds // 2:
            return "Computer wins the game!"
        return None
    
    def play(self):
        while self.current_round < self.rounds:
            self.current_round += 1
            user_choice = input("Enter rock, paper, or scissors: ").strip().lower()
            if user_choice not in self.choices:
                print("Invalid choice. Try again.")
                self.current_round -= 1
                continue
            
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            
            result = self.find_winner(user_choice, computer_choice)
            if result == "draw":
                print("It's a draw!")
            elif result == "user":
                print("You win this round!")
            else:
                print("Computer wins this round!")
            
            game_winner = self.check_winner()
            if game_winner:
                print(game_winner)
                break
        else:
            print("Game over! Final Scores - User: ", self.user_wins, ", Computer: ", self.computer_wins)

rounds = int(input("Enter number of rounds: "))
game = Rock_paper_scissors(rounds)
game.play()
