// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = l1
        head2 = l2
        result = ListNode()
        rhead = result
        carry = 0

        while head1 or head2:

            if head1 and head2:
                val = (head1.val+head2.val+carry) % 10
                carry = (head1.val+head2.val+carry) // 10
                head1 = head1.next
                head2 = head2.next

            elif head1:
                 val = (head1.val + carry ) % 10
                 carry = (head1.val + carry ) // 10
                 head1 = head1.next

            elif head2:
                 val = (head2.val + carry ) % 10
                 carry = (head2.val + carry ) // 10
                 head2 = head2.next
            
            rhead.val = val

            if head1 or head2:
                rhead.next = ListNode()
                rhead = rhead.next
            

        if carry>0:
            rhead.next = ListNode()
            rhead = rhead.next
            rhead.val = carry
     
        rhead = result
    
        return result
            



        