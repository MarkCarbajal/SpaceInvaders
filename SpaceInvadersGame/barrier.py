import pygame as pg
from pygame.sprite import Sprite, Group

class Barrier(Sprite):
    color = 255, 0, 0
    black = 0, 0, 0

    def __init__(self, game, x, y, width, height):
        super().__init__()
        self.screen = game.screen
        #self.rect = rect
        self.settings = game.settings

        # self.settings = game.settings
        self.image = pg.image.load('images/barrier.png')
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
    def hit(self):
        self.kill()
    def update(self): self.draw()
    def draw(self): 
        #pg.draw.rect(self.screen, Barrier.color, self.rect)
        self.screen.blit(self.image, self.rect)
        #pg.draw.circle(self.screen, self.settings.bg_color, (self.rect.centerx, self.rect.bottom), self.rect.width/6)


class Barriers:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.barriers = Group()
        self.create_barriers()
        

    def create_barriers(self):     
        width = self.settings.screen_width / 10
        height = 2.0 * width / 4.0
        top = self.settings.screen_height - 2.1 * height
        #rects = [pg.Rect(x * 2 * width + 1.5 * width, top, width / 6, height / 4) for x in range(4)]   # SP w  3w  5w  7w  SP
        #repleacemt to build 4 groups of 4x4 bariers
        x = y = i = 0
        for y in range (4):
            k = 0
            l = 0
            for x in range (16):
                if 0 <= i <16:
                    #rects.insert(i, pg.Rect(k * 2 * width + 1.5 * width + l, top - 30, width / 9, height / 6))
                    single_barrier = Barrier(self.game, k * 2 * width + 1.5 * width + l, top - 70, 15, 15) 
                if 16 <= i < 32:
                    single_barrier = Barrier(self.game, k * 2 * width + 1.5 * width + l, top - 50, 15, 15)
                if 32 <= i < 48: 
                    single_barrier = Barrier(self.game, k * 2 * width + 1.5 * width + l, top - 30, 15, 15)
                if 48 <= i < 64:
                    single_barrier = Barrier(self.game, k * 2 * width + 1.5 * width + l, top - 10, 15, 15)
                self.barriers.add(single_barrier)
                i += 1
                l += 20
                if (i % 4) == 0:
                    k += 1
                    l = 0


        #self.barriers = [Barrier(game=self.game, rect=rects[j]) for j in range(64)]

    def hit(self): pass 
    
    def reset(self):
        self.create_barriers()

    def update(self):
        for barrier in self.barriers: barrier.update()

    # def draw(self):
    #     for barrier in self.barriers: barrier.draw()

