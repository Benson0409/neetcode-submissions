# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None

        mid_val = preorder[0]
        root = TreeNode(mid_val)

        mid_val = inorder.index(mid_val)

        root.left = self.buildTree(preorder[1:mid_val+1],inorder[:mid_val])
        root.right = self.buildTree(preorder[mid_val+1:],inorder[mid_val+1:])

        return root
            
