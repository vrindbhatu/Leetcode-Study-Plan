# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head is None:
            return
        
        dummy = ListNode()
        dummy.next = head
        
        leng = 0
        curr = head
        
        while curr!=None:
            leng +=1
            curr = curr.next
            
        leng = leng - n
        
        
        curr = dummy
        while leng > 0:
            leng -=1
            curr = curr.next
            
         
        
        curr.next = curr.next.next
        
        
        return dummy.next
        
        
