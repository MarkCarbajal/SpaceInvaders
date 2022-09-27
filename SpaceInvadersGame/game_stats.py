class GameStats():

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()

        #start game in inactive state
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit