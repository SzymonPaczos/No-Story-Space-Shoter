from abc import ABC, abstractmethod
import pygame

class GameObject(ABC):
    def __init__(self):
        self.position = pygame.Vector2(0, 0)

    @abstractmethod
    def update(self, delta_time):
        pass

    @abstractmethod
    def draw(self, renderer):
        pass
