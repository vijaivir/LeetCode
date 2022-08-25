# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        int1 = ''
        int2 = ''
        
        while head1 != None:
            int1 += str(head1.val)
            head1 = head1.next
            
        while head2 != None:
            int2 += str(head2.val)
            head2 = head2.next
        
        result = str(int(int1[::-1]) + int(int2[::-1]))
        
        head = None
        print(head)
        for x in result:
            if head == None:
                head = ListNode(x, None)
            else:
                head = ListNode(x, head)
        return head
