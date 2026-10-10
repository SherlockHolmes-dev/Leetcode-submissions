# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to get the k-th node from the current position
        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr  # Returns None if less than k nodes remain

        dummy = ListNode(0)
        dummy.next = head  # Dummy node points to the start of the list
        group_prev = dummy  # Points to the node before the current group

        while True:
            # Find the k-th node ahead of group_prev
            kth = getKth(group_prev, k)
            if not kth:
                break  # If fewer than k nodes remain, we're done

            group_next = kth.next  # Store the next group's head
            prev = group_next      # Start reversing from group_next backwards
            curr = group_prev.next # First node in the group to reverse

            # Reverse k nodes in-place
            while curr != group_next:
                tmp = curr.next    # Temporarily store next node
                curr.next = prev   # Reverse the pointer
                prev = curr        # Move prev forward
                curr = tmp         # Move curr forward

            # After reversing, group_prev.next was the start of the group
            # which is now the end, so we connect it to the next section later
            tmp = group_prev.next
            group_prev.next = kth  # Connect previous part to new head of group
            group_prev = tmp       # Move group_prev to the end of the reversed group

        return dummy.next  # Return the real head
        