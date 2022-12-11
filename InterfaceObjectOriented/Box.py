import pygame

class Box:

    def __init__(self, size, position, color, flashColor, column, line) :
        
        self.size = size
        self.position = position
        self.color = color
        self.flashColor = flashColor
        self.column = column
        self.line = line
        self.currentColor = color

    def flash(self):
        self.currentColor = self.flashColor
    
    def getColumn(self):
        return self.column

    def getLine(self):
        return self.line
        

    