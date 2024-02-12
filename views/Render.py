import pygame


def load_number_images():
    numbers = []
    for i in range(10):
        filename = f"assets/images/numbers_images/{i}.png"
        number_image = pygame.image.load(filename)
        numbers.append(number_image)
    return numbers


class Renderer:
    def __init__(self):
        self.width = 400
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.image.load("assets/images/background-day.png")
        self.base = pygame.image.load("assets/images/base.png")
        self.bird = pygame.image.load("assets/images/yellowbird-downflap.png")
        self.bird1 = pygame.image.load("assets/images/yellowbird-midflap.png")
        self.bird2 = pygame.image.load("assets/images/yellowbird-upflap.png")
        self.numbers = load_number_images()
        self.pipe = pygame.image.load("assets/images/pipe-green.png")

    def render(self, bird, pipes, score):
        self.screen.fill((0, 0, 0))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.base = pygame.transform.scale(self.base, (self.width, 200))

        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.base, (0, 570))

        # this needs to be remade
        if bird.test:
            self.screen.blit(self.bird1, (bird.x, bird.y))
            self.screen.blit(self.bird2, (bird.x, bird.y))
            bird.test = False
        else:
            self.screen.blit(self.bird, (bird.x, bird.y))

        for pipe in pipes:
            flipped_pipe = pygame.transform.flip(self.pipe, False, True)
            flipped_pipe = pygame.transform.scale(flipped_pipe, (pipe.size_x, pipe.height))
            self.screen.blit(flipped_pipe, (pipe.x, pipe.y))
            self.screen.blit(self.pipe, (pipe.x, pipe.bottom_pipe_y))

        self.render_score(score.score)

        pygame.display.flip()

    def render_score(self, score):
        score_str = str(score)
        digit_width = self.numbers[0].get_width()
        x = 200 - (digit_width * len(score_str)) // 2
        y = 100
        for digit in score_str:
            digit_index = int(digit)
            self.screen.blit(self.numbers[digit_index], (x, y))
            x += digit_width
