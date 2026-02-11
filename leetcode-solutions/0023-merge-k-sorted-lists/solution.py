# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(min_heap,(node.val,i,node))
        dummy = ListNode(0)
        tail = dummy
        while min_heap:
            val,list_no,curr = heapq.heappop(min_heap)
            tail.next = curr
            tail = tail.next
            if curr.next:
                heapq.heappush(min_heap,(curr.next.val,list_no,curr.next)) 
        return dummy.next
