"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
from typing import Optional
from xml.dom import Node
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node : return node

        q, clones = deque([node]), {node.val: Node(node.val, [])}

        while q:
            cur = q.popleft()
            curClone = clones[cur.val]

            for nbgr in cur.neighbors:
                if nbgr.val not in clones:
					clones[nbgr.val] = Node(nbgr.val, [])
					q.append(nbgr)

				curClone.neighbors.append(clones[nbgr.val])

		return clones[node.val]