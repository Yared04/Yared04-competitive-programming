class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        def union(x,y):
            px = find(x)
            py = find(y)
            
            if rank[px] > rank[py]:
                root[py] = px
            elif rank[px] < rank[py]:
                root[px] = py
            else:
                root[py] = px
                rank[py] += 1
                
        if len(connections) + 1 < n:
            return -1
        
        root = [i for i in range(n)]
        rank = [1 for i in range(n)]
    
        for c1, c2 in connections:
            union(c1, c2)
        return len(set(find(i) for i in root))-1
        