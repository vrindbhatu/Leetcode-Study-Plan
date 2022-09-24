#Vrinda
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        seen_nodes = set()
        while head != None:
            if head in seen_nodes:
                 return True
            seen_nodes.add(head)
            head = head.next
            
        return False

    
#time complexity : O(n) : we visit each of the n elements
#space complexity: O(n) : n elements added to hashmap

# Method 2

# class ListNode:
#     def __init__(self,node):
#         self.val = node
#         self.next = None
        
# class Solution:
#     def hasCycle(self, head):
#         slow = head
#         fast = head
        
#         while slow!=fast:
#             if fast = None or fast.next.next = None:
#                 return False
          
#             slow = slow.next
#             fast = flast.next.next
            
#         return True
    
    
#time complexity : O(n) : we visit each of the n elements
#space complexity: O(1) : we only use two nodes slow and fast
        
    
        