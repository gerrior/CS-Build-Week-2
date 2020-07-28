# https://leetcode.com/problems/linked-list-cycle-ii/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node_set = {None}
        node = head
        
        while(node != None):
            if node in node_set:
                return node
            
            node_set.add(node)
            node = node.next

        return None
        
# Tried so solve it without using extra space

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node = head
        
        while(node != None):
            if node.val == sys.maxsize:
                return node
            
            node.val = sys.maxsize
            node = node.next

        return None