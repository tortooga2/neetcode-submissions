# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        head = None
        next_node = None
        n1 = list1
        n2 = list2
        while n2 != None and n1 != None:
            n = None
            if n2.val < n1.val:
                n = n2
                n2 = n2.next
            else:
                n = n1
                n1 = n1.next
            
            if head == None:
                head = n
                next_node = head
            else:
                next_node.next = n
                next_node = next_node.next
        
        if n2 != None:
            next_node.next = n2
        if n1 != None:
            next_node.next = n1
        
                

            

                

                


        return head



        