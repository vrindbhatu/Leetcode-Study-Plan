"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
            
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
            
        return oldToCopy[head]
    
    
    
    
# class Node:
#     def __init__(self,node):
#         self.val = 0
#         self.next = None
#         self.random = None
        
# class Solution:
#     def randomPointer(self, head):
        
#         hashMap = {None : None}
        
#         curr = head
#         while curr:
#             copy = Node(curr.val)
#             hashMap[curr] = copy
#             cuu = curr.next
            
#         curr = head
#         while curr:
#             copy = hashMap[curr]
#             copy.next = hashMap[curr.next]
#             copy.random = hashMap[curr.random]
              # curr = curr.next
            
            
#         return hashMap[head]
            
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        