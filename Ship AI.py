class Ship:
     def __init__(self, ai_game):
          self.screen = ai_game.screen
          self.settings = ai_game.settings
          self.screen_rect = ai_game.screen.get_rect()