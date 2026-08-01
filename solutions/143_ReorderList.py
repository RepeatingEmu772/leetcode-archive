from _LinkedList import *

def reverseListOrder(head):
    prev = None
    curr = head

    while curr:
        _next = curr.next
        curr.next = prev

        prev = curr
        curr = _next

    return prev


def reorderList(head):
    if not head or not head.next:
        return head

    fast = slow = head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    second = slow.next
    slow.next = None
    second = reverseListOrder(second)

    first = head

    while second:
        first_next = first.next
        second_next = second.next

        first.next = second
        second.next = first_next

        first = first_next
        second = second_next


l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
printasList(reorderList(l1))