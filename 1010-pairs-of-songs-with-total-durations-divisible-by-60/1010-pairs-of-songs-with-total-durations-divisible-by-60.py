class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0: # check if a%60==0 && b%60==0
                ret += remainders[0]
            else: # check if a%60+b%60==60
                ret += remainders[60-t%60]
            remainders[t % 60] += 1 # remember to update the remainders
        return ret
        
        
        ## brute force solution
        
#         count = 0
#         for i in range(0,len(time)):
#             for j in range(i+1,len(time)):
#                 if ((time[i] + time[j]) % 60 == 0):
#                     count+=1
                    
                    
#         return count

    
        