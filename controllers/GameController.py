import random
import sys
import pygame
from models.Bird import Bird
from models.Pipe import Pipe
from views.Render import Renderer
from models.Score import Score


class GameController:
    def __init__(self):
        self.height = 100
        self.width = 400
        self.bird = Bird(100, 300)
        self.pipes = []
        self.started = True
        self.score = Score()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.test = True
                    self.bird.jump()

    def update(self):
        self.bird.update()

        if len(self.pipes) == 0 or self.pipes[-1].x < self.width - 200:
            pipe_gap = 200
            pipe_height = random.randint(100, 400)
            mirrored_y = pipe_height + pipe_gap
            self.pipes.append(Pipe(self.width, 0, pipe_height, mirrored_y))

        for pipe in self.pipes:
            pipe.update()

            if (
                    self.bird.x + self.bird.size_x > pipe.x and
                    self.bird.x < pipe.x + pipe.width and
                    (
                            (self.bird.y < pipe.y + pipe.height) or
                            (self.bird.y + self.bird.size_y > pipe.bottom_pipe_y)
                    )
            ):
                self.started = False
            elif self.bird.x == pipe.x:
                self.score.score += 1

            if self.bird.y + self.bird.size_y > 550 or self.bird.y + self.bird.x < 0:
                self.started = False

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        renderer = Renderer()

        while self.started:
            self.handle_events()
            self.update()
            renderer.render(self.bird, self.pipes, self.score)
            clock.tick(30)
