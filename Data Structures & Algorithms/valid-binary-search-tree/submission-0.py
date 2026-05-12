# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isLargrNum(node:Optional[TreeNide],high:int,low:int) -> bool:

            if node is None:
                return True

            if node.val <= low or node.val >= high:
                return False
            
            return isLargrNum(node.right,high,node.val) and isLargrNum(node.left,node.val,low)

           
        
        return isLargrNum(root,float('inf'),-float('inf'))
            

