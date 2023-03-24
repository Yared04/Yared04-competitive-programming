class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, True))
            graph[v].append((u, False))
        
        visited = set()
        self.ans = 0
        
        def dfs(node):
            for neighbor, flag in graph[node]:
                if neighbor not in visited:
                    self.ans += flag
                    visited.add(neighbor)
                    dfs(neighbor)
        
        visited.add(0)
        dfs(0)
        return self.ans