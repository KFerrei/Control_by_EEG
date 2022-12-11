import pygame
import Color as c

class Button():

    def __init__(self, size, position,  text, textColor,  color, colorIfOver,colorIfClicked = c.GREEN, font = "Calibri", font_size = 40, function = None) :
        self.size = size
        self.position = position
        self.text = text
        self.textColor = textColor
        self.color = color
        self.colorIfClicked = colorIfClicked
        self.colorIfOver = colorIfOver
        self.currentColor = color
        self.function = function
        self.waitingColor = colorIfClicked

        self.font = pygame.font.SysFont(font, font_size, bold = True )

        #########   Creates the visible objects for the shape of the button  ########
        #Create a pygame surface with the size desired
        self.surf = pygame.Surface(self.size)
        #Create a visible rectangle  with the position and the surface
        self.rect = self.surf.get_rect(center = self.position)

        ########   Creates the visible objects for the text   #########
        self.text_surf = self.font.render(self.text, 1, self.textColor)
        self.text_rect = self.text_surf.get_rect(center=[wh//2 for wh in self.size])



    def call_back(self, *args):
        if self.function:
            return self.function(*args)



    ###### To call in handling events   #########
    def isMouseOver(self):
        mousePosition = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePosition):
            return True


