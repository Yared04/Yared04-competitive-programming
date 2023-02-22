class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        n = len(time)
        temp = []
        for i in range(n):
            temp.append(time[i]%60)
        counter = collections.Counter(temp)
        for key, val in counter.items():
            if key == 0:
                count += counter[0]*(counter[0] - 1) // 2
            elif key > 0 and key < 30:
                if 60 - key in counter:
                    count += counter[key] * counter[60 - key]
            elif key == 30:
                count += counter[key]*(counter[key] - 1) // 2
        return count