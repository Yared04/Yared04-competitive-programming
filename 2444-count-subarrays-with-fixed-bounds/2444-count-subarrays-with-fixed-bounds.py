class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        i=0
        j=0
        cnt=0
        min_idx=-1 
        max_idx=-1 
        while j<len(nums): 
            while j<len(nums): 
                if not(minK <= nums[j] <= maxK): 
                    break
                if nums[j]==minK: 
                    min_idx=j
                if nums[j]==maxK:
                    max_idx=j
                if min_idx !=-1 and max_idx != -1:
                    cnt += (min(min_idx,max_idx) - i+1) 
                j+=1 
            j += 1 
            i = j 
            min_idx = -1 
            max_idx = -1 
        return cnt
            