import pygame as pg 
from game_stats import GameStats
import random
from random import choice

# import pygame.font

class Scoreboard:
    def __init__(self, game): 
        self.score = 0
        self.level = 0

        
        self.settings = game.settings
        self.screen = game.screen

        self.stats = GameStats(self.settings)

        
        self.screen_rect = self.screen.get_rect()

        self.text_color = (255, 255, 255)
        self.font = pg.font.SysFont(None, 48)

        self.score_image = None 
        self.score_rect = None

        self.prep_score()
        self.prep_high_score()

    def increment_score(self, type): 
        self.score += 50 if type==0 else 0 #self.settings.alien_points
        self.score += 25 if type==1 else 0
        self.score += 10 if type==2 else 0
        self.score += choice([75,100,150]) if type==3 else 0
        self.prep_score()
        #if stats.score > stats.high_score:
           # stats.high_score = stats.score
            #sb.prep_high_score()
        #self.stats.high_score = self.score
        #self.prep_high_score()
        if self.score >= self.stats.high_score:
            self.stats.high_score = self.score
            self.prep_high_score()
        else:
            self.stats.update_highscore()

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "HS: " +"{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top   


    def prep_score(self): 
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def reset(self): 
        self.score = 0
        self.update()

    def update(self): 
        # TODO: other stuff
        self.draw()

    def draw(self): 
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)