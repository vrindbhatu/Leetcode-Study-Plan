class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        time,fresh = 0,0
        
        q = deque()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append([r,c])
                    
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
                    
        while q and fresh > 0:
            
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = dr+r,dc+c
                    if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    fresh -=1
                    q.append([row,col])
                
            time +=1
            
        if fresh == 0:
            return time
        else:
            return -1
                
            
        