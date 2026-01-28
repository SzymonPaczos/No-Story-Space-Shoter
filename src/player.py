import pygame
from src.game_object import GameObject
from src.assets_manager import assets_manager

class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.sprite = assets_manager.get_texture("assets/player.png")
        self.position = pygame.Vector2(320, 240)
        self.speed = 200
        self.shoot_timer = 0.0
        self.shoot_delay = 0.25

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position.y -= self.speed * delta_time
        if keys[pygame.K_s]:
            self.position.y += self.speed * delta_time
        if keys[pygame.K_a]:
            self.position.x -= self.speed * delta_time
        if keys[pygame.K_d]:
            self.position.x += self.speed * delta_time
            
        if self.shoot_timer > 0:
            self.shoot_timer -= delta_time

    def shoot(self):
        if self.shoot_timer <= 0:
            self.shoot_timer = self.shoot_delay
            from src.bullet import Bullet
            # Spawn bullet slightly above the player
            return Bullet(self.position.x, self.position.y - 20)
        return None


    def draw(self, renderer):
        # Lazy load texture from Pygame Surface to GPU Texture
        if not hasattr(self, 'texture'):
            self.texture = renderer.texture_from_surface(self.sprite)
            
        renderer.draw(self.texture, self.position)
