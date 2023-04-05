class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(cur_max, nums):
            temp = 0
            for i in range(len(nums)):
                if nums[i] < cur_max:
                    temp += cur_max - nums[i]
                    
                else: 
                    if temp < nums[i] - cur_max:
                        return False
                    temp -= nums[i] - cur_max
            return True
        
        low = 0
        high = max(nums)
        while low < high:
            mid = (low + high)//2
            if check(mid, nums):
                high = mid 
            else:
                low = mid + 1
        return high
