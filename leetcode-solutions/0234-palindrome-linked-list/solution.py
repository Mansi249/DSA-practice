# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        curr = slow
        prev = None
        while curr:
            next_nod = curr.next
            curr.next = prev
            prev = curr
            curr = next_nod
        right = prev
        left = head
        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True
        
