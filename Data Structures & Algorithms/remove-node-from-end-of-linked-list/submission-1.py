# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cache = []
        curr = dummy
        while curr:
            cache.append(curr)
            curr = curr.next
            if len(cache) > n + 1:
                cache.pop(0)

        
        cache[0].next = cache[0].next.next
        return dummy.next