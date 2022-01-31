
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Brute Force Approach: 
        # - Traverse all the linked lists and collect the values of the nodes into an array.
        # - Sort and iterate over this array to get the proper value of nodes.
        # - Create a new sorted linked list and extend it with the new nodes.
        
        # O(Nlog(N)) time | O(N) space 
        # Where N is the total number of nodes in the final linked-list
        
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
        
        #---------------------------------PRIORITY QUEUE APPROACH----------------------------#
#         from Queue import PriorityQueue
        
#         dummy = ListNode(None)
#         curr = dummy
#         q = PriorityQueue()
#         for node in lists:
#             if node: q.put((node.val,node))
#         while q.qsize()>0:
#             curr.next = q.get()[1]
#             curr=curr.next
#             if curr.next: q.put((curr.next.val, curr.next))
#         return dummy.next