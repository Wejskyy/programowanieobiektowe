import pygame

class snake():
    #konstruktor klasy
    def __init__(self):
        self.dlugosc=1
        self.punkty=0
        self.pozycja=[(120,120)]
    def getHead(self):
        return self.pozycje[-1]
    def eating(self):
        self.dlugosc+=1
        self.punkty+=1
    def drawSnake(self):
        for wspolrzendne in self.pozycje[::-1]:
            wazShape = pygame.Rect((wspolrzendne[0],
            wspolrzendne[1]), (40, 40))
            pygame.draw.rect(OknoGry, (255, 192, 203),
            wazShape)
