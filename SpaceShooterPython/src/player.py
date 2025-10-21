import pygame
from src.game_object import GameObject
from src.assets_manager import assets_manager

class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.sprite = assets_manager.get_texture("assets/player.png")
        self.position = pygame.Vector2(320, 240)
        self.speed = 200

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

    def draw(self, screen):
        screen.blit(self.sprite, self.position)
