import heapq

def parse_input(filename):
    with open(filename, 'r') as file:
        maze = [list(map(int, line.strip().split())) for line in file]
    start = None
    goals = []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                goals.append((i, j))
    return maze, start, goals

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(position, maze):
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # L, R, U, D
    neighbors = []
    rows, cols = len(maze), len(maze[0])
    for move in moves:
        new_x, new_y = position[0] + move[0], position[1] + move[1]
        if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] != 1:
            neighbors.append((new_x, new_y))
    return neighbors

def astar(maze, start, goals):
    visited_order = []
    total_steps = 0
    current_start = start
    while goals:
        priority_queue = [(0, current_start, [], 0)]
        visited = set()
        path_found = False
        while priority_queue and not path_found:
            cost, (x, y), path, step_cost = heapq.heappop(priority_queue)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            visited_order.append((x, y))
            if (x, y) in goals:
                goals.remove((x, y))
                total_steps += step_cost
                current_start = (x, y)
                path_found = True
                break
            for neighbor in get_neighbors((x, y), maze):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (step_cost + 1 + min(heuristic(neighbor, g) for g in goals), neighbor, path + [neighbor], step_cost + 1))
    return visited_order, total_steps

def write_output(filename, visited, steps):
    with open(filename, 'w') as file:
        for tile in visited:
            file.write(f"{tile}\n")
        file.write(f"Total steps: {steps}\n")

def main():
    input_file = "input2.txt"
    output_file = "out_astar.txt"
    maze, start, goals = parse_input(input_file)
    visited, steps = astar(maze, start, goals)
    write_output(output_file, visited, steps)
    print(f"Output written to {output_file}")

if __name__ == "__main__":
    main()