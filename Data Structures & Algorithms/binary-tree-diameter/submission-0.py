# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_ans = 0 
        
        def maxDepth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_depth = maxDepth(node.left)
            right_depth = maxDepth(node.right)

            self.max_ans = max(self.max_ans, left_depth + right_depth)

            return max(left_depth, right_depth) + 1
        
        maxDepth(root)
        return self.max_ans