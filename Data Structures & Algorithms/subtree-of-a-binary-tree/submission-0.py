# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r: Optional[TreeNode], s: Optional[TreeNode])->bool:
            if r is None and s is None:
                return True
            if r is None or s is None or r.val != s.val:
                return False

            return isSame(r.right,s.right) and isSame(r.left,s.left)

        if root is None:
            return False
        
        if isSame(root,subRoot):
            return True

        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)


