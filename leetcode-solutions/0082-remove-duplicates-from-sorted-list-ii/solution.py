class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        dummy = ListNode(0)
        tail = dummy
        curr = head
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                duplicate_val = curr.val
                while curr and curr.val == duplicate_val:
                    curr = curr.next
                tail.next = curr 
            else:
                tail.next = curr
                tail = curr
                curr = curr.next
                
        return dummy.next

