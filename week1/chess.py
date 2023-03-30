#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:15:22 2023

@author: nouman
"""
def find(src, dest):
    # Convert source and destination squares to (x, y) coordinates
    src_x, src_y = src % 8, src // 8
    dest_x, dest_y = dest % 8, dest // 8
    # Define the possible moves a knight can make from any square
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]
    
    # Initialize a dictionary to keep track of the minimum distance to each square and a queue to store the squares to be visited in breadth-first order
    distances = {square: float('inf') for square in range(64)}
    queue = []
    
    distances[src] = 0
    queue.append(src)
    # Use breadth-first search to find the shortest path to the destination square
    while queue:
        curr_square = queue.pop(0) 
        # Check if the current square is the destination square
        if curr_square == dest:
            return distances[dest]       
        # Consider all possible knight moves from the current square
        curr_x, curr_y = curr_square % 8, curr_square // 8
        for dx, dy in moves:
            next_x, next_y = curr_x + dx, curr_y + dy
            if 0 <= next_x < 8 and 0 <= next_y < 8:
                next_square = next_x + 8 * next_y
                if distances[next_square] == float('inf'):
                    distances[next_square] = distances[curr_square] + 1
                    queue.append(next_square)
    
    # If the destination square is not reachable, return -1
    return -1
print(find(19, 36))