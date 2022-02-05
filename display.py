import pygame

from node import GREY, WHITE, Node

# Program's screen window
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

# Creates the grid 
def make_grid(rows, width):
    grid = []
    g_width = width // rows  # individual grid width
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, g_width, rows)
            grid[i].append(node)   
            
    return grid

# Draws horizontal and vertical lines to draw the grid    
def draw_grid(win, rows, width):
    g_width = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * g_width), (width, i * g_width))
        for j in range (rows):
            pygame.draw.line(win, GREY, (j*g_width, 0), (j*g_width, width))     

def draw(win, grid, rows, width):
    win.fill(WHITE)
    
    for row in grid:
        for node in row:
            node.draw(win)
    
    draw_grid(win, rows, width)
    pygame.display.update()

# Returns clic's position    
def get_clicked_pos(pos, rows, width):
    g_width = width // rows
    y, x = pos
    
    row = y // g_width
    col = x // g_width
    
    return row, col


