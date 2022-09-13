class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        for i in range(0,len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            maxSum = max(maxSum,curSum)
            
        return(maxSum)
            
            
        