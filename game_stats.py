class GameStats():
    #Track AI stats
    def __init__(self, ai_game):
        #Initialize game stats
        self.settings = ai_game.settings
        self.reset_stats()

        #Start AI in active state
        self.game_active = False
        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        #Initialize changeable stats during game
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

