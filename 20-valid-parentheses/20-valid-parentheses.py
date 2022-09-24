
#vrinda

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack  = []   # create an array
        
        mapping = {")":"(","}":"{","]":"["}  #create an hashmap
        
        
        for brac in s:
             
            if brac in mapping: #here we encounter closing bracket
                topelement = stack.pop() if stack else "#"   #so we pop top element if present else to avoid edge case make the top element as #
                
                if topelement != mapping[brac]:   #if the top elemnt does not match the vakue of the closing brac in hashmap return false
                    return False
                
                
            else:                          #here we encountered opening bracket so we append it to stack
                stack.append(brac)
                
                
        return not stack   #if in the end stack is emplty we return true
        
        