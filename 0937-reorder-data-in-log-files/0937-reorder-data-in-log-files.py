class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
       
        def isLetterLog(log):
            return not log.split(' ')[1].isdigit()
               
        letter_logs = []
        digit_logs = []
        for log in logs:
            if isLetterLog(log):
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        
        letter_logs.sort(key=lambda x: (x.split(' ')[1:], x.split(' ')[0]))
        return letter_logs + digit_logs
                    
                
        