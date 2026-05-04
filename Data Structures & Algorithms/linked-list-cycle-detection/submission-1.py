# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev = None
        curr = head
        nums = []

        while curr is not None:
            #記憶體位置相等
            if curr in nums:
                return True

            next_stamp = curr.next
            nums.append(curr)
            curr = next_stamp
            
            
        return False 