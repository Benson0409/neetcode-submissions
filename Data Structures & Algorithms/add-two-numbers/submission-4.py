# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # if not l1:
        #     return l2
        # elif not l2:
        #     return l1
            

        dummy = ListNode(-1)
        ans = dummy

        lis1 = l1
        lis2 = l2

        num = 0

        while lis1 is not None and lis2 is not None:
            

            next_value = lis1.val + lis2.val
            
            if num!=0:
                next_value += num
                num = 0

            if next_value >= 10:
                next_value = next_value -10
                num = 1
            
            new_node = ListNode(next_value)
            ans.next = new_node
            ans = new_node

            if lis1.next == None and lis2.next != None:
                new_node = ListNode(0)
                lis1.next = new_node
            elif lis2.next == None and lis1.next != None:
                new_node = ListNode(0)
                lis2.next = new_node

            lis1 = lis1.next
            lis2 = lis2.next
                

        if num !=0 :
            new_node = ListNode(num)
            ans.next = new_node

        return dummy.next

