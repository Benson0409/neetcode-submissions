# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nums = [k]

        def findNum(node:Optional[TreeNode])->int:

            if node is None:
                return None

            left = findNum(node.left)

            if left is not None:
                return left
            
            self.nums[0] -= 1
            if self.nums[0] == 0:
                return node.val
                
            return findNum(node.right)
        
        return findNum(root)

            