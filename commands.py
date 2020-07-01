import pygame
from settings import *

class Grid:
    def __init__(self, game):
        self.game = game
        self.pos = (0, 0)
        self.cells = []
        self.make_grid()

    def make_grid(self):
        for x in range(3):
            for y in range(3):
                self.cells.append(Cell(x,y,self))
#            print(self.cells)

    def update():
        for cell in cells:
            cell.update()

    def draw():
        for cell in self.cells:
            cell.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.grid = Grid(self)


    def run(self):
        while self.running:
            self.get_events()
            self.update()
            self.draw()
        pygame.quit()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BG_COLOR)
        pygame.display.update()

class Cell:
    def __init__(self, x, y, grid):
        self.pos = (x, y)
        self.grid = grid
        self.revealed = False

    def update(self):
        for cell in cells:
            cell.update()

    def draw(self):
        pygame.draw.rect(self.grid.game.screen, CELL_BG_COLOR,
                (self.grid.pos[0]+(self.pos[0]*self.size),self.grid.pos[1]+(self.pos[1]*self.size),self.size, self.size), 2)
