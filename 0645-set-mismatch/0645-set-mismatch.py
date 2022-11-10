class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = 0
        for i, num in enumerate(nums):
            if nums[abs(num) - 1] < 0:
                duplicate = abs(num)
            else:
                nums[abs(num) - 1] *= -1
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                return duplicate, i + 1
  