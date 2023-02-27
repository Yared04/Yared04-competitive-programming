class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 100
        for start, end in logs:
            for i in range(start, end):
                years[(i + 1950) % 1950] += 1
        _max = max(years)
        for i in range(100):
            if years[i] == _max:
                return i + 1950