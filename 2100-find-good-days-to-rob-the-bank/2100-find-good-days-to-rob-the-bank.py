class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0:
            return list(range(len(security)))
        n= len(security)
        lft = [1]
        rgt = [1]
        
        curr = 1
        for i in range(1,n):
            if security[i] <= security[i-1]:
                curr +=1
            else:
                curr = 1
            lft.append(curr)
            
        curr = 1
        for i in range(n-2,-1,-1):
            if security[i] <= security[i+1]:
                curr +=1
            else:
                curr = 1
            rgt.append(curr)
        rgt.reverse()
        result = []    
        for i in range(n):
            if lft[i] >= time +1 and rgt[i] >=time+1:
                result.append(i)
    
                
        return result
                
            
        
                
        
        