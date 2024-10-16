import pygame
# pygame setup


pygame.init()


class Window:
    """Window class renders the screen and updates all objects"""
    def __init__(self, g):
        lis = pygame.display.get_desktop_sizes()
        self.screen = pygame.display.set_mode(lis[0], pygame.FULLSCREEN)#screen object to draw on
        self.clock = pygame.time.Clock() #clock object used to measure frames and dt
        self.running = True #running boolean to see if game should still run
        self.dt = 0 #dt/deltaTime used to get a more crisp movement at different framerates
        self.game: Game
        self.game = g #this is the game object which is updated and drawn with window class
        self.runGame()
        pygame.quit()

    def runGame(self):
        """runGame runs the game loop and runs the update and draw function for game"""        
        #game loop
        while self.running:
            #quit function for game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            keys = pygame.key.get_pressed()# key presses (only one is in this method for closing the game)
            if keys[pygame.K_ESCAPE]:
                self.running = False


            self.game.draw(self.screen)

            self.game.update(self.dt)
            pygame.display.flip() # flips display
            self.dt = self.clock.tick(60) / 1000 # does clock.tick and gets deltatime


class Game:
    
    def __init__(self):
        pass

    def update(self,dt: int):
        dt: int
        """updates the game and all the variables in game"""
        pass

    def draw(self,scr: pygame.surface.Surface):
        """draws the objects from game to window Class"""
        pass



ga = Game()
game = Window(ga)