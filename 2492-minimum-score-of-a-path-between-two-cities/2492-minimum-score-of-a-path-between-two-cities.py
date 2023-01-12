class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
        ans = float('inf')
        q = collections.deque([1])
        visited = set()
        while q:
            cur = q.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            for neighbor_city, distance in graph[cur]:
                    ans = min(ans, distance)
                    q.append(neighbor_city)
            
        return ans
