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
        if not head:
            return None
        
        head_copy = None
        curr_copy = head_copy
        prev_copy = None

        pointer_map = {None:None}

        curr = head
        while curr:
            curr_copy = Node(curr.val, None, curr.random)
            pointer_map[curr] = curr_copy
        
            if prev_copy:
                prev_copy.next = curr_copy
            else:
                head_copy = curr_copy

            prev_copy = curr_copy
            
            curr_copy = curr_copy.next
            curr = curr.next
        
        print(head_copy)
        
        curr = head_copy
        while curr:
            if curr.random:
                curr.random = pointer_map[curr.random]
            curr = curr.next
        
        return head_copy



        
        

        