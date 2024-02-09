import pygame


class Renderer:
    def __init__(self):
        self.width = 400
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.image.load("assets/images/background-day.png")
        self.base = pygame.image.load("assets/images/base.png")
        self.bird = pygame.image.load("assets/images/yellowbird-downflap.png")
        self.pipe = pygame.image.load("assets/images/pipe-green.png")

    def render(self, bird, pipes):
        self.screen.fill((0, 0, 0))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.base = pygame.transform.scale(self.base, (self.width, 200))

        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.base, (0, 570))
        self.screen.blit(self.bird, (bird.x, bird.y))

        for pipe in pipes:
            pygame.draw.rect(self.screen, (0, 255, 0), (pipe.x, pipe.y, pipe.width, pipe.height))

            mirrored_y = pipe.height + 150
            mirrored_height = 600 - mirrored_y
            pygame.draw.rect(self.screen, (255, 255, 0), (pipe.x, mirrored_y, pipe.width, mirrored_height))

        pygame.display.flip()
