import random

class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        self.position = self.new_position()

    def new_position(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        return (x, y)

    def draw(self):
        x, y = self.position
        self.canvas.delete("food")
        self.canvas.create_oval(x, y, x + 10, y + 10, fill="red", tags="food")

    def remove(self):
        self.position = self.new_position()
