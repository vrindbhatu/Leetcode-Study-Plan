class Solution:
    def minSwaps(self, s: str) -> int:
        
        
        
        
        def countSwap(start):
            countMissSwap = 0
            for c in s:
                if start != c:
                    countMissSwap +=1
                start = "1" if start == "0" else "0"
                
            return countMissSwap // 2
            
            
            
            
        cntOne = s.count("1")
        cntZero = s.count("0")
        
        diff = abs(cntOne - cntZero)
        
        if diff > 1:
            return -1
        if cntOne > cntZero:
            return countSwap("1")  # one should be at even position
        if cntZero > cntOne:
            return countSwap("0")
        
        return min(countSwap("0"),countSwap("1"))
        
        


        