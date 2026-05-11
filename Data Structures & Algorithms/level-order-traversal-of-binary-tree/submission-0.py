# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if root is None:
            return answer
        bus = deque([root])

        while bus:
            currentBus = []
            level_bus = len(bus)

            for _ in range(level_bus):
                node = bus.popleft()
                currentBus.append(node.val)

                if node.left:
                    bus.append(node.left)
                if node.right:
                    bus.append(node.right)
                
            answer.append(currentBus)
        return answer

        

      