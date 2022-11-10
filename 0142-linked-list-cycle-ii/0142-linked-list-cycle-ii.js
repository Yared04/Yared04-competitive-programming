/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
    let slow = head;
    let fast = head;
    let cycle = false;

    while(fast && fast.next && fast.next.next){
        fast = fast.next.next;
        slow = slow.next;
        if(fast == slow){
            cycle = true;
            break;
        }
    }
    if(cycle){
        while(head != fast){
            head = head.next;
            fast = fast.next;
            }
        return head;
    }
    return null;
        
};