
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
               
        _map = {None: None}
        cur_node = head
        while cur_node:
            _map[cur_node] = Node(cur_node.val)
            cur_node = cur_node.next
        
        cur_node = head
        while cur_node:
            _map[cur_node].next = _map[cur_node.next]
            _map[cur_node].random = _map[cur_node.random]
            cur_node = cur_node.next
        
        return _map[head]