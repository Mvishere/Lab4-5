def search(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    all_paths = []
    
    def backtrack(x, y, path, visited):
        if (x, y) == end:
            all_paths.append(path[:])
            return
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != -1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                backtrack(nx, ny, path + [(nx + 1, ny + 1)], visited)
                visited.remove((nx, ny))

    visited = set()
    visited.add(start)
    backtrack(start[0], start[1], [(start[0] + 1, start[1] + 1)], visited)
    
    return all_paths[0]
