class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        root = [i for i in range(n)]
        depth = [1 for _ in range(n)]
        
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if depth[rootX] >depth[rootY]:
                root[rootY] = rootX
            elif depth[rootX] < depth[rootY]:
                root[rootX] = rootY
            else:
                root[rootY] = rootX
                depth[rootX] += 1
        for u, v in edges:
            union(u, v)

        groups = Counter(find(i) for i in range(n))
        aList = list( groups.values())
        answer = 0
        cur_answer = aList[0]
        for i in range(1, len(aList)):
            answer += cur_answer * aList[i]
            cur_answer += aList[i]
        
        return answer