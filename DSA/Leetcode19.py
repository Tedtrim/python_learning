def removeNthFromEnd(self, head, n):
    current = head
    size = 0
    while current.next is not None:
        current = current.next
        size += 1
    pos = size - n 
    current2 = ListNode(0)
    current2.next = head
    for _ in range(pos):
        current2 = current2.next
        
    current2.next = current2.next.next
    return current2.next

def reverse(head):
    prev = None 
    current = head

    while current is not None:
        next_node = current
        current.next = prev
        prev = current 
        current.next = next_node

    return prev



