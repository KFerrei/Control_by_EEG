from Scene import Scene 
from pygame.locals import *
import pygame
import Color as c
import sys

class Menu(Scene):
    
    ##Attributs
        #title -> title of the menu window
        #listParam -> list of parameters that can be modified
        #listImages -> list of images used in the menu window
        #listButtons -> list of buttons to choose the parameters

    def __init__(self, backgroundColor, title):
        
        super().__init__(backgroundColor)
        self.title = title 

        self.listParam = []
        self.listImages = []
        self.listButtons = []

    def addImage(self,image, position):
        self.listImages.append([image,position])
        self.screen.blit(image, position)

    def addButton(self, b):
        self.listButtons.append(b)

    def addParam(self, parameter, position):
        self.listParam.append([parameter, position])


    



    def handling_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    for k in range(len(self.listButtons)):
                        if self.listButtons[k].isMouseOver():
                            self.listButtons[k].currentColor = self.listButtons[k].colorIfClicked
                        else :
                            self.listButtons[k].currentColor = self.listButtons[k].color
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for k in range(len(self.listButtons)):
                        if self.listButtons[k].isMouseOver():
                            self.listButtons[k].call_back()
                            pass


    def update(self):
        pass


    def display(self):

        #Set the background color
        self.screen.fill(self.backgroundColor)

        #Display the title of the menu window
        title = pygame.font.SysFont('calibri',40, bold = True).render(self.title, True, c.TITLEMENU)
        title_rect = title.get_rect(center=(self.windowWidth/2, self.windowHeight/6))
        self.screen.blit(title, title_rect)


        ####### Buttons 
        for k in range(len(self.listButtons)):
            self.listButtons[k].surf.fill(self.listButtons[k].currentColor)
            self.listButtons[k].surf.blit(self.listButtons[k].text_surf, self.listButtons[k].text_rect)
            self.screen.blit(self.listButtons[k].surf, self.listButtons[k].rect)

        for k in range(len(self.listImages)):
            self.screen.blit(self.listImages[k][0], self.listImages[k][1])





        #Display the changes
        pygame.display.flip()

        
        

