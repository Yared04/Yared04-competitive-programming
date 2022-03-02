# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        ret = answer
        st1, st2 = "", ""
        while l1:
            st1 += str(l1.val)
            l1 = l1.next
        while l2:
            st2 += str(l2.val)
            l2 = l2.next
        st1 = st1[::-1]
        st2 = st2[::-1]
        print(st1,st2)
        ans = int(st1) + int(st2)
        ans = str(ans)
        ans = ans[::-1]
        print(ans)
        for num in ans:
            answer.next = ListNode(num)
            answer = answer.next
        return ret.next
            
        