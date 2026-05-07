# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        dummy.next = head
        ans = dummy
        
        while True:
            find = ans
            for _ in range(k):
                find = find.next
                if not find:
                    return dummy.next

            next_head = find.next
            first_head = ans.next

            find.next = None

            new_head = ReverseListNode(first_head)

            ans.next = new_head
            first_head.next = next_head

            ans = first_head

def ReverseListNode(nums:Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = nums

            while curr is not None:
                next_step = curr.next
                curr.next = prev
                prev = curr
                curr = next_step

            return prev
       
                

                