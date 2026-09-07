# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list2 = slow.next
        previous = None
        slow.next = None
        
        while list2:
            temp = list2.next
            list2.next = previous
            previous = list2
            list2 = temp

        list1 = head
        list2 = previous
        while list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            
            list1 = temp1
            list2 = temp2
