# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        
        prev = None
        curr = second

        while curr is not None:
            next_step = curr.next
            curr.next = prev
            prev = curr
            curr = next_step

        first = head
        second = prev
        
        while second is not None:
            # 1. 記住雙方原本的下一步
            tmp1 = first.next
            tmp2 = second.next
            
            # 2. 搭橋交叉接線 (1接5, 5接2)
            first.next = second
            second.next = tmp1
            
            # 3. 探險家們走到下一個位置，準備下一回合
            first = tmp1
            second = tmp2