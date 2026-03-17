class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        ans = []

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            cur = queue.popleft()
            ans.append(cur)

            for nextCourse in adj[cur]:
                indegree[nextCourse] -= 1

                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)

        return ans if len(ans) == numCourses else []