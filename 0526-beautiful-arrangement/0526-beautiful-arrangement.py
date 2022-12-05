class Solution:
    def countArrangement(self, n: int) -> int:
        self.beautiful_arr = 0
        def backtrack(perm, visited):
            if len(perm) == n:
                self.beautiful_arr += 1
                return
            for i in range(1, n+1):
                k = len(perm) + 1
                if i not in visited and (i % k == 0 or k % i == 0):
                    visited.add(i)
                    perm.append(i)
                    backtrack(perm, visited)
                    visited.remove(i)
                    perm.pop()
                    
        backtrack([], set())
        return self.beautiful_arr
                    
        