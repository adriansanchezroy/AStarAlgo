import pygame

from astaralgo import algorithm
from display import WIDTH, WIN, get_clicked_pos, make_grid, draw

# main application loop
def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)
    
    start = None
    goal = None
    
    run = True
    started = False
    
    while run:
        draw (win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # exits application
                run = False

            if pygame.mouse.get_pressed()[0]:  # left-mouse click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width) 
                node = grid[row][col]
                if not start and node != goal:
                    start = node
                    start.make_start()
                elif not goal and node != start:
                    goal = node
                    goal.make_goal()
                elif node != goal and node != start:
                    node.make_wall()
                        
            elif pygame.mouse.get_pressed()[2]: # right-mouse click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == goal:
                    goal = None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, goal)
                
                # Pressing c key clears the grid        
                if event.key == pygame.K_c:
                    start = None
                    goal = None
                    grid = make_grid(ROWS, width)
                     
    pygame.quit()
    
main(WIN, WIDTH)


