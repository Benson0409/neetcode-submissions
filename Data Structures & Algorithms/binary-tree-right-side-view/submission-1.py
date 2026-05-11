# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []
        if root is None:
            return answer
        
        bus = deque([root])

        while bus:
            curr_size = len(bus)

            for i in range(curr_size):
                num = bus.popleft()
                if i == curr_size - 1:
                    answer.append(num.val)

                if num.left:
                    bus.append(num.left)
                if num.right:
                    bus.append(num.right)
                
        return answer
