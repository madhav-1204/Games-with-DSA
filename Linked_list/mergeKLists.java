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
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        ListNode head=null;
        ListNode tail=null;
        for(int i=0;i<lists.length;i++){
           ListNode temp = lists[i];
           while(temp!=null){
            pq.add(temp.val);
            temp = temp.next;
           }
        }
        while(pq.size()>0){
            ListNode newNode = new ListNode(pq.peek());
            if(head==null){
                head = newNode;
                tail = newNode;
            }else{
                tail.next = newNode;
                tail = newNode;
            }
            pq.remove();
        }
        return head;
    }
}
