"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dictionary = {None: None}
        current = head
        
        while current:
            copy = Node(current.val)
            dictionary[current] = copy
            current = current.next
        
        current = head
        while current:
            copy = dictionary[current]
            copy.next = dictionary[current.next]
            copy.random = dictionary[current.random]
            current = current.next
        
        return dictionary[head]


