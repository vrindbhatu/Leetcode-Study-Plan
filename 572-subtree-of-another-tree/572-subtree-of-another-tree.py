# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
                    
        def isCheck(node,subroot):
            if not node and not subroot:
                return True
            if not node or not subroot:
                return False
            if node.val != subroot.val:
                return False
            return isCheck(node.left, subroot.left) and isCheck(node.right, subroot.right)
 

        queue = deque([root])
        ans = False
        while queue:
            node = queue.popleft()       
            ans = isCheck(node, subRoot)
                
            if node:
                queue.append(node.left)
                queue.append(node.right)
            
            if ans:
                return True
                
        return ans
                
        
            