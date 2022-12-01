class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        output = [intervals[0]]
        for i in range(1, n):
            if output[-1][1] >= intervals[i][0]:
                temp = [output[-1][0], max(output[-1][1], intervals[i][1])]
                output.pop()
                output.append(temp)
            else:
                output.append(intervals[i])
        return output
        
     