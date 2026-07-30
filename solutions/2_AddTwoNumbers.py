class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

def printasList(list1):
    list2 = []
    while list1 != None:
        list2.append(list1.val)
        list1 = list1.next
    print(list2)


def addTwoNumbers_bloated(l1, l2):
    head = ListNode()
    ptr = head
    carry = 0 

    while l1 and l2:
        # printasList(head)

        nextNode = ListNode()
        _sum = l1.val + l2.val + carry

        if _sum > 9:
            carry = 1
            nextNode.val = _sum % 10

        else:
            carry = 0
            nextNode.val = _sum

        ptr.next = nextNode
        ptr = ptr.next
        l1 = l1.next
        l2 = l2.next

    while l1:
        nextNode = ListNode()
        _sum = l1.val + carry

        if _sum > 9:
            carry = 1
            nextNode.val = _sum % 10

        else:
            carry = 0
            nextNode.val = _sum

        ptr.next = nextNode
        ptr = ptr.next
        l1 = l1.next

    while l2:
        nextNode = ListNode()
        _sum = l2.val + carry

        if _sum > 9:
            carry = 1
            nextNode.val = _sum % 10

        else:
            carry = 0
            nextNode.val = _sum

        ptr.next = nextNode
        ptr = ptr.next
        l2 = l2.next

    if carry > 0:
        ptr.next = ListNode(1, None)

    return head.next 


def addTwoNumbers(l1, l2):
    dummy = ListNode()
    ptr = dummy
    carry = 0 

    while l1 or l2:
        printasList(dummy.next)

        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        _sum = x + y + carry

        val = _sum % 10
        carry = _sum // 10

        nextNode = ListNode(val=val)

        ptr.next = nextNode
        ptr = ptr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry > 0:
        ptr.next = ListNode(1, None)

    return dummy.next 


l1 = ListNode(2, ListNode(4, ListNode(3, None)))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))

printasList(addTwoNumbers(l1, l2))

l1 = ListNode(9, ListNode(9, ListNode(9, None)))
l2 = ListNode(9, None)

printasList(addTwoNumbers(l1, l2))

