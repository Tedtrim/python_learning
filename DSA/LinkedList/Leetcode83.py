def remove_duplicates(self, head):
    current = head

    while current is not None and current.next is not None:
        if current == current.next:
            current.next = current.next.next
        else:
            current = current.next

    return head