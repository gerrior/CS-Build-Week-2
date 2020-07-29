# Singly-linked lists are already defined with this interface:

class ListNode(object):
  def __init__(self, x, next = None):
    self.value = x
    self.next = next

length = 0
fromEnd = 0

def remove_kth_from_end(head, k):
    global length
    global fromEnd

    length += 1
    
    if head.next != None:
        currentPos = remove_kth_from_end(head.next, k)
    
    fromEnd += 1
    
    if fromEnd == (k + 1): # +1 because we need to backup another node to make the switch
        head.next = currentPos.next

    return head
    

[20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

a = ListNode(20, ListNode(19, ListNode(18, ListNode(17, ListNode(16, ListNode(15, ListNode(14, ListNode(13, ListNode(12, ListNode(11))))))))))
result = remove_kth_from_end(a, 4)
print(result)