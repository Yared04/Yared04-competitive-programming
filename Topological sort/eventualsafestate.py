class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegree = [0]*len(graph)
        neighbor = defaultdict(set)
        ans = []
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                indegree[i] = len(graph[i]) 
                neighbor[graph[i][j]].add(i)
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            ans.append(cur)
            for nei in neighbor[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        ans.sort()
        return ans 
        