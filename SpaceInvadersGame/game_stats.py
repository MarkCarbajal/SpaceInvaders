class GameStats():

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()

        f = open("hs.txt","r")
        self.high_score = int(f.read())
        f.close()

        #start game in inactive state
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit

    def update_highscore(self):
        f = open("hs.txt","w")
        f.write(str(self.high_score))
        f.close()