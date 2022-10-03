import pygame as pg
from pygame.sprite import Sprite
from pygame.sysfont import SysFont
import random
from random import choice
import timer as Timer
from vector import Vector
from sys import exit


class Ufo(Sprite):
    """Represents a UFO meant to move across the screen at random intervals"""

    def __init__(self, settings, screen, game):
        super().__init__()
        # screen, settings, score values
        self.screen = screen
        self.settings = settings
        self.possible_scores = settings.ufo_point_values
        self.score = None
        self.run_at = random.randint(0,1000)  #10000
        self.run_count = 0
        self.sb = game.scoreboard

        # images, score text
        self.image = pg.image.load('images/alien__30.png')
        self.rect = self.image.get_rect()
        self.score_image = None
        self.font = SysFont(None, 32, italic=True)
        self.prep_score()

        # death frames
        self.death_frames = []
        self.death_index = None
        self.death_frames.append(pg.image.load('images/alien__30.png'))
        self.death_frames.append(self.score_image)
        self.last_frame = None
        self.wait_interval = 500

        # initial position, speed/direction
        self.speed = settings.ufo_speed * (choice([-1, 1]))
        self.rect.x = 0 if self.speed > 0 else settings.screen_width
        self.rect.y = settings.screen_height * 0.8 

        self.dying = self.dead = False

    def kill(self):
        super().kill()

    def check_edges(self): 
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def begin_death(self):
        self.dead = True
        self.death_index = 0
        self.image = self.death_frames[self.death_index]
        self.last_frame = pg.time.get_ticks()

    def get_score(self):
        """Get a random score from the UFO's possible score values"""
        self.score = choice(self.possible_scores)
        return self.score

    def prep_score(self):
        score_str = str(self.get_score())
        self.score_image = self.font.render(score_str, True, (255, 0, 0), self.settings.bg_color)

    def hit(self):
        if not self.dying:
            print("hi there")
            self.dying = True
            self.dead = True  # remove later
            #self.rect.y = self.settings.screen_height * 1.1
            #self.timer = self.timer_explosion
            value = self.sb.increment_score(3)
            if value == 75:
                self.image = pg.image.load('images/75.png')
            if value == 100:
                self.image = pg.image.load('images/100.png')
            if value == 150:
                self.image = pg.image.load('images/150.png')

    def reset(self):
        self.speed = self.settings.ufo_speed * (choice([-1, 1]))
        self.rect.x = 0 if self.speed > 0 else self.settings.screen_width
        self.rect.y = self.settings.screen_height * 0.8
        self.run_at = random.randint(0,1000)  #10000
        self.run_count = 0
        self.dying = self.dead = False
        self.speed = self.settings.ufo_speed * (choice([-1, 1]))
        self.rect.x = 0 if self.speed > 0 else self.settings.screen_width
        self.image =  pg.image.load('images/alien__30.png')

    def update(self):
        #self.run_count += 1
        #self.rect.x = 0
        #if self.run_at <= self.run_count:
            #self.rect.x += self.speed
        self.rect.x += self.speed

    def blitme(self):
        if self.run_at <= self.run_count:
            self.screen.blit(self.image, self.rect)
        
