import pygame
from src.game_object import GameObject
from src.assets_manager import assets_manager

class Bullet(GameObject):
    def __init__(self, x, y):
        super().__init__()
        self.sprite = assets_manager.get_texture("assets/bullet.png")
        self.position = pygame.Vector2(x, y)
        self.speed = 400
        
    def update(self, delta_time):
        self.position.y -= self.speed * delta_time
        
    def draw(self, renderer):
        if not hasattr(self, 'texture'):
            self.texture = renderer.texture_from_surface(self.sprite)
        renderer.draw(self.texture, self.position)
