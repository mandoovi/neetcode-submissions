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
            new_start = current.next
            kth.next = None

            newHead = self.reverseList(new_start)

            current.next = newHead
            new_start.next = next_group   

            current = new_start

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev    