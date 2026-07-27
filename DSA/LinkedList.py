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
        next_node = current.next   # rescue the rest of the chain
        current.next = prev        # repoint backwards
        prev = current             # move prev up
        current = next_node        # move current up

    return prev
