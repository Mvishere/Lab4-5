import sys
from collections import deque
import heapq

# Define the maze and its properties
class Maze:
    def __init__(self, width, height, start, goal, obstacles):
        self.width = width
        self.height = height
        self.start = start
        self.goal = goal
        self.obstacles = set(obstacles)
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    def is_valid(self, x, y):
        return 0 < x <= self.width and 0 < y <= self.height and (x, y) not in self.obstacles

# Search algorithms
def dfs(maze):
    stack = [(maze.start, [maze.start])]
    explored = set()
    while stack:
        (x, y), path = stack.pop()
        if (x, y) == maze.goal:
            return path, len(path) - 1
        if (x, y) not in explored:
            explored.add((x, y))
            for dx, dy in reversed(maze.directions):
                nx, ny = x + dx, y + dy
                if maze.is_valid(nx, ny):
                    stack.append(((nx, ny), path + [(nx, ny)]))
    return None, -1


def bfs(maze):
    queue = deque([(maze.start, [maze.start])])
    explored = set()
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == maze.goal:
            return path, len(path) - 1  # Cost is steps in path
        if (x, y) not in explored:
            explored.add((x, y))
            for dx, dy in maze.directions:
                nx, ny = x + dx, y + dy
                if maze.is_valid(nx, ny):
                    queue.append(((nx, ny), path + [(nx, ny)]))
    return None, -1


def dls(maze, limit):
    stack = [(maze.start, [maze.start], 0)]
    explored = set()
    while stack:
        (x, y), path, depth = stack.pop()
        if (x, y) == maze.goal:
            return path, len(path) - 1
        if depth < limit and (x, y) not in explored:
            explored.add((x, y))
            for dx, dy in maze.directions:
                nx, ny = x + dx, y + dy
                if maze.is_valid(nx, ny):
                    stack.append(((nx, ny), path + [(nx, ny)], depth + 1))
    return None, -1


def ucs(maze):
    heap = [(0, maze.start, [maze.start])]
    explored = set()
    while heap:
        cost, (x, y), path = heapq.heappop(heap)
        if (x, y) == maze.goal:
            return path, cost
        if (x, y) not in explored:
            explored.add((x, y))
            for dx, dy in maze.directions:
                nx, ny = x + dx, y + dy
                if maze.is_valid(nx, ny):
                    heapq.heappush(heap, (cost + 1, (nx, ny), path + [(nx, ny)]))
    return None, len(explored)

def gbfs(maze):
    def heuristic(x, y):
        return abs(x - maze.goal[0]) + abs(y - maze.goal[1])

    heap = [(heuristic(*maze.start), maze.start, [maze.start])]
    explored = set()
    while heap:
        _, (x, y), path = heapq.heappop(heap)
        if (x, y) == maze.goal:
            return path, len(path) - 1
        if (x, y) not in explored:
            explored.add((x, y))
            for dx, dy in maze.directions:
                nx, ny = x + dx, y + dy
                if maze.is_valid(nx, ny):
                    heapq.heappush(heap, (heuristic(nx, ny), (nx, ny), path + [(nx, ny)]))
    return None, -1


def astar(maze):
    def heuristic(x, y):
        return abs(x - maze.goal[0]) + abs(y - maze.goal[1])

    heap = [(heuristic(*maze.start), 0, maze.start, [maze.start])]
    explored = set()
    while heap:
        _, cost, (x, y), path = heapq.heappop(heap)
        if (x, y) == maze.goal:
            return path, cost
        if (x, y) not in explored:
            explored.add((x, y))
            for dx, dy in maze.directions:
                nx, ny = x + dx, y + dy
                if maze.is_valid(nx, ny):
                    heapq.heappush(heap, (cost + 1 + heuristic(nx, ny), cost + 1, (nx, ny), path + [(nx, ny)]))
    return None, len(explored)

# Read input file
def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        width, height = map(int, lines[0].strip().split(','))
        start = tuple(map(int, lines[1].strip().split('-')))
        goal = tuple(map(int, lines[2].strip().split(';')[-1].split(',')))
        obstacles = [tuple(map(int, obs.split(','))) for obs in lines[3].strip().split(';')]
        strategy = lines[4].strip()
    return width, height, start, goal, obstacles, strategy

# Write output file
def write_output(filename, path, cost):
    with open(filename, 'w') as file:
        for step in path:
            file.write(f"{step[0]},{step[1]}\n")
        file.write(f"Total search cost: {cost}\n")



# Main function
def main(input_file, output_file):
    width, height, start, goal, obstacles, strategy = read_input(input_file)
    maze = Maze(width, height, start, goal, obstacles)

    if strategy == "dfs":
        path, cost = dfs(maze)
    elif strategy == "bfs":
        path, cost = bfs(maze)
    elif strategy == "dls":
        path, cost = dls(maze, 8)
    elif strategy == "ucs":
        path, cost = ucs(maze)
    elif strategy == "gbfs":
        path, cost = gbfs(maze)
    elif strategy == "astar":
        path, cost = astar(maze)
    else:
        raise ValueError("Invalid search strategy")

    write_output(output_file, path, cost)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python TA_4_5_P2_maze_world.py input.txt output.txt")
    else:
        main(sys.argv[1], sys.argv[2])