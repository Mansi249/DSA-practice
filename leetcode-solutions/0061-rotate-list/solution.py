# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0 or not head or not head.next :
           return head
        length = 1
        curr = head
        while curr.next:
            length +=1
            curr = curr.next
        k = k%length
        if k==0:
            return head
        curr.next = head
        steps_to_new_tail = length-k
        new_tail = head
        for _ in range(steps_to_new_tail-1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head

