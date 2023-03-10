class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        inc_stack = [nums[0]]
        dec_stack = []
        num_min = {}
        for i in range(1, len(nums)):
            while inc_stack and inc_stack[-1] >= nums[i]:
                inc_stack.pop()
            inc_stack.append(nums[i])
            while dec_stack and dec_stack[-1] <= nums[i]:
                dec_stack.pop()
            dec_stack.append(nums[i])
            
            num_min[nums[i]] = inc_stack[0]
            
            if len(dec_stack) >= 2:
                if num_min[dec_stack[-2]] < dec_stack[-1]:
                    return True
        return False
                
        
        