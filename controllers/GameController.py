import random
import sys

import pygame

from models.Bird import Bird
from models.Pipe import Pipe
from views.Render import Renderer


class GameController:
    def __init__(self):
        self.height = 100
        self.width = 400
        self.bird = Bird(100, 300)
        self.pipes = []
        self.started = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.jump()

    def update(self):
        self.bird.update()

        if len(self.pipes) == 0 or self.pipes[-1].x < self.width - 200:
            pipe_gap = 200
            pipe_height = random.randint(100, 400)
            self.pipes.append(Pipe(self.width, 0, pipe_height))
            #self.pipes.append(Pipe(self.width, pipe_height + pipe_gap, self.height - pipe_height - pipe_gap))

        for pipe in self.pipes:
            pipe.update()

            # this needs to be changed
            if self.bird.x + 30 > pipe.x and self.bird.x < pipe.x + pipe.width:
                if self.bird.y < pipe.y or self.bird.y + 30 > pipe.y + pipe.height:
                    pass

            if self.bird.y > 550 or self.bird.y < 0:
                self.started = False

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        renderer = Renderer()

        while self.started:
            self.handle_events()
            self.update()
            renderer.render(self.bird, self.pipes)
            clock.tick(30)
