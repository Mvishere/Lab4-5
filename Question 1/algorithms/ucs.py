from heapq import heappop, heappush

def search(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    pq = [(0, start, [(start[0] + 1, start[1] + 1)])]  # (cost, (x, y), path)
    visited = set()

    while pq:
        cost, (x, y), path = heappop(pq)

        if (x, y) == end:
            return path

        if (x, y) in visited:
            continue
        visited.add((x, y))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != -1 and (nx, ny) not in visited:
                heappush(pq, (cost + 1, (nx, ny), path + [(nx + 1, ny + 1)]))

    return []
