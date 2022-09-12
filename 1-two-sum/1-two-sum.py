class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum = {}
        
        for i,num in enumerate(nums):
            diff = target - num
            if diff in twoSum:
                return(twoSum[diff],i)
            else:
                twoSum[num] = i 