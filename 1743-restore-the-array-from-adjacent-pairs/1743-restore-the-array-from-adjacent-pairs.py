class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        q = deque([])
        visited = set()
        for key, val in indegree.items():
            if val == 1:
                q.append(key)
                visited.add(key)
                break
        path = []
        while q:
            cur = q.pop()
            path.append(cur)
            if len(path) == len(adjacentPairs) + 1:
                return path
            for adj in graph[cur]:
                if adj not in visited:
                    visited.add(adj)
                    q.append(adj)
                
                
            