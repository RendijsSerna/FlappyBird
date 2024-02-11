class Pipe:
    def __init__(self, x, y, height, bottom_pipe_y):
        self.x = x
        self.y = y
        self.width = 70
        self.height = height
        self.bottom_pipe_y = bottom_pipe_y
        self.size_x = 52
        self.size_y = 320

    def update(self):
        self.x -= 5
