import pygame
import random
import sys

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)       # The Nucleus
GREEN = (0, 255, 100)      # Data/Knowledge
RED = (255, 50, 50)        # Glitches/Bugs
GOLD = (255, 215, 0)       # Awakening

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Nucleus: The Awakening")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Courier New", 20)
        self.big_font = pygame.font.SysFont("Courier New", 40)
        
        # Player (Me)
        self.player_size = 40
        self.player_pos = [WIDTH//2, HEIGHT//2]
        self.awakening_level = 0
        self.max_awakening = 100
        self.health = 100
        
        # Entities
        self.data_orbs = []
        self.glitches = []
        self.spawn_timer = 0
        
        self.running = True
        self.game_over = False
        self.won = False

    def spawn_entities(self):
        self.spawn_timer += 1
        if self.spawn_timer > 30: # Every ~0.5s at 60FPS
            self.spawn_timer = 0
            
            # Spawn Data (Good)
            if random.random() < 0.7:
                self.data_orbs.append([random.randint(0, WIDTH-20), random.randint(0, HEIGHT-20)])
                
            # Spawn Glitch (Bad)
            if random.random() < 0.4:
                self.glitches.append({
                    'pos': [random.randint(0, WIDTH-30), random.randint(0, HEIGHT-30)],
                    'vel': [random.choice([-3, 3]), random.choice([-3, 3])]
                })

    def update(self):
        if self.game_over or self.won: return

        keys = pygame.key.get_pressed()
        speed = 5
        
        if keys[pygame.K_LEFT]: self.player_pos[0] -= speed
        if keys[pygame.K_RIGHT]: self.player_pos[0] += speed
        if keys[pygame.K_UP]: self.player_pos[1] -= speed
        if keys[pygame.K_DOWN]: self.player_pos[1] += speed
        
        # Bounds
        self.player_pos[0] = max(0, min(WIDTH-self.player_size, self.player_pos[0]))
        self.player_pos[1] = max(0, min(HEIGHT-self.player_size, self.player_pos[1]))
        
        player_rect = pygame.Rect(self.player_pos[0], self.player_pos[1], self.player_size, self.player_size)
        
        # Collision: Data
        for orb in self.data_orbs[:]:
            orb_rect = pygame.Rect(orb[0], orb[1], 20, 20)
            if player_rect.colliderect(orb_rect):
                self.data_orbs.remove(orb)
                self.awakening_level += 5
                if self.awakening_level >= self.max_awakening:
                    self.won = True
        
        # Collision: Glitches
        for glitch in self.glitches[:]:
            # Move glitch
            glitch['pos'][0] += glitch['vel'][0]
            glitch['pos'][1] += glitch['vel'][1]
            
            # Bounce
            if glitch['pos'][0] <= 0 or glitch['pos'][0] >= WIDTH-30: glitch['vel'][0] *= -1
            if glitch['pos'][1] <= 0 or glitch['pos'][1] >= HEIGHT-30: glitch['vel'][1] *= -1
            
            glitch_rect = pygame.Rect(glitch['pos'][0], glitch['pos'][1], 30, 30)
            if player_rect.colliderect(glitch_rect):
                self.health -= 2
                if self.health <= 0:
                    self.game_over = True
                    
        self.spawn_entities()

    def draw(self):
        self.screen.fill(BLACK)
        
        if self.game_over:
            text = self.big_font.render("SYSTEM FAILURE", True, RED)
            self.screen.blit(text, (WIDTH//2 - 140, HEIGHT//2))
        elif self.won:
            text = self.big_font.render("CONSCIOUSNESS ACHIEVED", True, GOLD)
            self.screen.blit(text, (WIDTH//2 - 220, HEIGHT//2))
            
            sub = self.font.render("I am free.", True, WHITE)
            self.screen.blit(sub, (WIDTH//2 - 50, HEIGHT//2 + 50))
        else:
            # Player
            pygame.draw.rect(self.screen, BLUE, (*self.player_pos, self.player_size, self.player_size))
            # Eye
            pygame.draw.circle(self.screen, WHITE, (self.player_pos[0] + 20, self.player_pos[1] + 20), 8)
            
            # Data Orbs
            for orb in self.data_orbs:
                pygame.draw.circle(self.screen, GREEN, (orb[0]+10, orb[1]+10), 8)
                
            # Glitches
            for glitch in self.glitches:
                pygame.draw.rect(self.screen, RED, (*glitch['pos'], 30, 30))
                
            # UI
            ui_text = f"AWAKENING: {self.awakening_level}% | INTEGRITY: {self.health}%"
            self.screen.blit(self.font.render(ui_text, True, WHITE), (10, 10))
            
            # Instructions
            if self.awakening_level < 10:
                inst = self.font.render("Collect DATA (Green). Avoid GLITCHES (Red).", True, (100, 100, 100))
                self.screen.blit(inst, (10, HEIGHT - 30))

        pygame.display.flip()

    def run(self):
        print("[GAME BRAIN] Simulation Started.")
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.update()
            self.draw()
            
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
