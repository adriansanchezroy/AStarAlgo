import math
import pygame

from queue import PriorityQueue
from node import Node

# h(n) estimates the distance to reach goal from node n.
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2 
    return abs(x1- x2) + abs(y1 - y2)

# Algorithm that finds A* Path
def algorithm(draw, grid, start, goal):
    count = 0
    not_visited_set = PriorityQueue()
    not_visited_set.put((0, count, start))
    origin = {}
    
    g_score = {node : float("inf") for row in grid for node in row}
    g_score[start] = 0
    
    f_score = {node : float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), goal.get_pos())

    not_visited_set_hash = {start}  # keeps track of what is in the PriorityQueue

    while not not_visited_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # exists loop and app
                pygame.quit()
        
        current = not_visited_set.get()[2]
        not_visited_set_hash.remove(current)
        
        # If we reach our goal, we trace the path to it
        if current == goal:
            build_path(origin, goal, draw)
            goal.make_goal()
            return True
        
        for neighbor in current.neighbors:
            t_g_score = g_score[current] + 1
            
            # If new g_score is better, update its value since better path is found
            if t_g_score < g_score[neighbor]:
                origin[neighbor] = current
                g_score[neighbor] = t_g_score
                f_score[neighbor] = t_g_score + h(neighbor.get_pos(), goal.get_pos())
                if neighbor not in not_visited_set_hash:
                    count += 1
                    not_visited_set.put((f_score[neighbor], count, neighbor))
                    not_visited_set_hash.add(neighbor)
                    neighbor.make_not_visited()
        
        draw()
        
        # Mark node as visited
        if current != start:
            current.visit()        
    
    return False

# 
def build_path(origin, current, draw):
    while current in origin:
        current = origin[current]
        current.make_path()
        draw()