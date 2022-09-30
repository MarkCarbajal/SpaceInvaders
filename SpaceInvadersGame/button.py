import pygame as pg
from pygame import font
from settings import Settings

class Button():
    def __init__(self, settings, screen, msg):

       #Initialize button attributes.
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.textfont = pg.font.Font("fonts/BungeeSpice-Regular.ttf", 100)
        self.textfont2 = pg.font.Font("fonts/BungeeSpice-Regular.ttf", 50)

        #Load sprite images
        self.spriteimage1 = pg.image.load("images/alien__00.png")
        self.spriteimage2 = pg.image.load("images/alien__10.png")
        self.spriteimage3 = pg.image.load("images/alien__20.png")
        self.shipimage = pg.transform.rotozoom(pg.image.load('images/ship.png'), 0, 3.0)
        

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pg.font.SysFont(None, 60)

        # Build the button's rect object and center it
        self.rect = pg.Rect(450, 600, self.width, self.height)

        # The button message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

        self.text1 = self.textfont.render("Space Invaders", 1, (25,229,59))
        self.screen.blit(self.text1, (175, 200))

        self.text1 = self.textfont2.render("= 50 Points", 1, (210,210,210))
        self.screen.blit(self.text1, (415, 350))

        self.text1 = self.textfont2.render("= 25 Points", 1, (210,210,210))
        self.screen.blit(self.text1, (415, 425))

        self.text1 = self.textfont2.render("= 10 Points", 1, (210,210,210))
        self.screen.blit(self.text1, (415, 500))

        self.text1 = self.textfont2.render("Player", 1, (192,45,52))
        self.screen.blit(self.text1, (850, 375))

        self.screen.blit(self.spriteimage1, (350,350))
        self.screen.blit(self.spriteimage2, (350,425))
        self.screen.blit(self.spriteimage3, (350,500))
        self.screen.blit(self.shipimage, (850,450))