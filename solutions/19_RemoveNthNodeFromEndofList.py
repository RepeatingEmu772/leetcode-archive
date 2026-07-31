from _LinkedList import ListNode, printasList

def removeNthFromEnd(head, n):
    dummy = ListNode(-1, head)

    fast = dummy
    slow = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        fast = fast.next 
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next

l1 = ListNode(1, (ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))))
printasList(removeNthFromEnd(l1, 2))

l2 = ListNode(1, None)
printasList(removeNthFromEnd(l2, 1))

l3 = ListNode(1, ListNode(2, None))
printasList(removeNthFromEnd(l3, 1))
