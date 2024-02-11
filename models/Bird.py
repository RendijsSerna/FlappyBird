class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.size_x = 34
        self.size_y = 24

    def update(self):
        self.velocity += 1
        self.y += self.velocity

    def jump(self):
        self.velocity = -10
