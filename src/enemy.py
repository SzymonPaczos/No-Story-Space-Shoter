import pygame
import random
from src.game_object import GameObject
from src.assets_manager import assets_manager

class Enemy(GameObject):
    def __init__(self, x, y):
        super().__init__()
        self.sprite = assets_manager.get_texture("assets/enemy.png")
        self.position = pygame.Vector2(x, y)
        self.speed = 150
        
    def update(self, delta_time):
        self.position.y += self.speed * delta_time
        
    def draw(self, renderer):
        if not hasattr(self, 'texture'):
            self.texture = renderer.texture_from_surface(self.sprite)
        
        # Draw with 180 degree rotation since the sprite is pointing down (or check sprite orientation)
        # The generated sprite prompt said "point downwards".
        # If the rendering expects 0 deg to be up, we might need rotation.
        # However, Renderer.draw takes rotation? No, it takes position and size.
        # Looking at Renderer.draw:
        # def draw(self, texture, position, size=None): ...
        # It creates a transform matrix. The create_transform_matrix helper takes 'rotation' but 'draw' doesn't expose it yet.
        # But 'create_transform_matrix' definition in renderer.py loaded earlier:
        # def create_transform_matrix(self, x, y, width, height, rotation=0):
        # But 'draw' method:
        # def draw(self, texture, position, size=None):
        # ...
        # model_mat = self.create_transform_matrix(position[0], position[1], size[0], size[1])
        # It seems 'draw' does not pass rotation to 'create_transform_matrix' (it uses default 0).
        # So we can't rotate yet without modifying Renderer.
        # But since the sprite is already pointing down (as requested), we probably don't need to rotate it if down is +Y.
        
        renderer.draw(self.texture, self.position)
