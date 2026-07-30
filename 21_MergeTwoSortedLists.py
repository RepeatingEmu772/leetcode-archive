class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeTwoLists(list1, list2):
        dummyhead = dummy = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            
            dummy = dummy.next

        if list1:
            dummy.next = list1
        else:
            dummy.next = list2

        return dummyhead.next

list1 = ListNode(1, ListNode(2, ListNode(3, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))

def printasList(list1):
     list2 = []
     while list1 != None:
          list2.append(list1.val)
          list1 = list1.next
     print(list2)

printasList(mergeTwoLists(list1, list2))