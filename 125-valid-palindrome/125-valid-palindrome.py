class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #using two pointers
        i = 0  #start index
        j = len(s) - 1   #end of string
        
        while i < j:    
            
            while i < j and not s[i].isalnum():   #if i < j and s[i] is a not alphanumeric character we increment i
                i +=1
                
            while i < j and not s[j].isalnum():
                j-=1
                
            if s[i].lower() != s[j].lower():
                return False
            
            
            i +=1
            j -=1
            
            
        return True
        