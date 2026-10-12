# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
        
        middle = count // 2
        count_2 = 0
        current = head

        while current:
            if count_2 == middle:
                return current
            count_2 += 1
            current = current.next