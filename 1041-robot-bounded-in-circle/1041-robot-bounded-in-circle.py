class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        cur = [0,0]
        cur_dir = 0 
        
        instructions = instructions*4
        
        for ins in instructions:
            if ins == 'G':
                if cur_dir == 0: 
                    cur[0]+=1
                elif cur_dir == 1: 
                    cur[1]+=1
                elif cur_dir == 2: 
                    cur[0]-=1
                elif cur_dir == 3:
                    cur[1]-=1
            elif ins == 'L':
                if cur_dir == 0: cur_dir = 3
                else: cur_dir -= 1
            elif ins == 'R':
                if cur_dir == 3: cur_dir = 0
                else: cur_dir +=1 
                    
        return cur == [0,0] and cur_dir == 0