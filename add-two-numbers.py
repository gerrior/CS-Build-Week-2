# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        carry = 0
        priorNode = None
        
        while(l1 != None or l2 != None):
            lhs = 0
            if l1 != None: 
                lhs = l1.val

            rhs = 0
            if l2 != None:
                rhs = l2.val
                l2 = l2.next

            value = lhs + rhs + carry

            carry = int(value / 10)
            value = int(value % 10)

            if l1 == None:
                priorNode.next = ListNode(0)
                l1 = priorNode.next

            l1.val = value
                
            priorNode = l1
            l1 = l1.next
            
        if carry > 0:
            priorNode.next = ListNode(carry)
            
        return head