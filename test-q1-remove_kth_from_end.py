# Singly-linked lists are already defined with this interface:

class ListNode(object):
  def __init__(self, x, next = None):
    self.value = x
    self.next = next

def remove_kth_from_end(head, k):
    bList = []
    tempHead = head

    if k == 0:
        return head 

    while True:
        bList.append(tempHead)
        tempHead = tempHead.next
        if tempHead == None:
            break

    indexOfNodeToRemove = len(bList) - k # -1 converts it to an index

    if indexOfNodeToRemove >= 0:
        bList[indexOfNodeToRemove - 1].next = bList[indexOfNodeToRemove].next

    return head
    

# [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

a = ListNode(20, ListNode(19, ListNode(18, ListNode(17, ListNode(16, ListNode(15, ListNode(14, ListNode(13, ListNode(12, ListNode(11))))))))))
result = remove_kth_from_end(a, 4)
print(result)

# [100, 200]
b = ListNode(100, ListNode(200))
result = remove_kth_from_end(b, 2)
print(result)
