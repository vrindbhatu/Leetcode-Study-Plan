class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        #we are given that each str has a-z (26) values
        #so we can maintain a count from [a-z] for each str in hashmap which will store like 1 e, 1 a, 1 t  
        # key : 1 e, 1 a, 1 t
        # value : lsit of strs having this values
        
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord("a")] +=1
                
            res[tuple(count)].append(s)
            
            
        return res.values()                
            
                
        
        
        