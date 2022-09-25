class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = defaultdict(int)
        
        for num in nums:
            if num in hashMap:
                hashMap[num] +=1
            else:
                hashMap[num] = 1
                
        newList = list(hashMap.items())
        print(newList)
        newList.sort(key = lambda x : x[1],reverse = True)
        print(newList)
        res = []
        for key,value in newList[:k]:
            res.append(key)
            
        return res
            
     
            