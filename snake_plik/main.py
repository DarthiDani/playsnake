import tkinter as tk
from tkinter import ttk
from game import Game
from settings import Settings

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Gra w Węża")
        self.settings = Settings()

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both")

        self.play_frame = tk.Frame(self.notebook)
        self.settings_frame = tk.Frame(self.notebook)
        self.exit_frame = tk.Frame(self.notebook)

        self.notebook.add(self.play_frame, text="Play")
        self.notebook.add(self.settings_frame, text="Settings")
        self.notebook.add(self.exit_frame, text="Exit")

        self.canvas = tk.Canvas(self.play_frame, width=400, height=400, bg="black")
        self.canvas.pack()

        self.start_game_button = tk.Button(self.play_frame, text="Rozpocznij grę", command=self.start_game)
        self.start_game_button.pack(pady=20)

        self.play_again_button = tk.Button(self.play_frame, text="Zagraj ponownie", command=self.start_game)
        self.play_again_button.pack(pady=20)
        self.play_again_button.pack_forget()

        self.game = None

    def start_game(self):
        if self.game:
            self.game.reset_game()
        self.game = Game(self.root, self.settings, self.canvas, self)
        self.game.start_game()
        self.start_game_button.pack_forget()
        self.play_again_button.pack_forget()

    def end_game(self):
        self.play_again_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
