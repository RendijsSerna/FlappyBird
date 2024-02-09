import pygame


class Renderer:
    def __init__(self):
        self.width = 400
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))

    def render(self, bird, pipes):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (255, 255, 255), (bird.x, bird.y, 30, 30))

        for pipe in pipes:
            pygame.draw.rect(self.screen, (0, 255, 0), (pipe.x, pipe.y, pipe.width, pipe.height))

        pygame.display.flip()