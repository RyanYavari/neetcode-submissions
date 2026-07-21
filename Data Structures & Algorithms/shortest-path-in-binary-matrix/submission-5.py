class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:
            return -1

        neighbors = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1,-1], [-1,1], [1,1]]
        visit = set()
        queue = deque()

        visit.add((0, 0))
        queue.append((0, 0))

        length = 1

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == n-1 and c == n-1:
                    return length

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < n and 0 <= nc < n and
                        grid[nr][nc] == 0 and
                        (nr, nc) not in visit):
                        visit.add((nr, nc))
                        queue.append((nr, nc))

            length += 1

        return -1