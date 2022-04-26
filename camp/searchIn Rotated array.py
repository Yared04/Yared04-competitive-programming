class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) //2
            if nums[mid] > nums[right]:
                left = mid + 1
            else: 
                right = mid
        start = 0
        end = len(nums) -1
        if target >= nums[left] and target <= nums[end]:
            start = left
        else:
            end = left
        while start <=  end:
            bst = (start + end) // 2
            if nums[bst] == target:
                return bst
            elif nums[bst] > target:
                end = bst - 1
            else:
                start = bst + 1
        return -1