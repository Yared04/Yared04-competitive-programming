class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def dfs(N):
            if N == 1: return [1]
            ans = []
            t1 = dfs((N+1)//2)
            for i in t1:
                ans.append(i*2 - 1)
            t2 = dfs(N//2)
            for i in t2:
                ans.append(i*2)
            
            return ans

        return dfs(n)

