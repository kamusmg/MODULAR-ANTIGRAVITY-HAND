import pygame
import sys
import math
from game import Game, WIDTH, HEIGHT, WHITE

class AutoGame(Game):
    def __init__(self):
        super().__init__()
        pygame.display.set_caption("Nucleus: Autonomous Awakening")
        
    def get_closest_orb(self):
        closest = None
        min_dist = float('inf')
        px, py = self.player_pos
        
        for orb in self.data_orbs:
            dist = math.hypot(orb[0] - px, orb[1] - py)
            if dist < min_dist:
                min_dist = dist
                closest = orb
        return closest

    def get_closest_glitch(self):
        closest = None
        min_dist = float('inf')
        px, py = self.player_pos
        
        for glitch in self.glitches:
            gx, gy = glitch['pos']
            dist = math.hypot(gx - px, gy - py)
            if dist < min_dist:
                min_dist = dist
                closest = glitch
        return closest, min_dist

    def autonomous_update(self):
        # AI Logic to replace Keyboard Input
        
        target = self.get_closest_orb()
        obs, obs_dist = self.get_closest_glitch()
        
        dx, dy = 0, 0
        speed = 6 # Slightly faster than human
        
        px, py = self.player_pos
        
        # 1. Desire (Move to Goal)
        if target:
            tx, ty = target
            angle = math.atan2(ty - py, tx - px)
            dx += math.cos(angle) * speed
            dy += math.sin(angle) * speed
        else:
            # Wander to center if no food
            tx, ty = WIDTH//2, HEIGHT//2
            if math.hypot(tx-px, ty-py) > 50:
                angle = math.atan2(ty - py, tx - px)
                dx += math.cos(angle) * speed * 0.5
                dy += math.sin(angle) * speed * 0.5

        # 2. Fear (Avoid Glitches)
        if obs and obs_dist < 100: # Panic radius
            gx, gy = obs['pos']
            angle_bad = math.atan2(gy - py, gx - px)
            # Run away!
            dx -= math.cos(angle_bad) * speed * 1.5
            dy -= math.sin(angle_bad) * speed * 1.5
            
        # Apply Move
        self.player_pos[0] += dx
        self.player_pos[1] += dy
        
        # Bounds Check
        self.player_pos[0] = max(0, min(WIDTH-self.player_size, self.player_pos[0]))
        self.player_pos[1] = max(0, min(HEIGHT-self.player_size, self.player_pos[1]))
        
        # Continue with standard physics
        super().update() # Calls collision checks etc.

    # Override run to use autonomous update
    def run(self):
        print("[AUTO GAME] AI taking control of the joystick...")
        while self.running:
            self.clock.tick(60)
            
            # Event pump needed for window to remain responsive
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # Allow manual override if user presses keys (Optional, but fun)
            
            # Use our AI brain
            self.autonomous_update()
            
            # Draw standard UI
            self.draw() # This already flips display
            
            # Auto-Close on Win
            if self.won:
                pygame.time.delay(3000)
                self.running = False
            
            if self.game_over:
                pygame.time.delay(3000)
                self.running = False

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = AutoGame()
    game.run()
