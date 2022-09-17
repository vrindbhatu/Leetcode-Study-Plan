class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(i):
            visited.add(i)
            for j in range(len(isConnected)):
                if j not in visited and isConnected[i][j]:
                    dfs(j)
        
        
        
        noProvinces = 0
        visited = set()
        
        for i in range(len(isConnected)):
            if i not in visited:
                noProvinces +=1
                dfs(i)
                
                
        return noProvinces