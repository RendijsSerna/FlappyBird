class Pipe:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.width = 70
        self.height = height

    def update(self):
        self.x -= 5
