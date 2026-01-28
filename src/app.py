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
        self.enemies = []
        self.bullets = []
        self.enemy_spawn_timer = 0.0
        self.enemy_spawn_delay = 1.0 # Spawn every second

    def run(self):
        while self.running:
            delta_time = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.player.update(delta_time)
            
            # Shooting
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                bullet = self.player.shoot()
                if bullet:
                    self.bullets.append(bullet)

            # Update Bullets
            for bullet in self.bullets:
                bullet.update(delta_time)
            self.bullets = [b for b in self.bullets if b.position.y > -50]
            
            # Enemy Spawning
            self.enemy_spawn_timer += delta_time
            if self.enemy_spawn_timer >= self.enemy_spawn_delay:
                from src.enemy import Enemy # Late import to avoid circular dependency if any
                import random
                # Spawn at random X, at the top (Y=-50)
                spawn_x = random.randint(50, 750)
                self.enemies.append(Enemy(spawn_x, -50))
                self.enemy_spawn_timer = 0.0
            
            # Update Enemies
            for enemy in self.enemies:
                enemy.update(delta_time)
            
            # Remove off-screen enemies
            self.enemies = [e for e in self.enemies if e.position.y < 800]
            
            # Collision Detection (Simple AABB or distance)
            # Enemies vs Bullets
            for enemy in self.enemies[:]:
                enemy_rect = pygame.Rect(enemy.position.x - 16, enemy.position.y - 16, 32, 32) # Approx hitbox
                for bullet in self.bullets[:]:
                    bullet_rect = pygame.Rect(bullet.position.x - 5, bullet.position.y - 10, 10, 20)
                    if enemy_rect.colliderect(bullet_rect):
                        if enemy in self.enemies: self.enemies.remove(enemy)
                        if bullet in self.bullets: self.bullets.remove(bullet)
                        print("Boom!")
                        break # Bullet hit one enemy

            # Render Phase
            self.renderer.clear()
            self.player.draw(self.renderer)
            for enemy in self.enemies:
                enemy.draw(self.renderer)
            for bullet in self.bullets:
                bullet.draw(self.renderer)
                
            pygame.display.flip() # Swap buffers (show the frame)
        
        pygame.quit()
