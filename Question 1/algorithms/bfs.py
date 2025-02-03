from collections import deque

def search(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    queue = deque([(start, [(start[0] + 1, start[1] + 1)], set([start]))])
    all_paths = []
    
    while queue:
        (x, y), path, visited = queue.popleft()
        
        if (x, y) == end:
            all_paths.append(path)
            continue
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != -1 and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx + 1, ny + 1)], visited | {(nx, ny)}))

    return all_paths
