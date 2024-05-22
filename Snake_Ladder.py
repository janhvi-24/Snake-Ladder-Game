import tkinter as tk
import random

class SnakeLadderGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake and Ladder Game")
        
        self.board = self.create_board()
        self.player_position = 1
        self.create_widgets()

        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    def create_board(self):
        board = {}
        count = 1
        for row in range(10):
            for col in range(10):
                board[count] = (row, col)
                count += 1
        return board

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.grid(row=0, column=0, columnspan=4)
        self.draw_board()

        self.roll_button = tk.Button(self.root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.grid(row=1, column=0)

        self.dice_label = tk.Label(self.root, text="Dice: ")
        self.dice_label.grid(row=1, column=1)

        self.player_label = tk.Label(self.root, text="Player Position: 1")
        self.player_label.grid(row=1, column=2)

    def draw_board(self):
        for num, pos in self.board.items():
            x1 = pos[1] * 60
            y1 = (9 - pos[0]) * 60
            x2 = x1 + 60
            y2 = y1 + 60
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            self.canvas.create_text(x1 + 30, y1 + 30, text=str(num))

        self.player = self.canvas.create_oval(5, 545, 55, 595, fill="blue")

    def roll_dice(self):
        dice_roll = random.randint(1, 6)
        self.dice_label.config(text=f"Dice: {dice_roll}")

        new_position = self.player_position + dice_roll

        if new_position > 100:
            return

        self.player_position = self.snakes.get(new_position, self.ladders.get(new_position, new_position))

        self.player_label.config(text=f"Player Position: {self.player_position}")

        new_pos_coords = self.board[self.player_position]
        x1 = new_pos_coords[1] * 60 + 5
        y1 = (9 - new_pos_coords[0]) * 60 + 5
        x2 = x1 + 50
        y2 = y1 + 50
        self.canvas.coords(self.player, x1, y1, x2, y2)

        if self.player_position == 100:
            self.roll_button.config(state="disabled")
            self.dice_label.config(text="Congratulations! You won!")

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeLadderGame(root)
    root.mainloop()
