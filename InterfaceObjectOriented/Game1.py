from Scene import Scene
import pygame
import Color as c
from Box import Box

class Game1(Scene) :


    def __init__(self, backgrounColor, size, nbBoat, flash, frequency, nbTest):

        super.__init__(backgrounColor)
        self.size = size
        self.nbBoat = nbBoat
        self.flash = flash
        self.frequency = frequency
        self.nbTest = nbTest
        self.Grid = {}

    
    def drawGrid(self):
        for i in range(self.taille[0]-1):
            for j in range(self.taille[1]-1):
                self.Grid[(i,j)] = pygame.Rect(self.screen, c.BLACK, pygame.Rect())


    
    def getBox(self, line, column):
        return self.Grid[(line,column)]

    def addBox():
        pass
        


