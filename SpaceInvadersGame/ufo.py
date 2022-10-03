import pygame
from pygame.sysfont import SysFont
import random
from random import choice


class Ufo(pygame.sprite.Sprite):
    """Represents a UFO meant to move across the screen at random intervals"""
    def __init__(self, settings, screen):
        super().__init__()
        # screen, settings, score values
        self.screen = screen
        self.settings = settings
        self.possible_scores = settings.ufo_point_values
        self.score = None
        self.run_at = random.randint(0,10000)
        self.run_count = 0

        # images, score text
        self.image = pygame.image.load('images/alien__30.png')
        self.rect = self.image.get_rect()
        self.score_image = None
        self.font = SysFont(None, 32, italic=True)
        self.prep_score()

        # death frames
        self.death_frames = []
        self.death_index = None
        self.death_frames.append(pygame.image.load('images/alien__30.png'))
        self.death_frames.append(self.score_image)
        self.last_frame = None
        self.wait_interval = 500

        # initial position, speed/direction
        self.speed = settings.ufo_speed * (choice([-1, 1]))
        self.rect.x = 0 if self.speed > 0 else settings.screen_width
        self.rect.y = settings.screen_height * 0.05

        # death flag
        self.dead = False

    def kill(self):
        super().kill()

    def check_edges(self): 
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def begin_death(self):
        self.dead = True
        self.death_index = 0
        self.image = self.death_frames[self.death_index]
        self.last_frame = pygame.time.get_ticks()

    def get_score(self):
        """Get a random score from the UFO's possible score values"""
        self.score = choice(self.possible_scores)
        return self.score

    def prep_score(self):
        score_str = str(self.get_score())
        self.score_image = self.font.render(score_str, True, (255, 0, 0), self.settings.bg_color)

    def hit(self):
        if not self.dying:
            self.dying = True 
            self.sb.increment_score(self.type)

    def reset(self):
        print("hi")
        #to implement

    def update(self):
        self.run_count += 1
        #self.rect.x = 0
        if self.run_at <= self.run_count:
            if not self.dead:
                self.rect.x += self.speed
                if self.speed > 0 and self.rect.left > self.settings.screen_width:
                    self.kill()
                elif self.rect.right < 0:
                    self.kill()
            else:
                time_test = pygame.time.get_ticks()
                if abs(time_test - self.last_frame) > self.wait_interval:
                    self.last_frame = time_test
                    self.death_index += 1
                    if self.death_index >= len(self.death_frames):
                        self.kill()
                    else:
                        self.image = self.death_frames[self.death_index]
                        self.wait_interval += 500

    def blitme(self):
        if self.run_at <= self.run_count:
            self.screen.blit(self.image, self.rect)
        
