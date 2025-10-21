import pygame
import os

class AssetsManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AssetsManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self._textures = {}
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def get_texture(self, path):
        if path not in self._textures:
            full_path = os.path.join(self.base_path, path)
            try:
                self._textures[path] = pygame.image.load(full_path).convert_alpha()
            except pygame.error as e:
                print(f"Unable to load texture: {full_path}")
                raise e
        return self._textures[path]

assets_manager = AssetsManager()
