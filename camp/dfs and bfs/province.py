class Solution:
    def normal_dfs(self, row, isConnected, visited):
        if (row) in visited:
            return
        visited.add((row))
        
        for i in range(len(isConnected[row])):
            if isConnected[row][i] == 1: 
                self.normal_dfs(i, isConnected,visited)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        result = 0
        for i in range(len(isConnected)):
            if i not in visited:
                result += 1
                self.normal_dfs(i,isConnected,visited)
           
        return result