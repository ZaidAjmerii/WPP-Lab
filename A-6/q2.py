


import random

class RockPaperScissors:
    def _init_(self, total_rounds):
        self.total_rounds = total_rounds  # Total rounds to play
        self.current_round = 0  # Track current round number
        self.user_wins = 0  # Track user wins
        self.computer_wins = 0  # Track computer wins
        self.choices = ["rock", "paper", "scissors"]  # Valid choices

    def get_computer_choice(self):
        """Returns a random choice for the computer"""
        return random.choice(self.choices)

    def find_winner(self, user_choice, computer_choice):
        """Determines winner of a round"""
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

    def is_game_over(self):
        """Checks if someone has won the game"""
        return self.current_round >= self.total_rounds

    def play(self):
        """Main game loop"""
        while not self.is_game_over():
            self.current_round += 1
            print(f"\nRound {self.current_round}/{self.total_rounds}")
            
            user_choice = input("Enter rock, paper, or scissors: ").lower()
            while user_choice not in self.choices:
                user_choice = input("Invalid choice. Enter rock, paper, or scissors: ").lower()
            
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")

            winner = self.find_winner(user_choice, computer_choice)
            if winner == "user":
                print("You win this round!")
            elif winner == "computer":
                print("Computer wins this round!")
            else:
                print("It's a draw!")

        # Final result
        print("\nGame Over!")
        print(f"Final Score - You: {self.user_wins}, Computer: {self.computer_wins}")
        if self.user_wins > self.computer_wins:
            print("🎉 You win the game!")
        elif self.user_wins < self.computer_wins:
            print("💻 Computer wins the game!")
        else:
            print("🤝 It's a tie!")

# Example Usage:
game = RockPaperScissors(total_rounds=3)
game.play()



