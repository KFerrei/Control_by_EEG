import pygame

class Scene : 

    ##Attributs
        #colorBackground -> background's color
        #running -> True by default to make the game run
        #screen -> initialise a screen to display the window

    def __init__(self, backgroundColor):
        self.running = True
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.backgroundColor = backgroundColor
        self.windowWidth, self.windowHeight = self.screen.get_size()

    def handling_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def update(self):
        pass

    def display(self):
        pygame.display.flip()

    def run(self):
        self.running = True
        while self.running :
            self.handling_events()
            self.update()
            self.display()
    
