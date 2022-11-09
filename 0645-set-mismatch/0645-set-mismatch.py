class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_set = set(i for i in range(1, len(nums)+1))
        answer = []
        for idx, num in enumerate(nums):
            if num in nums_set:
                nums_set.remove(num)
            else:
                answer.append(num)
        return answer + list(nums_set)