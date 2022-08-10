class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        no_of_trees = Counter(arr)
        res = 0
        def helper(idx):
            for i in range(idx):
                temp = arr[idx] / arr[i] 
                if temp in no_of_trees:
                    no_of_trees[arr[idx]] += no_of_trees[arr[i]] * no_of_trees[temp]
        for i in range(len(arr)):
            helper(i)
        for key, val in no_of_trees.items():
            res += val
        return res % (10**9 + 7)
     
    
            