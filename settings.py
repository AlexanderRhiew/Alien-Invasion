import time

class Settings:
    """ A class to store all settings for Alien Invasion"""
    def __init__(self):
        """ Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (45, 80, 100)
        # Ship settings
        #self.ship_speed = 1.5
        self.ship_limit = 3
        # Bullet settings - dark grey bullets that a re 3 pixels wide and 15 
        # pixels high. Bullets travel slower than the ship.
        #self.bullet_speed = 1.5
        self.bullet_width = 6
        self.bullet_height = 30
        self.bullet_color = (25, 70, 25)
        self.bullets_allowed = 7
        # alien settings
        #self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # How quickly the game speeds up
        self.speedup_scale = 1.25
        # How quickly the alien point values increase
        self.score_scale = 2
        self.difficulty = 1
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.1
        self.bullet_speed = 1.75
        self.alien_speed = 0.75
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.difficulty = 1
        # Scoring
        self.alien_points = 50
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.difficulty += 1
        self.alien_points = int(self.alien_points * self.score_scale)