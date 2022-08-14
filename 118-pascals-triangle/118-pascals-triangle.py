class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums = [[1] * i for i in range(1, numRows+1)]
        for i in range(1,numRows):
            for j in range(1,i):
                nums[i][j] = nums[i-1][j-1]+nums[i-1][j]
        return nums
        