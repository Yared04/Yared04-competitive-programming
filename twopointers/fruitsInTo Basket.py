class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cntr = {}
        i=j=0
        res = 0
        for j,fruit in enumerate(fruits):
            if fruit not in cntr:
                cntr[fruit] = 1
            else:
                cntr[fruit]+=1
            while len(cntr)>2 and i<j:
                cntr[fruits[i]]-=1
                if cntr[fruits[i]] == 0:
                    cntr.pop(fruits[i],None)
                i+=1
            res = max(res,sum(cntr.values()))
        return res
            
        