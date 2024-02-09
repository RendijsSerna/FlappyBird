class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0

    def update(self):
        self.velocity += 1
        self.y += self.velocity

    def jump(self):
        self.velocity = -10
