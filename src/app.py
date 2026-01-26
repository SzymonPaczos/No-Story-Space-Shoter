import pygame
from src.player import Player
from src.renderer import Renderer

class App:
    def __init__(self):
        pygame.init()
        # Request an OpenGL context instead of a standard software 2D surface
        self.screen = pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
        pygame.display.set_caption("Space Shooter (ModernGL)")
        
        # Initialize our custom ModernGL renderer
        self.renderer = Renderer((800, 600))
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Initialize game objects
        self.player = Player()

    def run(self):
        while self.running:
            delta_time = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.player.update(delta_time)

            # Render Phase
            self.renderer.clear()
            self.player.draw(self.renderer) # Delegate drawing to the renderer
            pygame.display.flip() # Swap buffers (show the frame)

        pygame.quit()
