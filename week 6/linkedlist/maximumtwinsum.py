
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        half = []
        ans = [0]
        size = 0
        ptr = 0
        nod = head
        while head:
            size += 1
            head = head.next
        while ptr < size/2:
            half.append(nod.val)
            ptr += 1
            nod = nod.next
        
        while nod:
            temp = nod.val + half[(size-1)-ptr]
            if ans and temp > ans[0]:
                ans.pop()
                ans.append(temp)
            nod = nod.next
            ptr += 1
        
        return ans[0]