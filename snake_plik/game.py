import tkinter as tk
from snake import Snake
from food import Food

class Game:
    def __init__(self, root, settings, canvas, app):
        self.root = root
        self.settings = settings
        self.canvas = canvas
        self.app = app

        self.snake = None
        self.food = None
        self.is_game_running = False
        self.root.bind("<KeyPress>", self.on_key_press)

    def start_game(self):
        self.canvas.delete("all")
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)
        self.food.draw()
        self.is_game_running = True
        self.snake.dead = False
        self.snake.direction = "Right"
        self.root.after(self.settings.get_speed(), self.update)

    def update(self):
        if self.is_game_running:
            self.snake.move()
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.food.remove()
                self.food.draw()
            self.snake.draw()

            if not self.snake.dead:
                self.root.after(self.settings.get_speed(), self.update)
            else:
                self.is_game_running = False
                self.canvas.create_text(200, 200, text="Koniec gry!", fill="white", font=("Arial", 24))
                self.app.end_game()

    def on_key_press(self, event):
        if self.is_game_running and event.keysym in ["Up", "Down", "Left", "Right"]:
            self.snake.change_direction(event.keysym)

    def reset_game(self):
        self.canvas.delete("all")
        self.snake = None
        self.food = None
        self.is_game_running = False
