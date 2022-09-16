class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        info = []
        for time,user,web in zip(timestamp,username,website):
            info.append((time,user,web))
            
        info.sort(key = lambda x : x[0])
        
        web_visited = defaultdict(list)
        for _,user,web in info:
            web_visited[user].append(web)

        
        web_comb = defaultdict(int)
        for user in web_visited:
            routes = set(combinations(web_visited[user],3))
            
            for route in routes:
                web_comb[route] += 1
                
        max_val, result = max(web_comb.values()), []
        
        for route,count in web_comb.items():
            if max_val == count:
                result.append(route)
                
        if len(route) > 1:
            result.sort()
            
        return result[0]
            

