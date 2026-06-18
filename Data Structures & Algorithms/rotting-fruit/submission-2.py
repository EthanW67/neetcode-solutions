class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        time, fresh = 0, 0
        queue = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        directions = [[1,0],[0,-1],[-1,0],[0,1]]
        while queue and fresh > 0:
            for i in range(len(queue)):
                ROW, COL = queue.popleft()

                for dr, dc in directions:
                    r, c = dr + ROW, dc + COL

                    if (r<0 or c<0 or r>=row or c>=col or grid[r][c] != 1):
                        continue 

                    grid[r][c] = 2
                    queue.append((r,c))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1

