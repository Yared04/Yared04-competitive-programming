class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.defaultdict(int)

        for char in s:
            counter[char] += 1

        for i, char in enumerate(s):
              if counter[char] < 2:
                    return i
        return -1
