import pygame

class Parameter :

    def __init__(self, text, textColor, textFont = "Calibri " , textSize = 40) :
        self.text = text
        self.textColor = textColor
        
        self.font = pygame.font.SysFont(textFont, textSize).render(self.text, True, self.textColor)


        #Liste de selecteurs associés au paramètre
        self.listSelectors = []

    
    def addSelector(self, selector):
        self.listSelectors.append(selector)

    def isSelected(self):
        for k in range(len(self.listSelectors)):
            if self.listSelectors[k].selected :
                return True
        return False
    
    def getSelectedSelector(self):
        for k in range(len(self.listSelectors)):
            if self.listSelectors[k].selected:
                return self.listSelectors[k]
    

    def getListSelectors(self):
        return self.listSelectors

    


