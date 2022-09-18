class Negstr(str):
    def __lt__(self,other):
        return self > other


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        
        trie = {}
        result = []
        
        for product in products:
            curr = trie
            for letter in product:
                curr = curr.setdefault(letter,{})
                if "$" in curr:
                    heapq.heappush(curr["$"],Negstr(product))
                    if len(curr["$"]) > 3:
                        heapq.heappop(curr["$"])
                    
                else:
                    curr["$"] = [Negstr(product)]
                    
        curr = trie
        for char in searchWord:
            curr = curr.get(char,{})
            result.append(sorted(curr.get("$",[]),reverse = True))
                    
        return result
                