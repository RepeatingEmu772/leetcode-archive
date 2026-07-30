class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDuplicates(head):
    curr = head
    while curr and curr.next:

        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head
     

def printasList(list1):
     list2 = []
     while list1 != None:
          list2.append(list1.val)
          list1 = list1.next
     print(list2)


list1 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None)))))
printasList(removeDuplicates(list1))

list3 = ListNode(1, ListNode(1, ListNode(2, None)))
printasList(removeDuplicates(list3))
