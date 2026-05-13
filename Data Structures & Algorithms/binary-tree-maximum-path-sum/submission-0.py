# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -float('inf')
        def findMax(node:Optional[TreeNode]) -> int:
            
            if node is None:
                return 0
            right = max(findMax(node.right),0)
            left = max(findMax(node.left),0)

            v_sum = node.val + right + left

            self.max_sum = max(self.max_sum,v_sum)

            l_sum = node.val + max(right,left)
            return l_sum

        findMax(root)
        return self.max_sum