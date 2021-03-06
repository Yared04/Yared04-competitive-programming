class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) - 1
        while True:
            if numbers[first] + numbers[last] == target:
                return [first + 1, last + 1]
            elif numbers[first] + numbers[last] < target:
                first += 1
            else:
                last -= 1