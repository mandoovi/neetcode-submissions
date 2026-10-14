# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = dummy

        while True:
            kth = self.getKth(current, k)
            if not kth:
                break

            next_group = kth.next
            start = current.next
            kth.next = None

            new_head_end = self.reverseList(start)

            current.next = new_head_end
            start.next = next_group   

            current = start

        return dummy.next

    def getKth(self, head, k):
        while head and k > 0:
            head = head.next
            k -= 1
        return head

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev    