class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            # Base case: out of bounds or water cell
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"  # Mark current land cell as visited
            # Visit all 4 adjacent directions
            for rr, cc in ways:
                dfs(r + rr, c + cc)

        rows, cols = len(grid), len(grid[0])  # Dimensions of the grid
        cnt = 0                               # Island counter
        ways = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # Up, Left, Down, Right directions

        # Traverse each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":  # Unvisited land found
                    dfs(r, c)          # Explore the full island
                    cnt += 1           # Increment island count
        
        return cnt  # Return total number of islands
