# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        while head and head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            head = head.next
            nod = head
        else:
            nod = head
      
        while nod and nod.next:  
            if nod.val == nod.next.val:
                while nod.next and nod.val == nod.next.val:
                    nod = nod.next
                nod = nod.next
                temp.next = nod
            else:
                temp = nod
                nod = nod.next
        return head