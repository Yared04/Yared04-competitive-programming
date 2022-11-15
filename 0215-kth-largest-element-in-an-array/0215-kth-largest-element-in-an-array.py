class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(l, r):
            p = l
            pivot = nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if len(nums) - k < p:
                return quickSelect(l, p-1)
            elif len(nums) - k > p:
                return quickSelect(p+1, r)
            else:
                return nums[p]
            
        return quickSelect(0, len(nums)-1)
                
            
        
                
            
        