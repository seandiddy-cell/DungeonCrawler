import pygame


class Game:
    
    def __init__(self):
        pass

    def update(self,dt: int):
        """updates the game and all the variables in game"""
        pass

    def draw(self,scr: pygame.surface.Surface):
        """draws the objects from game to window Class"""
        pass


    def keyPressed(self, ke: pygame.key.ScancodeWrapper):
        pass

    def mousePressed(self,m: tuple):
        pass


class GameObject:
    """base object for rendering and updating"""
    def __init__(self,n: str,x: int,y: int,w: int,h: int):
        self.Objx = x
        self.Objy = y
        self.Objw = w
        self.Objh = h

    def update(self,dt: int):
        """updates gameObject"""
        pass

    def draw(self,scr: pygame.surface.Surface):
        """draws gameobject to surface"""
        pygame.draw.rect(scr,(255,0,0), self.getDrawLis())

    def keyPressed(self, ke: pygame.key.ScancodeWrapper):
        pass

    def mousePressed(self,m: tuple):
        pass

    def getDrawLis(self):
        return [self.Objx,self.Objy,self.Objw,self.Objh]