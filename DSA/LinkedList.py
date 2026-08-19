class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node(3)
b = Node(7)
c = Node(1)
a.next = b
b.next = c

def length(head):
    count = 0
    current = head
    while current is not None:
        current = current.next
        count += 1

    return count

def reverse(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def middle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    return slow






