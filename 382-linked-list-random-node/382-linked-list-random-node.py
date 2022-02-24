import random
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        # Note that the head is guaranteed to be not null, so it contains at least one node.

        self.head = head

    def getRandom(self) -> int:
        # Returns a random node's value.
        
        curr = self.head
        res = 0
        index = 1
        
        while curr:
            if random.random() < (1/index):
                res = curr.val
            
            index += 1
            curr = curr.next
        
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()