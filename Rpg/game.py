import Game
import pygame

class RPG(Game.Game):
    def __init__(self):
        self.player = Game.GameObject("Player",100,100,100,100)

    def update(self,dt: int):
        """updates the game and all the variables in game"""
        pass

    def draw(self,scr: pygame.surface.Surface):
        """draws the objects from game to window Class"""
        self.player.draw(scr)


    def keyPressed(self, ke: pygame.key.ScancodeWrapper):
        pass

    def mousePressed(self,m: tuple):
        pass




