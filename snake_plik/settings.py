class Settings:
    def __init__(self):
        self.difficulty = "Medium"
        self.speed = 100

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        if difficulty == "Easy":
            self.speed = 150
        elif difficulty == "Medium":
            self.speed = 100
        elif difficulty == "Hard":
            self.speed = 50
        elif difficulty == "Hardcore":
            self.speed = 30

    def get_speed(self):
        return self.speed
