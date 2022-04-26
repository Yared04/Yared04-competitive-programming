class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        depth = [1] * len(isConnected)
        root = [i for i in range(len(isConnected))]
        cnt = 0
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if depth[rootX] > depth[rootY]:
                    root[rootY] = rootX
                    depth[rootX] += depth[rootY]
                elif depth[rootX] <= depth[rootY]:
                    root[rootX] = rootY
                    depth[rootY] += depth[rootX]
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i > j and isConnected[i][j] == 1:
                    union(i,j)
        for i in range(len(root)):
            if root[i] == i:
                cnt += 1
        return cnt