# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        ptr  = 0
        stack = []
        size = 0
        node = head
        while node:
            size += 1
            node = node.next
        answer = [0] * size
        while head:
            temp = ptr-1
            while stack and head.val > stack[-1]:
                if answer[temp] == 0:
                    stack.pop()
                    answer[temp] = head.val
                else:
                    temp -= 1                
            stack.append(head.val)
            ptr += 1
            head = head.next
        return answer
            
            
    
            
        
        
                