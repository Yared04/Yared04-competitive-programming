# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lis =[]
        for i in range(len(lists)):
            node = lists[i]
            while node:
                heapq.heappush(lis,node.val)
                node = node.next
        ans = ListNode(0)
        node = ans
        for i in range(len(lis)):
            node.next = ListNode(heapq.heappop(lis))
            node = node.next
        return ans.next
        
                
        
        