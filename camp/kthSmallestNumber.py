class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def helper(target):
            count = 0
            for i in range(1, m+1):
                count += min (target // i, n)
            return count
                
        
        left = 1
        right = m * n
        while left < right:
            mid = (left + right) // 2
            if helper(mid) >= k:
                right = mid
            else: 
                left = mid + 1
        return left
           
        
            
        