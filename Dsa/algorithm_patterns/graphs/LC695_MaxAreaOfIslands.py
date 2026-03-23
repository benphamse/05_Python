class Solution:
	directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(self, grid, i, j):
		if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == 0:
			return 0
		
		grid[i][j] = 0
		area = 1
		for di, dj in self.directions:
			area += self.dfs(grid, i + di, j + dj)
		return area
		
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.m, self.n = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j))
        return max_area