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
    public void reorderList(ListNode head) {
        // reverse the linkedlist from mid -> tail
        // find the list length
        int len = 0;
        ListNode ptr = head;
        while (ptr != null){
            len++;
            ptr = ptr.next;
        }
        System.out.println("len is " + len);
        ptr = head;
        ListNode prev = null;
        int halfLen = len / 2;
        for (int i = 0; i < halfLen; i++){
            prev = ptr;
            ptr = ptr.next;
        }
        System.out.println("mid value is at " + ptr.val);
        if (prev != null) prev.next = null;
        else return;
        ListNode reversedRight = reverseList(ptr);
        System.out.println("ReversedRight is: ");
        printList(reversedRight);
        System.out.println("IntactLeft is: ");
        printList(head);

        // sandwich the head -> mid into the reversed linkedlist
        head = mergeList(head, reversedRight);
        //printList(res);
    }
    public void printList(ListNode node){
        while (node != null){
            System.out.print(node.val + "->");
            node = node.next;
        }
        System.out.println();
    }

    public ListNode reverseList(ListNode head){
        ListNode prev = null;
        ListNode ptr = head;
        ListNode tmp;
        while (ptr != null){
            tmp = ptr.next;
            ptr.next = prev;
            prev = ptr;
            ptr = tmp;
        }
        return prev;
    }

    public ListNode mergeList(ListNode list1, ListNode list2){
        if (list1 == null) return list2;
        if (list2 == null) return list1;
        ListNode head = list1;
        ListNode ptr = head;
        list1 = list1.next;
        int last = 1;
        while (list1 != null || list2 != null){
            if (list1 == null || last == 1) {
                ptr.next = list2;
                ptr = ptr.next;
                if (list2 != null) list2 = list2.next;
                last = 2;
                continue;
            }
            if (list2 == null || last == 2) {
                ptr.next = list1;
                ptr = ptr.next;
                if (list1 != null) list1 = list1.next;
                last = 1;
                continue;
            }
        }
        return head;
    }
}
