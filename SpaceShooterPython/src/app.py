import pygame
from src.player import Player

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Shooter")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()

    def run(self):
        while self.running:
            delta_time = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.player.update(delta_time)

            self.screen.fill((0, 0, 255))  # Blue background
            self.player.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
