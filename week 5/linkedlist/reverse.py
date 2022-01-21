class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(ListNode):
     def toll(self,lis):
        if len(lis) == 0:
            return 
        elif len(lis) == 1:
            return ListNode(lis[0])
        else:
            return ListNode(lis[0], self.toll(lis[1:]))
     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = []
        while head:
            new.append(head.val)
            head = head.next
        new.reverse()

        return self.toll(new)