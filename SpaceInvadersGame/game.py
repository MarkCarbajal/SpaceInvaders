import pygame as pg
from settings import Settings
import game_functions as gf

from laser import Lasers, LaserType
from alien import Aliens
from ship import Ship
from sound import Sound
from scoreboard import Scoreboard
from barrier import Barriers
from game_stats import GameStats
from button import Button
import sys


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Alien Invasion")

        self.sound = Sound(bg_music="sounds/startrek.wav")
        self.scoreboard = Scoreboard(game=self)  

        self.ship_lasers = Lasers(settings=self.settings, type=LaserType.SHIP)
        self.alien_lasers = Lasers(settings=self.settings, type=LaserType.ALIEN)
        
        self.barriers = Barriers(game=self)
        self.ship = Ship(game=self)
        self.aliens = Aliens(game=self, sound=self.sound, barriers=self.barriers)
        self.settings.initialize_speed_settings()

        self.stats = GameStats(self.settings)
        self.play_button = Button(self.settings, self.screen, "Play")
        self.mouse_x, self.mouse_y = pg.mouse.get_pos()

    def reset(self):
        print('Resetting game...')
        # self.lasers.reset()
        self.barriers.reset() 
        self.ship.reset()
        self.aliens.reset()
        self.sound.reset()
        # self.scoreboard.reset()

    def game_over(self):
        print('All ships gone: game over!')
        self.sound.gameover()
        pg.quit()
        sys.exit()

    def play(self):
        self.sound.play_bg()
        while self.stats.game_active == False:  
            self.play_button.draw_button()
            gf.check_events(settings=self.settings, ship=self.ship, stats=self.stats, play_button = self.play_button)
            pg.display.flip()


        while self.stats.game_active == True:     # at the moment, only exits in gf.check_events if Ctrl/Cmd-Q pressed
            gf.check_events(settings=self.settings, ship=self.ship, stats=self.stats, play_button = self.play_button)
            self.screen.fill(self.settings.bg_color)
            self.ship.update()
            self.aliens.update()
            self.barriers.update()
            # self.lasers.update()
            self.scoreboard.update()
            pg.display.flip()


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
