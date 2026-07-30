from solutions._LinkedList import ListNode, printasList

def reverseList(head):
    prev = None
    curr = head

    while curr:
        _next = curr.next 
        curr.next = prev

        prev = curr
        curr = _next

    return prev

l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
l2 = ListNode(1, ListNode(2, None))

printasList(reverseList(l1))
printasList(reverseList(l2))
