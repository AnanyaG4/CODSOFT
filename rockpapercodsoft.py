import tkinter as tk
from random import choice

class RockPaperScissorsGUI:
    def __init__(self):
        self.window = (tk.Tk)()
        self.window.title("Rock, Paper, Scissors")

        self.user_score = 0
        self.computer_score = 0

        self.user_score_label = tk.Label(self.window, text="Your score: 0")
        self.user_score_label.pack()

        self.computer_score_label = tk.Label(self.window, text="Computer score: 0")
        self.computer_score_label.pack()

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        self.rock_button = tk.Button(self.window, text="Rock", command=self.rock_clicked)
        self.rock_button.pack()

        self.paper_button = tk.Button(self.window, text="Paper", command=self.paper_clicked)
        self.paper_button.pack()

        self.scissors_button = tk.Button(self.window, text="Scissors", command=self.scissors_clicked)
        self.scissors_button.pack()

    def play_game(self, user_choice):
        computer_choice = choice(["rock", "paper", "scissors"])
        if user_choice == computer_choice:
            self.result_label['text'] = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.result_label['text'] = "You win!"
            self.user_score += 1
        else:
            self.result_label['text'] = "Computer wins!"
            self.computer_score += 1

        self.user_score_label['text'] = f"Your score: {self.user_score}"
        self.computer_score_label['text'] = f"Computer score: {self.computer_score}"

    def rock_clicked(self):
        self.play_game("rock")

    def paper_clicked(self):
        self.play_game("paper")

    def scissors_clicked(self):
        self.play_game("scissors")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = RockPaperScissorsGUI()
    gui.run()