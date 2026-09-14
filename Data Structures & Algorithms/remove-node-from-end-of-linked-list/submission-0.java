/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode last = head;
        ListNode first = head;
        
        for (int i = 0; i < n+1; i++){
            if (first == null) {
                head = head.next;
                return head;
            }
            first = first.next;
        }

        while (first != null){
            first = first.next;
            last = last.next;
        }

        last.next = last.next.next;
        return head;
    }
}
