import random

class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"
        self.dead = False

    def move(self):
        if not self.dead:
            head_x, head_y = self.body[0]
            if self.direction == "Up":
                new_head = (head_x, head_y - 10)
            elif self.direction == "Down":
                new_head = (head_x, head_y + 10)
            elif self.direction == "Left":
                new_head = (head_x - 10, head_y)
            elif self.direction == "Right":
                new_head = (head_x + 10, head_y)

            self.body.insert(0, new_head)
            self.body.pop()
            self.check_collision()

    def grow(self):
        self.body.append(self.body[-1])

    def change_direction(self, new_direction):
        opposite_directions = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left"
        }
        if new_direction != opposite_directions[self.direction]:
            self.direction = new_direction

    def check_collision(self):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400:
            self.dead = True
        if len(self.body) > 1 and (head_x, head_y) in self.body[1:]:
            self.dead = True

    def draw(self):
        self.canvas.delete("snake")
        for segment in self.body:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green", tags="snake")
