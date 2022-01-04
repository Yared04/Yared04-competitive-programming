class Solution:
    def merge(self,intervals):
        intervals.sort()
        print(intervals)
        output = [intervals[0]]
        if len(intervals) == 1:
            return output
        else:
            for i in range(len(intervals)-1):
                if intervals[i][1] >= intervals[i+1][0]:
                    temp = [intervals[i][0],max(intervals[i][1],intervals[i+1][1])]
                    output.append(temp)
                    intervals[i+1] = temp
                    print(output)
                    k =len(output)
                    if k > 1 and output[k-2][1] >= output[k-1][0]:
                        temp = [output[k-2][0], max(output[k-2][1],output[k-1][1])]
                        output[k-2] = temp
                        output.pop()
                else:
                    output.append(intervals[i+1])
        # if len(output) == 0:
        #     return intervals
        return output
    
intervals =[[1,3],[2,5],[6,9]]
print(merge(intervals))
