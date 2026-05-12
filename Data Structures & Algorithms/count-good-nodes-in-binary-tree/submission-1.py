# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.num = 0
        def findGood(nums:TreeNode,max_num:int):

            if nums is None:
                return

            if nums.val >= max_num:
                self.num += 1
                
            new_max = max(nums.val,max_num)
                
            findGood(nums.left,new_max)
            findGood(nums.right,new_max)
            

        findGood(root,-float('inf'))

        return self.num
