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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
      // Handle edge cases when one or both lists are null
        if (list1 == null) return list2;
        if (list2 == null) return list1;

        // Create a dummy node to simplify edge cases
        ListNode dummy = new ListNode(-1);
        ListNode current = dummy;

        // Iterate through both lists until one is empty
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                current.next = list1; // Link the smaller node to the merged list
                list1 = list1.next;  // Move to the next node in list1
            } else {
                current.next = list2; // Link the smaller node to the merged list
                list2 = list2.next;  // Move to the next node in list2
            }
            current = current.next; // Move to the next node in the merged list
        }

        // Attach any remaining nodes from list1 or list2
        if (list1 != null) {
            current.next = list1;
        } else if (list2 != null) {
            current.next = list2;
        }

        return dummy.next; // The merged list starts from dummy.next  
    }
}