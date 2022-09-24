class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_vol = 0
        
        l,r = 0,len(height) - 1
        dist = len(height) - 1
        
        while l < r:
            max_vol = max(min(height[l],height[r]) * dist,max_vol)
            
            if height[l] < height[r]:
                l+=1
            elif height[l] > height[r]:
                r-=1
            else:
                l+=1
                
            dist -=1
            
        return max_vol
            
            
        
        