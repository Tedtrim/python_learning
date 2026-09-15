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


def middle(head):
    fast = head
    slow = head

    while fast is not None and fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

def reverse(head):
    current = head
    prev = None

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev