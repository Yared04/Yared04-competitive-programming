class Solution:
    def countArrangement(self, n: int) -> int:
        self.beautiful_arr = 0
        def backtrack(perm, visited):
            if len(perm) == n:
                self.beautiful_arr += 1
                return
            for i in range(1, n+1):
                k = len(perm) + 1
                if not visited & 1<<i-1 and (i % k == 0 or k % i == 0):
                    visited ^= 1<<i-1
                    perm.append(i)
                    backtrack(perm, visited)
                    visited ^= 1<<i-1
                    perm.pop()
                    
        backtrack([], 0)
        return self.beautiful_arr
                    
        