# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # Initialize previous node pointer to None (new tail)
        curr = head  # Start with the head of the list

        while curr:
            temp = curr.next  # Temporarily store the next node
            curr.next = prev  # Reverse the current node's pointer
            prev = curr       # Move prev pointer forward to current node
            curr = temp       # Advance to the next node in the original list

        return prev  # Prev is the new head of the reversed list
