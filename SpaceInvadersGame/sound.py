import pygame as pg
from laser import LaserType
import time


class Sound:
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer.music.load(bg_music)
        pg.mixer.music.set_volume(0.1)
        bg_music_2x_sound = pg.mixer.Sound('sounds/startrek2.wav')
        bg_music_3x_sound = pg.mixer.Sound('sounds/startrek3.wav')
        bg_music_4x_sound = pg.mixer.Sound('sounds/startrek4.wav')
        alienlaser_sound = pg.mixer.Sound('sounds/alienlaser.wav')
        photontorpedo_sound = pg.mixer.Sound('sounds/photon_torpedo.wav')
        gameover_sound = pg.mixer.Sound('sounds/gameover.wav')
        self.sounds = {'alienlaser': alienlaser_sound, 'photontorpedo': photontorpedo_sound,
                       'gameover': gameover_sound, 'bg_music_2x': bg_music_2x_sound, 
                       'bg_music_3x': bg_music_3x_sound, 'bg_music_4x': bg_music_4x_sound}
        self.alien_count = 48

    def play_bg(self):
        pg.mixer.music.play(-1, 0.0)

    def stop_bg(self):
        pg.mixer.music.stop()

    def shoot_laser(self, type): 
        pg.mixer.Sound.play(self.sounds['alienlaser' if type == LaserType.ALIEN else 'photontorpedo'])

    def gameover(self): 
        self.stop_bg() 
        pg.mixer.music.load('sounds/gameover.wav')
        self.play_bg()
        time.sleep(2.8)

    def change_music_speed(self):
        self.alien_count -= 1
        if self.alien_count == 12:
            self.stop_bg()
            pg.mixer.music.load('sounds/startrek4.wav')
            self.play_bg()
        if self.alien_count == 24:
            self.stop_bg()
            pg.mixer.music.load('sounds/startrek3.wav')
            self.play_bg()
        if self.alien_count == 36:
            self.stop_bg()
            pg.mixer.music.load('sounds/startrek2.wav')
            self.play_bg()
        
    def reset(self):
        self.stop_bg()
        pg.mixer.music.load('sounds/startrek.wav')
        self.play_bg()
        self.alien_count = 48
