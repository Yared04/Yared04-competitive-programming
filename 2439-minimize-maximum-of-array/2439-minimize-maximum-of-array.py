class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(cur_max, nums):
            for i in range(len(nums)-1, 0, -1):
                diff = nums[i] - cur_max
                nums[i] -= max(diff, 0)
                nums[i-1] += max(diff, 0)
            return nums[0] <= cur_max
        
        low = 0
        high = max(nums)
        while low < high:
            mid = (low + high)//2
            if check(mid, nums[:]):
                high = mid 
            else:
                low = mid + 1
        return high
