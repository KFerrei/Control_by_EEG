from Scene import Scene 
import pygame
import Color as c
from Game1 import Game1

class Game1Menu(Scene):

    
    def __init__(self, backgroundColor, title):
        super().__init__(backgroundColor)
        self.title = title
        self.listParam = []
        self.listImages = []
        self.listButtons = []
        self.listSelectors = []

        self.buttonSelected = 0


    def getVariable(self, selector):
        selector.getVariable()
    
    def getAllVariables(self):
        variables = []
        for k in range(len(self.listSelectors)):
            if self.listSelectors[k].isSelected():
                variables.append(self.listSelectors[k])
        return variables

    

    def addButton(self, b):
        self.listButtons.append(b)

    def addSelector(self, s):
        self.listSelectors.append(s)

    def addParam(self, parameter, position):
        self.listParam.append([parameter, position])

    def playFunction(self):
        if self.isGameReady():
            variables = self.getAllVariables()
            game1 = Game1(c.BLACK, variables[0], variables[1], variables[2], variables[3], variables[4])
            game1.run()


    def isGameReady(self):
        for k in range(len(self.listParam)):
            if not self.listParam[k][0].isSelected():
                return False
        return True





    def handling_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                

                if event.type == pygame.MOUSEMOTION:
                    for k in range(len(self.listButtons)):
                        if self.listButtons[k].isMouseOver():
                            self.listButtons[k].currentColor = self.listButtons[k].colorIfOver
                        else :
                            self.listButtons[k].currentColor = self.listButtons[k].color 
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for k in range(len(self.listButtons)):
                        if self.listButtons[k].isMouseOver():
                            self.listButtons[k].call_back()

                    for k in range(len(self.listSelectors)):
                        if self.listSelectors[k].isMouseOver():
                            if self.listSelectors[k].getParameter().isSelected():
                                oldSelector = self.listSelectors[k].getParameter().getSelectedSelector()
                                oldSelector.selected = False
                                oldSelector.currentColor = oldSelector.color
                            self.listSelectors[k].selected = True
                            self.listSelectors[k].currentColor = self.listSelectors[k].colorIfClicked
                            pass


  
  
  
    def display(self):

        #Set the background color
        self.screen.fill(self.backgroundColor)

        #Display the title of the menu window
        title = pygame.font.SysFont('calibri',40).render(self.title, True, c.TITLEMENU)
        title_rect = title.get_rect(center=(self.windowWidth/2, self.windowHeight/15))
        self.screen.blit(title, title_rect)

        ####### Buttons 
        for k in range(len(self.listButtons)):
            self.listButtons[k].surf.fill(self.listButtons[k].currentColor)
            self.listButtons[k].surf.blit(self.listButtons[k].text_surf, self.listButtons[k].text_rect)
            self.screen.blit(self.listButtons[k].surf, self.listButtons[k].rect)

        for k in range(len(self.listParam)):
            self.screen.blit(self.listParam[k][0].font, self.listParam[k][1])

        for k in range(len(self.listSelectors)):
            self.listSelectors[k].surf.fill(self.listSelectors[k].currentColor)
            self.listSelectors[k].surf.blit(self.listSelectors[k].text_surf, self.listSelectors[k].text_rect)
            self.screen.blit(self.listSelectors[k].surf, self.listSelectors[k].rect)
        



        #Display the changes
        pygame.display.flip()