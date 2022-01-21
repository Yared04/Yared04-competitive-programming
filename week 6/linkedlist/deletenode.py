class Solution:
    def deleteNode(self, node):
        node.next.val
        node.next = node.next.next
        