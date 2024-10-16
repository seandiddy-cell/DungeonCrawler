import Game
import pygame

class RPG(Game.Game):
    def __init__(self):
        pass

    def update(self,dt):
        """updates the game and all the variables in game"""
        pass

    def draw(self,scr):
        """draws the objects from game to window Class"""
        pygame.draw.rect(scr,(255,255,255), [100,100,100,100])


