# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        previous = None
        current = slow

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        count = 0

        first = head
        second = previous

        while second:
            count = max(count, first.val + second.val)
            first = first.next
            second = second.next
    
        return count