# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nums = []
        def findNum(node:Optional[TreeNode]):

            if node is None:
                return

            self.nums.append(node.val)

            findNum(node.right)
            findNum(node.left)

        findNum(root)
        
        self.nums = sorted(self.nums)
        
        return self.nums[k-1]

            