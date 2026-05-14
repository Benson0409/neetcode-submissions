# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        answer = []
        bus = deque([root])
        while bus:
            busNum = len(bus)
            for _ in range(busNum):
                current = bus.popleft()

                if current:
                    answer.append(str(current.val))
                    bus.append(current.left)
                    bus.append(current.right)
                else:
                    answer.append(str('N'))
        
        return ",".join(answer)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        if not data or data == "N":
            return None

        data_queue = deque(data.split(","))

        head = data_queue.popleft()
        root = TreeNode(int(head))

        tree = deque([root])


        while tree:
            current = tree.popleft()

            left_data = data_queue.popleft()
            if left_data != 'N':
                current.left = TreeNode(int(left_data))
                tree.append(current.left)
        

            
            right_data = data_queue.popleft()
            if right_data != 'N':
                current.right = TreeNode(int(right_data))
                tree.append(current.right)

        return root
            


        







