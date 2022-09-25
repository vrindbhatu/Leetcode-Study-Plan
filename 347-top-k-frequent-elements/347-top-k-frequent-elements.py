#vrinda

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}
        freq = [[] for i in range(len(nums) +1)]
        
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num,0)
            
        for key, val in hashMap.items():
            freq[val].append(key)
            
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
            
        
        
        
        
        
        
        
        
        
#         hashMap = defaultdict(int)
        
#         for num in nums:
#             if num in hashMap:
#                 hashMap[num] +=1
#             else:
#                 hashMap[num] = 1
                
#         newList = list(hashMap.items())
#         print(newList)
#         newList.sort(key = lambda x : x[1],reverse = True)
#         print(newList)
#         res = []
#         for key,value in newList[:k]:
#             res.append(key)
            
#         return res
            
# O(nlogn)   
            