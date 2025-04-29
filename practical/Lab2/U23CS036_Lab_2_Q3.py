building = [[0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0],
            [0, 1, 1, 0, 1, 0],
            [1, 0, 0, 1, 0, 1],
            [0, 1, 0, 0, 1, 0]]

required_path = []
start_node = 2
end_node = 5

def dfs(building, node, visited, path):
    if visited[node]:
        return
    
    if node == end_node:
        required_path.append(path)
        return
    
    visited[node] = 1

    for i, x in enumerate(building[node]):
        if x:
            dfs(building, i, visited[:], path + [i])

    return

def bfs(building, start_node, end_node):
    queue = [(start_node, [start_node])]
    while queue:
        current, path = queue.pop(0)
        if current == end_node:
            required_path.append(path)
        for i, is_connected in enumerate(building[current]):
            if is_connected and i not in path:
                queue.append((i, path + [i]))

print("using bfs")
bfs(building, start_node, end_node)
for path in required_path:
    print("-".join(map(str, path)))

required_path = []

print("using dfs")
dfs(building, start_node, [0, 0, 0, 0, 0, 0], [2])
for path in required_path:
    print("-".join(map(str, path)))