class Solution:
    def bfs(self, queue, heights):
        visited = set(queue)

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.n and 0 <= ny < self.m and (nx, ny) not in visited and heights[nx][ny] >= heights[x][y]:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return visited

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []

        self.n, self.m = len(heights), len(heights[0])
        pacificQueue = deque()
        atlanticQueue = deque()

        for i in range(self.n):
            pacificQueue.append((i, 0))
            atlanticQueue.append((i, self.m - 1))

        for i in range(self.m):
            pacificQueue.append((0, i))
            atlanticQueue.append((self.n - 1, i))

        pacificReachable = self.bfs(pacificQueue, heights)
        atlanticReachable = self.bfs(atlanticQueue, heights)

        return list(pacificReachable & atlanticReachable)

