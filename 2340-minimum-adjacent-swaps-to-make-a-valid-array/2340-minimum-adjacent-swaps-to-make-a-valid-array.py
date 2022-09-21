class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        
        n = len(nums)
        mi,ma = min(nums),max(nums)
        if mi == ma:
            return 0
        
        mii,mai = 0,n-1
        
        for i in range(n):
            if nums[i] == mi:
                mii = i
                break
        for i in range(n-1,-1,-1):
            if nums[i] == ma:
                mai = i
                break
                
        if mii < mai:
            return mii + n - 1 - mai
        return mii + n - 2 - mai
            
