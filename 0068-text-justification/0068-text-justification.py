class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0 
        cur_total_chars = 0
        cur_line = []
        last_line = False
        while i < len(words) or len(cur_line)>0:      
            occupied_space = cur_total_chars + len(cur_line)  
            if i < len(words) and occupied_space + len(words[i]) <= maxWidth:
                cur_line.append(words[i])
                cur_total_chars += len(words[i])
                if i == len(words)-1:
                    last_line = True
                i += 1           
            else:    
                remaining_space = maxWidth - (occupied_space-1)           
                if last_line or len(cur_line) == 1:
                    common_extra_space = 0
                    left_extra_space = 0
                    last_space = remaining_space
                else:
                    common_extra_space = remaining_space//(len(cur_line)-1)
                    left_extra_space = remaining_space%(len(cur_line)-1)
                    last_space = 0
                
                line_content = ""
                for j in range(len(cur_line)):
                    if j > 0:
                        space = " " * (common_extra_space + 1)
                        if left_extra_space > 0:
                            space += " "
                            left_extra_space -= 1
                        line_content += space 
                    line_content += cur_line[j]
                
                if last_space > 0:
                    line_content += " " * last_space
                    
                res.append(line_content)
                cur_line = []
                cur_total_chars = 0
        return res