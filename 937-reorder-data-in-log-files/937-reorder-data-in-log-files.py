class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digit_log = []
        letter_log = []
        
        for log in logs:
            current_log = log.split()
            if current_log[1].isdigit():
                digit_log.append(log)
            else:
                letter_log.append(log)
                
        letter_log.sort(key = lambda x: x.split()[0])
        letter_log.sort(key = lambda x: x.split()[1:])
        
        return letter_log + digit_log
                

        