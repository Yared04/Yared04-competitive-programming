class Solution:
    def search(self, nums: List[int], target: int, bo):
        left =0 
        right = len(nums)-1
        start=-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1  
            else:
                if bo:
                    start = mid
                    right = mid -1
                else:
                    start = mid
                    left = mid + 1
        return start
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.search(nums, target ,True), self.search(nums,target, False)]

            
        
        
        
            
        