import copy

# Directions: L, R, U, D
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

maze = [
    [2, 0, 0, 0, 1],
    [0, 1, 3, 0, 0],
    [0, 3, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [3, 0, 1, 2, 3]
]

A_start = (0, 0)
B_start = (4, 3)

rewards = {(1,2), (2,1), (4,0), (4,4)}

def is_valid(pos):
    x, y = pos
    return 0 <= x < 5 and 0 <= y < 5 and maze[x][y] != 1

def minimax(posA, posB, rewards_left, is_A_turn, depth):
    if not rewards_left:
        # Whoever collected more in fewer turns wins
        return (1 if is_A_turn else -1), []

    if depth == 20:  # cutoff
        return 0, []

    best_score = float('-inf') if is_A_turn else float('inf')
    best_path = []

    current_pos = posA if is_A_turn else posB

    for dx, dy in DIRECTIONS:
        new_pos = (current_pos[0] + dx, current_pos[1] + dy)
        if not is_valid(new_pos):
            continue

        new_rewards = set(rewards_left)
        collected = False
        if new_pos in rewards_left:
            new_rewards.remove(new_pos)
            collected = True

        if is_A_turn:
            score, path = minimax(new_pos, posB, new_rewards, not is_A_turn, depth + 1)
        else:
            score, path = minimax(posA, new_pos, new_rewards, not is_A_turn, depth + 1)

        if is_A_turn and score > best_score:
            best_score = score
            best_path = [("A", new_pos, collected)] + path
        elif not is_A_turn and score < best_score:
            best_score = score
            best_path = [("B", new_pos, collected)] + path

    return best_score, best_path

# Run minimax
score, sequence = minimax(A_start, B_start, rewards, is_A_turn=True, depth=0)

with open("out_advsearch.txt", "a") as f:
    f.write("\nPart 2 - Minimax Turn Based:\n")
    for step in sequence:
        agent, pos, got_reward = step
        f.write(f"{agent} moved to {pos}, reward collected: {got_reward}\n")
    f.write(f"Winner: {'Agent A' if score == 1 else 'Agent B' if score == -1 else 'Draw'}\n")
