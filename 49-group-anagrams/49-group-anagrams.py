class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        
        
        res = defaultdict(list)
        
        for string in strs:
            
            count = [0] * 26
            
            for char in string:
                count[ord(char) - ord("a")] +=1
                
            res[tuple(count)].append(string)
            
            
        return res.values()
        
        
        #we are given that each str has a-z (26) values
        #so we can maintain a count from [a-z] for each str in hashmap which will store like 1 e, 1 a, 1 t  
        # key : 1 e, 1 a, 1 t
        # value : lsit of strs having this values
        
              
            
                
        
        
        