class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode(0)
        m = new
        while list1 or list2:
            if list1 == None:
                new.next = ListNode(list2.val)
                list2 = list2.next
                new = new.next
            elif list2 == None:
                new.next = ListNode(list1.val)
                list1 = list1.next
                new = new.next
            elif list1.val <= list2.val:
                new.next = ListNode(list1.val)
                list1 = list1.next
                new = new.next
            elif list1.val > list2.val:
                new.next = ListNode(list2.val)
                list2 = list2.next
                new = new.next
                
        return m.next
        # print(list2.val)