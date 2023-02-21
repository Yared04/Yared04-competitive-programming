class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
            
        def dfs(node):
            for neighboring_node in graph[node]:
                if neighboring_node not in seen:
                    seen.add(neighboring_node)
                    dfs(neighboring_node)

                
        seen = set()
        answer = []
        for idx, ind in enumerate(indegree):
            if ind == 0 and idx not in seen:
                seen.add(idx)
                answer.append(idx)
                dfs(idx)
       
        return answer
            
                
            
        