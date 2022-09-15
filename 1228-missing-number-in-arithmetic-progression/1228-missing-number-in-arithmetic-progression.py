class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        diff = (arr[n-1] - arr[0])//n
        
        start, end = 0,n-1
        
        while start < end:
            mid = (start + end) // 2
            
            if arr[mid] == (arr[0] + (mid * diff)):
                start +=1
                
            else:
                end = mid
                
        return arr[0] + start* diff
            
        
        
        
#         expected_value = arr[0]
#         n = len(arr)
#         diff = (arr[n-1] - arr[0])//n
        
#         for i in range(0,len(arr)):
#             if expected_value == arr[i]:
#                 expected_value += diff
            
#         return expected_value
        