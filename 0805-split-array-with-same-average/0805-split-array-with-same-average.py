class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        
        if total == 0:
            return True if n > 1 else False
        
        @lru_cache(None)
        def subset_sum(idx,val,rem):                
            if idx==n:
                return True if (val==0 and rem==0) else False
            
            res = False
            if val >= nums[idx]:
                res = res or subset_sum(idx+1,val-nums[idx],rem-1)
            res = res or subset_sum(idx+1,val,rem)
            
            return res
        
        for i in range(1,n):  
            
            if (total*i) % n == 0 and subset_sum(0,(total*i) // n, i):
                return True
            
        return False
        