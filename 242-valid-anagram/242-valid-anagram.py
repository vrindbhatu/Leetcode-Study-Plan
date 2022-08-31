class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s = sorted(s)
        t = sorted(t)
        if len(s) != len(t):
            return False
        
        for i in range(0,len(s)):
            if s[i] !=t[i]:
                return False

        return True
        