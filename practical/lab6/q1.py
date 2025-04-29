from collections import deque
import random
import copy

# Directions: L, R, U, D
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start, rewards, maze):
    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)
    steps = 0
    collected = 0

    while queue and collected < len(rewards):
        (x, y), steps = queue.popleft()
        if (x, y) in rewards:
            rewards.remove((x, y))
            collected += 1
            queue = deque([((x, y), steps)])  # reset from new position

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and maze[nx][ny] != 1 and (nx, ny) not in visited:
                queue.append(((nx, ny), steps + 1))
                visited.add((nx, ny))

    return steps

def simulate_round(maze):
    rewards = [(i, j) for i in range(5) for j in range(5) if maze[i][j] == 3]
    starts = [(i, j) for i in range(5) for j in range(5) if maze[i][j] == 2]
    
    a_maze = copy.deepcopy(maze)
    b_maze = copy.deepcopy(maze)

    a_steps = bfs(starts[0], rewards[:], a_maze)
    b_steps = bfs(starts[1], rewards[:], b_maze)

    if a_steps < b_steps:
        winner = "A"
    elif b_steps < a_steps:
        winner = "B"
    else:
        winner = "Draw"

    return a_steps, b_steps, winner

maze = [
    [2, 0, 0, 0, 1],
    [0, 1, 3, 0, 0],
    [0, 3, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [3, 0, 1, 2, 3]
]

# Simulate 10 rounds
wins = {"A": 0, "B": 0, "Draw": 0}
with open("out_advsearch.txt", "w") as f:
    for round_num in range(1, 11):
        a, b, w = simulate_round(maze)
        wins[w] += 1
        f.write(f"Round {round_num}: A={a} steps, B={b} steps, Winner={w}\n")

    overall = max(wins, key=wins.get)
    f.write(f"Overall Winner: {overall}\n")
