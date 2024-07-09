#import pygame

class Entity:
    def __init__(self, game, name, pos=(0, 0)):
        self.game = game
        self.name = name
        self.pos = list(pos)

    def render(self, display=None):
        if display != None:
            display.blit(self.game.get_texture(self.name), self.pos)
        else: self.game.screen.blit(self.game.get_texture(self.name), self.pos)