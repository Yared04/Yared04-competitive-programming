class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dfs(node, count, arr, visited):
            if node in visited or node == -1:
                return
            visited.add(node)
            arr[node] = count
            return dfs(edges[node], count + 1, arr, visited)
        
        fromOne = [-1] * len(edges)
        fromTwo = [-1] * len(edges)
        
        dfs(node1, 0, fromOne, set())
        dfs(node2, 0, fromTwo, set())
        
        ans = [float('inf'), -1]
        for i in range(len(edges)):
            if fromOne[i] != -1 and fromTwo[i] != -1:
                temp = max(fromOne[i], fromTwo[i])
                if ans[0] > temp:
                    ans = [temp, i]
        
        return ans[1]
        
        
        