import pygame

# RGB for Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
BLACK = (0, 0, 0)


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_visited(self):
        return self.color == TURQUOISE

    def is_not_visited(self):
        return self.color == BLUE

    def is_wall(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_goal(self):
        return self.color == RED

    def reset(self):
        self.color = WHITE

    def visit(self):
        self.color = TURQUOISE

    def make_start(self):
        self.color = ORANGE

    def make_not_visited(self):
        self.color = BLUE

    def make_wall(self):
        self.color = BLACK

    def make_goal(self):
        self.color = RED

    def make_path(self):
        self.color = YELLOW

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        
        # Prevents going out of bounds from bottom, top, right, and left of grid
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall():
            self.neighbors.append(grid[self.row + 1][self.col])
         
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():  
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall():
            self.neighbors.append(grid[self.row][self.col + 1])
            
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():  
            self.neighbors.append(grid[self.row][self.col - 1])
            
    def __lt__(self, other):
        return False
    
    