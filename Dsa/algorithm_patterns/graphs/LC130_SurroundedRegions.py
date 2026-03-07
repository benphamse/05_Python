class Solution:
    def bfs(self, board, i, j):
        q = deque([(i, j)])
        board[i][j] = 'B'

        while q:
            x, y = q.popleft()
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.n and 0 <= ny < self.m and board[nx][ny] == 'O':
                    board[nx][ny] = 'B'
                    q.append((nx, ny))

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        self.n, self.m = len(board), len(board[0])
        if self.n <= 2 or self.m <= 2: return

        for i in range(self.n):
            for j in range(self.m):
                if (i == 0 or i == self.n - 1 or j == 0 or j == self.m - 1) and board[i][j] == 'O': 
                    self.bfs(board, i, j)
                
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'B':
                    board[i][j] = 'O'