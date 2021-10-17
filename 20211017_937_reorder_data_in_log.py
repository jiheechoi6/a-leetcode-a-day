class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        numbers = []
        letters = []
        
        for log in logs:
            cont = log[log.find(' ')+1:]
            if re.match('^[0-9 ]*$', cont):
                numbers.append(log)
            else:
                letters.append(log)
        
        def custom(log):
            i = log.find(' ')
            return log[i+1:], log[:i]
        letters = sorted(letters, key=custom)
        
        return letters + numbers
