# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # best guess, create a stack FILO, then count 3 nodes while recording the start node (min head) and last node(mini end). if mini_end cannot be found in k iterations. end. Then we have a list of our 3 nodes, while queue pop and set to mini_head next and so on. 

        start = ListNode()
        start.next = head
        curr = start.next
        left = start
        right = None

        while curr:
            stack = []

            count = k
            while curr and count > 0:
                count -= 1
                stack.append(curr)
                curr = curr.next
            
            if count > 0:
                break
            

            
            
            for i in range(len(stack)):
                left.next = stack.pop()
                left = left.next
            
            left.next = curr
                
            
        
        return start.next

            




        