class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        maph = {}
        
        for i in range(0,len(nums)):
            diff = target - nums[i]
            
            if diff in maph:
                return (maph[diff],i)
            
            
            else:
                maph[nums[i]] = i
        