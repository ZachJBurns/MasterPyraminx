import pyraminx
import heapq
import copy
import random
import time
import statistics
import math

#Template for A* found at the following with modifications
#SOURCE: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.puzzle = position

        self.g = 0
        self.h = 0
        self.f = 0
        self.move = "" # Holds each move done to get to the child node

    #defining if two puzzles are equal to each other
    def __eq__(self, other):
        return self.puzzle.__dict__ == other.puzzle.__dict__

    # defining less than for purposes of heap queue
    def __lt__(self, other):
      return self.f < other.f
    
    # defining greater than for purposes of heap queue
    def __gt__(self, other):
      return self.f > other.f

def astar(start):  
    expansions = 0

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, pyraminx.Pyraminx())
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    heapq.heapify(open_list) 
    heapq.heappush(open_list, start_node)
    # Add the start node

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        # Pop current off open list, add to closed list
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None and current.move != "":
                path.append(current.move)
                current = current.parent
            return (path[::-1], len(closed_list)) # Return reversed path

        # Generate children
        children = []
        mainMoves = ["RI", "LI", "BI", "UI", "lI", "rI", "bI", "uI"]
        for move in mainMoves: # Adjacent squares
            expansions += 1
            # Get node position
            node_position = copy.deepcopy(current_node.puzzle)
            node_position.move(move)

            # Create new node
            new_node = Node(current_node, node_position)
            new_node.move = move
            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = math.sqrt(child.puzzle.wrongPos())
            child.f = child.g + child.h

            # Child is already in the open list
            if len([open_node for open_node in open_list if child.puzzle == open_node.puzzle and child.g > open_node.g]) > 0:
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)

def main():
    start = pyraminx.Pyraminx()

    # Initialization for lists to hold move statistics and 
    moveSet = ["R", "L", "B", "U", "l", "r", "b", "u"]
    times = []
    moves = []
    for k in range(3, 21):
        avgExpansion = []
        for i in range(5):
            start = pyraminx.Pyraminx()
            moves = [] 
            for i in range(k):
                x = random.choice(moveSet)
                moves.append(x)
                start.move(x)
            startTime = time.time()
            path, nodes = astar(start)
            endTime = time.time()

            #print(moves) # Uncomment to print the random moves done to each puzzle
            #print(path) # Uncomment to print the moves to solve each puzzle
            times.append(endTime-startTime)
            avgExpansion.append(nodes)
        print("K value", k, "\n", "Average Time to complete each puzzle", round(statistics.mean(times),3), "seconds", "\n", "Average nodes expanded to find path", statistics.mean(avgExpansion))
        
if __name__ == '__main__':
    main()