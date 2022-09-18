# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        cur = head
        while cur.next != None:
            count += 1
            cur = cur.next
        size = count + 1
        if size % 2 == 0:
            cur = head
            count = 0
            while count < (size/2):
                count += 1
                cur = cur.next
            return cur
        else:
            cur = head
            count = 1
            while count < (size/2):
                count += 1
                cur = cur.next
            return cur
