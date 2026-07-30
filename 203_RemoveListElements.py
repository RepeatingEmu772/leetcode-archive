class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    dummy = ListNode(-1, head)

    curr = dummy

    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next

def printasList(list1):
     list2 = []
     while list1 != None:
          list2.append(list1.val)
          list1 = list1.next
     print(list2)


list1 = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))))
printasList(removeElements(list1, 6))

list2 = ListNode(None, None)
printasList(removeElements(list2, 1))

list3 = ListNode(7, ListNode(7, ListNode(7, ListNode(7, None))))
printasList(removeElements(list3, 7))
