class Solution:
    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1: int, node2: int) -> List[int]:
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return [node1, node2]

        if self.size[root1] > self.size[root2]:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
        else:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = [i for i in range(len(edges) + 1)]
        self.size = [1] * (len(edges) + 1)
        for u, v in edges:
            if self.union(u, v):
                return [u, v]
        return []