def MergeTwoLists(self, list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.val > list2.val:
            tail.next = list2
            list2 = list2.next
        else:
            tail.next = list1
            list1 = list1.next
        tail = tail.next

    if list1 is None:
        tail.next = list2
    else:
        tail.next = list1

    return dummy.next
    