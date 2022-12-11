import pygame

import Color as c
import Image as img
from Menu import Menu
from Button import Button
from Game1Menu import Game1Menu
from Parameter import Parameter
from Selector import Selector


pygame.init()


################################        WINDOWS      ###############################

menu = Menu(c.BGMENU, "Démonstration d’une capacité de commande mains-libres par EEG")
game1Menu = Game1Menu(c.BGMENU, "Game 1")




#################################       GAME1MENU     ##############################
""" Parameters """
param1 = Parameter("Taille de la carte :", c.WHITE)
game1Menu.addParam(param1, (menu.windowWidth/10, menu.windowHeight/5 + (0*90)))

param2 = Parameter("Nombre de bateaux :", c.WHITE)
game1Menu.addParam(param2, (menu.windowWidth/10, menu.windowHeight/5 + (1*90)))

param3 = Parameter("Clignotement :", c.WHITE)
game1Menu.addParam(param3, (menu.windowWidth/10, menu.windowHeight/5 + (2*90)))

param4 = Parameter("Fréquences aléatoires :", c.WHITE)
game1Menu.addParam(param4, (menu.windowWidth/10, menu.windowHeight/5 + (3*90)))

param5 = Parameter("Nombre de tests :", c.WHITE)
game1Menu.addParam(param5, (menu.windowWidth/10, menu.windowHeight/5 + (4*90)))


""" Buttons """
buttonMenu = Button((menu.windowWidth/15 , menu.windowHeight/20), (menu.windowWidth/20, menu.windowHeight/20), "Menu", c.WHITE, c.BLUE, c.GREY, font_size = 20, function = menu.run)
game1Menu.addButton(buttonMenu)

bPlay = Button((menu.windowWidth/3 , menu.windowHeight/9), (menu.windowWidth/2, menu.windowHeight/1.10), "PLAY", c.WHITE, c.BLUE, c.GREY, font_size = 80)
game1Menu.addButton(bPlay)


""" Selectors """
S2x2 = Selector((menu.windowWidth/16 , menu.windowHeight/15), (menu.windowWidth/2, menu.windowHeight/4.5), "2x2", c.WHITE, c.LIGHTBLUE, c.GREY, 2,param1, font_size = 40)
game1Menu.addSelector(S2x2)

S4x4 = Selector((menu.windowWidth/16 , menu.windowHeight/15), (menu.windowWidth/1.5, menu.windowHeight/4.5), "4x4", c.WHITE, c.LIGHTBLUE, c.GREY,4,param1, font_size = 40)
game1Menu.addSelector(S4x4)

S6x6 = Selector((menu.windowWidth/16 , menu.windowHeight/15), (menu.windowWidth/1.20, menu.windowHeight/4.5), "6x6", c.WHITE, c.LIGHTBLUE, c.GREY, 6,param1,font_size = 40)
game1Menu.addSelector(S6x6)

SNb1 = Selector((menu.windowWidth/16 , menu.windowHeight/15), (menu.windowWidth/2, menu.windowHeight/4.5 + (1*90)), "1", c.WHITE, c.LIGHTBLUE, c.GREY,1, param2,font_size = 40)
game1Menu.addSelector(SNb1)

SNb2 = Selector((menu.windowWidth/16 , menu.windowHeight/15), (menu.windowWidth/1.5, menu.windowHeight/4.5 + (1*90)), "2", c.WHITE, c.LIGHTBLUE, c.GREY,2,param2 ,font_size = 40)
game1Menu.addSelector(SNb2)

SNb3 = Selector((menu.windowWidth/16 , menu.windowHeight/15), (menu.windowWidth/1.20, menu.windowHeight/4.5 + (1*90)), "3", c.WHITE, c.LIGHTBLUE, c.GREY, 3,param2,font_size = 40)
game1Menu.addSelector(SNb3)

SC1 = Selector((menu.windowWidth/16 , menu.windowHeight/15), (menu.windowWidth/2, menu.windowHeight/4.5 + (2*90)), "1", c.WHITE, c.LIGHTBLUE, c.GREY, 1,param3, font_size = 40)
game1Menu.addSelector(SC1)

SC2 = Selector((menu.windowWidth/16 , menu.windowHeight/15), (menu.windowWidth/1.5, menu.windowHeight/4.5 + (2*90)), "5", c.WHITE, c.LIGHTBLUE, c.GREY, 5,param3,font_size = 40)
game1Menu.addSelector(SC2)

SC3 = Selector((menu.windowWidth/16 , menu.windowHeight/15), (menu.windowWidth/1.20, menu.windowHeight/4.5 + (2*90)), "10", c.WHITE, c.LIGHTBLUE, c.GREY,10, param3,font_size = 40)
game1Menu.addSelector(SC3)

SOui = Selector((menu.windowWidth/16 , menu.windowHeight/15), (menu.windowWidth/2, menu.windowHeight/4.5 + (3*90)), "Oui", c.WHITE, c.LIGHTBLUE, c.GREY, True,param4, font_size = 40)
game1Menu.addSelector(SOui)

SNon = Selector((menu.windowWidth/16 , menu.windowHeight/15), (menu.windowWidth/1.5, menu.windowHeight/4.5 + (3*90)), "Non", c.WHITE, c.LIGHTBLUE, c.GREY, False,param4, font_size = 40)
game1Menu.addSelector(SNon)

ST1 = Selector((menu.windowWidth/16 , menu.windowHeight/15), (menu.windowWidth/2, menu.windowHeight/4.5 + (4*90)), "1", c.WHITE, c.LIGHTBLUE, c.GREY, 1,param5,font_size = 40)
game1Menu.addSelector(ST1)

ST2 = Selector((menu.windowWidth/16 , menu.windowHeight/15), (menu.windowWidth/1.5, menu.windowHeight/4.5 + (4*90)), "5", c.WHITE, c.LIGHTBLUE, c.GREY,5,param5, font_size = 40)
game1Menu.addSelector(ST2)

ST3 = Selector((menu.windowWidth/16 , menu.windowHeight/15), (menu.windowWidth/1.20, menu.windowHeight/4.5 + (4*90)), "10", c.WHITE, c.LIGHTBLUE, c.GREY, 10,param5,font_size = 40)
game1Menu.addSelector(ST3)




#################################         MENU        #############################
""" Buttons  """
buttonG1 = Button((menu.windowWidth/3 , menu.windowHeight/6), (2*menu.windowWidth/3, 2*menu.windowHeight/5), "Game 1",c.WHITE, c.BLUE, c.GREY, font_size = 100, function = game1Menu.run )
menu.addButton(buttonG1)

buttonG2 = Button((menu.windowWidth/3 , menu.windowHeight/6), (2*menu.windowWidth/3, 4*menu.windowHeight/5), "Game 2", c.WHITE, c.BLUE, c.GREY, font_size = 100)
menu.addButton(buttonG2)


""" Images  """
menu.addImage(img.THALES, (menu.windowWidth/8, menu.windowHeight/3 + (0*90)))
menu.addImage(img.IMT, (menu.windowWidth/8, menu.windowHeight/3 + (2*90)))



menu.run()

pygame.quit()