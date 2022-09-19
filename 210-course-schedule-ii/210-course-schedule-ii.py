class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        
        preMap = {i:[] for i in range(numCourses)}
        
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
            
        result = []   
        cycle = set()
        visited = set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
                
            cycle.remove(crs)
            visited.add(crs)
            result.append(crs)
            
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
            
        return result

        
        