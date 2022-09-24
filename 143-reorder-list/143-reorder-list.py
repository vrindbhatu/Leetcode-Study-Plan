# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head:
            return 
        
        slow = head
        fast = head
        
        while fast!= None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            
            
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        first = head
        second = prev
        
        while second.next:
            temp = first.next
            first.next = second
            first = temp
            
            
            temp = second.next
            second.next = first
            second = temp
            
        return head
   
        
        