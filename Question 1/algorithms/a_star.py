from heapq import heappop, heappush

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def search(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    pq = [(0 + heuristic(start, end), 0, start, [(start[0] + 1, start[1] + 1)])]
    visited = set()

    while pq:
        _, g_cost, (x, y), path = heappop(pq)

        if (x, y) == end:
            return path

        if (x, y) in visited:
            continue
        visited.add((x, y))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != -1 and (nx, ny) not in visited:
                new_g_cost = g_cost + 1
                f_cost = new_g_cost + heuristic((nx, ny), end)
                heappush(pq, (f_cost, new_g_cost, (nx, ny), path + [(nx + 1, ny + 1)]))

    return []
