# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get values or 0 if a list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add digits + carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # Create new node for this digit
            current.next = ListNode(digit)
            current = current.next

            # Advance input pointers
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
        