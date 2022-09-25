class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longestStreak = 0
        numSet = set(nums)
        
        
        for num in nums:
            if num-1 not in numSet:
                currNum = num
                streak  = 1
                
                while currNum +1 in numSet:
                    currNum = currNum +1 
                    streak+=1
                    
                longestStreak = max(longestStreak,streak)
                
        return longestStreak

