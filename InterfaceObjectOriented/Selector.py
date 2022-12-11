from Button import Button
import Color as c

class Selector(Button):

    def __init__(self, size, position, text, textColor, color, colorIfOver, variable, parameter, colorIfClicked=c.GREEN, font="Calibri", font_size=40):
        super().__init__(size, position, text, textColor, color, colorIfOver, colorIfClicked, font, font_size)

        self.variable = variable
        self.parameter = parameter

        self.parameter.addSelector(self)

        self.selected = False

    def getVariable(self):
        return self.variable

    def getParameter(self):
        return self.parameter
    
    def getAssociatedSelectors(self):
        return self.parameter.getListSelectors()
    
    def isSelected(self):
        return self.selected