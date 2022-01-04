class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        output=[]
        result= []
        changed.sort()
        if len(changed)%2 != 0:
            return output
        else:
            for num in changed:
                if len(output) == 0:
                    output.append(num)
                elif num/2 == output[0]:
                        result.append(output.pop(0))
                else:
                        output.append(num)
            if len(output) == 0:
                return result
            return []

change = [1,3,4,2,6,7]

print(findOriginalArray(change))

