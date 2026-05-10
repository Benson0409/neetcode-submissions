# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depth(node : Optional[TreeNode]) -> int:
            if not node:
                return 0

            right = depth(node.right)
            left = depth(node.left)

            if right == -1 or left == -1:
                return -1
            if abs(right - left) > 1:
                return -1

            return max(right,left) + 1

        return depth(root) != -1
