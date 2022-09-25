

#vrinda
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashMapS = {}
        hashMapT = {}
        
        for i in range(len(s)):
            hashMapS[s[i]] = 1 + hashMapS.get(s[i],0)
            hashMapT[t[i]] =  1 + hashMapT.get(t[i],0)
            
        return hashMapS == hashMapT
    
#time complexity O(s + t) as we need to iterate to both string and space complexity will we same